"""
Advent of Code 2022
Day 15

b:
hmm 4 miljoen bij 4 miljoen gaat niet lukken om allemaal af te lopen, iets slimmers bedenken

er zijn niet zoveel sensors (nl maar 38), dus beter per sensor nagaan en het gebied verkleinen
maar hoe kan dat slim.
Hmm misschien alleen de omtrek bijhouden en een functie om te bepalen of het binnen of buiten het gebied ligt...
maar dan moet je als nog alle 4mln^2 punten nagaan, niet handig

nu kan ik het wel als een numpy matrix bekijken, misschien is dat sneller rekenen?
even testen:
n1 = np.ones(4000000, 4000000)
n1 + 1
print(n1[3,3])

oei dat lukt al niet voor float, int.
en voor bool duurt het minuten voor het uberhaupt aanmaken... gaat um niet worden...

n1 = np.ones([4000000, 4000000], bool)
Process finished with exit code 137 (interrupted by signal 9: SIGKILL)

nope gaat um niet worden
DUS WEER geen numpy array

===
ah wacht ander idee, het zijn allemaal cirkels, kan ik dit niet wiskundig oplossen?
dus 38 cirkels met een middelpunt en een straal
en daarvan het enige punt zoeken die niet in die cirkel valt!
ik moet toch alle punten langs? 4 miljoen in het kwadraat!
als ik maar een supersnelle manier van rekenen heb
dus:
- for punt in 4x4 miljoen punten:
    - for cirkel in cirkels
        als punt in cirkel: sluit punt uit, break
    voeg punt toe aan geldige punten

eerst ff testen hoe lang het duurt om door een lijst van 4x4 miljoen te lopen, uberhaupt zonder wat te doen !!!
ow nee zelfs dat duur te lang, gaat ook niet werken!!!


===
dan maar met polygonen / vormen werken? dus eerst polygoon van 4mln bij 4 mln,
lijst van areas_avail(square4x4mln)
- cirkel 1: polygoon minus cirkel
- cirkel 2: polygoon minus cirkel, minus cirkel
- shapely?
nee geen shapely, zelf bouwen

- cirkel 1: sla buiten coordinaten op
- cirkel 2: sla buiten coordinaten op
    - merge met cirkel 1
        - als ze overlappen dan een nieuwe shape
        - anders 2 shapes
- cirkel 38: klaar
- resultaat:
    - als het goed is 1 grote shape
    - maar nu moet ik het ene punt vinden dat daar niet binnenvalt
    - misschien mergen met de vierkant 4x4 miljoen?


"""
from helpers.io import read_input
import numpy as np
import copy
import sys

def read_sensors(lines: list):
    sensors = {}
    beacons = []
    for line in lines:
        sensor_data = line.split(':')[0]
        beacon_data = line.split(':')[1]
        sensor_coord = (int(sensor_data.split(',')[0].split('=')[1]),
                        int(sensor_data.split(',')[1].split('=')[1]))
        beacon_coord = (int(beacon_data.split(',')[0].split('=')[1]),
                        int(beacon_data.split(',')[1].split('=')[1]))
        beacons.append(beacon_coord)
        # sensors[(int(sensor_x), int(sensor_y))] = (int(beacon_x), int(beacon_y))
        sensors[sensor_coord] = man_dist(sensor_coord, beacon_coord)
    return sensors, beacons

def man_dist(coord1, coord2):
    dist_x = abs(coord1[0] - coord2[0])
    dist_y = abs(coord1[1] - coord2[1])
    return dist_x + dist_y

def get_x_bounds(sensors):
    x_min = list(sensors.keys())[0][0]
    x_max = x_min
    for sensor, sensor_range in sensors.items():
        x_min = min(x_min, sensor[0] - sensor_range)
        x_max = max(x_max, sensor[0] + sensor_range)
    return x_min, x_max

def get_num_occupied_pos(sensors, beacons, x_bounds, y):
    num_occ_pos = 0
    prev_perc = -1
    range_from = 0
    range_to = 4000000
    for x in range(range_from, range_to + 1):
        perc = round((x - range_from) / (range_to - range_from) * 100)
        if perc % 5 == 0:
            if perc != prev_perc:
                print(f'{perc}%')
                prev_perc = perc

        x_checked = False
        for sensor_coord, sensor_range in sensors.items():
            if man_dist((x,y), sensor_coord) <= sensor_range and not x_checked and (x,y) not in beacons:
                num_occ_pos += 1
                # print(x, y)
                x_checked = True
        if False:
            if (x,y) in beacons:
                print('B', end="")
            elif x_checked:
                print('#', end="")
            else:
                print('.', end="")
    print()
    return num_occ_pos

# ======================================
# MAIN
# ======================================
test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)

print('Start reading sensors and beacons')
sensors, beacons = read_sensors(file_lines)
print('Sensors and beacons read')
x_bounds = get_x_bounds(sensors)
print(f"x bounds: {x_bounds}, number of xes: {x_bounds[1]-x_bounds[0]}")

num = get_num_occupied_pos(sensors, beacons, x_bounds, 2000000)
print()
print(num)

print()
