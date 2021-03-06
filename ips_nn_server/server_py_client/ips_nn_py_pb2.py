# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ips_nn_py.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ips_nn_py.proto',
  package='ips_data_exchange',
  syntax='proto3',
  serialized_options=b'\n\032io.ipsnn.ips_data_exchangeB\021ips_data_exchangeP\001\242\002\005IPSNN',
  serialized_pb=b'\n\x0fips_nn_py.proto\x12\x11ips_data_exchange\"8\n\x07\x64\x61ta2nn\x12\x11\n\tdevserial\x18\x01 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x03(\t\x12\x0c\n\x04rssi\x18\x03 \x03(\x02\"~\n\x05nn2db\x12\x10\n\x08p_frst_x\x18\x01 \x01(\t\x12\x10\n\x08p_frst_y\x18\x02 \x01(\t\x12\x10\n\x08p_scnd_x\x18\x03 \x01(\t\x12\x10\n\x08p_scnd_y\x18\x04 \x01(\t\x12\x11\n\tdevserial\x18\x05 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x06 \x03(\t\x12\x0c\n\x04rssi\x18\x07 \x03(\x02\"\"\n\x0fresponse2client\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2[\n\tExchanger\x12N\n\nputData2nn\x12\x1a.ips_data_exchange.data2nn\x1a\".ips_data_exchange.response2client\"\x00\x32V\n\x06Putter\x12L\n\nputData2DB\x12\x18.ips_data_exchange.nn2db\x1a\".ips_data_exchange.response2client\"\x00\x42\x39\n\x1aio.ipsnn.ips_data_exchangeB\x11ips_data_exchangeP\x01\xa2\x02\x05IPSNNb\x06proto3'
)




_DATA2NN = _descriptor.Descriptor(
  name='data2nn',
  full_name='ips_data_exchange.data2nn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devserial', full_name='ips_data_exchange.data2nn.devserial', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='ips_data_exchange.data2nn.addr', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='ips_data_exchange.data2nn.rssi', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=38,
  serialized_end=94,
)


_NN2DB = _descriptor.Descriptor(
  name='nn2db',
  full_name='ips_data_exchange.nn2db',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_frst_x', full_name='ips_data_exchange.nn2db.p_frst_x', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_frst_y', full_name='ips_data_exchange.nn2db.p_frst_y', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_scnd_x', full_name='ips_data_exchange.nn2db.p_scnd_x', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_scnd_y', full_name='ips_data_exchange.nn2db.p_scnd_y', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devserial', full_name='ips_data_exchange.nn2db.devserial', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='ips_data_exchange.nn2db.addr', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='ips_data_exchange.nn2db.rssi', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=96,
  serialized_end=222,
)


_RESPONSE2CLIENT = _descriptor.Descriptor(
  name='response2client',
  full_name='ips_data_exchange.response2client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='ips_data_exchange.response2client.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=224,
  serialized_end=258,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='ips_data_exchange.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=260,
  serialized_end=267,
)

DESCRIPTOR.message_types_by_name['data2nn'] = _DATA2NN
DESCRIPTOR.message_types_by_name['nn2db'] = _NN2DB
DESCRIPTOR.message_types_by_name['response2client'] = _RESPONSE2CLIENT
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

data2nn = _reflection.GeneratedProtocolMessageType('data2nn', (_message.Message,), {
  'DESCRIPTOR' : _DATA2NN,
  '__module__' : 'ips_nn_py_pb2'
  # @@protoc_insertion_point(class_scope:ips_data_exchange.data2nn)
  })
_sym_db.RegisterMessage(data2nn)

nn2db = _reflection.GeneratedProtocolMessageType('nn2db', (_message.Message,), {
  'DESCRIPTOR' : _NN2DB,
  '__module__' : 'ips_nn_py_pb2'
  # @@protoc_insertion_point(class_scope:ips_data_exchange.nn2db)
  })
_sym_db.RegisterMessage(nn2db)

response2client = _reflection.GeneratedProtocolMessageType('response2client', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE2CLIENT,
  '__module__' : 'ips_nn_py_pb2'
  # @@protoc_insertion_point(class_scope:ips_data_exchange.response2client)
  })
_sym_db.RegisterMessage(response2client)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'ips_nn_py_pb2'
  # @@protoc_insertion_point(class_scope:ips_data_exchange.Empty)
  })
_sym_db.RegisterMessage(Empty)


DESCRIPTOR._options = None

_EXCHANGER = _descriptor.ServiceDescriptor(
  name='Exchanger',
  full_name='ips_data_exchange.Exchanger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=269,
  serialized_end=360,
  methods=[
  _descriptor.MethodDescriptor(
    name='putData2nn',
    full_name='ips_data_exchange.Exchanger.putData2nn',
    index=0,
    containing_service=None,
    input_type=_DATA2NN,
    output_type=_RESPONSE2CLIENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXCHANGER)

DESCRIPTOR.services_by_name['Exchanger'] = _EXCHANGER


_PUTTER = _descriptor.ServiceDescriptor(
  name='Putter',
  full_name='ips_data_exchange.Putter',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=362,
  serialized_end=448,
  methods=[
  _descriptor.MethodDescriptor(
    name='putData2DB',
    full_name='ips_data_exchange.Putter.putData2DB',
    index=0,
    containing_service=None,
    input_type=_NN2DB,
    output_type=_RESPONSE2CLIENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUTTER)

DESCRIPTOR.services_by_name['Putter'] = _PUTTER

# @@protoc_insertion_point(module_scope)
