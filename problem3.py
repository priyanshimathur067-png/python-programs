num = []
n = int(input("hoe many no.s: "))
for i in range(n):
    value = int(input("Enter a no.:"))
    num.append(value)
    if value % 2 != 0 :
        count+ = 1
print("The no. of odd no.s are:")