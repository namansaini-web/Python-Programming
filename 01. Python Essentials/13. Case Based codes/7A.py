scores = {}
for i in range(1,6):
    name = input("Enter name of player : ")
    runs = int(input("Enter runs of that player : "))
    scores[name] = runs
print(scores)

sum = 0
for i in scores:
    sum += scores[i]
print("Average score : ", sum/5)

h_score = 0
for i in scores:
    if scores[i] > h_score:
        h_score = scores[i]
        h_scorer = i
print("Highest scorer : ", h_scorer, "-->", h_score)

# Bonus: 
player = max(scores, key = scores.get)