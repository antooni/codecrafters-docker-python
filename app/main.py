import subprocess
import sys
import os
import shutil

PATH = "/tmp/codecrafters/docker"

def main():
    command = sys.argv[3]
    args = sys.argv[4:]


    commandPath = os.path.dirname(command)
    executableDest = os.path.join(PATH, commandPath[1:])
    
    if not os.path.exists(executableDest):
        os.makedirs(executableDest)

    shutil.copy(command, executableDest)

    os.chroot(PATH)

    completed_process = subprocess.run(['/usr/bin/unshare', '--pid', command, *args], capture_output=True)
    
    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)

    sys.exit(completed_process.returncode)

if __name__ == "__main__":
    main()
