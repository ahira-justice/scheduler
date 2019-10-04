"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


from . import algorithm


class Schedule(algorithm.Algorithm):
    def __init__(self, jobs):
        super().__init__(jobs)
        self.name = 'roundrobin'

    def setquantum(self, value):
        self.quantum = value

    def run(self):
        self.log = []
        self.log.append(self.dump_to_log())

        while self.q.empty() is False:
            process = self.q.get()
            process.decrease(self.quantum)

            if process.burst <= 0:
                process.set_burst(0)
                process.set_status('complete')
            elif process.burst > 0:
                self.q.put(process)

            self.log.append(self.dump_to_log())

        return self.log
