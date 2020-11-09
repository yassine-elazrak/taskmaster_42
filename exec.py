from subprocess import Popen
from threading import Timer
import os
import re



global list_pid

list_pid = defaultdict(lambda: None)

def ENV(env_program):
    new_env = dict(os.environ)
    for arg in env_program:
        data=arg.split('=')
        new_env[data[0]]=data[1]
    return new_env


def my_job(program):
    with open(,'w') as out, open(,'w') as err:
        args = program.cmd.split()
        env_new = ENV(program.env)
        out_cmd = Popen(args, stdout=out,stderr=err,shell=True,cwd=program.dir_work,\           env=env_new, umask=program.umask)
        list_pid[program.name]=out_cmd


def run_all(list_program):
    for program in list_program:
        Timer(program.time_wait,my_job,[program]).start()
