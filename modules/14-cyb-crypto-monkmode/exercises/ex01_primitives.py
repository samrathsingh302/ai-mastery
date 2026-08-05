"""Rung 1 — the primitives, rebuilt. Python's hashlib/hmac only (stdlib).
Verify with: python check.py"""
import base64
import hashlib
import hmac


def sha256_hex(text):
    """Return the SHA-256 hex digest of text (UTF-8 encoded).
    sha256_hex("hello") -> "2cf24dba...9824" (64 hex characters)"""
    raise NotImplementedError("your code here")


def hmac_sha256_b64(key_bytes, text, encoding="utf-16-le"):
    """monk-mode's ComputeConfigMac, in Python: HMAC-SHA256 over text encoded with
    `encoding`, keyed with key_bytes, returned Base64. Default encoding is UTF-16LE
    because that is what .NET's Encoding.Unicode means (this is the trap)."""
    raise NotImplementedError("your code here")


def pbkdf2_b64(code, salt_bytes, iterations=600000, length=32):
    """monk-mode's ComputePartnerHash, in Python: PBKDF2-HMAC-SHA256 over code
    (UTF-8) with salt_bytes, `iterations` rounds, `length` bytes out, Base64."""
    raise NotImplementedError("your code here")


def safe_equals(a_b64, b_b64):
    """Constant-time comparison of two Base64 MACs (decode first, then compare the
    RAW BYTES). Must not exit early on the first difference — that's the whole point.
    Return False (never raise) if either string isn't valid Base64: fail-closed."""
    raise NotImplementedError("your code here")
