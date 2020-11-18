from subprocess import Popen
from threading import Timer, Thread
from time import sleep
import os
import re
from signal import *
from collections import defaultdict

#list_pid = defaultdict(lambda: None)

global global_signal
global_signal=-1

global dic_signal
dic_signal= defaultdict(lambda: None)
dic_signal={SIGINT:'SIGINT',SIGHUP:'SIGHUB',SIGILL:'SIGILL', SIGQUIT:'SIGQUIT', SIGTRAP:'SIGTRAP',\
            SIGABRT:'SIGABRT' , SIGBUS:'SIGBUS' , SIGFPE :'SIGFPE', SIGKILL:'SIGKILL',\
            SIGUSR1:'SIGUSR1', SIGSEGV:'SIGUSR2', SIGPIPE:'SIGPIPE', SIGALRM:'SIGALRM', SIGTERM:'SIGTERM'}

def ENV(env_program):
    new_env = dict(os.environ)
    for arg in env_program:
        data=arg.split('=')
        new_env[data[0]]=data[1]
    return new_env

def initchildproc():
    os.setpgrp()
    os.umask(400)

def my_process(program):
    print(program.stdout)
   # os.chdir("/tmp/")#(program.workingdir)
    with open(program.stdout,'a') as out, open(program.stderr, 'a') as err:
        cmd_args = program.cmd.split()
        #if program.starttime  > 0:
        sleep(2)
        print("print arg cmd", cmd_args)
        env_new = ENV(program.env)
        out_cmd = Popen(cmd_args, stdout=out,stderr=err,shell=True,cwd=program.workingdir, env=env_new)
        #mkdir and touch does not work in the same subprocess  preexec_fn=initchildproc::::;
        # umask=program.umask)
        program.pid=os.getpid()
        program.out_cmd=out_cmd
        print("hello yassine _is run out_cmd= ", out_cmd.pid, " getpid =",program.pid)
# t4=threading.Thread(target=task)

def status_process(program):
    out=program.out_cmd
    ## must init global_signal with =-1 all foiis
    if global_signal != -1:
        if dic_signal[global_signal] in program.stopsignal:
            if program.stoptime > 0:
                sleep(program.stoptime)#khata2  time0 - time
            print("kill this process with signal =", global_signal)
            os.kill(out.pid,global_signal)
            return 1
    #print("status_name", out.pid,"poll()", str(out.poll()), "rety=", program.startretries)
    if out.poll() is not None:
        print("polll=",str(out.poll()))
        if program.startretries > 1:
            program.startretries-=1
            my_process(program)
            return 0
        else:
            return 1
    return 0


def my_job(program):
    my_process(program)
    while True:
        if status_process(program) == 1:
            break



def run_all_jobs(jobs):
    for name  in jobs.names:
        print("nameall=", name, jobs.list_jobs[name].info_process.starttime)
        program=jobs.list_jobs[name].info_process
        jobs.list_jobs[name].thread=Thread(target=my_job, args=[program])
        jobs.list_jobs[name].thread.start()


        #thread(my_job,[program]).start()
        #Timer(program.starttime, my_job,[p1rogram]).start()
