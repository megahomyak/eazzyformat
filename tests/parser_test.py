from eazzyformat import parse_eazzyformat

print(parse_eazzyformat(r"""
[
    "abc" "quote: \" AFTER QUOTE \\ <- SPECIAL SYMBOL"
    "String with a
     newline"
     "Another

      string"]
"""))
