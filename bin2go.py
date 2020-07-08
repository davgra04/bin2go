import argparse
import sys

# parse args
########################################

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--width", type=int, default=120, help="sets maximum width in characters of output Go bytes array")
parser.add_argument("infile", help="file to convert into a Go bytes array")
args = parser.parse_args()

# read file
########################################

byte_list = []

with open(args.infile, "rb") as f:
    byte = f.read(1)
    while byte:
        byte_as_int = int.from_bytes(byte, byteorder=sys.byteorder)
        byte_list.append(byte_as_int)
        byte = f.read(1)

# print byte array
########################################

print("var myBytesArray []byte = []byte{")
line = "    {}, ".format(byte_list[0])

for b in byte_list[1:]:

    if len("{}{},".format(line, b)) > args.width:
        print(line)
        line = "    {}, ".format(b)
    else:
        line += "{}, ".format(b)

print(line)
print("}")
