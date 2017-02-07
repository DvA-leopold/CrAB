# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='block.proto',
  package='blockchain',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x62lock.proto\x12\nblockchain\"\xf6\x01\n\x05\x42lock\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.blockchain.Block.Header\x12\x35\n\x0b\x62ranch_data\x18\x02 \x03(\x0b\x32 .blockchain.Block.TreeBranchData\x1aW\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x13\n\x0bmerkle_root\x18\x02 \x01(\x0c\x12\x14\n\x0cparent_block\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\r\x1a\x33\n\x0eTreeBranchData\x12\x13\n\x0bparent_hash\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BLOCK_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='blockchain.Block.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='blockchain.Block.Header.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='merkle_root', full_name='blockchain.Block.Header.merkle_root', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_block', full_name='blockchain.Block.Header.parent_block', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='blockchain.Block.Header.timestamp', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=221,
)

_BLOCK_TREEBRANCHDATA = _descriptor.Descriptor(
  name='TreeBranchData',
  full_name='blockchain.Block.TreeBranchData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent_hash', full_name='blockchain.Block.TreeBranchData.parent_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='blockchain.Block.TreeBranchData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=274,
)

_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blockchain.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='blockchain.Block.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='branch_data', full_name='blockchain.Block.branch_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BLOCK_HEADER, _BLOCK_TREEBRANCHDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=274,
)

_BLOCK_HEADER.containing_type = _BLOCK
_BLOCK_TREEBRANCHDATA.containing_type = _BLOCK
_BLOCK.fields_by_name['header'].message_type = _BLOCK_HEADER
_BLOCK.fields_by_name['branch_data'].message_type = _BLOCK_TREEBRANCHDATA
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(

  Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
    DESCRIPTOR = _BLOCK_HEADER,
    __module__ = 'block_pb2'
    # @@protoc_insertion_point(class_scope:blockchain.Block.Header)
    ))
  ,

  TreeBranchData = _reflection.GeneratedProtocolMessageType('TreeBranchData', (_message.Message,), dict(
    DESCRIPTOR = _BLOCK_TREEBRANCHDATA,
    __module__ = 'block_pb2'
    # @@protoc_insertion_point(class_scope:blockchain.Block.TreeBranchData)
    ))
  ,
  DESCRIPTOR = _BLOCK,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Block)
  ))
_sym_db.RegisterMessage(Block)
_sym_db.RegisterMessage(Block.Header)
_sym_db.RegisterMessage(Block.TreeBranchData)


# @@protoc_insertion_point(module_scope)
