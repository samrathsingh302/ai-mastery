"""Mission 5 — launching programs. Args as a LIST, always (no shell strings)."""


def python_version():
    """Run THIS Python (sys.executable) with --version; return just the number,
    e.g. "3.14.5". (capture_output=True, text=True; the text may arrive on stdout
    OR stderr depending on version — handle both.)"""
    raise NotImplementedError("your code here")


def git_head_short(repo_path):
    """Return the current short commit hash of the git repo at repo_path
    (git rev-parse --short HEAD, cwd=repo_path), stripped. If the command fails
    (non-zero returncode), return None."""
    raise NotImplementedError("your code here")
