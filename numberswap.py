a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
a = a + b + c # a = 1+2+3 = 6
b = a - (b + c) # b = 6- 2+3 = 1
c = a - (b + c) # c =  6- 1+3 = 2
a = a - (b + c) # a = a - 3 = 3
print("The new values are {0}, {1}, {2}.".format(a, b, c))