#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:

    def __init__(self, name=None, job=None):
        self.name = name
        self.job = job

        if name is None:
            pass
        elif isinstance(name, str) and (len(name) > 0) and (len(name) < 26):
            self.name = " ".join([n.capitalize() for n in name.split(" ")])
        else:
            print("Name must be string between 1 and 25 characters.")

        if job is None:
            pass
        elif job in APPROVED_JOBS:
            self.job = job            
        else:
            print("Job must be in list of approved jobs.")
