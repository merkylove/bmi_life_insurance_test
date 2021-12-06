from aiohttp import web

from src.life_insurance.entities import Person
from src.life_insurance.quotes.bmi_quote_calculator import BMIAgeGenderQuoteCalculator


class QuoteHandler:
    """
    Web service to produce quote based on user's data
    """

    async def handle_get_quote(self, request):

        # TODO: migrate to model
        weight = request.rel_url.query["weight"]
        height = request.rel_url.query["height"]
        age = request.rel_url.query["age"]
        gender = request.rel_url.query["gender"]

        # TODO: separate from handler cpde
        person = Person(weight, height, age, gender)
        quote_calculator = BMIAgeGenderQuoteCalculator()
        quote = quote_calculator(person)

        # TODO: make response structured
        return web.Response(
            text=f"Your quote is: {quote.quote} {quote.currency}\nReason:\n{quote.reason}"
        )
