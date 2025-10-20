import random
import time
import matplotlib.pyplot as plt

# Define a Car class to represent each car
class Car:
    def __init__(self, car_id, speed):
        self.car_id = car_id
        self.speed = speed  # speed in km/h
        self.position = 0  # position of the car on the road in km

    def move(self):
        # Randomly decide whether the car slows down, speeds up, or continues at the same speed
        behavior = random.choice(['normal', 'slow_down', 'speed_up', 'stop'])
        if behavior == 'slow_down':
            self.speed = max(20, self.speed - random.randint(5, 20))  # Slow down but not below 20 km/h
        elif behavior == 'speed_up':
            self.speed = min(150, self.speed + random.randint(5, 20))  # Speed up but not above 150 km/h
        elif behavior == 'stop':
            self.speed = 0  # Temporary stop

        # Move the car forward by updating its position based on its speed
        self.position += self.speed / 60  # Assume move is called every minute

    def __repr__(self):
        return f"Car {self.car_id}: Speed={self.speed} km/h, Position={self.position:.2f} km"


# Define a TrafficFlow class to represent the flow of cars
class TrafficFlow:
    def __init__(self, num_cars):
        self.cars = [Car(car_id=i, speed=random.randint(40, 120)) for i in range(num_cars)]

    def simulate(self, minutes, checkpoint=10):
        flow_rates = []  # List to store the number of cars passing the checkpoint every minute

        for minute in range(minutes):
            cars_passed = 0
            for car in self.cars:
                car.move()
                # Count how many cars pass the checkpoint in this minute
                if car.position >= checkpoint:
                    cars_passed += 1

            # Reset positions of cars that pass the checkpoint for continuous flow
            for car in self.cars:
                if car.position >= checkpoint:
                    car.position = 0  # Reset to zero after passing checkpoint

            flow_rates.append(cars_passed)

            # Optionally print out the state of each car at each minute
            print(f"Minute {minute + 1}:")
            for car in self.cars:
                print(car)
            print(f"Cars passed checkpoint: {cars_passed}\n")

            time.sleep(0.1)  # Simulate real-time passage (optional, can be removed for faster runs)

        return flow_rates


# Plot the flow rate across time
def plot_flow_rate(flow_rates):
    plt.figure(figsize=(10, 5))
    plt.plot(flow_rates, label="Cars Passing per Minute", color='blue', marker='o')
    plt.title('Traffic Flow Rate Over One Hour')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Number of Cars Passing')
    plt.grid(True)
    plt.legend()
    plt.show()


# Create a traffic flow simulation with 100 cars
traffic = TrafficFlow(num_cars=100)

# Simulate the traffic for 60 minutes (1 hour)
flow_rates = traffic.simulate(minutes=60, checkpoint=10)

# Plot the flow rates
plot_flow_rate(flow_rates)
