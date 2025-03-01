student_heights = input("Input a list of students' heights: ").split()

# Convert input heights to integers
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initialize total_height
total_height = 0

# Calculate total height
for height in student_heights:
    total_height += height

# Calculate number of students
number_of_students = len(student_heights)

# Calculate average height
average_height = round(total_height / number_of_students)

# Print the average height
print(average_height)