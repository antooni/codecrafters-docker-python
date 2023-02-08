import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]
    completed_process = subprocess.run([command, *args], capture_output=True)
    
    completed_process.wait()

    print(completed_process.stderr.decode())
    print(completed_process.stdout.decode())


if __name__ == "__main__":
    main()
