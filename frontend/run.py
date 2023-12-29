import argparse

from src.bashmemo.main import run

parser = argparse.ArgumentParser(
    prog='Bashmemo',
    description='Second brain to remind commands',
    epilog='')
parser.add_argument('-b', '--bookmark', action='store_true')
parser.add_argument('-ad', '--autodiscover')

args = parser.parse_args()


run(args)
