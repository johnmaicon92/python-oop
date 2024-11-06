"""
1. City Infrastructure Management System
Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class without methods.

class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
- Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script showing the creation of Vehicle objects and updating their owners.

"""

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of vehicle {self.registration_number} has been updated to {self.owner}.")

if __name__ == "__main__":
    vehicle1 = Vehicle("ABC123", "Car", "John Doe")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")

    print(f"Vehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

    vehicle1.update_owner("Alice Johnson")
    vehicle2.update_owner("Bob Brown")

    print(f"Updated Vehicle 1 Owner: {vehicle1.owner}")
    print(f"Updated Vehicle 2 Owner: {vehicle2.owner}")

    # I'm still a little confused about this task. Not sue I really understood it.

"""
Task 2: Event Management System Enhancement

- Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

- Code Example: Basic Event class without participant tracking.

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
"""

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

if __name__ == "__main__":
    event_name = input("Enter the event name: ")
    event_date = input("Enter the event date: ")
    event = Event(event_name, event_date)

    while True:
        add_part = input("Would you like to add a participant? (yes/no): ").strip().lower()
        if add_part == 'yes':
            event.add_participant() 
        elif add_part == 'no':
            break 
        else:
            print("Please enter 'yes' or 'no'.")

    print(f"Total participants for {event.name} on {event.date}: {event.get_participant_count()}")

