
class program:
    def __init__(self):
        self.name=''
        self.cmd=''
        self.pid=0
        self.env=[]
        self.stdout='/dev/null'
        self.stderr='/dev/null'
        self.umask= 2
        self.workingdir='/temp'
        self.autostart=False
        self.autorestart=False
        self.exitcodes=0
        self.startretries=0
        self.starttime=0
        self.stopsignal=''
        self.stoptime=-1
        self.out_cmd=None


    def init(list_args):
        pass

    def update(list_args):
        pass

class jobs:
    def __init__(self):
        self.names=list([])
        self.list_jobs=dict({})
