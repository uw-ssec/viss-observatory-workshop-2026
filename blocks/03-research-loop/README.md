# Block 3: Agent-Driven Research Software Engineering

**Duration:** ~30 minutes
**Tool focus:** a coding agent (**Claude Code** in a JupyterHub terminal, or **GitHub Copilot Chat** in agent mode) driven by workshop **skills** that live in [`.github/skills/`](../../.github/skills/). This block's demo uses `profile-dataset` and the new `fits-to-zarr` skill, and ends in [astrowidget](https://github.com/ovro-lwa/astrowidget).

## Learning goals

By the end of this block, an attendee can:

1. Recognize a **skill-driven workflow**, see that each phase is just a `.github/skills/<name>/SKILL.md` file (sometimes with scripts), and pick the right subset for a given task.
2. Name the common **agent failure modes** (context exhaustion, looping, niche-library hallucination, confidently wrong answers, tool misuse, and scope creep).
3. Apply the corresponding **mitigations** (tighter scope per turn, auditable artifacts, deterministic steps in scripts, verification as a quality gate, AGENTS.md as durable project memory, manual intervention).
4. Stay in control of an agent that edits files: **review the diff (not the chat), commit per phase, and roll back cleanly with git**, and recognize **prompt injection** (the agent acting on instructions hidden in untrusted code/data/web) and the tool-scoping that mitigates it.
5. **Verify, don't trust:** check an agent's data conversion against the original data, and spot-check it independently.

## What's in this folder

```
03-research-loop/
  README.md            # this file
  slides.md            # Marp slides (includes demo prompts)
  resources.md         # the skills, FITS/Zarr references, failure-mode reading
  demo/                # FITS -> Zarr -> astrowidget (the live demo)
    AGENTS.md          # project memory: what the FITS cube is + conversion conventions
    notebook.ipynb     # the guided walkthrough: prompts, checks, moment 0, sky view
    starter/README.md  # where the FITS data lives (it is not in git)
    expected-artifacts/  # pre-generated docs/ outputs + figures, as fallback
  demo-hci/            # the previous statistical-analysis demo (text-entry study),
                       # kept as a Block 4 target and for the stats skills
```

The FITS data (26 files, ~100 MB) is **not in git**. On the JupyterHub it is
read in place from the shared S3 mount (`~/s3/schmidt-observatory-system/nov26-symposium/`)
or from `FITS_DATA_DIR`; elsewhere put it in `.data/TSOS_Science_Symposium/`
at the repo root. See [`demo/starter/README.md`](demo/starter/README.md).

## How to run the material

### Run the demo

This is a **live, instructor-led demo**, followed along in
[`demo/notebook.ipynb`](demo/notebook.ipynb).

1. Open the notebook and run **Setup** (section 0).
2. Open the agent: in a JupyterHub terminal run `claude` from the repo root; in a
   Codespace open **Copilot Chat** in **Agent** mode.
3. Wipe any leftover artifacts from prior runs (from the repo root):
   `rm -rf blocks/03-research-loop/demo/docs/ blocks/03-research-loop/demo/output/`.
4. Walk the four demos from [`slides.md`](slides.md) (Demo 1/4 through 4/4), one
   at a time, pasting each prompt into the agent. The notebook mirrors them and
   has a "run it yourself" fallback cell for the conversion. The **first** prompt
   tells the agent to read `blocks/03-research-loop/demo/AGENTS.md` first.
5. When you're done, **commit the trail**:
   `git add blocks/03-research-loop/demo/docs/ && git commit`. That's the
   auditability lesson. The Zarr itself stays out of git; the record of what was
   converted and how it was checked goes in.

If anything goes wrong on the day, the [`expected-artifacts/`](demo/expected-artifacts/)
folder ships pre-generated outputs (profile, conversion record, verification
report, and a channel image) to walk through instead.

## Bridge to Block 4

Block 4 is the capstone where attendees write their first custom agent / skill
(like `fits-to-zarr`) and run it against their own data or code.
