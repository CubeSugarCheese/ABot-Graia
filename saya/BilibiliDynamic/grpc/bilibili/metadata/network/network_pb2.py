# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rnetwork.proto\x12\x19\x62ilibili.metadata.network\"{\n\x07Network\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.bilibili.metadata.network.NetworkType\x12-\n\x02tf\x18\x02 \x01(\x0e\x32!.bilibili.metadata.network.TFType\x12\x0b\n\x03oid\x18\x03 \x01(\t*^\n\x0bNetworkType\x12\x0e\n\nNT_UNKNOWN\x10\x00\x12\x08\n\x04WIFI\x10\x01\x12\x0c\n\x08\x43\x45LLULAR\x10\x02\x12\x0b\n\x07OFFLINE\x10\x03\x12\x0c\n\x08OTHERNET\x10\x04\x12\x0c\n\x08\x45THERNET\x10\x05*]\n\x06TFType\x12\x0e\n\nTF_UNKNOWN\x10\x00\x12\n\n\x06U_CARD\x10\x01\x12\t\n\x05U_PKG\x10\x02\x12\n\n\x06\x43_CARD\x10\x03\x12\t\n\x05\x43_PKG\x10\x04\x12\n\n\x06T_CARD\x10\x05\x12\t\n\x05T_PKG\x10\x06\x62\x06proto3')

_NETWORKTYPE = DESCRIPTOR.enum_types_by_name['NetworkType']
NetworkType = enum_type_wrapper.EnumTypeWrapper(_NETWORKTYPE)
_TFTYPE = DESCRIPTOR.enum_types_by_name['TFType']
TFType = enum_type_wrapper.EnumTypeWrapper(_TFTYPE)
NT_UNKNOWN = 0
WIFI = 1
CELLULAR = 2
OFFLINE = 3
OTHERNET = 4
ETHERNET = 5
TF_UNKNOWN = 0
U_CARD = 1
U_PKG = 2
C_CARD = 3
C_PKG = 4
T_CARD = 5
T_PKG = 6


_NETWORK = DESCRIPTOR.message_types_by_name['Network']
Network = _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), {
  'DESCRIPTOR' : _NETWORK,
  '__module__' : 'network_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.metadata.network.Network)
  })
_sym_db.RegisterMessage(Network)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NETWORKTYPE._serialized_start=169
  _NETWORKTYPE._serialized_end=263
  _TFTYPE._serialized_start=265
  _TFTYPE._serialized_end=358
  _NETWORK._serialized_start=44
  _NETWORK._serialized_end=167
# @@protoc_insertion_point(module_scope)
