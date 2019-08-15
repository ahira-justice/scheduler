# scheduler

## What is scheduler?

scheduler is born out of an undergraduate operating systems assignment. It is a package that implements some common operating system process scheduling algorithms. These are the algorithms responsible for allocating the CPU and moving jobs through the system.

Currently implemented algorithms are

- first come, first served (_fcfs_)
- roundrobin

## What scheduler is **not**

scheduler doesn't talk to the OS or affect it in anyway. It's only a useful _tool_ to visualize these basic OS concepts, and understand key terms such as _turnaround time_, _waiting time_, etcetera.

## Usage
```sh
scheduler.py --help

Usage: main.py [OPTIONS]

Options:
  -a, --algo TEXT  Name of sheduling algorithm.
  --help           Show this message and exit.
```

### Custom Algorithms
Each custom algorithm is a python _.py_ script created in _base_directory/algorithm/_ that defines a **Schedule** class

The Schedule class inherits from a **Algorithm** class. This Algorithm class contains the **setquantum()** and **run()** methods which are to be overridden in the Schedule class.

A _self.name_ should be defined for each Schedule class.

_sample_ **custom_algorithm.py**
```sh
from . import algorithm
from process.process import Process

class Schedule(algorithm.Algorithm):
    def __init__(self, jobs):
        super().__init__(jobs)
        self.name = 'fcfs'

```

**run()** must be overridden. **setquantum()** is to be overridden as applicable.

## Entry Points
```sh
scheduler.py --algo [ALGORITHM]
```
You can change the supply of processes by editing the _process.txt_ file found in _base_directory/process/_

_sample_ **process.txt**
```sh
5
A 0 10
B 2 12
C 3 3
D 6 1
E 9 15
```
The first line represents the time slice/quantum given to run. This is present in some algorithms like roundrobin and multi level queues.

The subsequent lines define a job each. The first value is the job's designation, the second value is the arrival time and the third is the execution time of the job.

## Installation
**git clone** this repo and add your custom algorithm scripts to the package in _base_directory/algorithm/_

```sh
git clone https://github.com/ahira-justice/scheduler.git
```

To run your custom algorithm

```sh
scheduler.py --algo custom_algorithm
```

## Dependencies
```sh
click
```

After cloning **scheduler**, run the below command from it's base directory to install **scheduler**'s dependencies.
```sh
pip install -r requrements.txt
```

## License

[GNU GENERAL PUBLIC LICENSE](LICENSE)
