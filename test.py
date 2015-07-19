from sketchy import Sketchy
from ball import Ball

class MyDrawing(Sketchy):
  def setup(self):
    width, height = [1000, 800]
    self.balls = []
    for i in range(0, 1500):
      self.balls.append(Ball(width, height))
    self.size(width, height)

  def update(self):
    for b in self.balls:
      b.update()

  def draw(self, g):
    g.background(0, 0, 0)
    for b in self.balls:
      b.draw(g)

MyDrawing()
