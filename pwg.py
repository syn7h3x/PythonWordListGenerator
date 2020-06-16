#!/bin/python
# -*- coding: UTF-8 -*-
# by @Syn7h3x

import argparse

charsets = []
modulos = []
length = 1
stack = 1

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%&*_+<>-=~?()'
symbols_extended = "!@#$%&*_+<>-=~?()\\/|^.,[]{}';:\""
digits = "0123456789"

help_message = '''+---------------------------+
| Python Wordlist Generator |
| By Syn7h3x                |
+---------------------------+

usage: pwg.py [OPTIONS] -p [PATTERN [PATTERN ...]] 

examples:
  pwg.py -H foo -p %d %d	pwg will generate a wordlist that starts at foo00 and ends with foo99

  pwg.py -H foo -T bar -p %S	pwg will generate a wordlist that starts at foo!bar and ends with foo"bar

  pwg.py %A%a %d %d %d 		pwg will generate a wordlist that starts at A000 and ends with z999

  pwg.py ABC 123 !@#   		pwg will generate a wordlist that starts at A1! and ends with C3#

default charsets:
  %d = 0123456789
  %a = abcdefghijklmnopqrstuvwxyz
  %A = ABCDEFGHIJKLMNOPQRSTUVWXYZ
  %s = !@#$%&*_+<>-=~?()
  %S = !@#$%&*_+<>-=~?()|/\\^.,[]{}';:"

optional arguments:
  -h, --help            			show this help message and exit
  -H, --head HEAD  				Append a string to the beginning of the text
  -o, --output OUTPUT				Write the result in a file
  -p, --pattern [PATTERN [PATTERN ...]]		The charset pattern to be used
  -q, --quiet           			Don't print the result
  -T, --tail TAIL  				Append a string to the end of the text
   '''


class MyParser(argparse.ArgumentParser):
    def format_help(self):
        return help_message


parser = MyParser(usage='pwg.py [OPTIONS] -p [PATTERN [PATTERN ...]]')
parser.add_argument("-H", "--head", help="Append a string to the beggining of the text", default='')
parser.add_argument("-o", "--output", help="Write the result in a file", type=argparse.FileType('w'))
parser.add_argument("-p", "--pattern", help="The charset pattern to be used", nargs='*', required=True)
parser.add_argument("-q", "--quiet", help="Don't print the result", action='store_true')
parser.add_argument("-T", "--tail", help="Append a string to the end of the text", default='')
args = parser.parse_args()

for arg in args.pattern:
    charset = ''

    if "%A" in arg:
        charset += alphabet_upper
    if "%a" in arg:
        charset += alphabet_lower
    if "%S" in arg:
        charset += symbols_extended
    elif "%s" in arg:
        charset += symbols
    if "%d" in arg:
        charset += digits
    charset += arg.replace('%A', '').replace('%a', '').replace('%S', '').replace('%s', '').replace('%d', '')
    charsets.append(charset)

charsets_len = len(charsets)
for i in range(charsets_len, 0, -1):
    length *= len(charsets[i-1])
    if i == charsets_len:
        modulos.append(stack)
    else:
        stack *= len(charsets[i])
        modulos.append(stack)
modulos.reverse()

for i in range(length):
    text = ''
    for j in range(charsets_len):
        text += charsets[j][(i // modulos[j]) % len(charsets[j])]
    if not args.quiet:
        print(args.head + text + args.tail)
    if args.output:
        args.output.write(args.head + text + args.tail + '\n')
