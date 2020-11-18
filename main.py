import json,sys, os
from signals import handler_signal
from exec import run_all_jobs
import exec
from kk import message
from clss import jobs , program , node
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
            job.list_jobs[name]= node(name, get_setting_program(data[name], name))
    print("___", job.names);
    return job



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
    print("name command=",jobs.list_jobs['ls'].info_process.name)
    run_all_jobs(jobs)

    while True:
        handler_signal()
        if exec.global_signal > -1:
            print("nbr_signalmain=", exec.dic_signal[exec.global_signal])
        line=input()
        if line == "exit":
            sys.exit()
        print(line)



if __name__ == "__main__":
    main()

    #print(data.keys())
        #data['run']['cmd']))
