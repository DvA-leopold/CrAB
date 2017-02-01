#!/usr/bin/env bash
protoc -I=blockchain_storage/protocol --python_out=blockchain_storage/protocol blockchain_storage/protocol/block.proto