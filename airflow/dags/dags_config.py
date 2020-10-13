

class Config:

    PROXY_WEBPAGE = "https://free-proxy-list.net/"

    TESTING_URL = "https://google.com"

    REDIS_CONFIG = {
        "host": "redis",
        "port": "6379",
        "db": 0
    }

    REDIS_KEY = "proxies"

    MAX_WORKERS = 50

    NUMBER_OF_PROXIES = 50

    RSS_FEEDS = {
        "goal.com": "https://www.goal.com/feeds/en/news",
        "eyefootball": "https://www.eyefootball.com/football_news.xml",
        "101greatgoals": "https://www.101greatgoals.com/feed/",
        "sportslens": "https://sportslens.com/feed/",
        "deadspin": "https://deadspin.com/rss"
    }

    BOOTSTRAP_SERVERS = ["kafka:9092"]

    TOPIC = "rss_news"

    VALIDATOR_CONFIG = {
        "description_length": 10,
        "languages": ["en"]
    }
