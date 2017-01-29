# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class block(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsblock(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = block()
        x.Init(buf, n + offset)
        return x

    # block
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # block
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # block
    def MerkleRoot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # block
    def ParentBlockHash(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # block
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # block
    def DataBlock(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # block
    def DataBlockLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def blockStart(builder): builder.StartObject(5)
def blockAddVersion(builder, version): builder.PrependUint32Slot(0, version, 0)
def blockAddMerkleRoot(builder, merkleRoot): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(merkleRoot), 0)
def blockAddParentBlockHash(builder, parentBlockHash): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(parentBlockHash), 0)
def blockAddTimestamp(builder, timestamp): builder.PrependUint64Slot(3, timestamp, 0)
def blockAddDataBlock(builder, dataBlock): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(dataBlock), 0)
def blockStartDataBlockVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def blockEnd(builder): return builder.EndObject()