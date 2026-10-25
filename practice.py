even_squares = { i: i*i for i in range(1, 11) if i % 2 == 0}
print(even_squares)
d = {"a": 1}
print(d.get("b"))
print(d.get("b", 0) + 1)
# print(d["b"])