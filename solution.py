# ==========================================
# Student Score Analyzer - Full Solution
# ==========================================

students = ["Alice", "Ben", "Chloe", "Daniel", "Eva"]
scores = [78, 55, 92, 67, 81]

print("=== Task 1: Student Scores ===")
for i in range(len(students)):
    print(students[i], ":", scores[i])

print("\n=== Task 2: Average Score ===")
avg = sum(scores) / len(scores)
print("Average score:", round(avg, 1))

print("\n=== Task 3: Top Performer ===")
max_score = scores[0]
max_index = 0

for i in range(len(scores)):
    if scores[i] > max_score:
        max_score = scores[i]
        max_index = i

print("Top student:", students[max_index], "with", max_score)

print("\n=== Task 4: Pass / Fail Count ===")
pass_count = 0
fail_count = 0

for score in scores:
    if score >= 60:
        pass_count += 1
    else:
        fail_count += 1

print("Pass:", pass_count)
print("Fail:", fail_count)

print("\n=== Task 5: Above Average Students ===")
above_avg_students = []

for i in range(len(scores)):
    if scores[i] > avg:
        above_avg_students.append(students[i])

print("Above average:", ", ".join(above_avg_students))

print("\n=== Challenge: Ranking ===")

# Pair scores with students
combined = []

for i in range(len(students)):
    combined.append((scores[i], students[i]))

# Sort by score (descending)
combined.sort()
combined.reverse()

rank = 1
for score, name in combined:
    print(str(rank) + ".", name, "-", score)
    rank += 1
