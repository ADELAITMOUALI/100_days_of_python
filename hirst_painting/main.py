from turtle import Turtle, Screen, colormode
from random import choice


# import colorgram 

# def extract_colors(num_colors):
#     list_colors = []
#     extract = colorgram.extract("image.jpg",num_colors)
#     for i in range(num_colors):
#         one_color = extract[i]
#         rgb = one_color.rgb
#         list_one = (rgb[0],rgb[1],rgb[2])
#         list_colors.append(list_one)
#     return list_colors
# print(extract_colors(30))


list_colors = [(239, 235, 68), (97, 169, 230), (40, 104, 181), (242, 76, 35), (221, 144, 85), (213, 62, 22), (156, 58, 91), (232, 55, 86), (34, 132, 49), (234, 121, 167), (45, 46, 134), (123, 240, 177), (122, 39, 64), (39, 177, 97), (163, 32, 26), (71, 39, 33), (188, 154, 53), (40, 33, 63), (95, 96, 203), (244, 163, 153), (99, 190, 168), (236, 233, 7), (37, 53, 45), (150, 211, 220), (43, 35, 43), (101, 96, 7)]   
colormode(255)
t = Turtle()
t.speed("fastest")
#set the position for the turtle
t.penup()
t.hideturtle()
for _ in range(2):
    t.right(90)
    t.forward(50*5)
t.right(180)
for _ in range(10):
    for _ in range(10):
        t.pendown()
        t.dot(20, choice(list_colors))
        t.penup()
        t.forward(50)
    t.back(50*10)
    t.left(90)
    t.forward(50)
    t.right(90)


Screen = Screen()
Screen.exitonclick() 