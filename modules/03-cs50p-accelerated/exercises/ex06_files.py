"""Rung 6 — file I/O. The `with open(...)` idiom, both directions. check.py hands you a
temporary folder path — never hard-code paths."""


def word_frequencies(path):
    """Read the text file at path; return a dict of lower-cased word -> count.
    "Words" are whitespace-separated; strip the punctuation .,!?;: from each end first;
    ignore anything that becomes empty. ("The cat, the CAT!" -> {"the": 2, "cat": 2})"""
    raise NotImplementedError("your code here")


def write_then_read(path, lines):
    """Write each string in `lines` to the file at path, one per line. Then read the file
    back and return the list of lines (without newline characters). Round-trip law:
    write_then_read(p, ["a", "b"]) -> ["a", "b"]"""
    raise NotImplementedError("your code here")
