#!/usr/bin/env python3

import turtle
import math
STARTING_X = -550
STARTING_Y = -400

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200

HOUSE_HEIGHT = 500
HOUSE_WIDTH = 700
TREE_HEIGHT = 250
TREE_WIDTH = 30
WINDOW_SIZE = 80
FIRST_STORY = 250
SECOND_STORY = 150
N_WINDOWS = 8
CLOUD_X = [400, 450, 350, -400, -350]
CLOUD_HEIGHT = 250

TRUNCK_COLOR = "brown"
BRANCH_COLOR = "green"
BRANCH_ANGLE = 180 - 45
HOUSE_COLOR = "#f571cb"
SKY_COLOR = "lightblue"
PEN_COLOR = "black"
CLOUD_COLOR = "white"
WINDOW_COLOR = "darkgray"
DOOR_COLOR = "#03a9fc"
DOORKNOB_COLOR = "#f5d60f"
GARAGE_COLOR = "grey"
GARAGE_WINDOW_COLOR = "white"


def draw_circle(t, radius, color=CLOUD_COLOR):
    """Draw a circle.
    Params:
        t: the Turtle object
        radius: radius of the circle
        color: color of the circle
    """
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.pencolor(PEN_COLOR)


def draw_bounding_box(t=turtle.Turtle(), sx = STARTING_X, sy=STARTING_Y, fc= SKY_COLOR):
    """Draw bounding box to put house in.
    Params:
        t: the Turtle object
    """
    t.fillcolor(fc)
    t.penup()
    t.goto(sx, sy)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)
    t.left(90)
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)
    t.end_fill()


def draw_house(t=turtle.Turtle(), sx = STARTING_X, sy=STARTING_Y, eq=False):
    """Draw outline of house and make it pink.
    Params:
        t: the Turtle object
        eq: draws post earthquake small house tilted.
    """
    t.penup()
    t.goto(sx + (BOUNDING_WIDTH - HOUSE_WIDTH) / 2, sy)
    t.seth(90)
    t.fillcolor(HOUSE_COLOR)
    t.begin_fill()
    t.pendown()
    if eq and HOUSE_HEIGHT < 500: #only small house is tilted
        t.right(5)
    t.forward(HOUSE_HEIGHT)
    t.right(90)
    t.forward(HOUSE_WIDTH)
    t.right(90)
    t.forward(HOUSE_HEIGHT)
    t.end_fill()


def draw_branches(t, tree_width):
    """Draw branches for the tree

    Params:
        t: the Turtle object.
        tree_width: width of the tree
    """

    # isosceles right triangle length
    length = tree_width * math.sqrt(2)

    t.fillcolor(BRANCH_COLOR)
    t.begin_fill()
    t.forward(tree_width)
    t.left(BRANCH_ANGLE)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(BRANCH_ANGLE)
    t.forward(tree_width)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(tree_width)
    t.right(90)
    t.pendown()


def draw_tree(t=turtle.Turtle()):
    """Draw a tree 

    Params:
        t: the Turtle object.
    """

    # tree trunk
    t.fillcolor(TRUNCK_COLOR)
    t.begin_fill()
    t.left(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.forward(TREE_WIDTH)
    t.right(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.forward(TREE_WIDTH / 2)
    t.end_fill()

    # move to branch location
    t.penup()
    t.right(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.pendown()

    # draw branches
    draw_branches(t, TREE_WIDTH * 4)
    draw_branches(t, TREE_WIDTH * 3)
    draw_branches(t, TREE_WIDTH * 2)


def draw_all_trees(t, sx=STARTING_X):
    """Draw two trees, one on each side of the house

    Params:
        t: the Turtle object.
    """

    # get width space for the two sides of the house
    side_widths = BOUNDING_WIDTH - HOUSE_WIDTH

    # get half the width space for one of the side
    half_w = side_widths / 4

    # set starting point to half of side width - half tree width
    gap = half_w - TREE_WIDTH / 2

    # move to starting point
    t.left(90)
    t.forward(gap)

    # draw right tree
    draw_tree(t)

    # move to the other side (1/2 side width + house width)
    if sx == STARTING_X:
        gap = half_w + HOUSE_WIDTH

    # move to left tree
    t.penup()
    t.goto(sx + half_w + gap, -400.00)
    t.pendown()
    t.right(180)
    t.forward(gap)
    t.right(180)

    # draw left tree
    draw_tree(t)


def draw_window(t=turtle.Turtle(), eq=False):
    """Draw a row of 4 windows

    Params:
        t: the Turtle object.
        eq: draws post earthquake window of small house broken.
    """
    t.fillcolor(WINDOW_COLOR)
    t.begin_fill()
    for i in range(4):
        t.forward(WINDOW_SIZE)
        t.left(90)
    if eq:
        t.left(45)
        t.forward(math.sqrt(2*(WINDOW_SIZE**2)))
        t.left(180)
        t.forward(math.sqrt(2 * (WINDOW_SIZE ** 2)))
        t.left(135)
    t.end_fill()


def draw_all_windows(t, windows_per_row, sx = STARTING_X, sy=STARTING_Y, eq=False):
    """Draw four windows on the house

    Params:
        t: the Turtle object.
        windows_per_row: number of windows per row
        eq: draws post earthquake garages of small house tilted and half of post eqrthquake windows broken.
    """
    start_loc = t.pos()

    # distance between window and edge of house to be nicely spaced
    margin = (HOUSE_WIDTH - (2 * windows_per_row - 1) * WINDOW_SIZE) / 2

    t.penup()
    t.goto(sx + BOUNDING_WIDTH / 2 + HOUSE_WIDTH / 2, sy)
    t.seth(90)
    t.forward(FIRST_STORY)
    t.left(90)
    t.forward(margin)
    t.pendown()
    if eq and WINDOW_SIZE < 80:
        t.right(5)
    draw_window(t, eq=eq)
    for i in range(windows_per_row - 1):
        t.penup()
        t.forward(2 * WINDOW_SIZE)
        t.pendown()
        draw_window(t, eq=eq)
    t.penup()
    t.right(90)
    t.forward(SECOND_STORY)
    t.right(90)
    t.forward(2 * (windows_per_row - 1) * WINDOW_SIZE)
    t.left(180)
    t.pendown()
    draw_window(t)
    for i in range(windows_per_row - 1):
        t.penup()
        t.forward(2 * WINDOW_SIZE)
        t.pendown()
        draw_window(t)
    t.penup()
    t.goto(start_loc)
    t.pendown()
    t.seth(270)


def draw_door(t, door_width, door_height, sx = STARTING_X, sy=STARTING_Y, eq=False):
    """Draw door of house, touching the bottom

    Params:
        t: the Turtle object.
        door_width: width of door
        door_height: height of door
        eq:draws post earthquake door of small house tilted.
    """

    doorknob = door_width / 15

    # save starting position for later
    start_loc = t.pos()

    # after drawing house, get to door starting point
    t.penup()
    t.goto(sx + BOUNDING_WIDTH / 2 - HOUSE_WIDTH / 4, sy)
    t.seth(90)
    if eq and HOUSE_WIDTH < 700:
        t.right(5)
    # draw door
    t.pendown()
    t.fillcolor(DOOR_COLOR)
    t.begin_fill()
    t.forward(door_height)
    t.left(90)
    t.forward(door_width)
    t.left(90)
    t.forward(door_height)
    t.end_fill()

    # draw doorknob
    t.left(90)
    t.forward(door_width * 0.8)
    t.left(90)
    t.penup()
    t.forward(door_height / 2)
    t.pendown()
    draw_circle(t, doorknob, DOORKNOB_COLOR)
    t.penup()
    t.left(180)
    t.forward(door_height / 2)
    t.pendown()
    t.left(90)
    t.forward(door_width * 0.2)
    t.penup()

    # go back to position before drawing door
    t.goto(start_loc)


def draw_rectangle(t, width, height, color, tilt=90):
    """Draw a rectangle starting at the bottom left corner

    Params:
        t: the Turtle object.
        width: the width of the rectangle
        height: the height of the rectangle
        color: the color of the rectangle
        tilt: angle from horizontal to draw rectangle
    """
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.seth(tilt)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.penup()
    t.end_fill()


def draw_garage_windows(t, window_width, window_height, garage_width=HOUSE_WIDTH / 5, garage_height=HOUSE_HEIGHT / 4, eq=False):
    """Draw two garage windows 

    Params:
        t: the Turtle object.
        window_width: the width of each window
        window_height: the height of each window
        garage_width: the width of the garage
        garage_height: the height of the garage
        eq: draws post earthquake garage windows of small house tilted.
    """
    # set starting location for window 1
    window_x = garage_width / 2.2
    window_y = 3 * garage_height / 4

    # move to window 1 location
    t.penup()
    t.right(180)
    t.forward(window_x)
    t.right(90)
    t.forward(window_y)

    if eq:
        tilt = 85
    else:
        tilt = 90

    # draw window 1
    draw_rectangle(t, window_width, window_height, GARAGE_WINDOW_COLOR, tilt=tilt)

    # move to window 2 location
    t.forward(window_x)

    # draw window 2
    draw_rectangle(t, window_width, window_height, GARAGE_WINDOW_COLOR, tilt=tilt)


def draw_all_garages(t=turtle.Turtle(), garage_width=HOUSE_WIDTH / 5, garage_height=HOUSE_HEIGHT / 4, sx = STARTING_X, sy=STARTING_Y, eq=False):
    """Draw two garages next to each other

    Params:
        t: the Turtle object.
        garage_width: the width of the garage
        garage_height: the height of the garage
        eq: draws post earthquake garages of small house tilted.
    """
    window_width = garage_width / 3
    window_height = garage_height / 7
    t.penup()
    garage_x_start = sx + BOUNDING_WIDTH / 2
    garage_x_locations = [0, 6 * garage_width / 5]

    # draw garages at garage_x_locations
    for x_value in garage_x_locations:
        if x_value == garage_x_locations[1] and eq and HOUSE_WIDTH < 700: #evens garage for tilted house
            sy = STARTING_Y - garage_height/8
        t.goto(garage_x_start + x_value, sy)
        if eq and HOUSE_WIDTH < 700:
            tilt = 85
        else:
            tilt = 90
        draw_rectangle(t, garage_width, garage_height, GARAGE_COLOR, tilt=tilt)
        t.right(180)
        t.forward(garage_width)
        if eq and HOUSE_WIDTH < 700:
            draw_garage_windows(t, window_width, window_height, garage_width, garage_height, eq=eq)
        else:
            draw_garage_windows(t, window_width, window_height, garage_width, garage_height)


def draw_cloud(t=turtle.Turtle(), radius=30, color=CLOUD_COLOR, x_start=0, y_start=0):
    """Draw a cloud. 
    Params:
        t: the Turtle object
        radius: radius of the circle
        color: color of the circle
        x_start: x coordinate for starting pos
        y_start: y coordinate for starting pos
    """
    t.up()
    t.goto(x_start, y_start)
    t.down()
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)


def draw_all_clouds(t=turtle.Turtle(), cloud_x = CLOUD_X, cloud_height = CLOUD_HEIGHT):
    """Draw two clouds.
    Params:
        t: the Turtle object.
        cloud_x: starting x positions
        cloud_height: starting cloud height
    """
    for position in cloud_x:
        draw_cloud(t, x_start=position, y_start=cloud_height)

"""
Draws a house at sx, sy. 
True clouds will draw clouds, true eq will draw half broken windows and smaller houses tilted.
"""
def main(t=turtle.Turtle(), sx=STARTING_X, sy=STARTING_Y, cloud=True, eq=False):

    draw_bounding_box(t, sx, sy)
    draw_house(t, sx, sy, eq=eq)
    draw_all_trees(t, sx)
    draw_door(t, HOUSE_WIDTH / 8, HOUSE_HEIGHT / 4, sx, sy, eq=eq)
    draw_all_windows(t, N_WINDOWS // 2, sx, sy, eq=eq)
    if cloud:
        draw_all_clouds(t, CLOUD_X, CLOUD_HEIGHT)
    draw_all_garages(t, HOUSE_WIDTH / 5, HOUSE_HEIGHT / 4, sx, sy, eq=eq)


if __name__ == "__main__":
    main(STARTING_X, STARTING_Y)
    turtle.done()
