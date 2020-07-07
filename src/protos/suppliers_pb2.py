# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: suppliers.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='suppliers.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fsuppliers.proto\"(\n\x17SuppliersByCodesRequest\x12\r\n\x05\x43odes\x18\x01 \x03(\x05\")\n\x18SuppliersByCodesResponse\x12\r\n\x05\x43odes\x18\x01 \x03(\x05\x32X\n\x08Supplier\x12L\n\x13GetSuppliersByCodes\x12\x18.SuppliersByCodesRequest\x1a\x19.SuppliersByCodesResponse\"\x00\x62\x06proto3'
)




_SUPPLIERSBYCODESREQUEST = _descriptor.Descriptor(
  name='SuppliersByCodesRequest',
  full_name='SuppliersByCodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Codes', full_name='SuppliersByCodesRequest.Codes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=59,
)


_SUPPLIERSBYCODESRESPONSE = _descriptor.Descriptor(
  name='SuppliersByCodesResponse',
  full_name='SuppliersByCodesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Codes', full_name='SuppliersByCodesResponse.Codes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['SuppliersByCodesRequest'] = _SUPPLIERSBYCODESREQUEST
DESCRIPTOR.message_types_by_name['SuppliersByCodesResponse'] = _SUPPLIERSBYCODESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SuppliersByCodesRequest = _reflection.GeneratedProtocolMessageType('SuppliersByCodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUPPLIERSBYCODESREQUEST,
  '__module__' : 'suppliers_pb2'
  # @@protoc_insertion_point(class_scope:SuppliersByCodesRequest)
  })
_sym_db.RegisterMessage(SuppliersByCodesRequest)

SuppliersByCodesResponse = _reflection.GeneratedProtocolMessageType('SuppliersByCodesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUPPLIERSBYCODESRESPONSE,
  '__module__' : 'suppliers_pb2'
  # @@protoc_insertion_point(class_scope:SuppliersByCodesResponse)
  })
_sym_db.RegisterMessage(SuppliersByCodesResponse)



_SUPPLIER = _descriptor.ServiceDescriptor(
  name='Supplier',
  full_name='Supplier',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=104,
  serialized_end=192,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSuppliersByCodes',
    full_name='Supplier.GetSuppliersByCodes',
    index=0,
    containing_service=None,
    input_type=_SUPPLIERSBYCODESREQUEST,
    output_type=_SUPPLIERSBYCODESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUPPLIER)

DESCRIPTOR.services_by_name['Supplier'] = _SUPPLIER

# @@protoc_insertion_point(module_scope)