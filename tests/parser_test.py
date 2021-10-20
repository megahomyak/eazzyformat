from eazzyformat import parse_eazzyformat

print(parse_eazzyformat(r"""
["abc" "quote: \" AFTER QUOTE \\ <- SPECIAL SYMBOL"]
"""))
