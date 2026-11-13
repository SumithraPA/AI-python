import csv
students=[{"Rollno":"101","Name":"Anitha","Department":"CSE","Mark":86},{"Rollno":"102","Name":"Bala","Department":"CSE","Mark":91},{"Rollno":"103","Name":"Chithra","Department":"ECE","Mark":78}]
course=("Python",4)
print("Course tuple:",course)
with open("students.txt","w") as file:
    for student in students:
        file.write(str(student)+"\n")
with open("students.csv","w",newline="") as file:
    fields=["Rollno","Name","Department","Mark"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)
print("\n___Records from csv___")
with open("students.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["Rollno"],row["Name"],row["Department"],row["Mark"])