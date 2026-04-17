"""
You are given a list of jobs. Each job takes 1 unit of time and has:

a deadline d
a profit p

If you finish a job on or before its deadline, you earn its profit.
You can only do one job at a time.

Your goal is to choose a subset of jobs and schedule them to maximize total profit.
jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]
(job_id, deadline, profit)
So:

J1 must be done by time 2 for profit 100
J2 must be done by time 1 for profit 19
etc.
"""

"""
sort by shortest time first (then if time is same, take highest profit)
continue
"""

def intervalSchedule(jobs):
    #sorted by shortest time first AND by profit
    sorted_job = sorted(jobs, key=lambda x: x[1])
    S = []
    return sorted_job

jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15)
]

print(intervalSchedule(jobs))