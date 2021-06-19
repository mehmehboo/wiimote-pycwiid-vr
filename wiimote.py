import cwiid
from time import sleep
from subprocess import call
from math import *
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

DRIVE_A="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0102"
DRIVE_B="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0103"
COAST_A="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=01020000"
COAST_B="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=01030000"
BREAK_A="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0002"
BREAK_B="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0003"

print('Press 1+2 on your Wiimote now...')
wm = None
i=1
while not wm:
    try:
        wm=cwiid.Wiimote()
    except RuntimeError:
        if(i>5):
            print("cannot create connection")
            quit()
        print("Error opening wiimote connection")
        print("attempt " + str(i))
        i += 1

wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

wm.led=15
wm.rumble=True
sleep(0.5)
wm.rumble=False
wm.led=0
sleep(1.5)

verticies = (
    (1.54, -1.81, -8),
    (1.54, 1.81, -8),
    (-1.54, 1.81, -8),
    (-1.54, -1.81, -8),
    (1.54, -1.81, 8),
    (1.54, 1.81, 8),
    (-1.54, -1.81, 8),
    (-1.54, 1.81, 8)
    )

#estimated finger dimesions
#length 10
#width 1.81
#depth 1.81

##offset 1.5

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def draw():
    glColor(0, 0, 255)

    glBegin(GL_LINES)

    glVertex3f(0, 0, -8)
    glVertex3f(0, 0, -12)

    glEnd()

    glColor(255, 255, 255)
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3f(*verticies[vertex])
    glEnd()


def main():    
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        buttons = wm.state['buttons']

        roll=(wm.state['acc'][0]-125)
        pitch=(wm.state['acc'][1]-125)

        roll=roll*2.5
        pitch=pitch*2.5

        if buttons == 2: #debug
            print("roll: " + str(roll))
            print("pitch: " + str(pitch))

        glLoadIdentity()
        gluPerspective(45, (display[0]/display[1]), 0.1, 50)
        glTranslatef(0.0,0.0, -40)

        glRotatef(-pitch, 1, 0, 0)
        glRotatef(-roll, 0, 0, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


if wm != None:
    main()
