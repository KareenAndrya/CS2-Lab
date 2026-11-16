def find(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

titles = []
copies = []
for i in range(3):
    title = input("Title: ")
    titles.append(title)
    ncopies = int(input("Copies: "))
    copies.append(ncopies)

stitle = input("Search title: ")
index = find(titles, stitle)
if index != -1:
    print(stitle, "has", copies[index], "copies")
else:
    print("Not in the library")

