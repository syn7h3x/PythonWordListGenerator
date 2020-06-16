# PythonWordListGenerator
A python tool for custom wordlist list generator with pattern
## Usage 
`pwg.py [OPTIONS] -p [PATTERN [PATTERN ...]] `

## Examples
  `pwg.py -H foo -p %d %d`	_pwg will generate a wordlist that starts at **foo00** and ends with **foo99**_

  `pwg.py -H foo -T bar -p %S`	_pwg will generate a wordlist that starts at **foo!bar** and ends with **foo"bar**_

  `pwg.py %A%a %d %d %d` 		_pwg will generate a wordlist that starts at **A000** and ends with **z999**_

  `pwg.py ABC 123 !@#`   		_pwg will generate a wordlist that starts at **A1!** and ends with **C3#**_

## Default charsets
Symbol | Charset
------ | -------
  %d | 0123456789
  %a | abcdefghijklmnopqrstuvwxyz
  %A | ABCDEFGHIJKLMNOPQRSTUVWXYZ
  %s | !@#$%&*_+<>-=~?()
  %S | \!\@\#\$\%\&\*\_\+\<\>\-\=\~\?\(\)\\/\|\^\.\,\[\]\{\}\'\;\:\"

## Arguments
Flag | Description
---- | -----------
  -h, --help            			|Show this help message and exit
  -H, --head HEAD  				|Append a string to the beginning of the text
  -o, --output OUTPUT				|Write the result in a file
  -p, --pattern [PATTERN [PATTERN ...]]		|The charset pattern to be used
  -q, --quiet           			|Don't print the result
  -T, --tail TAIL  				|Append a string to the end of the text
