"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


import os
import sys

from queue import Queue

from iom import inout
from process.process import Process


def initialize(jobs):
    q = Queue()

    for i in list(range(1, len(jobs))):
        job = jobs[i]
        process = Process(job[0], job[1], job[2])
        q.put(process)

    return q


def dump_to_log(q):
    round_log = []
    _round = list(q.queue)

    for process in _round:
        round_log.append([process.name, process.burst])

    return round_log


def round(q, quantum):
    log = []
    log.append(dump_to_log(q))

    while q.empty() == False:
        process = q.get()
        process.decrease(quantum)

        if process.burst < 0:
            process.set_burst(0)
            process.set_status('complete')
        elif process.burst > 0:
            q.put(process)

        log.append(dump_to_log(q))
    
    return log
