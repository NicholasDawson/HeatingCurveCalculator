def calculate_water_energy(grams, start_temp, end_temp):
    total_energy = 0

    if start_temp < 0:
        start_state = 1
    elif 0 < start_temp < 100:
        start_state = 2
    elif start_temp > 100:
        start_state = 3

    if end_temp < 0:
        end_state = 1
    elif 0 < end_temp < 100:
        end_state = 2
    elif end_temp > 100:
        end_state = 3
    
    # State 1 -> Ice
    # State 2 -> Water
    # State 3 -> Steam

    if start_state == 1:
        if end_state == 1:
            total_energy += grams * 2.03 * (end_temp - start_temp)
        elif end_state == 2:
            total_energy += grams * 2.03 * -start_temp
            total_energy += grams * 333.6
            total_energy += grams * 4.18 * end_temp
        elif end_state == 3:
            total_energy += grams * 2.03 * -start_temp
            total_energy += grams * 333.6
            total_energy += grams * 4.18 * 100
            total_energy += grams * 2263.6
            total_energy += grams * 2.01 * (end_temp - 100)
    
    elif start_state == 2:
        if end_state == 1:
            total_energy -= grams * 4.18 * start_temp
            total_energy -= grams * 333.6
            total_energy -= grams * 2.03 * end_temp
        elif end_state == 2:
            total_energy += grams * 4.18 * (end_temp - start_temp)
        elif end_state == 3:
            total_energy += grams * 4.18 * (100 - start_temp)
            total_energy += grams * 2263.6
            total_energy += grams * 2.01 * (end_temp - 100)
    
    elif start_state == 3:
        if end_state == 1:
            total_energy -= grams * 2.01 * (start_temp - 100)
            total_energy -= grams * 2263.6
            total_energy -= grams * 4.18 * 100
            total_energy -= grams * 333.6
            total_energy -= grams * 2.03 * -end_temp
        elif end_state == 2:
            total_energy -= grams * 2.01 * (start_temp - 100)
            total_energy -= grams * 2263.6
            total_energy -= grams * 4.18 * (100 - end_temp)
        elif end_state == 3:
            total_energy += grams * 2.01 * (end_temp - start_temp)
    return round(total_energy, 2)

print('-----HEATING CURVE CALCULATOR-----')
print('-----BY: NICK DAWSON-----\n')
joules = calculate_water_energy(float(input('Grams: ')), float(input('Start Temp: ')), float(input('End Temp: ')))
print('\n' + str(joules) + ' Joules')


