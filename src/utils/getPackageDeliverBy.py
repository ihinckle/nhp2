import time
from src.constants import DEADLINE_STR, EOD, TIME_FORMAT


def get_package_deliver_by(node):
    deliver_by = node.get(DEADLINE_STR)
    if deliver_by == EOD:
        return None
    return time.strptime(deliver_by, TIME_FORMAT)
