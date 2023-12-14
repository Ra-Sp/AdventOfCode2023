# Day 5 - Problem 2

data = list(open('day5-input.txt'))

seed_to_soil_i = data.index('seed-to-soil map:\n')
soil_to_fertilizer_i = data.index('soil-to-fertilizer map:\n')
fertilizer_to_water_i = data.index('fertilizer-to-water map:\n')
water_to_light_i = data.index('water-to-light map:\n')
light_to_temperature_i = data.index('light-to-temperature map:\n')
temperature_to_humidity_i = data.index('temperature-to-humidity map:\n')
humidity_to_location_i = data.index('humidity-to-location map:\n')

seeds_line = list(map(int, (data[0][6:].split())))


seeds =[]
for i in range(0, len(seeds_line), 2):
    seeds.append((seeds_line[i], seeds_line[i] + seeds_line[i+1]))

def src_to_dest(src_i, dest_i, input_range):

    ret = []
    
    sub_data = []
    if dest_i == 0:
        for line in data[src_i+1:]:
            sub_data.append(list(map(int, line.strip().split())))
    else:
        for line in data[src_i+1:dest_i-1]:
            sub_data.append(list(map(int, line.strip().split())))

    for start, stop in input_range:
        processed = False
        delta = stop - start

        for dest, src, range_ in sub_data:
            
            if src <= start and stop <= src + range_:
                ret.append((dest + start - src, dest + start - src + delta))
                processed = True

            elif start < src and src <= stop <= src + range_:
                branch1 = (start, src - 1)                
                sub_ret = src_to_dest(src_i, dest_i, [branch1])
                ret.extend(sub_ret)
                
                branch2 = (src, stop)
                ret.append((dest, dest + stop - src))
                processed = True

            elif src <= start <= src + range_ and src + range_ < stop:
                branch1 = (start, src + range_)
                ret.append((dest + start - src, dest + range_))
                processed = True

                branch2 = (src + range_ + 1, stop)
                sub_ret = src_to_dest(src_i, dest_i, [branch2])
                ret.extend(sub_ret)
        
        if not processed:
            ret.append((start, stop))
        
    return ret



result = []
    
for start, stop in seeds:
    input_range = [(start, stop)]
    input_range = src_to_dest(seed_to_soil_i, soil_to_fertilizer_i, input_range)
    input_range = src_to_dest(soil_to_fertilizer_i, fertilizer_to_water_i, input_range)
    input_range = src_to_dest(fertilizer_to_water_i, water_to_light_i, input_range)
    input_range = src_to_dest(water_to_light_i, light_to_temperature_i, input_range)
    input_range = src_to_dest(light_to_temperature_i, temperature_to_humidity_i, input_range)
    input_range = src_to_dest(temperature_to_humidity_i, humidity_to_location_i, input_range)
    input_range = src_to_dest(humidity_to_location_i, 0, input_range)
    result.extend(input_range)
    

lowest_loc = 1 << 60
for i, j in result:
    lowest_loc = min(i, lowest_loc)
print(lowest_loc)


