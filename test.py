#!/usr/bin/env python

import os

# First compile the Datum, protobuf so that we can load using protobuf
# This will create datum_pb2.py
os.system('protoc -I={0} --python_out={1} {0}proto/exchange_format.proto'.format("./", "./"))

import exchange_format_pb2 as proto

#data = open("./data/11-1727-965.traffic.protobuf", "rb").read()






