last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]

subjects.append("Computer Science")
grades.append(100)

Gradebook = list(zip(subjects, grades))

subjects.append("Visual Arts")
grades.append(93)

Gradebook.append(("Visual Arts", 93))

full_gradebook = Gradebook + last_semester_gradebook

print(tuple(full_gradebook))