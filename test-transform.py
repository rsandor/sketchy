from sketchy import Sketchy
from ball import Ball

width, height = [1024, 768]

class MyDrawing(Sketchy):
  def setup(self):
    self.x = width / 2.0
    self.y = height / 2.0
    self.dx = 7.0
    self.dy = 7.0
    self.r = 0.0
    self.dr = 0.1
    self.size(width, height)

  def update(self):
    self.x += self.dx
    if (self.x < 0 or self.x > width):
      self.dx *= -1.0;
    self.y += self.dy
    if (self.y < 0 or self.y > height):
      self.dy *= -1.0;
    self.r += self.dr
    if (self.r > 6.28):
      self.r -= 6.28

  def draw(self, g):
    g.background(0, 0, 0)
    g.push()
    g.translate(self.x, self.y)
    g.rotate(self.r)
    g.scale(250, 250)
    g.fill(1.0, 0.5, 0.25, 1.0)
    g.rect(-0.5, -0.5, 1.0, 1.0)
    g.pop()


MyDrawing()
