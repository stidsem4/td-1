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

def norme1d(p1):
    return (p1.x ** 2) ** 0.5 

p_09 = ajout_point1d(p_04 , p_05)

print(norme1d(p_09))

Point2D = namedtuple("Point2D", "x y")

p1 = Point2D(0, 1)
p2 = Point2D(1, 0)

print(p1)
print(p2)


def ajout_point2d(p_1, p_2):
    x = p_1[0] + p_2[0]
    y = p_1[1] + p_2[1]
    return Point2D(x, y)
p3 = ajout_point2d(p1, p2)

print(p3)

print(f"Addition ok: {ajout_point2d(p1, p2) == Point2D(1,1)} ")

def ajout_point2d(p_1, p_2):
    coord = []
    for indice in range((len(p_1))):
        coord.append(p_1[indice] + p_2[indice])
    return Point2D(coord[0], coord[1])

print(f"Addition ok: {ajout_point2d(p1, p2) == Point2D(1,1)} ")


def ajout_point2d(p_1, p_2):
    coord = tuple(x + y for x, y in zip(p_1, p_2))
    return Point2D(coord[0], coord[1])

print(f"Addition ok: {ajout_point2d(p1, p2) == Point2D(1,1)} ")

def ajout_point2d(p_1, p_2):
    coord = tuple(x + y for x, y in zip(p_1, p_2))
    return Point2D._make(coord)

print(f"Addition ok: {ajout_point2d(p1, p2) == Point2D(1,1)} ")


# La 3d

Point3D = namedtuple("Point3D", "x y z")
#x1, x2, x3 ????

def ajout_point3d(p_1, p_2):
    
    return Point3D._make((p1 + p2 for p1, p2 in zip(p_1, p_2) ))

p3_1 = Point3D(0,0,1)
p3_2 = Point3D(0,0,1)

print(ajout_point3d(p3_1, p3_2))

class Point1D:
    def __init__(self, x):
        self.x = x


np1d = Point1D(0.9)
print(np1d)

def afficher_point1d(point):
    return f"Point: {point.x}"



class Point1D:
    def __init__(self, x):
        self.x = x

    def afficher(self):
        return f"Point: {self.x}"

np1d = Point1D(0.9)
print(np1d.afficher())

class Point1D:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"Point: {self.x}"

np1d = Point1D(0.9)

print(np1d)