from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin, cos, pi
import sys

class Graphics(object):
  def __init__(self):
    self.fillColor = [0, 0, 0, 0]
    self.strokeColor = [0, 0, 0, 0]
    self.segments = 40

  def background(self, r, g, b):
    glClearColor(r, g, b, 1.0)

  def fill(self, r, g, b, a):
    self.fillColor = [float(r), float(g), float(b), float(a)]

  def stroke(self, r, g, b, a):
    self.strokeColor = [float(r), float(g), float(b), float(a)]

  def circleSegments(s):
    self.segments = s

  def pointSize(self, w):
    glPointSize(float(w))

  def strokeWeight(self, w):
    glLineWidth(float(w))

  def translate(self, x, y):
    glTranslatef(float(x), float(y), 0.0)

  def circle(self, x, y, r):
    self.ellipse(x, y, r, r)

  def ellipse(self, x, y, w, h):
    r1 = float(w)
    r2 = float(h)
    glBegin(GL_POLYGON)
    glColor4fv(self.fillColor)
    for i in range(0, self.segments):
      theta = float(2 * pi * i) / float(self.segments)
      glVertex2f(
        float(r1) * cos(theta) + float(x),
        float(r2) * sin(theta) + float(y)
      )
    glEnd()
    glBegin(GL_LINE_STRIP)
    glColor4fv(self.strokeColor)
    for i in range(0, self.segments):
      theta = float(2 * pi * i) / float(self.segments)
      glVertex2f(
        float(r1) * cos(theta) + float(x),
        float(r2) * sin(theta) + float(y)
      )
    glVertex2f(float(r1) * 1 + float(x), float(y))
    glEnd()

  def rect(self, x, y, w, h):
    x, y, w, h = float(x), float(y), float(w), float(h)
    glBegin(GL_QUADS)
    glColor4fv(self.fillColor)
    glVertex2f(x, y)
    glVertex2f(x+w, y)
    glVertex2f(x+w, y+h)
    glVertex2f(x, y+h)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glColor4fv(self.strokeColor)
    glVertex2f(x, y)
    glVertex2f(x+w, y)
    glVertex2f(x+w, y+h)
    glVertex2f(x, y+h)
    glVertex2f(x, y)
    glEnd()

  def point(self, x, y):
    glBegin(GL_POINTS)
    glColor4fv(self.strokeColor)
    glVertex2f(float(x), float(y))
    glEnd()

  def line(self, x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor4fv(self.strokeColor)
    glVertex2f(float(x1), float(y1))
    glVertex2f(float(x2), float(y2))
    glEnd()

  def push(self):
    glPushMatrix()

  def pop(self):
    glPopMatrix()

  def rotate(self, angle):
    glRotatef(float(180.0*angle/3.1415), 0.0, 0.0, 1.0)

  def translate(self, x, y):
    glTranslatef(float(x), float(y), 0.0)

  def scale(self, x, y):
    glScalef(float(x), float(y), 1.0)


class Sketchy(object):
  def __init__(self):
    self.title = "Sketchy"
    self.mouseX = 0
    self.mouseY = 0
    self.g = Graphics()
    self._glutReady = False
    self.setup()

  def size(self, width, height):
    self.width = width
    self.height = height
    if not self._glutReady:
      self._glutReady = True
      self._initializeGlut()

  def _initializeGlut(self):
    # Initialize glut
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(self.width, self.height)
    self.window = glutCreateWindow(self.title)
    glutSetWindow(self.window)

    glutPassiveMotionFunc(self._mouseMove)

    # Set the display function
    self.g.background(1.0, 1.0, 1.0)
    glutDisplayFunc(self._render)

    # Setup basic drawing mode flags
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POINT_SMOOTH)
    glHint(GL_POINT_SMOOTH_HINT, GL_FASTEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Setup the projection and model view affine transforms
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, self.width, 0.0, self.height)
    glMatrixMode(GL_MODELVIEW)
    glScalef(1.0, -1.0, 1.0)
    glTranslatef(0.0, -self.height, 0.0)

    # Start the glut main loop
    glutTimerFunc(16, self._update, 1)
    glutMainLoop()

  def _mouseMove(self, x, y):
    self.mouseX = x
    self.mouseY = y

  def _update(self, value):
    self.update()
    glutPostRedisplay()
    glutTimerFunc(16, self._update, 1)

  def _render(self):
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    self.draw(self.g)
    glPopMatrix()
    glutSwapBuffers()

  def setup(self):
    return

  def update(self):
    return

  def draw(self):
    return
