#!/usr/bin/env python3
"""Self-checker for module 14. Every expected value below was computed on this
machine and pinned — if your function disagrees, your function is wrong.

  python check.py              -> test YOUR files
  python check.py ex02         -> one exercise
  python check.py --solutions  -> harness self-verify against reference solutions
"""
import sys as _sys  # keep the tick/cross marks printable on a cp1252 console
if hasattr(_sys.stdout, "reconfigure"):
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import base64
import importlib.util
import inspect
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# A fixed 32-byte key, standing in for monk-mode's per-block random one.
KEY = b"monk-mode-demo-key-32-bytes!!!!!"
# A fixed 16-byte salt (PartnerSaltBytes = 16), bytes 0x00..0x0f.
SALT = bytes(range(16))
CODE = "7QMTX9WKZ3"  # 10 chars from the Crockford-style alphabet, already normalised


def load(name, from_solutions):
    folder = HERE / "solutions" if from_solutions else HERE
    spec = importlib.util.spec_from_file_location(name, folder / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def t_ex01(mod):
    # --- sha256: the exact digest TEACH §1 prints, and the avalanche neighbour ---
    got = mod.sha256_hex("hello")
    want = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert got == want, f"sha256_hex('hello'): expected {want!r}, got {got!r}"
    near = mod.sha256_hex("hellp")
    assert near == "fdd7585e08c4e2afd71dcabdb4636c89d557a3f42db9e2040c8bbd1708aa4ce7", \
        f"sha256_hex('hellp'): got {near!r} (one letter changed — the whole digest must change)"
    assert len(got) == 64, f"a SHA-256 hex digest is 64 characters; yours is {len(got)}"

    # --- HMAC: the default encoding IS the lesson (TEACH §4) ---
    text = "Until=2026-08-05\nCommitted=yes\n"
    utf16 = mod.hmac_sha256_b64(KEY, text)
    assert utf16 == "PCCV1FiwvyTVrlT/jkz18CBNF68bkwZf1JLEHAKrAh4=", \
        (f"hmac_sha256_b64 default (UTF-16LE, i.e. .NET's Encoding.Unicode): got {utf16!r}"
         " — if you got the UTF-8 value your default encoding is wrong")
    utf8 = mod.hmac_sha256_b64(KEY, text, encoding="utf-8")
    assert utf8 == "qs3n17EUoL1dgDqHAcSbeXeR/AxEKC6USwM9Jss1Ejo=", \
        f"hmac_sha256_b64(..., encoding='utf-8'): got {utf8!r}"
    assert utf16 != utf8, ("encoding is not a detail: the SAME text HMAC'd as UTF-16LE and as"
                           " UTF-8 must give COMPLETELY different MACs. Yours matched, so you"
                           " are ignoring the encoding argument.")

    # --- PBKDF2: cheap vector to keep this checker fast, plus the real defaults ---
    got = mod.pbkdf2_b64(CODE, SALT, iterations=1000, length=32)
    assert got == "ifFqbbcrOJfRWahoWFCpC7owTQxrZQ9Py3B+5I4TrGs=", \
        (f"pbkdf2_b64({CODE!r}, 16-byte salt, 1000 rounds, 32 bytes): got {got!r}"
         " — if you got c2ID/nZ57D/HXK8GGSjSu9j0RJGoUFUTwKU571C3LrU= you encoded the"
         " code as UTF-8. PartnerKdf feeds it Encoding.Unicode.GetBytes(...), so it is"
         " UTF-16LE here too: the SAME trap as the MAC, one function later.")
    short = mod.pbkdf2_b64(CODE, SALT, iterations=1000, length=16)
    assert len(base64.b64decode(short)) == 16, "pbkdf2_b64 must honour `length`"
    assert got != mod.pbkdf2_b64(CODE, bytes(16), iterations=1000, length=32), \
        "a different salt must give a different hash — that is what salt is FOR"
    # The 600,000 is pinned without paying 0.39 s per run (monk-mode pins it by unit
    # test for the same reason: a retune must be one loud edit).
    defaults = inspect.signature(mod.pbkdf2_b64).parameters
    assert defaults["iterations"].default == 600000, \
        (f"default iterations must be 600000 (ConfigIntegrity.vb PartnerKdfIterations);"
         f" yours is {defaults['iterations'].default}")
    assert defaults["length"].default == 32, \
        f"default length must be 32 (PartnerHashBytes); yours is {defaults['length'].default}"

    # --- safe_equals: constant-time, and fail-closed (TEACH §6–7) ---
    assert mod.safe_equals(utf16, utf16) is True, "identical MACs must compare equal"
    assert mod.safe_equals(utf16, utf8) is False, "different MACs must compare unequal"
    # "AA==" and "AB==" are DIFFERENT strings that both decode to b"\x00". A string
    # comparison says no; decoding first and comparing the raw bytes says yes — which
    # proves you compared bytes, exactly like FixedTimeEquals does.
    assert mod.safe_equals("AA==", "AB==") is True, \
        ('safe_equals("AA==", "AB==") must be True: both decode to b"\\x00". You are'
         " comparing the Base64 STRINGS instead of decoding to raw bytes first.")
    for bad in ("not base64!!", "", "AAA", "PCCV1FiwvyTVrlT/jkz18CBNF68bkwZf1JLEHAKrAh4"):
        try:
            r = mod.safe_equals(bad, utf16)
        except Exception as e:
            raise AssertionError(
                f"safe_equals({bad!r}, ...) raised {type(e).__name__} — it must FAIL CLOSED:"
                " return False, never throw (ConfigMacIsValid's whole spine)") from None
        assert r is False, f"safe_equals({bad!r}, ...) must be False, got {r!r}"


def t_ex02(mod):
    fields = [("Until", "2026-08-05"), ("Committed", "yes")]
    got = mod.build_canonical(fields)
    want = "Until=2026-08-05\nCommitted=yes\n"
    assert got == want, f"build_canonical: expected {want!r}, got {got!r}"
    assert mod.build_canonical([]) == "", "no fields -> empty canonical"

    got = mod.build_naive(fields)
    want = "Until=2026-08-05Committed=yes"
    assert got == want, f"build_naive: expected {want!r} (no separator at all), got {got!r}"

    a, b = mod.forge_naive()
    assert a != b, "forge_naive: the two field-lists must actually DIFFER"
    na, nb = mod.build_naive(a), mod.build_naive(b)
    assert na == nb, (f"forge_naive: the naive strings must be IDENTICAL — that is the"
                      f" forgery.\n  a -> {na!r}\n  b -> {nb!r}")
    ca, cb = mod.build_canonical(a), mod.build_canonical(b)
    assert ca != cb, (f"forge_naive: build_canonical must still tell them apart — that is"
                      f" the fix working. Both gave {ca!r}")
    names_a, names_b = [n for n, _ in a], [n for n, _ in b]
    assert names_a != names_b or dict(a) != dict(b), \
        "the two field-sets must mean different things, not just be reordered"
    assert set(names_a) ^ set(names_b) or dict(a) != dict(b), \
        ("make it a real attack: a security-relevant field should end up missing or"
         " changed in the second set, not merely reshuffled")


TESTS = {"ex01_primitives": t_ex01, "ex02_canonical": t_ex02}


def main():
    from_solutions = "--solutions" in sys.argv
    only = next((a for a in sys.argv[1:] if not a.startswith("--")), None)
    passed = failed = todo = 0
    for name, test in TESTS.items():
        if only and not name.startswith(only):
            continue
        try:
            test(load(name, from_solutions))
            passed += 1
            print(f"  PASS  {name}")
        except NotImplementedError:
            todo += 1
            print(f"  TODO  {name}: not written yet")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {name}: {e}")
        except Exception as e:
            failed += 1
            print(f"  FAIL  {name}: {type(e).__name__}: {e}")
    src = "solutions" if from_solutions else "your files"
    print(f"\n{src}: {passed} passed · {failed} failed · {todo} not started")


if __name__ == "__main__":
    main()
