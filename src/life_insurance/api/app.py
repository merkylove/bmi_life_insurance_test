from aiohttp import web

from src.life_insurance.api.handlers.quote_handler import QuoteHandler


def init_func(argv):

    handler = QuoteHandler()

    app = web.Application()

    app.add_routes([web.get("/get_quote", handler.handle_get_quote)])

    return app
