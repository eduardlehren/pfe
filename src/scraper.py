import scrapy


class PreciousMetalsPriceFinder(scrapy.Spider):
    name = "Preisfinder"

    start_urls = [
        "https://www.kitco.com/silver-price-today-canada/index.html",
        "https://www.kitco.com/gold-price-today-canada/index.html",
        "https://www.kitco.com/platinum-price-today-canada/index.html",
        "https://www.kitco.com/palladium-price-today-canada/index.html",
    ]

    def parse(self, response):
        PRICE_SELECTOR = ".table-price--body-table--overview-bid"
        for p in response.css(PRICE_SELECTOR):
            price = p.css("p::text").extract()[1]

        if "gold" in response.url:
            metal = "gold"
        elif "silver" in response.url:
            metal = "silver"
        elif "platinum" in response.url:
            metal = "platinum"
        elif "palladium" in response.url:
            metal = "palladium"

        yield {
            "price": price,
            "metal": metal,
        }
