ages = [20,50,70,80,90,56]
ages = list(map(lambda x:x+1,ages))
print(ages)
#exercise 1 grades=[20,10,99,85,40,75,65,64,12,74,71,98,59]
#TASK   filter the grades to only display everyone above(and including70%
from functools import reduce
grades=[20,10,99,85,40,75,65,64,12,74,71,98,59]
def my_func(x):
    if x >= 70:
        return True
    else:
        return False
grades = list(filter(my_func, grades))
print(grades)
#excersis 2 dog_ages =[12,8,4,1,2,6,4,4,5]
#TASK   convert the ages into dog years(x7)
dog_ages =[12,8,4,1,2,6,4,4,5]
dog_ages =list(map(lambda x:x*7, dog_ages))
print(dog_ages)

#exercise 3 transactions =[51.0,49.99,80.99,67.99,120.52,23.49]
#TASK   convert the transactions to a single total