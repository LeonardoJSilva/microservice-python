from typing import Coroutine, Any
from aiohttp import web
from aiohttp.web_response import Response
from aiohttp.web_routedef import RouteTableDef
from execution.product_handle import create_product_handle


def create_product_routes(routes: RouteTableDef):
    @routes.get('/')
    async def get():
        return web.Response(text="Hello")

    @routes.post('/')
    async def post(request) -> Response:
        payload = await request.json()

        response = await create_product_handle(payload)

        return response
