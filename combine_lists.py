# # Gets the job done, but not optimized and generally has greater time complexity than other methods.

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# for i in list2:
#     list1.append(i)
# print(list1)

# # Combining more than 2 lists in Python. Two loops, imagine what time complexity must be like if our input is huge!

# list0 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9, 10]

# for i in list2:
#     list0.append(i)
# for i in list3:
#     list0.append(i)
# print(list0)

# # Pythons built-in extend method is better than using loops. Time complexity is O(n). Also, we are making changes to listor but not listy. 

# listy = [1, 2, 3, 4]
# listor = [5, 6, 7, 8]

# listor.extend(listy)
# print(listor)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.append(list2)
print(list1)