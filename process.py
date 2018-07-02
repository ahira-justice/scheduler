"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


class Process:
    def __init__(self, name, arrival, burst):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.status = 'active'

    def decrease_burst(self, amount):
        if self.status == 'active':
            self.burst -= amount
        
        if self.burst <= 0:
            self.deactivate()

    def deactivate(self):
        self.status = 'deactivated'