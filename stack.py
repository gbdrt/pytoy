"""
The ultimate stack!
"""


class Stack:
    def __init__(self):
        self.empty = True

    def isempty(self):
        return self.empty

    def push(self, v):
        self.empty = False
