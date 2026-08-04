"""Rung 7 — regular expressions. Raw strings ALWAYS: r"...". Build patterns piece by piece
in the REPL (python, then: import re; re.findall(r"\\d+", "a1b22"))."""


def find_dates(text):
    """Return every dd/mm/yyyy date in text, in order, as strings.
    find_dates("due 07/08/2026, resat 12/09/2026") -> ["07/08/2026", "12/09/2026"]
    (Two digits, slash, two digits, slash, four digits — don't validate real calendars.)"""
    raise NotImplementedError("your code here")


def extract_usernames(text):
    """Return the username part (before the @) of every email-shaped token in text.
    extract_usernames("mail samrath@leeds.ac.uk or admin@psoc.org") -> ["samrath", "admin"]
    (Email-shaped: word-chars/dots before @, word-chars/dots after — keep it simple.)"""
    raise NotImplementedError("your code here")
