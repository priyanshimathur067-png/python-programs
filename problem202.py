def func2(n) :
    if n == 0:
        return

    print(n)
    func2(n - 1)

n = int (input("Enter a no.  : "))
func2(n)