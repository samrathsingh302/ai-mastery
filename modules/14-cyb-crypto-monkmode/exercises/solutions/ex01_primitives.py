"""Reference solution — rung 1."""
import base64
import hashlib
import hmac


def sha256_hex(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def hmac_sha256_b64(key_bytes, text, encoding="utf-16-le"):
    mac = hmac.new(key_bytes, text.encode(encoding), hashlib.sha256).digest()
    return base64.b64encode(mac).decode("ascii")


def pbkdf2_b64(code, salt_bytes, iterations=600000, length=32):
    dk = hashlib.pbkdf2_hmac("sha256", code.encode("utf-8"), salt_bytes,
                             iterations, length)
    return base64.b64encode(dk).decode("ascii")


def safe_equals(a_b64, b_b64):
    try:
        a, b = base64.b64decode(a_b64, validate=True), base64.b64decode(b_b64, validate=True)
    except Exception:
        return False                      # fail-closed, like ConfigMacIsValid
    return hmac.compare_digest(a, b)      # constant time — no early exit
