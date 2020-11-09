import json
from subprocess import Popen , check_output

def load_file():
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
    return data
def cmd(command):
    #print command
    #with open('out-file.txt', 'w') as f:
    out = open("log_out", 'w')
    err = open("log_err", 'w')
    pip = Popen(command.split(), stdout=out, stderr=err, shell=True)
    out.close()
    err.close()
    print pip

if __name__ == "__main__":
    data = load_file()
    print(cmd("ls"))
        #data['run']['cmd']))
