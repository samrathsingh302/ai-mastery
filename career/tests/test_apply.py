"""Tests for career/apply.py.

Run from the repo root:

    python -m unittest discover -s career/tests -t career

Every test works on a tempfile copy of targets.json, so the real one and the
real drafts/ folder are never touched.
"""
import copy
import io
import json
import re
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import apply  # noqa: E402

SEED = Path(apply.__file__).resolve().parent / "targets.json"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="apply-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.file = self.tmp / "targets.json"
        shutil.copyfile(SEED, self.file)
        self.data = apply.load(self.file)

    def run_cli(self, argv):
        """Run main() with stdout and stderr captured. Returns (code, stdout)."""
        buf = io.StringIO()
        with redirect_stdout(buf), redirect_stderr(io.StringIO()):
            code = apply.main(argv + ["--file", str(self.file)])
        return code, buf.getvalue()

    def reload(self):
        return apply.load(self.file)


class TestValidate(Base):
    def test_seed_is_clean(self):
        self.assertEqual([], apply.problems(self.data))
        code, out = self.run_cli(["validate"])
        self.assertEqual(0, code)
        self.assertIn("OK: %d targets" % len(self.data["targets"]), out)

    def test_duplicate_id_is_caught(self):
        data = copy.deepcopy(self.data)
        data["targets"][1]["id"] = data["targets"][0]["id"]
        bad = apply.problems(data)
        self.assertTrue(any("duplicate id" in p for p in bad), bad)

    def test_bad_status_is_caught(self):
        data = copy.deepcopy(self.data)
        data["targets"][0]["status"] = "maybe-someday"
        bad = apply.problems(data)
        self.assertTrue(any("status 'maybe-someday'" in p for p in bad), bad)

    def test_validate_exits_non_zero_on_a_bad_file(self):
        data = copy.deepcopy(self.data)
        data["targets"][0]["url"] = "http://insecure.example"
        apply.save(data, self.file)
        code, _ = self.run_cli(["validate"])
        self.assertEqual(1, code)


class TestStatus(Base):
    def test_status_updates_and_logs(self):
        before = apply.find(self.data, "palantir-fde")["status"]
        code, out = self.run_cli(
            ["status", "palantir-fde", "submitted", "--note", "sent 02/09"])
        self.assertEqual(0, code)
        self.assertIn("palantir-fde: %s -> submitted" % before, out)
        t = apply.find(self.reload(), "palantir-fde")
        today = date.today().isoformat()
        self.assertEqual("submitted", t["status"])
        self.assertEqual(today, t["status_date"])
        self.assertEqual({"date": today, "status": "submitted", "note": "sent 02/09"},
                         t["log"][-1])
        self.assertEqual(today, self.reload()["updated"])

    def test_unknown_status_is_a_user_error(self):
        before = apply.find(self.data, "palantir-fde")["status"]
        code, _ = self.run_cli(["status", "palantir-fde", "nearly"])
        self.assertEqual(1, code)
        self.assertEqual(before, apply.find(self.reload(), "palantir-fde")["status"])

    def test_unknown_id_is_a_user_error(self):
        code, _ = self.run_cli(["status", "not-an-employer", "submitted"])
        self.assertEqual(1, code)

    def test_key_order_survives_a_write(self):
        before = list(self.data["targets"][0])
        self.run_cli(["status", self.data["targets"][0]["id"], "verified"])
        self.assertEqual(before, list(self.reload()["targets"][0]))

    def test_file_ends_with_a_newline(self):
        self.run_cli(["status", "gchq", "verified"])
        self.assertTrue(self.file.read_text(encoding="utf-8").endswith("}\n"))


class TestDraft(Base):
    def test_draft_creates_the_folder_and_its_files(self):
        code, out = self.run_cli(["draft", "gchq"])
        self.assertEqual(0, code)
        folder = self.tmp / "drafts" / "gchq"
        self.assertTrue(folder.is_dir())
        self.assertTrue((folder / "brief.md").is_file())
        self.assertTrue((folder / "tracking.json").is_file())
        self.assertIn(str(folder), out)
        brief = (folder / "brief.md").read_text(encoding="utf-8")
        self.assertIn("Cyber Specialist Development Programme", brief)
        self.assertIn("paste or WebFetch the live JD here", brief)
        self.assertIn("## Drafting prompt", brief)
        self.assertIn("FACTS.md", brief)
        self.assertIn("cv-gchq.md", brief)
        self.assertIn("answers-gchq.md", brief)
        self.assertIn("cover-gchq.md", brief)
        tracking = json.loads((folder / "tracking.json").read_text(encoding="utf-8"))
        self.assertEqual(
            {"id": "gchq", "created": date.today().isoformat(), "files": []}, tracking)

    def test_draft_refuses_to_overwrite_without_force(self):
        self.assertEqual(0, self.run_cli(["draft", "gchq"])[0])
        marker = self.tmp / "drafts" / "gchq" / "brief.md"
        marker.write_text("hand edits", encoding="utf-8")
        self.assertEqual(1, self.run_cli(["draft", "gchq"])[0])
        self.assertEqual("hand edits", marker.read_text(encoding="utf-8"))
        self.assertEqual(0, self.run_cli(["draft", "gchq", "--force"])[0])
        self.assertIn("## Drafting prompt", marker.read_text(encoding="utf-8"))

    def test_draft_of_an_unknown_id_is_a_user_error(self):
        self.assertEqual(1, self.run_cli(["draft", "nobody"])[0])
        self.assertFalse((self.tmp / "drafts" / "nobody").exists())


class TestRender(Base):
    def test_render_writes_header_and_one_row_per_target(self):
        out_path = self.tmp / "TARGETS.md"
        code, _ = self.run_cli(["render", "--out", str(out_path)])
        self.assertEqual(0, code)
        text = out_path.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("> GENERATED by career/apply.py render on "))
        self.assertIn("- edit targets.json, not this file.", text)
        self.assertIn(date.today().strftime("%d/%m/%Y"), text.splitlines()[0])
        for limb in apply.LIMBS:
            self.assertIn(apply.LIMB_TITLE[limb], text)
        rows = [ln for ln in text.splitlines()
                if re.match(r"^\| \d+ \|", ln)]  # limb-table rows only (priority first)
        self.assertEqual(len(self.data["targets"]), len(rows))
        self.assertIn("[apply](https://jobs.lever.co/palantir", text)
        self.assertIn("## Next due", text)
        self.assertIn("## Counts", text)
        self.assertIn("total %d" % len(self.data["targets"]), text)

    def test_render_shows_dates_as_dd_mm_yyyy(self):
        data = self.reload()
        data["targets"][0]["closes"] = "2026-10-15"
        apply.save(data, self.file)
        out_path = self.tmp / "TARGETS.md"
        self.run_cli(["render", "--out", str(out_path)])
        text = out_path.read_text(encoding="utf-8")
        self.assertIn("15/10/2026", text)
        self.assertNotIn("2026-10-15", text)


class TestDue(Base):
    def _set(self, tid, **fields):
        data = self.reload()
        apply.find(data, tid).update(fields)
        apply.save(data, self.file)

    def test_due_filters_by_window_and_includes_rolling(self):
        today = date.today()
        self._set("google", closes=(today + timedelta(days=10)).isoformat())
        self._set("meta", closes=(today + timedelta(days=90)).isoformat())
        self._set("amazon-london", closes="rolling")
        code, out = self.run_cli(["due"])
        self.assertEqual(0, code)
        self.assertIn("google", out)
        self.assertNotIn("meta", out)
        self.assertIn("amazon-london", out)
        code, out = self.run_cli(["due", "--days", "120"])
        self.assertEqual(0, code)
        self.assertIn("meta", out)

    def test_due_drops_rolling_once_submitted(self):
        self._set("amazon-london", closes="rolling")
        self.assertIn("amazon-london", self.run_cli(["due"])[1])
        self.run_cli(["status", "amazon-london", "submitted"])
        self.assertNotIn("amazon-london", self.run_cli(["due"])[1])

    def test_due_ignores_a_window_that_has_already_closed(self):
        self._set("google", closes=(date.today() - timedelta(days=1)).isoformat())
        self.assertNotIn("google", self.run_cli(["due"])[1])


class TestList(Base):
    def test_list_is_sorted_by_priority_and_filters(self):
        code, out = self.run_cli(["list"])
        self.assertEqual(0, code)
        lines = out.splitlines()
        self.assertTrue(lines[0].startswith("id"))
        first = min(self.data["targets"], key=lambda t: t["priority"])["id"]
        self.assertTrue(lines[2].startswith(first))  # priority 1
        n = len(self.data["targets"])
        self.assertIn("%d of %d targets" % (n, n), out)
        code, out = self.run_cli(["list", "--limb", "clearance"])
        self.assertEqual(0, code)
        k = sum(1 for t in self.data["targets"] if t["limb"] == "clearance")
        self.assertIn("%d of %d targets" % (k, n), out)
        self.assertIn("gchq", out)
        self.assertNotIn("google", out)

    def test_list_status_filter(self):
        self.run_cli(["status", "gchq", "interview"])
        code, out = self.run_cli(["list", "--status", "interview"])
        self.assertEqual(0, code)
        self.assertIn("1 of %d targets" % len(self.data["targets"]), out)
        self.assertIn("gchq", out)


class TestErrors(Base):
    def test_missing_file_is_a_user_error_not_a_traceback(self):
        buf = io.StringIO()
        with redirect_stdout(buf), redirect_stderr(io.StringIO()):
            code = apply.main(["list", "--file", str(self.tmp / "nope.json")])
        self.assertEqual(1, code)


if __name__ == "__main__":
    unittest.main()
