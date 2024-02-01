# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional
#         # Part as Answer
#         result = x // y
#         print("Yeah ! Your answer is :", result)
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#
#     # Look at parameters and note the working of Program
#
#
# divide(3, 2)
# divide(3, 0)

# def numberreverse(s):
#     str = " "
#     for ele in s:
#         str += ele
#     return str
#
# s = ["Hi", "Hello","How"]
# print(numberreverse(s))
#
# def my_function(x):
#   return x[::-1]
#
# x = my_function("I wonder how this text looks like backwards")
#
# print(x)

a = ("b", "g", "a", "d", "f", "c", "h", "e")
b=sorted(a)
print(b)