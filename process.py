"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


class Process:
    def __init__(self, name, arrival, burst):
        self.name = name
        self.arrival = int(arrival)
        self.burst = int(burst)


    def set_burst(self, value):
        self.burst = value


    def decrease(self, value):
        self.burst -= value
