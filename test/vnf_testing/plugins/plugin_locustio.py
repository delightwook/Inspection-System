# -*- coding: utf-8 -*-
# plugin_locustio.py

from ssh_manager import listener
import subprocess
import logging
LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


def start(hosts=None, auth=None, vnf_testing_args_dict=None):
    cmd = 'locust -f locustfile.py'
    # locustfile.py transfer needed
    # vnf_testing_args_dict has the path of locustfile.py
    listener.start_command(hosts=hosts, auth=auth, command=cmd)
    # Todo : How to open new tab for locustio gui page?
