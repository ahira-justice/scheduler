"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


import os
import click

from iom import inout
from algorithms import roundrobin as rr


BASE_DIR = os.path.join(os.path.dirname(__file__))

@click.command()
def main():
    output_string = ''
    jobs = inout.readFile('process/process.txt')
    quantum = int(jobs[0][0])

    q = rr.initialize(jobs)
    log = rr.round(q, quantum)

    for _round in log:
        for process in _round:
            output_string = inout.writeToString(process, output_string)
        output_string += '\n\n'
    
    inout.writeToFile(output_string, os.path.join(BASE_DIR, 'log/log.txt'))


if __name__ == '__main__':
    main()
