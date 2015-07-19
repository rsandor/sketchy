from random import randint, random

class Ball(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.x = randint(0, width)
    self.y = randint(0, height)

    self.color = [random(), random(), random(), 0.25]

    self.dx = 10*(random() - 0.5)
    self.dy = 10*(random() - 0.5)

  def update(self):
    # Update the ball's position
    self.x += self.dx
    if self.x > self.width or self.x < 0:
      self.dx *= -1

    self.y += self.dy
    if self.y > self.height or self.y < 0:
      self.dy *= -1

  def draw(self, g):
    # Draw a simple ball using the point method
    g.pointSize(40)
    g.stroke(self.color[0], self.color[1], self.color[2], self.color[3]) # Color
    g.point(self.x, self.y)
