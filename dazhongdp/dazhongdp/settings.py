# -*- coding: utf-8 -*-

# Scrapy settings for dazhongdp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dazhongdp'

SPIDER_MODULES = ['dazhongdp.spiders']
NEWSPIDER_MODULE = 'dazhongdp.spiders'

LOG_FILE = 'scrapy.log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dazhongdp (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
   'Cookie':'tencentSig=8422400; __mta=222756516.1529666865758.1529667445978.1550489555886.12; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1529666693; _hc.v=d0c8e041-96db-62bc-1956-983e0d61c4d3.1529666693; _lxsdk_cuid=164273d6a60c8-090d7c2f837abd-39614807-1fa400-164273d6a60c8; _lxsdk=164273d6a60c8-090d7c2f837abd-39614807-1fa400-164273d6a60c8; cy=7; cye=shenzhen; _qddaz=QD.4xdt24.gdgdka.jipw5wjc; __mta=222756516.1529666865758.1529667436699.1529667445978.11; __utma=1.2030629870.1529667485.1529667485.1529667485.1; s_ViewType=10; ua=%E9%BB%91%E7%8C%AB%E4%B9%8B%E6%9C%AF; ctu=ce557761a21998eb141c943b3dbedc48c002286749ebf04015c3acde49e98cad; _dp.ac.v=8d338aec-e954-43bf-8932-74c0b213cced; dper=782fc523e18cd148d045d26a26a244c45c92846d365c2ab3948d58d237f2627e6716dfe817d517d6123a0e3d39695a363aa28675bfa024f4c923668c92236e36b90d62780746f5783ea90e1c8723d37f39ed8a4fe272e981d9776967eec0dcd5; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dazhongdp.middlewares.DazhongdpSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dazhongdp.middlewares.DazhongdpDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'dazhongdp.pipelines.DazhongdpPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
