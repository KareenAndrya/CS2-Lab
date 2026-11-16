scores = []
for i in range(5):
    score = int(input("Score: "))
    scores.append(score)
    
total = sum(scores)
print("Total:", total)
print("Average:", total / len(scores))
