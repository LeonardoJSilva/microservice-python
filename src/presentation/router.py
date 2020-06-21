from typing import Coroutine
from aiohttp.web_routedef import RouteTableDef
from presentation.product_controller import create_product_routes


def create_routes(routes: RouteTableDef) -> Coroutine:
    return create_product_routes(routes)
