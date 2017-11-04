import argparse

parser = argparse.ArgumentParser()

parser.add_argument("searchString",help="Search String to be found")
parser.add_argument("fileName",help="Filename to be searched")
parser.add_argument("threshold",help="Minimum of occurrences of searchString", type=int)
parser.add_argument("--linecount",help="Count lines in file")

args = parser.parse_args()

print args.searchString
print args.fileName
print args.threshold
if args.linecount:
	print args.linecount

print "Type of threshold is:",type(args.threshold)
