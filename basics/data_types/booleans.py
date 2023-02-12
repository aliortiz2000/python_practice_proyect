"""
Boolean Values
    In programming you often need to know if an expression is True or False.
    You can evaluate any expression in Python, and get one of two answers, True or False.
    When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""
print(10 > 9)
print(10 == 9)
print(10 < 9)




"""
Most Values are True
    Almost any value is evaluated to True if it has some sort of content.
    Any string is True, except empty strings.
    Any number is True, except 0.
    Any list, tuple, set, and dictionary are True, except empty ones.
"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})