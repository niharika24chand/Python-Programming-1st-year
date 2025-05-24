# Create and write to the file
with open("your_name.txt", "w") as file:
    file.write("Hello my name is Niharika Chand.\n")
    file.write("I am a 1st year B.TECH CSE Student.\n")
    file.write("I enjoy learning new coding languages.\n")
    file.write("I'm currently learning python.\n")
    file.write("I have to build 5 projects.\n")
    file.write("I am interested in Data Science.\n")
    file.write("I love solving coding challenges.\n")
    file.write("In my free time I like to watch movies and be in peace.\n")
    file.write("I also enjoy baking\n")
    file.write("In august I'll be in my 2nd year\n")
print("File 'your_name.txt' created and written successfully.")

# Read and display the file line by line
with open("your_name.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the extra newline

# Count lines that do not start with 'A'
count = 0
with open("your_name.txt", "r") as file:
    for line in file:
        # Check if line (after stripping leading spaces) doesn't start with 'A'
        if not line.lstrip().startswith('A'):
            count += 1

print("Number of lines not starting with 'A':", count)

# Count the total number of words in the file
with open("your_name.txt", "r") as file:
    content = file.read()  # Read the entire content of the file
    words = content.split()  # Split the content into words based on spaces

print("Total number of words in the file:", len(words))

# Count words with length less than 4
count_short= 0
with open("your_name.txt", "r") as file:
    content = file.read()  # Read the entire content of the file
    words = content.split()  # Split the content into words based on spaces
    # Count words whose length is less than 4
    count_short = sum(1 for word in words if len(word) < 4)

print("Number of words with length less than 4:", count_short)



