import colorset

c1, c2 = colorset.color.random()
c3 = colorset.color.get("gr", 2)

print(c1, c2, *c3)