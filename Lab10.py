import csv
import pickle
import shutil
import os

# Task 1: Create a CSV file
with open("sample.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Subject1", "Subject2", "Subject3"])
    writer.writerow(["101", "John", 85, 90, 95])

# Task 2: Read CSV and convert to dictionary, calculate total
with open("sample.csv", "r") as file:
    reader = csv.DictReader(file)
    data = {}
    for row in reader:
        total = sum(int(row[sub]) for sub in ["Subject1", "Subject2", "Subject3"])
        data[row["Name"]] = {"Roll No": row["Roll No"], "Total": total}
print("Dictionary data:", data)

# Task 3: Create a vCard
contact = input("Enter name: "), input("Enter phone: "), input("Enter email: ")
vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{contact[0]}
TEL:{contact[1]}
EMAIL:{contact[2]}
END:VCARD"""
with open("contact.vcf", "w") as file:
    file.write(vcard)

# Task 4: Create subdirectory and copy file
os.makedirs("new_dir", exist_ok=True)
shutil.copy("sample.csv", "new_dir/sample.csv")

# Task 5: Copy file content, convert to uppercase
with open("sample.txt", "w") as file:
    file.write("hello world")
with open("sample.txt", "r") as file:
    content = file.read()
with open("output.txt", "w") as file:
    file.write(content.upper())

# Task 6: Merge lines from two files alternately
with open("file1.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3")
with open("file2.txt", "w") as file:
    file.write("A\nB\nC\nD")
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for l1, l2 in zip(lines1, lines2):
        out.write(l1 + l2)
    out.writelines(lines1[len(lines2):] if len(lines1) > len(lines2) else lines2[len(lines1):])

# Task 7: Serialize and deserialize Employee object
employee = {"empcode": "101", "empname": "John", "date": "2023-01-01", "salary": 50000}
with open("employee.pkl", "wb") as file:
    pickle.dump(employee, file)
with open("employee.pkl", "rb") as file:
    loaded_emp = pickle.load(file)
print("Deserialized employee:", loaded_emp)

# Task 8: Replace 'a', 'the', 'an' with space in text file
with open("input.txt", "w") as file:
    file.write("the cat and a dog")
with open("input.txt", "r") as file, open("output.txt", "w") as out:
    text = file.read()
    for word in ['a', 'the', 'an']:
        text = text.replace(word, " ")
    out.write(text)
