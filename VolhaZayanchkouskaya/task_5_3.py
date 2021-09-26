"""
File `data/students.csv` stores information about students in [CSV]
(https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark.
1) Implement a function which receives file path and returns names of top performer
 students
```python
def get_top_performers(file_path, number_of_top_students=5):
    pass

2) Implement a function which receives the file path with students info
and writes CSV student information to the new file in descending order of age.
"""


import csv


def get_top_performers(file_path, number_of_top_students=5):
    """Returns a list of names of top performer students"""
    with open(file_path, 'r') as f:
        file_reader = csv.reader(f)
        count = 0
        for _row in file_reader:
            if count == 0:
                sorted_list = sorted(file_reader, key=lambda row: row[2], reverse=True)
        res = []
        for item in sorted_list:
            if len(res) < number_of_top_students:
                res.append(item[0])
        return res


def sorted_age(filepath):
    """Create CSV file (sort_by_age.csv) with sorted list of student in descending order of age"""
    with open(filepath, 'r') as f:
        file_reader = csv.reader(f)
        count = 0
        for _row in file_reader:
            if count == 0:
                sorted_list = sorted(file_reader, key=lambda row: row[1], reverse=True)
    with open("data/sort_by_age.csv", "w") as nf:
        file_writer = csv.writer(nf, lineterminator="\r")
        file_writer.writerow(["student name", "age", "average mark"])
        for line in sorted_list:
            file_writer.writerow(line)


if __name__ == "__main__":
    f = "data/students.csv"
    print(get_top_performers(f))
    sorted_age(f)

