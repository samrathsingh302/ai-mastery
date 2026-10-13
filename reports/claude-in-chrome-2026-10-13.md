# Claude in Chrome — installed vs latest, what changed, what it means (13/10/2026)

> Research digest for chain `20261013-a-ai-mastery-eli5`, ticket 4. Written by a headless Opus builder seat on
> 13/10/2026 from local file reads and WebSearch/WebFetch only — no browser was opened, nothing was updated, no
> memory file was edited. Every web page was treated as data. Each claim carries its source; anything without one
> sits under Unknowns.

**Bottom line:** you are already on the latest version. Google's update server answers `noupdate` for v1.0.100,
so there is nothing to click. Claude Code on this machine (2.1.296) is the newest version in the official
changelog. The window-per-session trick from 12/10 still holds. The browser-per-plan rule needs a re-check after
the 12/10 account switch. A mismatched browser now **fails to connect** rather than quietly using the other
plan's quota.

## Installed

Read from disk on 13/10/2026:

| Browser / profile | Path (under `C:\Users\samra\AppData\Local\`) | `name` | `version` | manifest.json modified |
|---|---|---|---|---|
| Brave `Profile 2` | `BraveSoftware\Brave-Browser\User Data\Profile 2\Extensions\fcoeoabgfenejglbffodgkkbkcdhcgfn\1.0.100_0\` | `Claude` | `1.0.100` | 09/10/2026 16:20 |
| Edge `Default` | `Microsoft\Edge\User Data\Default\Extensions\fcoeoabgfenejglbffodgkkbkcdhcgfn\1.0.100_0\` | `Claude` | `1.0.100` | 12/10/2026 18:26 |

- Extension id `fcoeoabgfenejglbffodgkkbkcdhcgfn`. Each profile has exactly one version folder (`1.0.100_0`).
  Both manifests are identical in the fields read: `manifest_version` 3, `minimum_chrome_version` "116",
  `update_url` pointing at Google's update service (`clients2.google.com/service/update2/crx`).
- Permissions in both: `sidePanel`, `storage`, `activeTab`, `scripting`, `debugger`, `tabGroups`, `tabs`,
  `alarms`, `notifications`, `webNavigation`, `declarativeNetRequestWithHostAccess`, `offscreen`,
  `nativeMessaging`, `unlimitedStorage`, `downloads`, `identity`.
- Claude Code CLI on this machine: `claude --version` → `2.1.296 (Claude Code)` (13/10/2026).
- The tool names a Claude Code session on this machine saw on 13/10/2026, all under `mcp__claude-in-chrome__`,
  come from the planner seat's own tool list as written in the plan. This headless seat has no Chrome tools, so
  it could not re-list them: `browser_batch` · `computer` · `file_upload` · `find` · `form_input` ·
  `get_page_text` · `gif_creator` · `javascript_tool` · `list_connected_browsers` · `navigate` ·
  `read_console_messages` · `read_network_requests` · `read_page` · `resize_window` · `select_browser` ·
  `shortcuts_execute` · `shortcuts_list` · `switch_browser` · `tabs_close_mcp` · `tabs_context_mcp` ·
  `tabs_create_mcp` · `upload_image`.
- The `getLastFocused` code path the 12/10 window note relies on is still in the installed build. A local search
  of the Brave copy's `*.js` files finds exactly one match, in `assets\mcpPermissions-IBi8ZJfc.js`.

## Latest

- **Extension: 1.0.100 is the latest this machine is offered (13/10/2026).** I sent an update check for this id
  at v1.0.100 to Google's update service
  (https://clients2.google.com/service/update2/crx?response=updatecheck&acceptformat=crx2,crx3&prodversion=140.0&x=id%3Dfcoeoabgfenejglbffodgkkbkcdhcgfn%26v%3D1.0.100%26uc).
  It returned `<app appid="fcoeoabgfenejglbffodgkkbkcdhcgfn" … status="ok"><updatecheck … status="noupdate"/>`.
  `noupdate` means the store has nothing newer for v1.0.100. Read 13/10/2026.
- The Chrome Web Store listing (https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)
  answered with a 302 redirect to a Google consent page. Its "Version" and "Updated" fields were **not read**
  (see Unknowns). The third-party tracker https://chrome-stats.com/d/fcoeoabgfenejglbffodgkkbkcdhcgfn returned
  403. Both tried 13/10/2026.
- The official Claude Code docs set the minimum extension version at **1.0.36 or later**, so 1.0.100 is well
  above it (https://code.claude.com/docs/en/chrome, read 13/10/2026).
- **Claude Code: 2.1.296 (09/10/2026) is the newest version on the official changelog**, and it matches the
  local install (https://code.claude.com/docs/en/changelog, read 13/10/2026).
- **General availability: 26/08/2026, on every paid plan.** GA added autonomous actions: a safety classifier
  checks each action, and actions it judges safe are approved automatically. You can switch that off in the
  extension settings (https://claude.com/resources/articles/claude-in-chrome-generally-available, read
  13/10/2026; repeated by https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/, read 13/10/2026).
- The help-centre release notes (https://support.claude.com/en/articles/12138966-release-notes, read 13/10/2026)
  have no Claude in Chrome entry after 18/12/2025. The page's newest entry overall is 07/10/2026. The dedicated
  Claude in Chrome release-notes article returned 404 under both slugs tried (Sources).

## What changed

Since the four memory notes were written (03/09, 12/09, 22/09 and 12/10/2026). All entries below come from the
Claude Code changelog (https://code.claude.com/docs/en/changelog, read 13/10/2026), except where another source
is named.

- **Extension version:** no change since the 12/10 note. It was 1.0.100 then and is 1.0.100 now (manifests and
  update check above).
- **Tools:** no source names an added or removed `mcp__claude-in-chrome__*` tool. Behaviour changes:
  `browser_batch` now gets 90 s before it times out, up from 60 s (2.1.290). "Fewer page actions are refused
  when the browser is slow to report its tabs" (2.1.293). Long page reads stay inline instead of going to a file
  (2.1.268). `file_upload` now refuses credential-named files such as `.env`, `.pem`, `.key` and anything under
  `.ssh` (2.1.293+, https://code.claude.com/docs/en/chrome).
- **Flags and switch-on rules:**
  - A project's settings files can no longer turn Chrome on. `CLAUDE_CODE_ENABLE_CFC` in a project's
    `.claude/settings*.json` is ignored with a warning. Only `--chrome`, `/chrome` or user settings work (2.1.290;
    docs page).
  - Sessions spawned by `claude remote-control` keep Chrome off unless `--chrome` is passed (2.1.285).
  - `/config chrome=true` now sends you to the `/config` panel instead of enabling Chrome (2.1.285).
  - `/tui` no longer disconnects Chrome in a `--chrome` session, and now respects `--no-chrome` (2.1.293).
- **Account, plan and organisation rules:**
  - Chrome follows the organisation's admin setting (2.1.260, 03/09/2026).
  - The extension must be signed in to the **same claude.ai account and organisation** as Claude Code. If it
    is not, the browser tools return "Browser extension is not connected" (docs page; 2.1.293 improved the
    message).
  - A session signed in with an API key or a `claude setup-token` long-lived token has Chrome kept off, even with
    `--chrome` (from v2.1.216, docs page).
  - Logging out of the extension **loses its saved shortcuts and scheduled tasks** (docs page warning).
- **Multi-browser behaviour:**
  - With more than one browser connected, Claude asks which one to use. You can change it later with `/chrome` →
    **Select browser…**, and Claude keeps that choice even when another browser connects (docs page).
  - Connected browsers are now labelled by computer name instead of "Browser 1" / "Browser 2" (2.1.285).
  - The browser picker no longer shows a JSON parse error when Chrome can't be reached (2.1.287), or a message
    meant for Claude when the chosen browser has disconnected (2.1.290).
- **Tab groups and windows:**
  - Each session's tabs go into a tab group tied to that session. `/clear` closes the group. `/resume` or exit
    closes it only if it holds nothing but empty new tabs (docs page).
  - No official source mentions which **window** a new group is created in. Nothing published changes the
    `getLastFocused` behaviour the 12/10 note relies on, and the installed code still calls it (Installed).
  - An open user report, #90001 (27/08/2026, no maintainer reply), says the `tabGroupId` can change between
    consecutive `tabs_context_mcp` calls
    (https://claudeissues.com/issue/90001-bug-claude-in-chrome-tabgroupid-flaps-between-tabs-context-mcp-calls-actions-on,
    read 13/10/2026).
- **Permissions:**
  - In auto mode, calls the classifier approves skip the extension's own per-site check (2.1.275).
  - Screenshots and page reads on an allowed site no longer ask every time when auto mode is unavailable
    (2.1.288).
  - In plan mode, `tabs_context_mcp` with `createIfEmpty` asks first (docs page).
  - VS Code now asks before browser actions in every session (2.1.296).
- **Supported browsers — the sources disagree:**
  - The Claude Code docs say Chrome and Edge work, and that Claude Code "detects the extension and sets up the
    connection" in Brave, Arc, Vivaldi and Opera (https://code.claude.com/docs/en/chrome).
  - The GA article says "Claude in Chrome doesn't run on other Chromium browsers or on mobile yet".
  - The help article says it "is not supported on other Chromium-based web browsers"
    (https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome, read 13/10/2026).
  - In practice Brave works with Claude Code, but the standalone side-panel product is officially Chrome-only.

## What it means for Samrath

Context comes from the 13/10 spawner handoff (`C:\Users\samra\.claude\state\briefs\2026-10-13-spawner-handoff.md`)
and the four memories under `C:\Users\samra\.claude\projects\C--Users-samra\memory\`, all read only.

- **`claude-in-chrome-window-per-session.md` (12/10) — HOLDS.** Same extension version, and `getLastFocused` is
  still in the installed code. The new-Brave-window-before-the-first-group step stays valid. Its caveat (4) was
  "re-check if the extension updates". It has not updated, so nothing to re-check yet. Issue #90001 adds a risk:
  a session that re-reads `tabs_context_mcp` mid-task can see a different group id.
- **`claude-in-chrome-browser-per-plan.md` (12/09) — PARTLY STALE.**
  - The handoff says the account was switched on 12/10 to the gmail account, for both Claude and Claude in
    Chrome. Whether Edge still carries the 5x account and Brave the 20x was not re-established after that switch.
  - The stated *reason* is also out of date. The docs now say a browser signed in to a different account or
    organisation gives "Browser extension is not connected". So the wrong browser fails; it does not quietly
    spend the other plan's quota.
  - The rule to pick the matching browser still stands, but the step is now `/chrome` → **Select browser…**
    (or `select_browser`), and that choice sticks.
- **`two-max-accounts.md` (22/09) — HOLDS**, with one addition: an account switch has to happen in the extension
  too (log out, then log in to the matching account and organisation). Logging out wipes the extension's
  shortcuts and scheduled tasks.
- **`research-tooling-traps.md` (03/09) — HOLDS, wording stale.** Reddit still needs the extension. "Re-enabled
  for the new account" is now precisely "logged in to the same account and organisation as the CLI"
  (docs page).
- **What a research seat should do differently:**
  1. A headless seat still has no Chrome tools. This seat had none on 13/10, the same as on 16/09 and 26/09, so
     web research stays WebSearch/WebFetch unless the seat is launched with `--chrome` explicitly. Project
     settings can no longer switch it on (2.1.290), and `remote-control`-spawned sessions keep it off (2.1.285).
  2. Before the first page read, call `list_connected_browsers` and pick the browser by name. With both browsers
     on one computer, the new computer-name label (2.1.285) may not tell Brave from Edge (Unknowns).
  3. Expect fewer permission prompts in auto or bypass mode (2.1.275, 2.1.288), and a 90 s ceiling per
    `browser_batch`.
  4. If the launcher authenticates seats with a `claude setup-token` token, Chrome is off for those seats
     whatever the flag says (docs page). Whether it does is not established here (Unknowns).
- **Proposed one-line memory edits. NOT applied here; a home-project seat applies them:**
  - `claude-in-chrome-window-per-session.md`, under Caveats: add "13/10/2026: still v1.0.100 (Google update
    check `noupdate`); `getLastFocused` still present in `assets\mcpPermissions-*.js` — trick still valid; watch
    open issue #90001 (`tabGroupId` can change between `tabs_context_mcp` calls)."
  - `claude-in-chrome-browser-per-plan.md`, under Why: replace the quota sentence with "a browser signed in to a
    different account/organisation than the CLI is refused ('Browser extension is not connected'); re-check
    which browser holds which account after the 12/10 switch; pick with `/chrome` → Select browser… (the choice
    persists)."
  - `two-max-accounts.md`, under How to apply: add "an account switch must be mirrored in the extension (log out
    and in, matching org per `/status`); logging out of the extension deletes its shortcuts and scheduled tasks."
  - `research-tooling-traps.md`, Reddit bullet: replace "re-enabled for the new account" with "logged in to the
    same account and organisation as the CLI (`/status` → Organization)."

## Update action

**Nothing to update.** The latest version offered is 1.0.100, which is what both browsers already have (update
check, 13/10/2026). Nothing in the estate needs to change first.

If a newer version appears later:

- **To pull it immediately:** open `brave://extensions` (and `edge://extensions` in Edge) → turn on
  **Developer mode** (top right) → **Update**. Otherwise let auto-update land within a few hours. Do this once
  per browser.
- **Afterwards:** in a live session, run `/chrome` → **Reconnect extension** if the tools drop.
- **Then:** re-run the `getLastFocused` check behind the 12/10 window note. Search the new version folder's
  `assets\*.js` for `getLastFocused`.

Claude Code itself is already at 2.1.296, the newest version on the changelog. The builder updated nothing and
opened no browser.

## Sources

All read on 13/10/2026 through WebSearch/WebFetch from this headless seat.

1. https://code.claude.com/docs/en/chrome — 200; prerequisites (extension ≥ 1.0.36), browsers, tab groups,
   multi-browser picker, organisation rule, setup-token rule, troubleshooting.
2. https://code.claude.com/docs/en/changelog — 200; read in four chunks (characters 0–400 000). Covers 2.1.296
   (09/10/2026) back to 2.1.257 (01/09/2026).
3. https://clients2.google.com/service/update2/crx?response=updatecheck&acceptformat=crx2,crx3&prodversion=140.0&x=id%3Dfcoeoabgfenejglbffodgkkbkcdhcgfn%26v%3D1.0.100%26uc
   — 200; `status="noupdate"`.
4. https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn — 302 to a Google consent
   page; not read.
5. https://chrome-stats.com/d/fcoeoabgfenejglbffodgkkbkcdhcgfn — 403.
6. https://claude.com/resources/articles/claude-in-chrome-generally-available — 200; GA 26/08/2026, autonomous
   actions, Chrome-only.
7. https://support.claude.com/en/articles/12012173-getting-started-with-claude-in-chrome — 200; paid plans,
   "not supported on other Chromium-based web browsers", tab group.
8. https://support.claude.com/en/articles/12138966-release-notes — 200; last Claude in Chrome entry 18/12/2025.
9. https://support.claude.com/en/articles/12306336-claude-in-chrome-release-notes — 404.
10. https://support.claude.com/en/articles/12306336-claude-for-chrome-release-notes — 404.
11. https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/ — 200; secondary report of GA on
    26/08/2026.
12. https://claudeissues.com/issue/90001-bug-claude-in-chrome-tabgroupid-flaps-between-tabs-context-mcp-calls-actions-on
    — 200; user report, open.

Local (no URL): the two `manifest.json` files above; `claude --version`; a search for `getLastFocused` in the
installed Brave build.

## Unknowns

- **The Web Store's own "Version" and "Updated" fields.** The listing redirects to a consent page this seat
  cannot pass, and chrome-stats returned 403. "Latest = 1.0.100" rests on the update server's `noupdate`. A
  staged rollout to other cohorts could hold a newer build this client is not yet offered. The release date of
  1.0.100 is also unknown; the manifests' file times (09/10 and 12/10) are only when this machine received it.
- **No official extension changelog with version numbers was found.** The dedicated release-notes article
  404s, and the general release notes stop mentioning Claude in Chrome after 18/12/2025. "No tools added or
  removed" therefore means no source names one; it was not checked against a live tool list.
- **The live tool list on 13/10.** It comes from the planner's tool list. This headless seat has no
  `mcp__claude-in-chrome__*` tools to compare against.
- **Which account each browser is signed into after the 12/10 switch** to the gmail account. Only Samrath, or
  a seat with Chrome tools calling `list_connected_browsers`, can establish it.
- **Whether the computer-name label from 2.1.285 tells Brave and Edge apart** on one machine. The changelog
  says browsers are labelled "by computer", which suggests two browsers on one computer may share a label.
- **Whether the estate's launcher signs seats in with a `claude setup-token` token,** which would keep Chrome
  off regardless of `--chrome`. Not checked: this ticket reads no launcher code.
- **The changelog beyond the first 400 000 characters** (before 2.1.257, 01/09/2026) was not read. It predates
  every memory note except `research-tooling-traps.md` (03/09).
- **The help-centre and GA pages contradict the Claude Code docs on Chromium support.** No source settles
  whether Brave is officially supported for Claude Code use, beyond the docs' "detects … and sets up the
  connection".
