import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]
    completed_process = subprocess.run([command, *args], capture_output=True, stdout=PIPE, stderr=PIPE)
    print(completed_process.stdout)
    print(completed_process.stderr)


if __name__ == "__main__":
    main()
