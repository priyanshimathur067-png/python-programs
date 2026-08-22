# Combining *args and **kwargs
def func(title, *args, **kwargs):
    print("Title :",title)
    print("Positional Arguments: ",args)
    print("Keyword Arguments: ",kwargs)
func("User Info","Emil", "Taiba", age = 25, city = "Bly")