import sys

charsets = []
modulos = []
length = 1
stack = 1

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%&*_+<>-=~?()'
symbols_extended = "!@#$%&*_+<>-=~?()\\/|^.,[]{}';:\""
digits = "0123456789"

for arg in sys.argv[1:]:
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
    print(text)
