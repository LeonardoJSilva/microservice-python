import logging
from aiohttp import web
from presentation.router import create_routes

PORT = 80
routes = web.RouteTableDef()

if __name__ == "__main__":  # pragma: no cover
    app = web.Application()
    create_routes(routes)
    app.add_routes(routes)
    logging.info(f"Application is running in port {PORT}")
    web.run_app(app, port=PORT)
