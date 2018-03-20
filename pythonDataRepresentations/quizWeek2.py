
#Problem #1
# list1 = list(range(0,5,1))
# print(list1)
# list2 = range(0,5)
# print(list2)
# list3 = list(range(0,4,1))
# print(list3)
# list4 = list(range(0,5))
# print(list4)
# print()

#Problem #2
my_list = ["This", "course","is", "great", "yes"]
# print(len(my_list))
# print(my_list[3])

#Problem #3
# print(my_list[0:len(my_list)//2])
# print(my_list[len(my_list)+1//2:len(my_list)])
# print()


# print(𝚖𝚢_𝚕𝚒𝚜𝚝[0:𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)//2])
# print(𝚖𝚢_𝚕𝚒𝚜𝚝[𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)//2:𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)])
# print()

# print(𝚖𝚢_𝚕𝚒𝚜𝚝[:𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)//2])
# print(𝚖𝚢_𝚕𝚒𝚜𝚝[𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)//2:])
# print()

# print(𝚖𝚢_𝚕𝚒𝚜𝚝[:𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)//2-1])
# print(𝚖𝚢_𝚕𝚒𝚜𝚝[𝚕𝚎𝚗(𝚖𝚢_𝚕𝚒𝚜𝚝)//2:])

#Problem #4
# n=4
# m=2
# init_list = list(range(1,n))
# print(init_list)
# final_list = init_list*m
# print(final_list)
# print(len(final_list))
#Len is (n-1)*m

#Problem #5
# n=6
# test_string = "xxx" + " " * n + "xxx"
# split_list = test_string.split(" ")
# print(split_list)
# print(len(split_list))
#len is n+1

#Problem #6
# list1 = list(range(1,10))
# print(list1)
# list2 = list1[:]
# print(list2)

# list1 = list(range(1, 10))
# print(list1)
# list2 = list1[:]
# print(list2)

# list1 = list(range(1, 10))
# print(list1)
# list2 = [] + list1
# print(list2)

#SUPER ODD I DIDN'T REALIZ 2 DIFFERENT VARIABLES COULD AFFECT EACH OTHER
# list1 = list(range(1, 10))
# list2 = list1
# list2[0]=4
# print(list1)
# print(list2)


#Problem #7
# def strange_sum(numbers):
#         i = 0
#         total = 0

#         for num in numbers:
#                 if num % 3 != 0:
#                         total = total+num
#                         print(total)


# strange_sum(list(range(123)) + list(range(77)))
#Answer is 6994

i = 1
b = i 
b = b + 1
print(i)
print(b)