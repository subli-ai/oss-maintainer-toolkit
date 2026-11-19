# The 23-project guide — explained for humans

[← Back to OSS Maintainer Toolkit](../README.md)

![Twenty-three developer tools across four groups](assets/oss-project-map.svg)

## Start here

**This repository installs just one tool: OSS Maintainer Toolkit.** Its job is to check for eight basic repository files. The 23 names below are **other, separately packaged MVP ideas** from four source bundles—not features included in this repository.

**MVP** means a small first version. **CLI** means a tool you run in Terminal. **MCP** is a protocol that lets AI assistants connect to external tools. **Git** tracks source-code changes.

If you're new to AI coding, start with **ScopeFence, LoopBrake, APITruth, DoneProof, and MockLeak**. Each relates to something that commonly goes wrong when AI writes software.

![Five coding safety MVPs matched to real user problems](assets/agent-safety-explained.svg)

Every example below is a **scenario**, not a claim that a full live integration has been tested.

## 1. AI coding safety

For people who use coding assistants such as Claude Code, Codex or Cursor.

### ScopeFence

**When you'd want it:** You asked AI to change the login page, but it also changed payment files.

**What the current MVP does:** Checks changed Git paths against your explicit allowed/protected path lists.

**What it doesn't do yet:** It does not understand natural-language intent or stop the AI. New policy files may themselves need to be allowed or reviewed.

### LoopBrake

**When you'd want it:** An AI assistant keeps repeating the same command and error.

**What the current MVP does:** Reads event logs and flags repeated actions and errors.

**What it doesn't do yet:** It does not automatically stop the assistant or prove a loop is harmful.

### APITruth

**When you'd want it:** AI writes code using a Python function that is not installed.

**What the current MVP does:** Checks selected imports and module function references against installed Python package sources.

**What it doesn't do yet:** It skips standard-library/local cases and cannot reliably understand every dynamic API.

### DoneProof

**When you'd want it:** AI says “finished,” but you never saw a test result.

**What the current MVP does:** Runs the acceptance commands you put in a trusted JSON checklist and reports results.

**What it doesn't do yet:** It cannot invent requirements. If you point it at a folder without tests, the test command correctly fails.

### MockLeak

**When you'd want it:** Your app looks complete, but contains NotImplementedError or placeholder code.

**What the current MVP does:** Scans runtime source for likely stubs and mock imports.

**What it doesn't do yet:** Findings can be false alarms, and clean scans do not prove that all data is real.

## 2. AI infrastructure

For maintainers who build agent workflows, MCP tools, or database-backed apps.

### Agent State Receipts

**When you'd want it:** An agent forgets what was finished after its conversation gets shortened.

**What the current MVP does:** Aims to keep task-status records backed by evidence.

**What it doesn't do yet:** Not a full agent transcript recorder; production agent adapters are not established here.

### MCP Retry Lab

**When you'd want it:** A tool finished a payment-like action, but its reply was lost and the client retried it.

**What the current MVP does:** Provides fault-injection examples for repeat/duplicate side-effect behavior.

**What it doesn't do yet:** Not an MCP firewall or a universal fix for duplicate writes.

### MCP Transport Lab

**When you'd want it:** You want to review whether MCP messages and trust boundaries behaved as expected.

**What the current MVP does:** Checks captured observations of transport and request relationships.

**What it doesn't do yet:** Not an active network vulnerability scanner.

### Spec Oracle

**When you'd want it:** An AI-generated test accidentally approves the same buggy behavior as the code.

**What the current MVP does:** Maintains expected behavior examples independent of the code being tested.

**What it doesn't do yet:** You must supply trustworthy expectations; it does not discover truth on its own.

### Vibe DB Guard

**When you'd want it:** An AI-generated database migration could break a rebuild.

**What the current MVP does:** Checks selected migration hazards and local rebuild inputs.

**What it doesn't do yet:** Does not certify production data safety or replace database backup and recovery tests.

## 3. Universal developer utilities

Small tools intended to make software easier to understand, review and share.

### A11y Scout

**When you'd want it:** A website might be hard to use with a screen reader or keyboard.

**What the current MVP does:** An early tool aimed at accessibility checks.

**What it doesn't do yet:** A full browser-wide accessibility audit is not verified.

### Dependency Impact

**When you'd want it:** A package update changes more than you expected.

**What the current MVP does:** An early tool for understanding dependency changes.

**What it doesn't do yet:** No complete transitive-dependency or release-impact analysis is confirmed.

### Plain Language Check

**When you'd want it:** Visitors cannot understand your README or instructions.

**What the current MVP does:** An early checker aimed at hard-to-read language.

**What it doesn't do yet:** It cannot replace testing explanations with real people.

### Repo Story

**When you'd want it:** Someone opens a code repository and cannot tell what it does.

**What the current MVP does:** An early utility for summarizing a repository.

**What it doesn't do yet:** No guarantee of accurate explanations for arbitrary codebases.

### Traceback Guide

**When you'd want it:** A Python error message makes no sense to a beginner.

**What the current MVP does:** An early utility intended to explain traceback information.

**What it doesn't do yet:** It is not a replacement for running a debugger or reproducing the bug.

## 4. Agent operations and reliability

Eight experimental foundations from the additional eight-repository bundle.

### Billshock

**When you'd want it:** You launch an AI feature and worry a burst of requests could cost too much.

**What the current MVP does:** Estimates potential request cost from input rates and usage assumptions.

**What it doesn't do yet:** It does not probe a live endpoint, count actual model tokens or prevent billing.

### FlowWitness

**When you'd want it:** You need to check whether a UI action links to an expected backend step.

**What the current MVP does:** Validates parent/child relationships in trace data you supply.

**What it doesn't do yet:** It does not capture real browser, API or database events.

### ActionLedger

**When you'd want it:** You want a record that reveals if an agent activity log has been altered.

**What the current MVP does:** Hash-chains events supplied to it so later changes can be detected.

**What it doesn't do yet:** It does not monitor your Mac's filesystem, processes or network.

### PolicyMirror

**When you'd want it:** Conflicting permission rules make it hard to tell what action is allowed.

**What the current MVP does:** Evaluates normalized allow/ask/deny rules you supply.

**What it doesn't do yet:** It does not yet read actual Codex or Claude permissions automatically.

### MCPRealityBench

**When you'd want it:** An MCP tool says it is read-only, but you want to compare that with observed behavior.

**What the current MVP does:** Compares declared capabilities with supplied observations or fixtures.

**What it doesn't do yet:** It does not launch arbitrary MCP servers or inspect real operating-system side effects.

### HandoffVault

**When you'd want it:** One AI subtask finishes and its result must be stored for later.

**What the current MVP does:** Stores task lifecycle information and acknowledgements using local SQLite.

**What it doesn't do yet:** It has no ready-made integration with major agent frameworks.

### MergeScope

**When you'd want it:** Two AI agents edit related features and may collide.

**What the current MVP does:** Finds overlapping changes using input JSON manifests.

**What it doesn't do yet:** It does not inspect branches or understand programming-language syntax automatically.

### SkillProof

**When you'd want it:** Someone shares an AI coding skill that needs tools not installed on your machine.

**What the current MVP does:** Checks whether declared executables exist.

**What it doesn't do yet:** It does not execute entire skills in a fresh container or guarantee that they work.

## So which one should you try first?

| Your situation | Start here |
|---|---|
| You are publishing your **first** open-source project | **OSS Maintainer Toolkit** (the executable in this repository) |
| You use AI to modify existing code | **ScopeFence** — reviews paths outside approved scope |
| Your agent keeps retrying the same task | **LoopBrake** — analyzes event logs |
| The AI made up a Python API | **APITruth** — best-effort installed-package checks |
| Your AI says everything is finished | **DoneProof** — run trusted acceptance commands |
| You suspect a feature is still a mock | **MockLeak** — review likely placeholder code |

## Which parts were verified?

- The first three project bundles previously reported **65/65 passing included unit tests** (31 + 17 + 17).
- The eight-project fourth bundle passed **15/15 unit tests**, **9/9 local functional checks**, and **8/8 wheel builds** in a separate environment.
- That makes **80 passing included unit tests** across all four bundles. These figures do **not** establish reliable real-world integrations.
- The source bundles are **separate from this GitHub repository**. No download links for those source bundles are hosted here; the individual projects are not claimed to be 23 published GitHub repos.
- These are not penetration tests, code quality certifications, or verified measures of community adoption. The eight-project Mac checker has not been run on the owner's Mac in the conversation so far.

**For an actual source-code release**, each project needs a clean installation test, verified examples, documentation, security review where relevant, and an honest limitations list.

[Return to the working OSS Maintainer Toolkit →](../README.md)
