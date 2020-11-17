import signal
import os

#global dict_signal = {'SIDHUP':signal.SIGHUP}
list_sinal = {2:signal.SIGHUP}

def _send_signal(sig):
    for name in jobs_all.names:
        program=jobs_all.list_jobs[name]
        if list_sinal[sig] in program.stopsigna:
            os.kill(sig,program.pid)

def  receiveSignal(nbr_signal, param):
    #_send_signal(nbr_signal)
    print("hello yassine", nbr_signal,"param",param)

def handler_signal():
    signal.signal(signal.SIGHUP, receiveSignal)
    signal.signal(signal.SIGINT, receiveSignal)
"""signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, receiveSignal)
"""
"""
def main():
    while True:
        handler_signal()
        line=input()
        print("command is -> ",line)
if __name__ == "__main__":
    main()"""


