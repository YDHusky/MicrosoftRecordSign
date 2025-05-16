import time

from husky_spider_utils import SeleniumSession


class MicrosoftSign(SeleniumSession):
    base_url = "https://rewards.bing.com/"

    def __init__(self, **kwargs):
        super().__init__(selenium_init_url=self.base_url,driver_type="edge" , **kwargs)

    def run(self):
        from parsel import Selector
        import time
        time.sleep(5)
        dom = Selector(self.get_page_source())
        record_urls = []
        record_urls.extend(dom.css("#daily-sets mee-card a::attr(href)").getall())
        record_urls.extend(dom.css("#more-activities mee-card a::attr(href)").getall())
        for url in record_urls:
            if url != "#":
                self.selenium_get(url)
                time.sleep(1)
        self.selenium_get("https://rewards.bing.com/")

session = MicrosoftSign()
session.run()
time.sleep(4000)
