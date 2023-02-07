#!/usr/bin/env python3

import house
import turtle

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200
STARTING_X = -800
STARTING_Y = -400
CLOUD_X1 = [150, 200, 100, -650, -700]
CLOUD_X2 = [1350, 1400, 1300, 550, 500]
CLOUD_X3 = [2550, 2600, 2500, 1750, 1700]

"""
Draws a normal sized new house at sx, sy. eq true is for cracked windows.
"""
def new_house_normal(sx,sy,eq=False, t=turtle.Turtle()):
    house.main(t=t, sx=sx, sy=sy, cloud=False, eq=eq)

"""
Draws a house shrink percent smaller than normal, eq true is for cracked windows and tilt.
"""
def new_house_small(sx, sy, shrink=0.9, eq=False, t=turtle.Turtle()):
    #old values
    HH = house.HOUSE_HEIGHT
    HW = house.HOUSE_WIDTH
    WS = house.WINDOW_SIZE
    FS = house.FIRST_STORY
    SS = house.SECOND_STORY

    #shrink values
    house.HOUSE_HEIGHT = shrink*house.HOUSE_HEIGHT
    house.HOUSE_WIDTH = shrink*house.HOUSE_WIDTH
    house.WINDOW_SIZE = shrink*house.WINDOW_SIZE
    house.FIRST_STORY = shrink*house.FIRST_STORY
    house.SECOND_STORY = shrink*house.SECOND_STORY
    house.main(t=t, sx=sx, sy=sy, cloud=False, eq=eq)

    #replace values
    house.HOUSE_HEIGHT = HH
    house.HOUSE_WIDTH = HW
    house.WINDOW_SIZE = WS
    house.FIRST_STORY = FS
    house.SECOND_STORY = SS

"""
draws the old house.
"""
def old_house():
    house.main()

"""
Adds a ground to the village starting at coordinates sx, sy
"""
def reearth(sx, sy, t=turtle.Turtle()):
    t.penup()
    t.goto(sx, sy-100)
    house.draw_rectangle(t, 3*BOUNDING_WIDTH, 100, 'green')

"""
draws a village pre-earthquake
"""
def make_village_peq(t=turtle.Turtle()):
    new_house_normal(STARTING_X, STARTING_Y, t=t)
    new_house_normal(STARTING_X + BOUNDING_WIDTH, STARTING_Y, t=t)
    new_house_small(STARTING_X + 2 * BOUNDING_WIDTH, STARTING_Y, t=t)
    house.draw_all_clouds(cloud_x=CLOUD_X1, t=t)
    house.draw_all_clouds(cloud_x=CLOUD_X2, t=t)
    house.draw_all_clouds(cloud_x=CLOUD_X3, t=t)
    reearth(STARTING_X, STARTING_Y, t)

"""
Draws a cloudless village post-earthquake. 
"""
def make_village_eq(t=turtle.Turtle()):
    new_house_normal(STARTING_X, STARTING_Y, eq=True, t=t)
    new_house_normal(STARTING_X + BOUNDING_WIDTH, STARTING_Y, eq=True, t=t)
    new_house_small(STARTING_X + 2 * BOUNDING_WIDTH, STARTING_Y, eq=True, t=t)
    reearth(STARTING_X, STARTING_Y, t)



if __name__ == "__main__":
    house_type = input("What would you like to see? You can respond with 'A' for the original house, 'B' for the pre-earthquake town, or 'C' for the post earthquake town.")

    win_width, win_height, bg_color = 6000, 1000, 'white'
    turtle.setup()
    turtle.screensize(win_width, win_height, bg_color)
    turtle.speed(0)

    if house_type == 'A':
        old_house()
    elif house_type == 'B':
        make_village_peq()
    elif house_type == 'C':
        make_village_eq()
    else:
        pass

    turtle.done()
