"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


import os
import sys

import inputoutput
from queue import Queue
from process import Process


def initialize(jobs):
    q = Queue()

    for i in list(range(1, len(jobs))):
        job = jobs[i]
        process = Process(job[0], job[1], job[2])
        q.put(process)

    return q

def round(q, quantum):
    while q.empty() == False:
        process = q.get()

        if process.burst > quantum:
            process.decrease_burst(quantum)


def main():
    jobs = inputoutput.readFile('process.txt')
    quantum = jobs[0]

    q = initialize(jobs)


if __name__ == '__main__':
    main()