import time
import rotatescreen

screen = rotatescreen.get_primary_display()

def screenRotate(axis):
    screen.rotate_to(axis)
    time.sleep(1)

axis = 0

while True:
    axis = axis + 90
    if axis > 270:
        axis = 90
    screenRotate(axis)