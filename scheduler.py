"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


import os
import click

from iom import inout


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@click.command()
@click.option('-a', '--algo', default="", help='Name of sheduling algorithm.')
def main(algo):
    package = 'algorithms'
    algorithm = getattr(__import__(package, fromlist=[algo]), algo)

    output_string = ''
    jobs = inout.readFile('process/process.txt')
    quantum = int(jobs[0][0])

    schedule = algorithm.Schedule(jobs)
    schedule.setquantum(quantum)

    log = schedule.run()

    for _round in log:
        for process in _round:
            output_string = inout.writeToString(process, output_string)
        output_string += '\n\n'
    
    inout.writeToFile(output_string, os.path.join(BASE_DIR, 'log/{}.txt'.format(schedule.name)))


if __name__ == '__main__':
    main()
