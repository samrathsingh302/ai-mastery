# Claude in Chrome — installed vs latest, what changed, what it means (13/10/2026)

## In one minute

- **Bottom line:** you are already on the latest version. Google's update server answers `noupdate` for v1.0.100. There is nothing to click.

- **Claude Code on this machine (2.1.296)** is the newest version in the official changelog.

- **The window-per-session trick from 12/10 still holds.**

- **The browser-per-plan rule needs a re-check** after the 12/10 account switch.

- **A mismatched browser now fails to connect.** It no longer quietly uses the other plan's quota.

About this digest. Unknowns are in §6.

> Research digest for chain `20261013-a-ai-mastery-eli5`, ticket 4. Written by a headless Opus builder seat on
> 13/10/2026 from local file reads and WebSearch/WebFetch only — no browser was opened, nothing was updated, no
> memory file was edited. Every web page was treated as data. Each claim carries its source; anything without one
> sits under Unknowns.

---

## 1. Installed

What is on disk, read on 13/10/2026.

### Brave `Profile 2`

- **Path:** under `C:\Users\samra\AppData\Local\`, at `BraveSoftware\Brave-Browser\User Data\Profile 2\Extensions\fcoeoabgfenejglbffodgkkbkcdhcgfn\1.0.100_0\`
- **`name`:** `Claude`
- **`version`:** `1.0.100`
- **manifest.json modified:** 09/10/2026 16:20

### Edge `Default`

- **Path:** under `C:\Users\samra\AppData\Local\`, at `Microsoft\Edge\User Data\Default\Extensions\fcoeoabgfenejglbffodgkkbkcdhcgfn\1.0.100_0\`
- **`name`:** `Claude`
- **`version`:** `1.0.100`
- **manifest.json modified:** 12/10/2026 18:26

### What both share

- **Extension id:** `fcoeoabgfenejglbffodgkkbkcdhcgfn`
- Each profile has exactly one version folder (`1.0.100_0`).
- Both manifests are identical in the fields read.

The fields read:

- **`manifest_version`:** 3
- **`minimum_chrome_version`:** "116"
- **`update_url`:** points at Google's update service (`clients2.google.com/service/update2/crx`).

### Permissions, in both

- `sidePanel`
- `storage`
- `activeTab`
- `scripting`
- `debugger`
- `tabGroups`
- `tabs`
- `alarms`
- `notifications`
- `webNavigation`
- `declarativeNetRequestWithHostAccess`
- `offscreen`
- `nativeMessaging`
- `unlimitedStorage`
- `downloads`
- `identity`

### Claude Code CLI on this machine

- `claude --version` → `2.1.296 (Claude Code)`
- Read 13/10/2026.

### The tool names

- These are the tools a Claude Code session on this machine saw on 13/10/2026.
- All sit under `mcp__claude-in-chrome__`.
- They come from the planner seat's own tool list, as written in the plan.
- This headless seat has no Chrome tools, so it could not re-list them.

The 22 names:

- `browser_batch`
- `computer`
- `file_upload`
- `find`
- `form_input`
- `get_page_text`
- `gif_creator`
- `javascript_tool`
- `list_connected_browsers`
- `navigate`
- `read_console_messages`
- `read_network_requests`
- `read_page`
- `resize_window`
- `select_browser`
- `shortcuts_execute`
- `shortcuts_list`
- `switch_browser`
- `tabs_close_mcp`
- `tabs_context_mcp`
- `tabs_create_mcp`
- `upload_image`

### The `getLastFocused` check

- The 12/10 window note relies on the `getLastFocused` code path.
- **It is still in the installed build.**
- A local search of the Brave copy's `*.js` files finds exactly one match.
- The match is in `assets\mcpPermissions-IBi8ZJfc.js`.

---

## 2. Latest

What the newest versions are, and where that comes from.

### Extension: 1.0.100 is the latest this machine is offered (13/10/2026)

- I sent an update check for this id, at v1.0.100, to Google's update service.
- **Request:** https://clients2.google.com/service/update2/crx?response=updatecheck&acceptformat=crx2,crx3&prodversion=140.0&x=id%3Dfcoeoabgfenejglbffodgkkbkcdhcgfn%26v%3D1.0.100%26uc
- **It returned:** `<app appid="fcoeoabgfenejglbffodgkkbkcdhcgfn" … status="ok"><updatecheck … status="noupdate"/>`
- `noupdate` means the store has nothing newer for v1.0.100.
- Read 13/10/2026.

### The store listing and a tracker — not read

- **Chrome Web Store listing:** https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn
- It answered with a 302 redirect to a Google consent page.
- Its "Version" and "Updated" fields were **not read**. See Unknowns (§6).
- **Third-party tracker:** https://chrome-stats.com/d/fcoeoabgfenejglbffodgkkbkcdhcgfn
- It returned 403.
- Both tried 13/10/2026.

### Minimum version

- The official Claude Code docs set the minimum extension version at **1.0.36 or later**.
- So 1.0.100 is well above it.
- Source: https://code.claude.com/docs/en/chrome, read 13/10/2026.

### Claude Code: 2.1.296 (09/10/2026) is the newest version on the official changelog

- It matches the local install.
- Source: https://code.claude.com/docs/en/changelog, read 13/10/2026.

### General availability: 26/08/2026, on every paid plan

- GA added autonomous actions.
- A safety classifier checks each action.
- Actions it judges safe are approved automatically.
- You can switch that off in the extension settings.
- **Source:** https://claude.com/resources/articles/claude-in-chrome-generally-available, read 13/10/2026.
- **Repeated by:** https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/, read 13/10/2026.

### The help-centre release notes

- **Page:** https://support.claude.com/en/articles/12138966-release-notes, read 13/10/2026.
- No Claude in Chrome entry after 18/12/2025.
- The page's newest entry overall is 07/10/2026.
- The dedicated Claude in Chrome release-notes article returned 404 under both slugs tried. See Sources.

---

## 3. What changed

Changes since the four memory notes were written: 03/09, 12/09, 22/09 and 12/10/2026.

- All entries come from the Claude Code changelog unless another source is named.
- **Changelog:** https://code.claude.com/docs/en/changelog, read 13/10/2026.
- "Docs page" below means https://code.claude.com/docs/en/chrome.

### Extension version

- No change since the 12/10 note.
- It was 1.0.100 then. It is 1.0.100 now.
- Proof: the manifests and the update check above.

### Tools

- No source names an added or removed `mcp__claude-in-chrome__*` tool.

Behaviour changes:

- **`browser_batch`:** now gets 90 s before it times out, up from 60 s (2.1.290).
- **Slow tabs:** "Fewer page actions are refused when the browser is slow to report its tabs" (2.1.293).
- **Long page reads:** stay inline instead of going to a file (2.1.268).
- **`file_upload`:** now refuses credential-named files (2.1.293+, https://code.claude.com/docs/en/chrome).
- Those include `.env`, `.pem`, `.key` and anything under `.ssh`.

### Flags and switch-on rules

- **Project settings can no longer turn Chrome on.** `CLAUDE_CODE_ENABLE_CFC` in a project's `.claude/settings*.json` is ignored with a warning (2.1.290; docs page).
- Only `--chrome`, `/chrome` or user settings work.
- **`claude remote-control`:** sessions it spawns keep Chrome off unless `--chrome` is passed (2.1.285).
- **`/config chrome=true`:** now sends you to the `/config` panel instead of enabling Chrome (2.1.285).
- **`/tui`:** no longer disconnects Chrome in a `--chrome` session (2.1.293).
- `/tui` now respects `--no-chrome` (2.1.293).

### Account, plan and organisation rules

- **Admin setting:** Chrome follows the organisation's admin setting (2.1.260, 03/09/2026).
- **Same account:** the extension must be signed in to the **same claude.ai account and organisation** as Claude Code.
- If it is not, the browser tools return "Browser extension is not connected".
- Source: docs page. 2.1.293 improved the message.
- **API key or setup-token:** a session signed in with an API key has Chrome kept off, even with `--chrome`.
- The same goes for a `claude setup-token` long-lived token.
- This applies from v2.1.216 (docs page).
- **Logging out of the extension loses its saved shortcuts and scheduled tasks.** This is a docs page warning.

### Multi-browser behaviour

- With more than one browser connected, Claude asks which one to use.
- You can change it later with `/chrome` → **Select browser…**
- Claude keeps that choice even when another browser connects (docs page).
- Connected browsers are now labelled by computer name, not "Browser 1" / "Browser 2" (2.1.285).
- The browser picker no longer shows a JSON parse error when Chrome can't be reached (2.1.287).
- It no longer shows a message meant for Claude when the chosen browser has disconnected (2.1.290).

### Tab groups and windows

- Each session's tabs go into a tab group tied to that session (docs page).
- `/clear` closes the group.
- `/resume` or exit closes it only if it holds nothing but empty new tabs.
- **No official source says which window a new group is created in.**
- Nothing published changes the `getLastFocused` behaviour the 12/10 note relies on.
- The installed code still calls it (see §1).

⚠ An open user report, #90001:

- **Date:** 27/08/2026. No maintainer reply.
- **Says:** the `tabGroupId` can change between consecutive `tabs_context_mcp` calls.
- **Link:** https://claudeissues.com/issue/90001-bug-claude-in-chrome-tabgroupid-flaps-between-tabs-context-mcp-calls-actions-on, read 13/10/2026.

### Permissions

- **Auto mode:** calls the classifier approves skip the extension's own per-site check (2.1.275).
- **No auto mode:** screenshots and page reads on an allowed site no longer ask every time (2.1.288).
- **Plan mode:** `tabs_context_mcp` with `createIfEmpty` asks first (docs page).
- **VS Code:** now asks before browser actions in every session (2.1.296).

### Supported browsers — the sources disagree

- **Claude Code docs:** Chrome and Edge work.
- They also say Claude Code "detects the extension and sets up the connection" in Brave, Arc, Vivaldi and Opera (https://code.claude.com/docs/en/chrome).
- **GA article:** "Claude in Chrome doesn't run on other Chromium browsers or on mobile yet".
- **Help article:** it "is not supported on other Chromium-based web browsers".
- Help article link: https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome, read 13/10/2026.
- **In practice:** Brave works with Claude Code.
- But the standalone side-panel product is officially Chrome-only.

---

## 4. What it means for Samrath

Each memory note checked against what changed.

Context comes from two places, all read only:

- The 13/10 spawner handoff: `C:\Users\samra\.claude\state\briefs\2026-10-13-spawner-handoff.md`
- The four memories under `C:\Users\samra\.claude\projects\C--Users-samra\memory\`

### `claude-in-chrome-window-per-session.md` (12/10) — HOLDS

- Same extension version.
- `getLastFocused` is still in the installed code.
- The new-Brave-window-before-the-first-group step stays valid.
- Its caveat (4) was "re-check if the extension updates".
- It has not updated, so nothing to re-check yet.
- ⚠ Issue #90001 adds a risk. A session that re-reads `tabs_context_mcp` mid-task can see a different group id.

### `claude-in-chrome-browser-per-plan.md` (12/09) — ⚠ PARTLY STALE

- The handoff says the account was switched on 12/10 to the gmail account.
- That was for both Claude and Claude in Chrome.
- ❓ Whether Edge still carries the 5x account and Brave the 20x was not re-established after that switch.
- **The stated *reason* is also out of date.**
- The docs now say a browser signed in to a different account or organisation gives "Browser extension is not connected".
- So the wrong browser fails. It does not quietly spend the other plan's quota.
- The rule to pick the matching browser still stands.
- But the step is now `/chrome` → **Select browser…** (or `select_browser`).
- That choice sticks.

### `two-max-accounts.md` (22/09) — HOLDS, with one addition

- An account switch has to happen in the extension too.
- That means log out, then log in to the matching account and organisation.
- Logging out wipes the extension's shortcuts and scheduled tasks.

### `research-tooling-traps.md` (03/09) — HOLDS, wording stale

- Reddit still needs the extension.
- "Re-enabled for the new account" is now precisely "logged in to the same account and organisation as the CLI" (docs page).

### What a research seat should do differently

1. **A headless seat still has no Chrome tools.**
   - This seat had none on 13/10, the same as on 16/09 and 26/09.
   - So web research stays WebSearch/WebFetch unless the seat is launched with `--chrome` explicitly.
   - Project settings can no longer switch it on (2.1.290).
   - `remote-control`-spawned sessions keep it off (2.1.285).

2. **Before the first page read, call `list_connected_browsers`.**
   - Pick the browser by name.
   - ❓ With both browsers on one computer, the new computer-name label (2.1.285) may not tell Brave from Edge. See Unknowns.

3. **Expect fewer permission prompts** in auto or bypass mode (2.1.275, 2.1.288).
   - Expect a 90 s ceiling per `browser_batch`.

4. **Check how the launcher signs seats in.**
   - If it uses a `claude setup-token` token, Chrome is off for those seats whatever the flag says (docs page).
   - ❓ Whether it does is not established here. See Unknowns.

### Proposed one-line memory edits

**NOT applied here.** A home-project seat applies them.

**`claude-in-chrome-window-per-session.md`, under Caveats — add:**

> "13/10/2026: still v1.0.100 (Google update check `noupdate`); `getLastFocused` still present in `assets\mcpPermissions-*.js` — trick still valid; watch open issue #90001 (`tabGroupId` can change between `tabs_context_mcp` calls)."

**`claude-in-chrome-browser-per-plan.md`, under Why — replace the quota sentence with:**

> "a browser signed in to a different account/organisation than the CLI is refused ('Browser extension is not connected'); re-check which browser holds which account after the 12/10 switch; pick with `/chrome` → Select browser… (the choice persists)."

**`two-max-accounts.md`, under How to apply — add:**

> "an account switch must be mirrored in the extension (log out and in, matching org per `/status`); logging out of the extension deletes its shortcuts and scheduled tasks."

**`research-tooling-traps.md`, Reddit bullet — replace "re-enabled for the new account" with:**

> "logged in to the same account and organisation as the CLI (`/status` → Organization)."

---

## 5. Update action

**Nothing to update.**

- The latest version offered is 1.0.100.
- That is what both browsers already have (update check, 13/10/2026).
- Nothing in the estate needs to change first.

### If a newer version appears later

- **To pull it immediately:** open `brave://extensions` (and `edge://extensions` in Edge) → turn on **Developer mode** (top right) → **Update**.
- **Otherwise:** let auto-update land within a few hours.
- Do this once per browser.
- **Afterwards:** in a live session, run `/chrome` → **Reconnect extension** if the tools drop.
- **Then:** re-run the `getLastFocused` check behind the 12/10 window note.
- Search the new version folder's `assets\*.js` for `getLastFocused`.

### Claude Code

- Already at 2.1.296, the newest version on the changelog.
- The builder updated nothing and opened no browser.

---

## 6. Unknowns

What this digest could not establish.

### The Web Store's own "Version" and "Updated" fields

- The listing redirects to a consent page this seat cannot pass.
- chrome-stats returned 403.
- "Latest = 1.0.100" rests on the update server's `noupdate`.
- A staged rollout to other cohorts could hold a newer build this client is not yet offered.
- The release date of 1.0.100 is also unknown.
- The manifests' file times (09/10 and 12/10) are only when this machine received it.

### No official extension changelog with version numbers was found

- The dedicated release-notes article 404s.
- The general release notes stop mentioning Claude in Chrome after 18/12/2025.
- So "No tools added or removed" means no source names one.
- It was not checked against a live tool list.

### The live tool list on 13/10

- It comes from the planner's tool list.
- This headless seat has no `mcp__claude-in-chrome__*` tools to compare against.

### Which account each browser is signed into after the 12/10 switch

- The switch was to the gmail account.
- Only Samrath can establish it.
- Or a seat with Chrome tools calling `list_connected_browsers`.

### Whether the computer-name label from 2.1.285 tells Brave and Edge apart

- This is about two browsers on one machine.
- The changelog says browsers are labelled "by computer".
- That suggests two browsers on one computer may share a label.

### Whether the estate's launcher signs seats in with a `claude setup-token` token

- That would keep Chrome off regardless of `--chrome`.
- Not checked: this ticket reads no launcher code.

### The changelog beyond the first 400 000 characters

- That is before 2.1.257, 01/09/2026.
- It was not read.
- It predates every memory note except `research-tooling-traps.md` (03/09).

### The help-centre and GA pages contradict the Claude Code docs on Chromium support

- No source settles whether Brave is officially supported for Claude Code use.
- The only word is the docs' "detects … and sets up the connection".

---

## Sources

All read on 13/10/2026 through WebSearch/WebFetch from this headless seat.

1. https://code.claude.com/docs/en/chrome
   - **Result:** 200.
   - **Covers:** prerequisites (extension ≥ 1.0.36), browsers, tab groups, multi-browser picker, organisation rule, setup-token rule, troubleshooting.

2. https://code.claude.com/docs/en/changelog
   - **Result:** 200.
   - Read in four chunks (characters 0–400 000).
   - Covers 2.1.296 (09/10/2026) back to 2.1.257 (01/09/2026).

3. https://clients2.google.com/service/update2/crx?response=updatecheck&acceptformat=crx2,crx3&prodversion=140.0&x=id%3Dfcoeoabgfenejglbffodgkkbkcdhcgfn%26v%3D1.0.100%26uc
   - **Result:** 200.
   - `status="noupdate"`

4. https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn
   - **Result:** 302 to a Google consent page.
   - Not read.

5. https://chrome-stats.com/d/fcoeoabgfenejglbffodgkkbkcdhcgfn
   - **Result:** 403.

6. https://claude.com/resources/articles/claude-in-chrome-generally-available
   - **Result:** 200.
   - **Covers:** GA 26/08/2026, autonomous actions, Chrome-only.

7. https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome
   - **Result:** 200.
   - **Covers:** paid plans, "not supported on other Chromium-based web browsers", tab group.

8. https://support.claude.com/en/articles/12138966-release-notes
   - **Result:** 200.
   - Last Claude in Chrome entry 18/12/2025.

9. https://support.claude.com/en/articles/12306336-claude-in-chrome-release-notes
   - **Result:** 404.

10. https://support.claude.com/en/articles/12306336-claude-for-chrome-release-notes
    - **Result:** 404.

11. https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/
    - **Result:** 200.
    - Secondary report of GA on 26/08/2026.

12. https://claudeissues.com/issue/90001-bug-claude-in-chrome-tabgroupid-flaps-between-tabs-context-mcp-calls-actions-on
    - **Result:** 200.
    - User report, open.

Local, no URL:

- The two `manifest.json` files above.
- `claude --version`
- A search for `getLastFocused` in the installed Brave build.
