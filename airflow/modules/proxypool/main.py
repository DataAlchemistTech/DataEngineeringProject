import json
from concurrent.futures import ThreadPoolExecutor
from proxypool.proxypool_validator import ProxyPoolValidator
from proxypool.proxypool_scraper import ProxyPoolScraper
from proxypool.redis_proxypool_client import RedisProxyPoolClient
from retry import RetryOnException as retry


@retry(5)
def update_proxypool(config):
    proxy_scraper = ProxyPoolScraper(config.PROXY_WEBPAGE)
    proxy_stream = proxy_scraper.get_proxy_stream(config.NUMBER_OF_PROXIES)
    proxy_validator = ProxyPoolValidator(config.TESTING_URL)

    with ThreadPoolExecutor(max_workers=config.MAX_WORKERS) as executor:
        results = executor.map(proxy_validator.validate_proxy, proxy_stream)
        valid_proxies = filter(lambda x: x.is_valid is True, results)
        sorted_valid_proxies = sorted(
            valid_proxies, key=lambda x: x.health, reverse=True
        )

    with RedisProxyPoolClient(config.REDIS_KEY, config.REDIS_CONFIG) as client:
        client.override_existing_proxies(
             [json.dumps(record.proxy) for record in sorted_valid_proxies[:5]]
        )
