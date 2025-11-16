# **kwargs (Keyword Arguments)
# **kwargs collects any extra keyword arguments passed to a function into a dictionary. Again, kwargs is the conventional name, but you could use any valid variable name preceded by two asterisks (e.g., **data, **options).



def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks 
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, vikrant=54, jack=34, Marie=90, Priya=45)