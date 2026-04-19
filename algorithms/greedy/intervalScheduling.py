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
    # Step 1: sort jobs by profit from highest to lowest
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Step 2: create empty time slots
    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline

    # Step 3: try to place each job in the latest possible slot
    for job in sorted_jobs:
        job_id, deadline, profit = job

        # try deadline-1, then deadline-2, ..., down to 0
        for slot in range(deadline - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job
                break

    return slots


jobs = [
    ("J1", 2, 100),
    ("J2", 1, 19),
    ("J3", 2, 27),
    ("J4", 1, 25),
    ("J5", 3, 15),
    ("J6", 1, 30)
]

schedule = intervalSchedule(jobs)
print("Schedule:", schedule)

total_profit = sum(job[2] for job in schedule if job is not None)
print("Total profit:", total_profit)