students = {
    "Ropafadzo": 80,
    "Tinotenda":75,
    "Jayden":87,
    "Kundai":95,
    "Hannah":66
}

print("students and marks:")
for name, mark in students.items():
    print(f"{name}:{mark}")

    top_student = max(students, key=students.get)
    print(f"\nstudent with highest mark : {top_student} with {students[top_student]}")