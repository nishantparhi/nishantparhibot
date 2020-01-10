import subprocess
from time import sleep
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read

class BashTerminal:
    def __init__(self):
        # Terminal
        self.process = subprocess.Popen(["/bin/bash"],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        flags = fcntl(self.process.stdout, F_GETFL)
        fcntl(self.process.stdout, F_SETFL, flags | O_NONBLOCK)

    def ex_command(self, command):
        try: 
            self.process.stdin.write(command+"\n");
            sleep(0.1);
            try:
                return self.process.stdout.read();
            except:
                return "";
        except:
            # New terminal
            self.process = subprocess.Popen(["/bin/bash"],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE);
            flags = fcntl(self.process.stdout, F_GETFL)
            fcntl(self.process.stdout, F_SETFL, flags | O_NONBLOCK)
            return "ERROR"
