import sys

data = int(1241241241241224124).to_bytes(8, sys.byteorder, signed=False)
print('conversion: ', data)

dataconv = int.from_bytes(data, sys.byteorder, signed=False)
print('conv2: ', dataconv)
