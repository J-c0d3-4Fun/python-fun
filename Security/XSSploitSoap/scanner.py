import argparse


parser = argparse.ArgumentParser()
parser.add_argument('xss', action='store_true', help='used to find cross site scripting vulnerabilities')
parser.add_argument('soap', action='store_true', help='used for soap payloads')

subparsers = parser.add_subparsers(required=True)


args = parser.parse_args()

args = parser.parse_args()