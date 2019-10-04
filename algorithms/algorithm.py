"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


from queue import Queue
from process.process import Process


class Algorithm:
    def __init__(self, jobs):
        self.quantum = 0
        self.log = []
        self.round_log = []

        self.q = Queue()

        for i in list(range(1, len(jobs))):
            job = jobs[i]
            process = Process(job[0], job[1], job[2])
            self.q.put(process)

    def setquantum(self, value):
        pass

    def dump_to_log(self):
        self.round_log = []
        _round = list(self.q.queue)

        for process in _round:
            self.round_log.append([process.name, process.burst])

        return self.round_log

    def run(self):
        pass
