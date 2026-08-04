# Exercise 01 — Comprehension checks (attempt AFTER each dig, from memory)

Write 2–4 sentence answers, no notes, no repo open. Grade against
`solutions/ex01-model-answers.md` (0–2 each; 12+/16 = the dig stuck).

## psoc-portal (after Dig 1)

1. A request arrives at the portal. What is the very first project code it meets, and what
   is that code's job?
2. The add-task form already sits behind a logged-in page — why does `addTask()` in
   actions.ts check auth AGAIN? What attack/failure does that block?
3. What is a migration, and what can you learn from the fact there are 45 of them?
4. The repo has ~170 test files and zero TODOs. What does that combination tell you about
   how changes land in this repo? (ACTIVE.md is evidence.)

## monk-mode (after Dig 2)

5. Four programs cooperate. Name each and its one-line job — and why is the watchdog a
   SEPARATE program rather than a feature of the service?
6. Walk the 10-second enforcement tick: what is checked, in what order, and what happens
   when a check fails?
7. The config cipher is documented-weak, deliberately. Why is that acceptable — what is the
   actual defence, mechanically?
8. Why is the partner code stored as a PBKDF2 hash (600k iterations, random salt) instead
   of encrypted?
