# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: C2.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='C2.proto',
  package='C2',
  syntax='proto3',
  serialized_options=b'Z\017golang/messages',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08\x43\x32.proto\x12\x02\x43\x32\x1a\x1fgoogle/protobuf/timestamp.proto\"O\n\x0cVictimStatus\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x31\n\rlastHeardFrom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"o\n\x08\x43\x32Update\x12\x11\n\tmalwareId\x18\x01 \x01(\t\x12!\n\x07victims\x18\x02 \x03(\x0b\x32\x10.C2.VictimStatus\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x11Z\x0fgolang/messagesb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VICTIMSTATUS = _descriptor.Descriptor(
  name='VictimStatus',
  full_name='C2.VictimStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='C2.VictimStatus.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastHeardFrom', full_name='C2.VictimStatus.lastHeardFrom', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=49,
  serialized_end=128,
)


_C2UPDATE = _descriptor.Descriptor(
  name='C2Update',
  full_name='C2.C2Update',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='malwareId', full_name='C2.C2Update.malwareId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='victims', full_name='C2.C2Update.victims', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='C2.C2Update.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=130,
  serialized_end=241,
)

_VICTIMSTATUS.fields_by_name['lastHeardFrom'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_C2UPDATE.fields_by_name['victims'].message_type = _VICTIMSTATUS
_C2UPDATE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['VictimStatus'] = _VICTIMSTATUS
DESCRIPTOR.message_types_by_name['C2Update'] = _C2UPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VictimStatus = _reflection.GeneratedProtocolMessageType('VictimStatus', (_message.Message,), {
  'DESCRIPTOR' : _VICTIMSTATUS,
  '__module__' : 'C2_pb2'
  # @@protoc_insertion_point(class_scope:C2.VictimStatus)
  })
_sym_db.RegisterMessage(VictimStatus)

C2Update = _reflection.GeneratedProtocolMessageType('C2Update', (_message.Message,), {
  'DESCRIPTOR' : _C2UPDATE,
  '__module__' : 'C2_pb2'
  # @@protoc_insertion_point(class_scope:C2.C2Update)
  })
_sym_db.RegisterMessage(C2Update)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
