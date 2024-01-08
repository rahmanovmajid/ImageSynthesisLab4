from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle_x = 0.0
angle_y = 0.0

def render_Scene():
    global angle_x, angle_y
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    glTranslatef(0.0, 0.0, -5.0)
    
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    
    # Enable depth test
    glEnable(GL_DEPTH_TEST)
    
    # Multi-colored side - FRONT
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)  # Point P1 is red
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, -0.5)  # Point P2 is green
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, 0.5, -0.5)  # Point P3 is blue
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)  # Point P4 is purple
    glEnd()
    
    # White side - BACK
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()
    
    # Purple side - RIGHT
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glEnd()
    
    # Green side - LEFT
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()
    
    # Blue side - TOP
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glEnd()
    
    # Red side - BOTTOM
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glEnd()
    
    glutSwapBuffers()

def special_keys(key, x, y):
    global angle_x, angle_y
    step = 5.0
    
    if key == GLUT_KEY_UP:
        angle_x += step
    elif key == GLUT_KEY_DOWN:
        angle_x -= step
    elif key == GLUT_KEY_RIGHT:
        angle_y += step
    elif key == GLUT_KEY_LEFT:
        angle_y -= step
    
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow("Rotating Cube")
    glutReshapeFunc(resize)
    glutDisplayFunc(render_Scene)
    glutSpecialFunc(special_keys)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()

def resize(width, height):
    if height == 0:
        height = 1
    
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width/height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

if __name__ == "__main__":
    main()
