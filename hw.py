import scrapy

class Sp500PerformanceSpider(scrapy.Spider):
    name = "sp500_performance"
    allowed_domains = ["slickcharts.com", "www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        rows = response.css("table tbody tr")
        for row in rows:
            number = row.css("td:nth-child(1)::text").get(default="").strip()
            company = (
                row.css("td:nth-child(2) a::text").get()
                or row.css("td:nth-child(2)::text").get()
                or ""
            ).strip()
            symbol = row.css("td:nth-child(3)::text").get(default="").strip()
            ytd = row.css("td:nth-child(4)::text").get(default="").strip()

            yield {
                "number": number,
                "company": company,
                "symbol": symbol,
                "ytd_return": ytd,
            }
