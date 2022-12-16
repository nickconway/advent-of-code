example = open("example.txt").read()
input = open("input.txt").read()

def merge(intervals):

    if len(intervals) == 0 or len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] - 1 <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)

    return result

def build(file, part, lineNumber=0):
    sensors = []
    beacons = []
    distances = []
    minX, minY, maxX, maxY = 100000, 100000, 0, 0
    for line in file.strip().split('\n'):
        words = line.split()
        sensorX = int(words[2][2:-1])
        sensorY = int(words[3][2:-1])
        beaconX = int(words[8][2:-1])
        beaconY = int(words[9][2:])
        distance = abs(sensorX - beaconX) + abs(sensorY - beaconY)
        minX = min(minX, sensorX, beaconX, sensorX - distance)
        minY = min(minY, sensorY, beaconY, sensorY - distance)
        maxX = max(maxX, sensorX, beaconX, sensorX + distance)
        maxY = max(maxY, sensorY, beaconY, sensorY + distance)
        sensors.append((sensorX, sensorY))
        beacons.append((beaconX, beaconY))
        distances.append(distance)

    blocked = [[] for _ in range(minY, maxY + 1)]
    for (sX, sY), distance in zip(sensors, distances):
        if part == 1:
            y = lineNumber
            left = sX - (distance - abs(sY - y))
            right = sX + (distance - abs(sY - y))
            blocked[y - minY].append([left, right])
            blocked[y - minY] = merge(blocked[y - minY])
        else:
            for y in range(sY - distance, sY + distance + 1):
                left = sX - (distance - abs(sY - y))
                right = sX + (distance - abs(sY - y))
                blocked[y - minY].append([left, right])
                blocked[y - minY] = merge(blocked[y - minY])

    return minX, minY, maxX, maxY, sensors, beacons, distances, blocked

def part_one(file, lineNumber):
    _, minY, _, _, sensors, beacons, _, blocked = build(file, 1, lineNumber)

    blockedAmount = sum([interval[1] - interval[0] + 1 for interval in blocked[lineNumber - minY]])
    lineSensors = set((x, y) for x, y in sensors if y == lineNumber)
    lineBeacons = set((x, y) for x, y in beacons if y == lineNumber)
    print(blockedAmount - len(lineSensors) - len(lineBeacons))

def part_two(file, limit):
    _, minY, _, _, _, _, _, blocked = build(file, 2)

    for y in range(limit):
        intervals = blocked[y - minY]
        if len(intervals) > 1:
            x = (intervals[0][1] + intervals[1][0]) // 2
            frequency = x * 4000000 + (y + minY)
            print(x, frequency)

part_one(example, 10)
part_one(input, 2000000)
print()
part_two(example, 20)
part_two(input, 4000000)
