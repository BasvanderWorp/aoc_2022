from shapely.geometry import Polygon
import matplotlib.pyplot as plt

p1 = Polygon([(0,0), (0,100), (100,100), (100,0)])
c1
plt.plot(*p1.exterior.xy)
plt.show