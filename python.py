# text = "hello sherbano"
# result = " ".join(text.split()[::-1])
# print(result)
# # ______________________
# lst = [10, 20, 4, 45, 99]
# lst = list(set(lst))
# lst.sort()
# print(lst[-2])
# # ___________________
# text = "aabbc"
# freq = {}
# for ch in text:
#     freq[ch] = freq.get(ch, 0) + 1
# print(freq)
# # __________________________
# text = "madam"
# is_palindrome = True
# for i in range(len(text)//2):
#     if text[i] != text[-i-1]:
#         is_palindrome = False

# print(is_palindrome)
# # ___________________________
# import math
# print(math.sqrt(16))
# # _________________________
# class Test:
#     def __init__(self):
#         self.__x = 10
#     def get_x(self):
#         return self.__x
# t = Test()
# print(t.get_x())
# # _________________________
# def find_max(a, b):
#     return a if a > b else b
# print(find_max(5, 10))
# # ________________________
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
# # ______________________________
# class Car:
#     def __init__(self, name):
#         self.name = name
# c = Car("BMW")
# print(c.name)        
# # ___________________________
# a = {1, 2}
# b = {2, 3}
# print(a | b)