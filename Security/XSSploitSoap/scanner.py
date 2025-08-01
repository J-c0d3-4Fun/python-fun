import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', action='store_true', help='the url of the website')
subparsers = parser.add_subparsers(required=True)


parser_a = subparsers.add_parser('xss', help='used to find cross site scripting vulnerabilities')
parser_a.add_argument('-f', '--file', help='provide an input file with your XSS attacks')

parser_b = subparsers.add_parser('soap', help='used for soap payloads')
parser_b.add_argument('-f', '--file', help='provide an input file with your Soap attacks')

parser.parse_args()