# gradebook.py Scenerio:
# You are a student and you are trying to organize your subjects and grades
# using Python. Let’s explore lists to organize your
# subjects and scores.

last_semester_gradebook = [["politics", 80], [
    "latin", 96], ["dance", 97], ["architecture", 65]]


# Create a list of subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Create a list of grades
grades = [98, 97, 85, 88]

# Create a list of subjects with their corresponding grades
# gradebook = [["physics", 98], ["calculus", 97],
#             ["poetry", 85], ["history", 88]]

# Create a list of subjects with their corresponding grades
# Method ii for creating the gradebook list using a list comprehension
gradebook = [[subject, grade] for subject, grade in zip(subjects, grades)]

print(gradebook)

# Add more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Access the index of the grade the visual arts class and modify it to be
# 5 points greater.
gradebook[-1][-1] += 5

print("\n")
print(gradebook)

# You decided to switch from a numerical grade value to a Pass/Fail option for
# your poetry class.

# Remove the grade for Poetry
gradebook[2].remove(85)

print("\n")
print(gradebook)

# Add a Pass to the Poetry class
gradebook[2].append("Pass")

print("\n")
print(gradebook)

# Create a new variable full_gradebook that combines both
# last_semester_gradebook and gradebook using + to have one complete grade
# book.
full_gradebook = gradebook + last_semester_gradebook

print("\n")
print(full_gradebook)
