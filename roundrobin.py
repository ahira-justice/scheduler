"""
    Adefokun Ahira Justice
    justiceahira@gmail.com
"""


import os
import sys


def readFile(filename):
    assert os.path.exists(filename), 'Cannot find the file: %s' % (filename)
    file = open(filename, 'r')
    content = []
    for line in file:
        newLine = line.split()
        content.append(newLine)
    file.close()
    return content


def writeToFile(output, name):
    file = open(name, 'w')
    file.write(output)
    file.close()
    sys.exit()


def writeToOutput(output, out_print):
    for item in output:
        item = str(item)
        out_print += item + '\t'
    out_print += '\n'

    return out_print


def main():
    processes = readFile('process.txt')
    print (processes)
    quantum = processes[0]



if __name__ == '__main__':
    main()