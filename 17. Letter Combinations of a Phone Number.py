import itertools



a = ["a", "b", "c"]
b = ["d", "e", "f"]
c = ["g", "h", "i"]


c = list(itertools.product(a, b))
print(c)