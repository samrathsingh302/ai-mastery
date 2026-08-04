"""Reference solution — mission 5."""
import subprocess
import sys


def python_version():
    r = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
    text = (r.stdout or r.stderr).strip()          # e.g. "Python 3.14.5"
    return text.split()[-1]


def git_head_short(repo_path):
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       capture_output=True, text=True, cwd=repo_path)
    if r.returncode != 0:
        return None
    return r.stdout.strip()
