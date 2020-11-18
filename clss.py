
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
        self.exitcodes=[]
        self.startretries=0
        self.starttime=0
        self.stopsignal=[]
        self.stoptime=-1
        self.out_cmd=None
        self.rety=1


    def init(list_args):
        pass

    def update(list_args):
        pass
class node:
    def __init__(self,name='', info_process=None, thread=None):
        self.name=name
        self.thread=thread
        self.info_process=info_process

class jobs:
    def __init__(self):
        self.names=list([])
        self.list_jobs=dict({})


        """
        def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    # function using _stop function
    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        while True:
            if self.stopped():
                return"""
