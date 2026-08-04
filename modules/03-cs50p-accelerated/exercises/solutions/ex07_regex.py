"""Reference solution — rung 7."""
import re


def find_dates(text):
    return re.findall(r"\d{2}/\d{2}/\d{4}", text)


def extract_usernames(text):
    return re.findall(r"([\w.]+)@[\w.]+", text)
