students = [
    {"name": "lucas", "house": "p2","patronus": "maria"},
    {"name": "luanna", "house": "lirio", "patronus": "luciana"},
    {"name": "luciana", "house": "lirio", "patronus": "otter"},
    {"name": "unknow", "house": "p2", "patronus": None}
]

for student in students:
    print(student["name"], student ["house"], student ["patronus"], sep= ", ")