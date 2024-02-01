# from collections import Counter
# from itertools import count
#
# string= "pppppppghhhijeuupffe"
# print(string)
#
# result= Counter(string)
# result= max(result, key=result.get)
# print("Most frequent character: ",result)
# print("Count of e in GeeksforGeeks is : "
#       + str(count[result]))
#
#
# # test_str = "GeeksforGeeks"
# # res = max(test_str, key=lambda x: test_str.count(x))
# # print(len(res))
# # print(res)

from collections import Counter

# initializing string
test_str = "Geeks for Geeks"
str1=test_str.replace(" ", "")
print(str1)
# using collections.Counter() to get count
# counting e
result = Counter(str1)
result1= max(result, key=result.get)
print("Most frequent character: ",result1)
#
# printing result
print("Count of e in GeeksforGeeks is : "
      + str(result[result1]))


# test_str = "GeeksforGeeks"
#
# # using operator.countOf() to get count
# # counting e
# counter = op.countOf(test_str, "e")
#
# # printing result
# print("Count of e in GeeksforGeeks is : "
#       + str(counter))