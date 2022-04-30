# dictionary, allows us to associate something with something else
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco":"Slytherin"
}

# value for the key hermione
print (students["Hermione"])

# all the keys in the dict
for student in students:
    print(student, students[student], sep = ", ")


# a list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    
]