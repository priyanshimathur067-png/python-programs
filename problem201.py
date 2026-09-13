def func(i):
    if i == 0:
        return 

    func(i - 1)
    print(i)

i = int (input("Enter a number: ") )
func(i)