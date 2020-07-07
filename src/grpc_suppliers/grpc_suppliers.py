import logging
from typing import List
import grpc

from grpc_suppliers.settings import SUPPLIERS_HOST, SUPPLIERS_PORT
from protos import suppliers_pb2_grpc
from protos.suppliers_pb2 import SuppliersByCodesResponse, SuppliersByCodesRequest


class GrpcSuppliers:

    def __init__(self):
        self._grpc = grpc.insecure_channel(target=f'{SUPPLIERS_HOST}:{SUPPLIERS_PORT}',
                                           options=[('grpc_suppliers.lb_policy_name', 'pick_first'),
                                                    ('grpc_suppliers.enable_retries', 0),
                                                    ('grpc_suppliers.keepalive_timeout_ms', 10000)
                                                    ])
        self._stub = suppliers_pb2_grpc.SupplierStub(self._grpc)

    def get_suppliers_by_codes(self, list_of_codes: List[int]) -> SuppliersByCodesResponse:
        logging.info(f"Call gRPC for supplier with code {list_of_codes[0]}")
        response = self._stub.GetSuppliersByCodes(SuppliersByCodesRequest(Codes=list_of_codes), timeout=10)
        return response
