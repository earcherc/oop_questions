# Parking lot management system
# Multiple levels
# motorcycles, cars, buses
# entrances and exits
# collect parking ticket and pay parking fee
# calculate parking fees based on duration
# track total occupancy and available parks 
# rate limiting during peak hours

# clarifying
# different vehicle types
# tracking available spots efficiently

# Classes
# Parking lot (entire)
    # contains levels
    # contains ticket system
    # contains vehicles 
    # contains entries and exits
# Parking level
    # Track current occupancy and type
    # get method
# Ticket system
    # Store all tickets
    # Print initial ticket
    # Calculate duration
# Vehicle
    # License plate
    # Entry time
    # Exit time

import random
from typing import Optional

class Vehicle:
    def __init__(self, license, type):
        self.license = license
        self.type = type

class ParkingLot:
    def __init__(self, levels, entries, exits):
        self.levels = [ParkingLevel(i) for i in range(levels)]

class ParkingLevel:
    def __init__(self, level_id, capacity=100):
        self.level_id = level_id
        self.capacity = capacity
        self.spaces = self.initialise_spaces()
        self.available_spaces = self.spaces.copy()
        self.occupied_spaces = {}
    
    def initialise_spaces(self):
        motorcycle = {id: {'type': 'Motorcycle', 'available': True} for id in range(int(self.capacity * .2))}
        bus = {id: {'type': 'Bus', 'available': True} for id in range(int(self.capacity * .2), int(self.capacity * .3))}
        car = {id: {'type': 'Car', 'available': True} for id in range(int(self.capacity * .3), int(self.capacity * .7))}
        self.spaces = {**motorcycle, **bus, **car}
    
    def get_capacity(self):
        print(self.capacity)

    def num_available_spaces(self):
        return {
            'Car': sum(1 for info in self.available_spaces.values() if info['type'] == 'Car'),
            'Car': sum(1 for info in self.available_spaces.values() if info['type'] == 'Car'),
            'Car': sum(1 for info in self.available_spaces.values() if info['type'] == 'Car'),
        }
    
    def park(self, vehicle: Vehicle) -> Optional[int]:
        available = [id for id, info in self.available_spaces.items() if info['type'] == vehicle.vehicle_type]
        if not available:
            return None

        selected_id = random.choice(available)
        self.spaces[selected_id]['available'] = False 
        del self.available_spaces[selected_id]
        self.occupied_spaces[vehicle.license] = selected_id
        
        return selected_id


    def exit(self, vehicle: Vehicle) -> Optional[int]:
        selected_id = self.occupied_spaces[vehicle.license]
        if not selected_id:
            return None
        
        self.spaces[selected_id]['available'] = True
        self.available_spaces[selected_id] = self.spaces[selected_id]
        del self.occupied_spaces[vehicle.license]

        return selected_id

        
        




level = ParkingLevel()

