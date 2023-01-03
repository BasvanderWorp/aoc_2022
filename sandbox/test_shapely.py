import shapely.geometry.multipolygon
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from shapely.ops import cascaded_union, unary_union

if False:
    p1 = Polygon([(100,100), (100,200), (200,200), (200,100)])
    p2 = Polygon([(0,0), (0,50), (50,50), (50,0)])
    p3 = Polygon([(125,125), (125,175), (175,175), (175,125)])
    plt.plot(*p1.exterior.xy, color='red')
    plt.plot(*p2.exterior.xy, color='green')
    plt.plot(*p3.exterior.xy, color='blue')
    p10 = cascaded_union([p1, p2, p3])
    if isinstance(p10, shapely.geometry.multipolygon.MultiPolygon):
        for poly1 in p10.geoms:
            plt.plot(*poly1.exterior.xy, color='green')
            for poly_int in poly1.interiors:
                plt.plot(*poly_int.xy, color='red')
    plt.show()

if False:
    # 2 overlappende vierkanten/rechthoeken
    p1 = Polygon([(100,100), (100,200), (200,200), (200,100)])
    p2 = Polygon([(50,125), (50,175), (250,175), (250,125)])
    # plt.plot(*p1.exterior.xy, color='red')
    # plt.plot(*p2.exterior.xy, color='green')
    p3 = cascaded_union([p1, p2])
    plt.plot(*p3.exterior.xy, color='green')
    plt.show()

if False:
    # vierkant en een u-vorm waardoor een interior ontstaat
    p1 = Polygon([(100,100), (100,200), (200,200), (200,100)])
    p2 = Polygon([(50,50), (50,175), (125,175), (125,75), (175,75), (175,175), (250,175), (250,50)])
    # plt.plot(*p1.exterior.xy, color='red')
    # plt.plot(*p2.exterior.xy, color='green')
    p3 = cascaded_union([p1, p2])
    # p3 = unary_union([p1, p2])
    plt.plot(*p3.exterior.xy, color='green')
    for poly_int in p3.interiors:
        plt.plot(*poly_int.exterior.xy, color='red')
    plt.show()

if True:
    # Vierkant binnen een vierkant, wordt GEEN interior
    p1 = Polygon([(100,100), (100,200), (200,200), (200,100)])
    p2 = Polygon([(125,125), (125,175), (175,175), (175,125)])
    # plt.plot(*p1.exterior.xy, color='red')
    # plt.plot(*p2.exterior.xy, color='green')
    p10 = unary_union([p1, p2])
    plt.plot(*p10.exterior.xy, color='green')
    for poly_int in p10.interiors:
        plt.plot(*poly_int.exterior.xy, color='red')
    plt.show()
