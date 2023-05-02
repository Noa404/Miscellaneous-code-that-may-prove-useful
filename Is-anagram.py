from typing import Dict


def isanagram(self, a, b):
    if (sorted(a) == sorted(b)):
        return True
    else:
        return False


