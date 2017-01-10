__author__ = 'robbie'


from opdracht2 import mystack


example_1 = "((<>)())"
example_2 = "[((<>))]()(()())"
example_3 = "((<>))"
example_4 = "([)]"
example_5 = "(((<)>))"
example_6 = "())"

def is_legid_expession(str):
    stack = mystack()
    opening = "([<"
    closing = ")]>"
    for c in str:
        if c in opening:
            stack.push(c)
        if c in closing:
            if stack.isEmpty():
                return False
            if stack.peek() == opening[closing.index(c)]:
                stack.pop()
            else:
                return False

    return True

print(is_legid_expession(example_1))
print(is_legid_expession(example_2))
print(is_legid_expession(example_3))
print(is_legid_expession(example_4))
print(is_legid_expession(example_5))
print(is_legid_expession(example_6))