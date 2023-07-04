def even_numbers(my_list):
    return list(i for i in my_list if i%2==0)

l=[1,2,3,4,5,6,7,8,9,10]
print(even_numbers(l))
