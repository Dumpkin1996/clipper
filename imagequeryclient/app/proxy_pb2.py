# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy.proto',
  package='proxytest',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bproxy.proto\x12\tproxytest\"\x11\n\x02hi\x12\x0b\n\x03msg\x18\x01 \x01(\t\"/\n\x05input\x12\x11\n\tinputType\x18\x01 \x01(\t\x12\x13\n\x0binputStream\x18\x02 \x01(\t\"B\n\tmodelinfo\x12\x11\n\tmodelName\x18\x01 \x01(\t\x12\x11\n\tmodelPort\x18\x02 \x01(\t\x12\x0f\n\x07modelId\x18\x03 \x01(\t\"\x13\n\x03\x64\x61g\x12\x0c\n\x04\x64\x61g_\x18\x01 \x01(\t\"\x1a\n\x08response\x12\x0e\n\x06status\x18\x01 \x01(\t2\x8d\x02\n\x0cProxyService\x12\x32\n\x07Predict\x12\x10.proxytest.input\x1a\x13.proxytest.response\"\x00\x12\x31\n\x06Return\x12\x10.proxytest.input\x1a\x13.proxytest.response\"\x00\x12\x37\n\x08SetModel\x12\x14.proxytest.modelinfo\x1a\x13.proxytest.response\"\x00\x12/\n\x06SetDAG\x12\x0e.proxytest.dag\x1a\x13.proxytest.response\"\x00\x12,\n\x04Ping\x12\r.proxytest.hi\x1a\x13.proxytest.response\"\x00\x62\x06proto3')
)




_HI = _descriptor.Descriptor(
  name='hi',
  full_name='proxytest.hi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='proxytest.hi.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=26,
  serialized_end=43,
)


_INPUT = _descriptor.Descriptor(
  name='input',
  full_name='proxytest.input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputType', full_name='proxytest.input.inputType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputStream', full_name='proxytest.input.inputStream', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=45,
  serialized_end=92,
)


_MODELINFO = _descriptor.Descriptor(
  name='modelinfo',
  full_name='proxytest.modelinfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modelName', full_name='proxytest.modelinfo.modelName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelPort', full_name='proxytest.modelinfo.modelPort', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelId', full_name='proxytest.modelinfo.modelId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=94,
  serialized_end=160,
)


_DAG = _descriptor.Descriptor(
  name='dag',
  full_name='proxytest.dag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dag_', full_name='proxytest.dag.dag_', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=162,
  serialized_end=181,
)


_RESPONSE = _descriptor.Descriptor(
  name='response',
  full_name='proxytest.response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proxytest.response.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=183,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['hi'] = _HI
DESCRIPTOR.message_types_by_name['input'] = _INPUT
DESCRIPTOR.message_types_by_name['modelinfo'] = _MODELINFO
DESCRIPTOR.message_types_by_name['dag'] = _DAG
DESCRIPTOR.message_types_by_name['response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

hi = _reflection.GeneratedProtocolMessageType('hi', (_message.Message,), dict(
  DESCRIPTOR = _HI,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:proxytest.hi)
  ))
_sym_db.RegisterMessage(hi)

input = _reflection.GeneratedProtocolMessageType('input', (_message.Message,), dict(
  DESCRIPTOR = _INPUT,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:proxytest.input)
  ))
_sym_db.RegisterMessage(input)

modelinfo = _reflection.GeneratedProtocolMessageType('modelinfo', (_message.Message,), dict(
  DESCRIPTOR = _MODELINFO,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:proxytest.modelinfo)
  ))
_sym_db.RegisterMessage(modelinfo)

dag = _reflection.GeneratedProtocolMessageType('dag', (_message.Message,), dict(
  DESCRIPTOR = _DAG,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:proxytest.dag)
  ))
_sym_db.RegisterMessage(dag)

response = _reflection.GeneratedProtocolMessageType('response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:proxytest.response)
  ))
_sym_db.RegisterMessage(response)



_PROXYSERVICE = _descriptor.ServiceDescriptor(
  name='ProxyService',
  full_name='proxytest.ProxyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=212,
  serialized_end=481,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='proxytest.ProxyService.Predict',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Return',
    full_name='proxytest.ProxyService.Return',
    index=1,
    containing_service=None,
    input_type=_INPUT,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetModel',
    full_name='proxytest.ProxyService.SetModel',
    index=2,
    containing_service=None,
    input_type=_MODELINFO,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetDAG',
    full_name='proxytest.ProxyService.SetDAG',
    index=3,
    containing_service=None,
    input_type=_DAG,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='proxytest.ProxyService.Ping',
    index=4,
    containing_service=None,
    input_type=_HI,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROXYSERVICE)

DESCRIPTOR.services_by_name['ProxyService'] = _PROXYSERVICE

# @@protoc_insertion_point(module_scope)
