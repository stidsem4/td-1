from collections import namedtuple

# tuples et nameed tuple
point_en_2d = (0, 0)

Point2D = namedtuple('Point2D', ['x', 'y'])


p2d = Point2D(x=0, y=1)
print(p2d)

p2d[0]
print(p2d.x) #y

Point1D = namedtuple("Point1D", ["x"])


print(Point1D)

p_04 = Point1D(0.4)
print(p_04)
p_05 = Point1D(0.5)

# Ce qu'on voudrait
# p_04 + p_05 == Point1D(0.9))
# ce que l'on a
# (0.4, 0.5) 

def ajout_point1d(point1, point2):
  x = point1.x + point2.x
  
  return Point1D(x)

print(f"Addition ok: {ajout_point1d(p_04, p_05)}")  