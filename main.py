import json,sys, os
from signals import handler_signal
from exec import run_all_jobs
from kk import message
from clss import jobs , program
from subprocess import Popen , check_output
from collections import defaultdict


def load_file():
    job = jobs()
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
        keys = list(data.keys())
        for key in keys:
            job.names.append(key)
        print("load_file",job.names)
        for name in job.names:
            job.list_jobs[name]=get_setting_program(data[name], name)
    print("___", job.names);
    return job
# def cmd(command):
#     #print command
#     #with open('out-file.txt', 'w') as f:
#     out = open("log_out", 'w')
#     err = open("log_err", 'w')
#     pip = Popen(command.split(), stdout=out, stderr=err, shell=True)
#     out.close()
#     err.close()
#     # print pip
#jobs=defaultdict(lambda : None)

# this func for test must you coding other func let security

def get_setting_program(setting,name):
    pr = program()
    keys=setting.keys()
    pr.name=name
    pr.cmd=setting["cmd"]
    pr.env=setting["env"]
    pr.stdout=setting["stdout"]
    pr.stderr=setting["stderr"]
    pr.umask=setting["umask"]
    pr.workingdir=setting["workingdir"]
    pr.autostart=setting["autostart"]
    pr.autorestart=setting["autorestart"]
    pr.exitcodes=setting["exitcodes"]
    pr.startretries=setting["startretries"]
    pr.starttime=setting["starttime"]
    pr.stopsignal=setting["stopsignal"]
    pr.stoptime=setting["stoptime"]
    return pr

def trait_data_json(file):
    pass
def main():
    jobs = load_file()
    print(jobs.names)
    run_all_jobs(jobs)
    """
    while True:
        #handler_signal(jobs)
        line=input()
        if line == "exit":
            sys.exit()
        print(line)"""




if __name__ == "__main__":
    main()

    #print(data.keys())
        #data['run']['cmd']))
