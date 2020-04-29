# Python program to
# demonstrate merging of
# two files
import os

path = "/etc/ansible/benchmarks/"
filenames = []

# get benchmarks contents and make sure the Results.txt is not added to the list
files = os.listdir(path)
for name in files:
    if name != "Results.txt":
        filenames.append(path + name)

#print(filenames)
# Open file3 in write mode
with open('/etc/ansible/benchmarks/Results.txt', 'w') as outfile:
    outfile.truncate(0)
    # Iterate through list
    for names in filenames:

        # Open each file in read mode
        with open(names) as infile:

            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")
