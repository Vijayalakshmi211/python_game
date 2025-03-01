import turtle as t
import random 

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# The below code is for making shapes 
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):  # Fixed indentation here
        tim.forward(100)  # Corrected 'foward' to 'forward'
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

t.done()  # Added to finish the turtle graphics