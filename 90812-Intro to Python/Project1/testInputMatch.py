import re

POS_FLOAT_NUMBER_PATTERN = "^[+]?[0-9]*\.?[0-9]+"
p = re.compile(POS_FLOAT_NUMBER_PATTERN)
print(p.match("123") != None)
assert((p.match("123") != None) == True)
assert(p.match("123.4") == True)
assert(p.match("0") == True)
assert(p.match("0.0") == True)
assert(p.match("+123") == True)
assert(p.match("+123.4") == True)
assert(p.match("-123") == False)
assert(p.match("-0") == False)
assert(p.match("-4") == False)
assert(p.match("-12.3") == False)