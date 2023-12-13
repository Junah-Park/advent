import math
def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line)
    seeds = input[0].strip().split(':')[1].strip().split(' ')
    seedRanges = []
    i = 0
    while i < len(seeds):
        seedRanges.append((seeds[i], seeds[i+1]))
        i += 2
    destinations = []

    index = 3
    seedSoil = []
    while input[index][0].isdigit():
        lineValues = input[index].strip().split(' ')
        destination, source, length = int(lineValues[0]), int(lineValues[1]), int(lineValues[2])
        seedSoil.append((source, source + length, destination, length))
        index+=1
    
    newSeedRanges = []
    for seedRange in seedRanges:
        seedStart = seedRange[0]
        seedLength = seedRange[1]
        for mapRange in seedSoil:
            mapDestin = mapRange[0]
            mapSource = mapRange[1]
            mapLength = mapRange[2]

    index += 2
    soilFertilizer = []
    while input[index][0].isdigit():
        lineValues = input[index].strip().split(' ')
        destination, source, length = int(lineValues[0]), int(lineValues[1]), int(lineValues[2])
        soilFertilizer.append((source, source + length, destination, length))
        index+=1

    index += 2
    fertilizerWater = []
    while input[index][0].isdigit():
        lineValues = input[index].strip().split(' ')
        destination, source, length = int(lineValues[0]), int(lineValues[1]), int(lineValues[2])
        fertilizerWater.append((source, source + length, destination, length))
        index+=1

    index += 2
    waterLight = []
    while input[index][0].isdigit():
        lineValues = input[index].strip().split(' ')
        destination, source, length = int(lineValues[0]), int(lineValues[1]), int(lineValues[2])
        waterLight.append((source, source + length, destination, length))
        index+=1
        
    index += 2
    lightTemperature = []
    while input[index][0].isdigit():
        lineValues = input[index].strip().split(' ')
        destination, source, length = int(lineValues[0]), int(lineValues[1]), int(lineValues[2])
        lightTemperature.append((source, source + length, destination, length))
        index+=1
        
    index += 2
    temperatureHumidity = []
    while input[index][0].isdigit():
        lineValues = input[index].strip().split(' ')
        destination, source, length = int(lineValues[0]), int(lineValues[1]), int(lineValues[2])
        temperatureHumidity.append((source, source + length, destination, length))
        index+=1
        
    index += 2
    humidityLocation = []
    while index < len(input) and input[index][0].isdigit():
        lineValues = input[index].strip().split(' ')
        destination, source, length = int(lineValues[0]), int(lineValues[1]), int(lineValues[2])
        humidityLocation.append((source, source + length, destination, length))
        index+=1

    lowestLocation = math.inf
    maps = [seedSoil, soilFertilizer, fertilizerWater, waterLight, lightTemperature,temperatureHumidity, humidityLocation]
    index = 0
    while index < len(seeds):
        seedStart, seedCount = int(seeds[index]), int(seeds[index+1])
        for mp in maps:
            seedRanges = [[seedStart, seedCount]]
            for ranges in mp:
                sourceStart, sourceEnd, destinationStart, length = ranges[0], ranges[1], ranges[2], ranges[3]
                newSeedRanges = []
                for i in range(len(seedRanges)):
                    seedStart = seedRanges[i][0]
                    seedCount = seedRanges[i][1]
                    if sourceStart <= seedStart < sourceEnd:
                        newSeedRanges.append([seedStart, seedStart + min(seedCount, length)])
                        break
            if newSeed == seed:
                seed = newSeed
                break
            seed = newSeed
        lowestLocation = min(lowestLocation, seed)
        index += 1
    print(lowestLocation)

if __name__ == "__main__":
    main()
    