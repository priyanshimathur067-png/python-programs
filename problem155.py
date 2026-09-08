def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    ci = amount - p

    return ci


p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Compound Interest =", compound_interest(p, r, t))