battery_capacity = 200
battery_level = 100

def reset_battery(initial, capacity):
    global battery_level, battery_capacity
    battery_level = initial
    battery_capacity = capacity

def allocate_energy(solar, wind, demand):
    global battery_level

    renewable = solar + wind
    renewable_used = min(renewable, demand)

    battery_used = 0
    grid_used = 0

    if renewable >= demand:
        surplus = renewable - demand
        battery_level = min(battery_capacity, battery_level + surplus)

    else:
        deficit = demand - renewable

        if battery_level >= deficit:
            battery_used = deficit
            battery_level -= deficit
        else:
            battery_used = battery_level
            grid_used = deficit - battery_level
            battery_level = 0

    return battery_used, grid_used, battery_level, renewable_used