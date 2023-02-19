import subprocess
import sys
import os

PATH = "/tmp/codecrafters/docker"

def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    os.mkdir(PATH)
    os.chdir(PATH)
    os.chroot(PATH)

    completed_process = subprocess.run([command, *args], capture_output=True)
    
    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)

    sys.exit(completed_process.returncode)

if __name__ == "__main__":
    main()
