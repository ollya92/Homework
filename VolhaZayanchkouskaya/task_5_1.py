"""
Open file `data/unsorted_names.txt` in data folder.
Sort the names and write them to a new file called `sorted_names.txt`.
Each name should start with a new line.
"""


with open("data/unsorted_names.txt", "r") as uf, open("data/sorted_names.txt", "w") as sf:
    unsorted_file = uf.readlines()
    sf.writelines(sorted(unsorted_file))

    