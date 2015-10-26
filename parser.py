import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-input', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.input)
print(args.accumulate(args.input))
__author__ = 'joezhou'
