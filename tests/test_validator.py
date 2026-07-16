from saes.validator import Validator

print("=" * 60)

samples = [

    "0110111101101011",

    "6F6B",

    "FFFF",

    "1010101010101010",

    "123",

    "XYZ"

]

for s in samples:

    print()

    print(s)

    print("Type :", Validator.detect_type(s))

    if Validator.detect_type(s):

        print("Value :", Validator.parse(s))