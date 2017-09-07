
import argparse

def do_option1(args):
    param1 = args.param1
    print(param1)
    # And continue

p = argparse.ArgumentParser()
subparsers = p.add_subparsers()

option1_parser = subparsers.add_parser('option1')
# Add specific options for option1 here, but here's
# an example
option1_parser.add_argument('param1')
option1_parser.add_argument('param2')
option1_parser.set_defaults(func=do_option1)



args = p.parse_args()
args.func(args)

