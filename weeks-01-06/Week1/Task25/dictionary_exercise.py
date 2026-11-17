# Task 25 - Dictionary data type
student = {"name": "Ali", "age": 21, "course": "AI/ML"}
print(student, "| type:", type(student).__name__)
print("access:", student["name"], student.get("grade", "N/A"))

student["grade"] = "A"; student["age"] = 22
del student["course"]
print("after update/delete:", student)

print("keys:", list(student.keys()))
print("values:", list(student.values()))
for k, v in student.items():
    print(f"  {k}: {v}")

print("pop:", student.pop("grade"), "| membership:", "name" in student)
student.update({"city": "Lahore", "age": 23})
print("after update():", student)

# Dictionary comprehension
squares = {n: n ** 2 for n in range(1, 6)}
print("squares:", squares)

# Word frequency counter
text = "to be or not to be that is the question to be"
freq = {}
for w in text.split():
    freq[w] = freq.get(w, 0) + 1
print("word frequency:", freq)
print("most common:", max(freq, key=freq.get))

# Nested dictionary
school = {"ali": {"math": 80, "cs": 90}, "sara": {"math": 95, "cs": 88}}
for n, m in school.items():
    print(n, "average:", sum(m.values()) / len(m))

# Sorting by value, merging
print("sorted by value:", dict(sorted(freq.items(), key=lambda kv: kv[1], reverse=True)))
print("merged:", {**{"a": 1}, **{"b": 2}})
