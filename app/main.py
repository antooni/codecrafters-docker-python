import subprocess
import sys
import os
import shutil
import ctypes

PATH = "/tmp/codecrafters/docker"

def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    commandPath = os.path.dirname(command)
    executableDest = os.path.join(PATH, commandPath[1:])
    
    if not os.path.exists(executableDest):
        os.makedirs(executableDest)

    shutil.copy(command, executableDest)

    os.makedirs(os.path.join(PATH, 'usr/bin'))
    shutil.copy('/usr/bin/unshare', os.path.join(PATH, 'usr/bin/unshare'))

    os.chroot(PATH)
    libc = ctypes.CDLL(None)
    CLONE_NEWPID = 0x20000000
    libc.unshare.argtypes = [ctypes.c_int]
    libc.unshare(CLONE_NEWPID)

    completed_process = subprocess.run([command, *args], capture_output=True)
    
    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)

    sys.exit(completed_process.returncode)

if __name__ == "__main__":
    main()
