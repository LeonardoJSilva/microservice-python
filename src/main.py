from aiohttp import web
from presentation.router import create_routes

routes = web.RouteTableDef()

if __name__ == "__main__":  # pragma: no cover
    app = web.Application()
    create_routes(routes)
    app.add_routes(routes)
    web.run_app(app)
