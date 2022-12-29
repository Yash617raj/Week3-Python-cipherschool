def func(name,**kwargs):
    if kwargs.get("rev")==True:
        name=[j[::-1] for j in name]
    return [i.title() for i in name]
names=["harish","hitesh","halva"]
print(func(names,rev=True))