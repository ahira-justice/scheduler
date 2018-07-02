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
        process = Process(job[0], int(job[1]), int(job[2]))
        q.put(process)

    return q


def dump_to_log(q):
    round_log = list(q.queue)
    return round_log


def round(q, quantum):
    log = []
    log.append(dump_to_log(q))

    while q.empty() == False:
        process = q.get()

        if process.status == 'active':
            process.decrease_burst(quantum)
        
        if process.status != 'deactivated':
            q.put(process)

        log.append(dump_to_log(q))
    
    return log


def main():
    output_string = ''
    jobs = inout.readFile('process.txt')
    quantum = int(jobs[0][0])

    q = initialize(jobs)
    log = round(q, quantum)

    for round_log in log:
        for process in round_log:
            out = [process.name, process.burst]
            output_string = inout.writeToString(out, output_string)
        output_string += '\n\n'
    
    inout.writeToFile(output_string, 'log.txt')



if __name__ == '__main__':
    main()