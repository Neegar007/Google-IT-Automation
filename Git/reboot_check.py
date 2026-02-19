import os


def reboot():
    """ Return true if the system needs a reboot"""

    return os.path.exist("/run/reboot-required")