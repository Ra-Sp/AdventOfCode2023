# Day 5 - Problem 1

data = list(open('day5-input.txt'))

seed_to_soil_i = data.index('seed-to-soil map:\n')
soil_to_fertilizer_i = data.index('soil-to-fertilizer map:\n')
fertilizer_to_water_i = data.index('fertilizer-to-water map:\n')
water_to_light_i = data.index('water-to-light map:\n')
light_to_temperature_i = data.index('light-to-temperature map:\n')
temperature_to_humidity_i = data.index('temperature-to-humidity map:\n')
humidity_to_location_i = data.index('humidity-to-location map:\n')

seeds = list(map(int, (data[0][6:].split())))
seeds = {seed:[seed] for seed in seeds}

def src_to_dest(src_i, dest_i):
    global seeds
    
    sub_data = []
    for line in data[src_i+1:dest_i-1]:
        sub_data.append(list(map(int, line.strip().split())))

    for seed in seeds:
        for dest_start, src, range_ in sub_data:
            if src <= seeds[seed][-1] < src + range_:
                seeds[seed].append(dest_start + seeds[seed][-1] - src)
                break

    
src_to_dest(seed_to_soil_i, soil_to_fertilizer_i)
src_to_dest(soil_to_fertilizer_i, fertilizer_to_water_i)
src_to_dest(fertilizer_to_water_i, water_to_light_i)
src_to_dest(water_to_light_i, light_to_temperature_i)
src_to_dest(light_to_temperature_i, temperature_to_humidity_i)
src_to_dest(temperature_to_humidity_i, humidity_to_location_i)
src_to_dest(humidity_to_location_i, 0)

lowest_loc = 1 << 60
for seed in seeds:
    lowest_loc = min(seeds[seed][-1], lowest_loc)

print(lowest_loc)
