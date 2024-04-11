utensils = {"hammer","spoon","knife","knife","knife"}

utensils.add("fork")
utensils.remove("hammer")
dishes = {"bowl","plate","cup"}

dinner_table = utensils.union(dishes)
#for x in utensils:
#   print(x)

for y in dinner_table:
    print(y)