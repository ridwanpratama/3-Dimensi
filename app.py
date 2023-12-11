import random

def calculate_memory_address(base_address, shape, indices, element_size):
    address = base_address
    for i, dim_size in enumerate(shape):
        stride = 1
        for j in range(i + 1, len(shape)):
            stride *= shape[j]
        address += (indices[i] - 1) * stride
    return address * element_size

def generate_weather_data(locations, days, times):
    weather_data = [[[0 for _ in times] for _ in days] for _ in locations]
    base_address = 0x0011
    element_size = 4

    for loc_index, _ in enumerate(locations):
        for day_index, _ in enumerate(days):
            for time_index, _ in enumerate(times):
                indices = [loc_index + 1, day_index + 1, time_index + 1]
                address = calculate_memory_address(
                    base_address, 
                    [len(locations), len(days), len(times)], 
                    indices, 
                    element_size
                )
                weather_data[loc_index][day_index][time_index] = (address, generate_random_temperature())

    return weather_data

def generate_random_temperature():
    return round((20 + 15 * random.random()), 2)

def display_weather_data(weather_data, locations, days, times):
    for loc_index, location in enumerate(locations):
        print(f"\nLocation {location}:")
        for day_index, day in enumerate(days):
            print(f"\n{day}:")
            for time_index, time in enumerate(times):
                address, temperature = weather_data[loc_index][day_index][time_index]
                print(f"{time}:  Temperature = {temperature} °C | Address = {hex(address)}")

def find_element_address(base_address, shape, indices, element_size, weather_data):
    address = calculate_memory_address(base_address, shape, indices, element_size)
    data = weather_data[indices[0] - 1][indices[1] - 1][indices[2] - 1]
    return address, data

def main():
    locations = ["City A", "City B"]
    days = ["Day 1", "Day 2"]
    times = ["Morning", "Afternoon", "Evening"]

    weather_data = generate_weather_data(locations, days, times)
    display_weather_data(weather_data, locations, days, times)    
    
    target_indices = [2, 2, 1]
    base_address = 0x0011
    element_size = 4
    found_address, found_data = find_element_address(
        base_address, 
        [len(locations), len(days), len(times)], 
        target_indices, 
        element_size, 
        weather_data
    )
    print(f"\nAddress for indices {target_indices}: {hex(found_address)}, Data: {found_data[1]}")

if __name__ == "__main__":
    main()