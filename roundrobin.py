"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


import os
import sys

import inout
from queue import Queue
from process import Process


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

        if process.burst > 0:
            q.put(process)
        elif process.burst < 0:
            process.set_burst(0)

        log.append(dump_to_log(q))
    
    return log


def main():
    output_string = ''
    jobs = inout.readFile('process.txt')
    quantum = int(jobs[0][0])

    q = initialize(jobs)
    log = round(q, quantum)
    print(log)

    for _round in log:
        for process in _round:
            output_string = inout.writeToString(process, output_string)
        output_string += '\n\n'
    
    inout.writeToFile(output_string, 'log.txt')



if __name__ == '__main__':
    main()