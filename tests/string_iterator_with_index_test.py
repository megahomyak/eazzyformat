from eazzyformat.string_iterators import StringIteratorWithIndex

string_iterator = StringIteratorWithIndex("abcdefg")

string_iterator.skip_to("c")
print(string_iterator.collect_to("f"))
print(next(string_iterator))
print(next(string_iterator))
try:
    print(next(string_iterator))
except StopIteration as stop_iteration:
    print(repr(stop_iteration))
try:
    print(string_iterator.skip_to("-"))
except StopIteration as stop_iteration:
    print(repr(stop_iteration))


print("\n-----\n")


string_iterator = StringIteratorWithIndex("abcdef")
string_iterator.skip_to("c")
for character in string_iterator:
    print(character)
