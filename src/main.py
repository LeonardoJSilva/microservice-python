import logging

from aiohttp import web
from presentation.router import create_routes


routes = web.RouteTableDef()

if __name__ == "__main__":  # pragma: no cover
    app = web.Application()
    create_routes(routes)
    app.add_routes(routes)
    logging.info("Application is running in port 80")
    web.run_app(app, port=80)
