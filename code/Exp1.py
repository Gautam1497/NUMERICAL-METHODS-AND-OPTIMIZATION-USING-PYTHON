#Variables
print("Variables")
age=24
name="Gautam Kumar"
uid="21BCS5998"
print(uid," ",name," ",age)
print()

#Data types
print("Data types")
num_int=24
num_float=24.02
print("num_int-",type(num_int),"num_float-",type(num_float))
print()

my_list=[1,2,3,"four",5.0] # it is mutable because it is using list data structure
my_list.remove(2)
print(my_list)
my_tuple=(1,2,3,"four",5.0)# it is mutable because it is using tuple data structure
print(my_tuple)
print()

print("Control Structure")
print("if statement")
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
print()

print("Loops")
print("For Loops")
for i in range(5):
    print(i)
print("While Loops")
count = 0
while count < 5:
    print(count)
    count += 1
print()

print("Functions")
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


