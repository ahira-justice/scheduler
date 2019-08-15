"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


from . import algorithm
from process.process import Process


class Schedule(algorithm.Algorithm):
    def __init__(self, jobs):
        super().__init__(jobs)
        self.name = 'fcfs'

    def run(self):
        self.log = []
        self.log.append(self.dump_to_log())

        while self.q.empty() == False:
            process = self.q.get()
            process.decrease(process.burst)

            process.set_burst(0)
            process.set_status('complete')

            self.log.append(self.dump_to_log())
        
        return self.log
