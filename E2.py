names = []
nn = int(input("How many names? "))
for i in range(nn):
    name = input("Name: ")
    names.append(name)
print(names)
print(len(names), "names stored")