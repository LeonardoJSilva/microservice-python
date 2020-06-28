from typing import Coroutine, Any
from aiohttp import web
from aiohttp.abc import Request
from aiohttp.web_response import Response
from aiohttp.web_routedef import RouteTableDef
from execution.product_handle import create_product_handle, get_all_product_handle, get_product_by_code_handle, \
    delete_product_by_code_handle


def create_product_routes(routes: RouteTableDef):
    @routes.get('/products/healthy-check')
    async def get_healthy_check(request: Request):
        return web.Response(text="Healthy")

    @routes.post('/products')
    async def post(request: Request) -> Response:
        payload = await request.json()

        response = await create_product_handle(payload)

        return response

    @routes.get('/products')
    async def get_all(request: Request) -> Response:
        response = await get_all_product_handle()

        return response

    @routes.get('/suppliers/{supplier}/products/{product}')
    async def get(request: Request) -> Response:
        supplier = request.match_info.get('supplier', None)
        product = request.match_info.get('product', None)

        response = await get_product_by_code_handle(int(supplier), int(product))

        return response

    @routes.delete('/suppliers/{supplier}/products/{product}')
    async def delete(request: Request) -> Response:
        supplier = request.match_info.get('supplier', None)
        product = request.match_info.get('product', None)

        response = await delete_product_by_code_handle(int(supplier), int(product))

        return response


