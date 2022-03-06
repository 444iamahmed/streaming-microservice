# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movie_list.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10movie_list.proto\"\x1a\n\tBoolValue\x12\r\n\x05value\x18\x01 \x01(\x08\"\"\n\x05Movie\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\"2\n\x08ListItem\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x15\n\x05movie\x18\x02 \x01(\x0b\x32\x06.Movie\"#\n\x10MovieListRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"/\n\x11MovieListResponse\x12\x1a\n\nmovie_list\x18\x01 \x03(\x0b\x32\x06.Movie2\x85\x01\n\x04List\x12\x30\n\x07GetList\x12\x11.MovieListRequest\x1a\x12.MovieListResponse\x12\"\n\tAddToList\x12\t.ListItem\x1a\n.BoolValue\x12\'\n\x0eRemoveFromList\x12\t.ListItem\x1a\n.BoolValueb\x06proto3')



_BOOLVALUE = DESCRIPTOR.message_types_by_name['BoolValue']
_MOVIE = DESCRIPTOR.message_types_by_name['Movie']
_LISTITEM = DESCRIPTOR.message_types_by_name['ListItem']
_MOVIELISTREQUEST = DESCRIPTOR.message_types_by_name['MovieListRequest']
_MOVIELISTRESPONSE = DESCRIPTOR.message_types_by_name['MovieListResponse']
BoolValue = _reflection.GeneratedProtocolMessageType('BoolValue', (_message.Message,), {
  'DESCRIPTOR' : _BOOLVALUE,
  '__module__' : 'movie_list_pb2'
  # @@protoc_insertion_point(class_scope:BoolValue)
  })
_sym_db.RegisterMessage(BoolValue)

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), {
  'DESCRIPTOR' : _MOVIE,
  '__module__' : 'movie_list_pb2'
  # @@protoc_insertion_point(class_scope:Movie)
  })
_sym_db.RegisterMessage(Movie)

ListItem = _reflection.GeneratedProtocolMessageType('ListItem', (_message.Message,), {
  'DESCRIPTOR' : _LISTITEM,
  '__module__' : 'movie_list_pb2'
  # @@protoc_insertion_point(class_scope:ListItem)
  })
_sym_db.RegisterMessage(ListItem)

MovieListRequest = _reflection.GeneratedProtocolMessageType('MovieListRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVIELISTREQUEST,
  '__module__' : 'movie_list_pb2'
  # @@protoc_insertion_point(class_scope:MovieListRequest)
  })
_sym_db.RegisterMessage(MovieListRequest)

MovieListResponse = _reflection.GeneratedProtocolMessageType('MovieListResponse', (_message.Message,), {
  'DESCRIPTOR' : _MOVIELISTRESPONSE,
  '__module__' : 'movie_list_pb2'
  # @@protoc_insertion_point(class_scope:MovieListResponse)
  })
_sym_db.RegisterMessage(MovieListResponse)

_LIST = DESCRIPTOR.services_by_name['List']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOLVALUE._serialized_start=20
  _BOOLVALUE._serialized_end=46
  _MOVIE._serialized_start=48
  _MOVIE._serialized_end=82
  _LISTITEM._serialized_start=84
  _LISTITEM._serialized_end=134
  _MOVIELISTREQUEST._serialized_start=136
  _MOVIELISTREQUEST._serialized_end=171
  _MOVIELISTRESPONSE._serialized_start=173
  _MOVIELISTRESPONSE._serialized_end=220
  _LIST._serialized_start=223
  _LIST._serialized_end=356
# @@protoc_insertion_point(module_scope)
