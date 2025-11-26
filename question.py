# def evenodd(num):
#     """
#     Determines if a number is even or odd.

#     Parameters:
#     num (int): The number to check.

#     Returns:
#     str: "Even" if the number is even, "Odd" if the number is odd.
#     """
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# # Example usage:
# result = evenodd(11)
# print(result)  # Output: Even


# def squarecube(num):
#     square = num**2
#     cube = num**3
#     return square, cube
# result = squarecube(100)
# print(result)

# def  factorial(n):
#     n = int(input("Enter a number: "))
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(100000000))



# def numberofvowels(s):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# result = numberofvowels("cwutycgxdmjuectfeacg,eukqyfcvlreqlycghvjre.gqvljhqgbj,dfsc,juryhgvqhfd,mchyugrfvjqh,cmdygverq,fchmgyveqr,ncfgveq rcfyuj")
# print(result)

# def reverse_string(s):
#     return s[::-1]
# result = reverse_string("bahan ke lund madharchod teri ma ki chool land ke")
# print(result)

# def vote_eligibility(age):
#     if age >= 18:
#         return "eligible to vote"
#     else:
#         return "not eligible to vote"

# n = int(input("Enter your age: "))
# result = vote_eligibility(n)
# print(result)
    
# def sum_of_all_number_in_list(n):
#     return sum(n)
# numbers = [1, 2, 3, 4, 5]
# result = sum_of_all_number_in_list(numbers)
# print(result)
















# def sumofallnumberinlist(n):
#     return sum(n)
# number=[1,34,5,6,7,4,87,90,34,54,23,12,45,67,89,23,45,67,89,90,21,43,65,87,32,14,56,78,90]
# result = sumofallnumberinlist(number)
# print(result)

# def vowelcount(s):
#     count = 0
#     vowels ="aeiouAEIOU"
#     for char in s:
#         if char in vowels:
#             count += 1
#             return count
#         s = "asdkjfhgqweoiuayxcvbnmASDFGHJKLZXCVBNMQWERTYUIOP"
#         result = vowelcount(s)
#         print(result)

# for i in range(11):
#     print(i)
#     if i == 0:
#         pass

# i = 1
# while i<11:
#     print(i)
#     i += 1
#     if i == 0:
#         pass

#sum of digit by loop
# sum =0
# for i in range (1,11):
#     sum += i
# print(sum)

# even numbers from 1 to 50
# for i in range (0,51):
#     if  i%2 == 0:
#         print(i)
# else:
#     pass

# for i in range (0,50):
#     if i%2 != 0:
#         print(i)
# else:
#     pass
# n = int(input())
# for i in range (1,11):
#     print(f"{n} x {i}= {n*i}")
     
# l = (1,2,3,4,5,6,7,8,10)
# sum = sum(l)
# print(sum)
# if avg := sum / len(l):
#     print(avg)
# else:
#     pass

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial (n-1)
# result = factorial(8)
# print(result)

# dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# key1 = dict.keys()
# value1 = dict.values()
# key2 = dict.keys()
# value2 = dict.values()
# key3 = dict.keys()
# value3 = dict.values()
# key4 = dict.keys()
# value4 = dict.values()
# for key, value in dict.items():
#     print(f"Key: {key}, Value: {value}")


# dict = {'jfgv': 2, 'khygf ': 4, 'hjg k': 6, 'yitkgv': 8}
# key1 = dict.keys()
# value1 = dict.values()
# key2 = dict.keys()
# value2 = dict.values()
# key3 = dict.keys()
# value3 = dict.values()
# key4 = dict.keys()
# value4 = dict.values()
# for key, value in dict.items():
#     print(f"key: {key}, value: {value}")
    
# l = [1,2,3,4,5,6,7,8,9,10]
# print(l)
# t = (12,3,4,5,654,43,42,)
# print(t)
# print(tuple(l))

# print(list(t))
# d = {'dhruv':100,'choudhary':200,'kumar':300}
# key1 = d.keys()
# value1  = d.values()
# key2 = d.keys()
# value2 = d.values()
# key3 = d.keys()
# value3 = d.values()
# for key, value in d.items():
#     print(f"key: {key}, value: {value}")


#frunion and intersection of two sets
# set1 = {1,4,9,8,6,2}
# set2 = {3,2,8,7,1,4}
# us = set1.union(set2)
# es = set1.intersection(set2)
# print(us)
# print(es)

l = [1,2,3,4,5,6,6,5,7,8,7,8,9,10]
# us = list(set(l))
# print(us)


# tup = (1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,21,21,2324,2324)
# hf = tuple(set(tup))
# print(hf)

# def is_polindrone(s):
#     s = s.lower()
#     return s[::-1] == s
# print(is_polindrone("Madam"))
# print(is_polindrone("Hello"))
# print(is_polindrone("Racecar"))

# def is_polindrone(s):
#     s =s.lower()
#     return s[::-1]==s
# print(is_polindrone("lolo"))
# print(is_polindrone("drord"))
# print(is_polindrone("pyp"))

#using function find maximum and minimum element in list
# def max_min(l):
#     maximum = max(l)
#     minimum = min(l)
#     return maximum, minimum
# l = [12,34,5,67,89,90,23,45,67,89,21,43,65,87]
# result = max_min(l)
# print(result)

# def max_min(l):
#     maximum = max(l)
#     minimum = min(l)
#     return maximum,minimum
# l =[11,22,32,43,5,345,2,43,5,4,0,434,98,434]
# result = max_min(l)
# print(result)

      
# def is_polindrone(s):
#     s= s.lower()
#     return s[::-1]==s
# print(is_polindrone("Liril"))
# print(is_polindrone("Dhruv"))

# write a function that take a dictionary and return a key with the highest value

# def key_with_highest_value(d):
#     if not d:
#         return None
#     highest_key = max(d, key=d.get)
#     return highest_key
# d = {'a': 10, 'b': 25, 'c': 15}
# result = key_with_highest_value(d)
# print(result)

# def only_even_numbers(l):
#     even_numbers = [num for num in l if num % 2 == 0]
#     return even_numbers

# l = [1,2,3,4,5,6,7,8,9,12,1,34,14,25,36,46,467,57,57,57,45,25,23,34,54,65,76,87,98,89,90]
# result = only_even_numbers(l)
# print(result)
# def only_odd_numbers(l):
#     odd_numbers = [num for num in l if num % 2 != 0]
#     return odd_numbers
# l = [1,2,3,4,5,6,7,8,9,12,1,34,14,25,36,46,467,57,57,57,45,25,23,34,54,65,76,87,98,89,90]
# result = only_odd_numbers(l)
# print(result)

# def merge_two_dicts(d1,d2):
#     merge_dict = {**d1,**d2}
#     return merge_dict
# d1 ={'a':1,'b':2,'c':3}
# d2 ={'d':4,'e':5,'f':6}
# result =merge_two_dicts(d1,d2)
# print(result)

# def merge_two_lists(l1,l2):
#     merge_list = l1+l2
#     return merge_list
# l1 = [1,2,3,4,5,6]
# l2 =[2,3,4,5,6,5,89,0]
# result = merge_two_lists(l1,l2)
# print(result)

 

# Print prime numbers from 1 to 100 using for loop
# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)
# print pattern using Look
for i in range(1,100):
    for j in range(1,i+1):
        print(j, end="")
    print()









