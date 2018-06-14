# ImperialCrest.py
# Justin Arends
# arendsje@g.cofc.edu
# Homework 3
# Due 02/20/2017
# Creates the Imperial Crest from Star Wars
# Output: Drawn in a display window created with Python.
# Image found at http://media.indiedb.com/images/members/1/366/365912/EmpireWallpaper.jpg

from gui import *

width = 960
height = 600


d = Display("The Galactic Empire", width, height, 0, 0, Color.BLACK)

# Left rectangles, from top to bottom.
d.drawRectangle(0, 180, 329, 210, Color.WHITE, True)
d.drawRectangle(0, 230, 303, 370, Color.WHITE, True)
d.drawRectangle(0, 390, 329, 420, Color.WHITE, True)

# Right rectangles, from top to bottom.
d.drawRectangle(631, 180, 960, 210, Color.WHITE, True)
d.drawRectangle(656, 230, 960, 370, Color.WHITE, True)
d.drawRectangle(631, 390, 960, 420, Color.WHITE, True)

# Outer most circle, same color as background.
d.drawCircle(width/2, height/2, 190, Color.BLACK, False, 30)

# Outer circles of crest, from outer to inner.
d.drawCircle(width/2, height/2, 160, Color.WHITE, False, 25)
d.drawCircle(width/2, height/2, 135, Color.WHITE, False, 10)

# Inner filled circle, different color than background.
d.drawCircle(width/2, height/2, 110, Color.WHITE, True)

# Bottom spoke
d.drawRectangle(475, 415, 485, 430, Color.WHITE, True)
d.drawPolygon([455,480,505], [420,360,420], Color.WHITE, True)

# Top spoke
d.drawRectangle(475, 170, 485, 185, Color.WHITE, True)
d.drawPolygon([455,480,505],[180,240,180], Color.WHITE, True)

# Bottom side spokes
d.drawPolygon([360,370,375,360],[350,345,355,360], Color.WHITE, True)
d.drawPolygon([360,425,380],[330,320,370], Color.WHITE, True)
d.drawPolygon([600,590,585,600],[350,345,355,360], Color.WHITE, True)
d.drawPolygon([600,535,580],[330,320,370], Color.WHITE, True)

# Top side spokes
d.drawPolygon([360,370,375,360],[250,255,245,240], Color.WHITE, True)
d.drawPolygon([360,425,380],[270,280,230], Color.WHITE, True)
d.drawPolygon([600, 590,585,600],[250,255,245,240], Color.WHITE, True)
d.drawPolygon([600,535,580],[270,280,230], Color.WHITE, True)

# Inner top and bottom spokes. Same color as background.
d.drawPolygon([465,480,495],[390,330,390], Color.BLACK, True)
d.drawPolygon([465, 480, 495],[210,270,210], Color.BLACK, True)

# Inner bottom side spokes.
d.drawPolygon([395,460,405],[325,310,345], Color.BLACK, True)
d.drawPolygon([565,500,555],[325,310,345], Color.BLACK, True)

# Inner top side spokes.
d.drawPolygon([395,460,405],[275,290,255], Color.BLACK, True)
d.drawPolygon([565,500,555],[275,290,255], Color.BLACK, True)

# Inner circle, same color as background.
d.drawCircle(width/2, height/2, 50, Color.BLACK, True)