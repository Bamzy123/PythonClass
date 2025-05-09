"""
check if length are the same
concatenate s with itself and check if goal is a substring
"""

def can_rotate(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)