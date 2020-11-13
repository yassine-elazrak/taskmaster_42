from subprocess import Popen
from threading import Timer, Thread
import os
import re


#list_pid = defaultdict(lambda: None)

def ENV(env_program):
    new_env = dict(os.environ)
    for arg in env_program:
        data=arg.split('=')
        new_env[data[0]]=data[1]
    return new_env


def my_job(program):
    print(program.stdout)
    #os.chdir(program.workingdir)
    with open(program.stdout,'w') as out, open(program.stderr, 'w') as err:
        cmd_args = program.cmd.split()
        env_new = ENV(program.env)
        out_cmd = Popen(cmd_args, stdout=out,stderr=err,shell=True,cwd=".", env=env_new)
        # umask=program.umask)
        program.out_cmd=out_cmd
        print("hello yassine _is run out_cmd= ", out_cmd.pid)
# t4=threading.Thread(target=task)


def run_all_jobs(jobs):
    for name  in jobs.names:
        print("nameall=", name, jobs.list_jobs[name].starttime)
        program=jobs.list_jobs[name]
        t2=Thread(target=my_job, args=[program])
        t2.start()

        #thread(my_job,[program]).start()
        #Timer(program.starttime, my_job,[program]).start()
