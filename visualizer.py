import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def visualizeWiimote(wm):
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

    #estimated finger dimesions (not implemented yet)
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


    def main(wm):    
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        glTranslatef(0.0,0.0, -40)

        wm.led = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            buttons = wm.state['buttons']

            roll=(wm.state['acc'][0]-117)
            pitch=(wm.state['acc'][1]-120)

            roll=roll*2.5
            pitch=pitch*2.5

            if buttons == 2: #debug
                print("roll: " + str(roll))
                print("pitch: " + str(pitch))
                print("state: " + str(wm.state))

            #roll glitches past 40 and -40
            #pitch glitches past 50 and -50
            #gimble lock causes this
            if roll > 40 or roll < -40 or pitch > 50 or pitch < -50: ##warning outside visulizer gimble lock
                wm.rumble = True

            else:
                wm.rumble = False

            glLoadIdentity()
            gluPerspective(45, (display[0]/display[1]), 0.1, 50)
            glTranslatef(0.0,0.0, -40)

            glRotatef(-pitch, 1, 0, 0)
            glRotatef(-roll, 0, 0, 1)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            draw()
            pygame.display.flip()
            pygame.time.wait(10)

    main(wm)
