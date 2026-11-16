passing = 0
for i in range(5):
    score = int(input("Score: "))
    if score >= 75:
        passing = passing + 1

print(passing, "of 5 passed")