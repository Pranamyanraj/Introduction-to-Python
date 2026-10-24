answers = ["b", "a", "c","d" ]
correct = 0
score = 0
for given, right in zip(answers, ["b", "a", "c","d"]):
    if given == right:
        correct += 1
        score += 5
print(f"Correct answers: {correct}")
print(f"Score: {score}/4")
