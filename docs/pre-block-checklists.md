# Pre-Block Checklists


## Block 1: The AI Coding Agent Landscape

- [ ] Open the demo workspace at `blocks/01-landscape/demo/starter`.
- [ ] Confirm the `sci_units` converters file is reset to the **buggy** state and the tests are **failing** — that's the starting point the demo fixes. Verify in the terminal: `uv run pytest -v` should show red.
- [ ] Open a JupyterHub terminal in `blocks/01-landscape/demo/starter` and run `claude`. Confirm a workshop model is selected with `/model` (Claude Sonnet 4.6 / Haiku 4.5).
- [ ] Have the demo prompt copied to a scratch buffer: *"There are failing tests in this project. Investigate, fix the bug, and verify with pytest. Make the smallest possible change."*
- [ ] Have the demo notebook ready as the Part B fallback.

## Block 2: How It Actually Works (Post-Training & Tool Calling)

- [ ] Restore the code changes in Block 1's starter file (revert the fix from the Block 1 demo) so the repo is back to a clean state.

## Block 3: Agent-Driven Research Software Engineering

- [ ] Confirm the agent can see the skills: they ship in [`.github/skills/`](.github/skills/) and Claude Code loads them through `.claude/skills/`. In `claude` at the repo root, type `/` and look for `profile-dataset` and `fits-to-zarr`. If they are missing, run `/reload-skills`.
- [ ] Confirm the FITS/Zarr stack is installed: in the terminal, `python -c "import ovro_lwa_portal.fits_to_zarr_xradio, astrowidget; print('ok')"` (use `uv run python` in a uv checkout). They're declared in the root `pyproject.toml`.
- [ ] Confirm the FITS data is reachable: the notebook's **Setup** cell should print `26 FITS files in ...`. On the hub it should point into `~/s3/schmidt-observatory-system/nov26-symposium/`; if no files are found, check that the cube has been uploaded there, or set `FITS_DATA_DIR` (see `blocks/03-research-loop/demo/starter/README.md`).
- [ ] Open `blocks/03-research-loop/demo/notebook.ipynb` and check the double-horned spectrum plot appears and the astrowidget cell renders the moment-0 map on top of the DSS sky survey (it needs WebGL2 in the browser, and internet access to load the survey tiles from esm.sh and CDS).
- [ ] In the integrated terminal (at the repo root): `rm -rf blocks/03-research-loop/demo/docs/ blocks/03-research-loop/demo/output/`. We want a clean slate so artifacts appear *during* the demo. (Explicit path so you never touch the repo's top-level `docs/`.) **Don't run any skill yet** — the demo starts with you running `profile-dataset` live in front of the room (Demo 1/4).
- [ ] Have **all the prompts copied to a scratch buffer** (text file, sticky note, Slack DM to yourself, wherever you can paste fast). The exact prompts are on the demo slides in [`blocks/03-research-loop/slides.md`](../blocks/03-research-loop/slides.md).
- [ ] Open `blocks/03-research-loop/demo/expected-artifacts/` in a side tab as the **fallback** in case the live demo fails.

## Block 4: Build Your Own Skill (capstone)

- [ ] Confirm both worked-example agents are available: in `claude` at the repo root, type `@agent-` and look for `scientific-python-reviewer` and `docstring-writer`. If not, `/exit` and start `claude` again from the repo root.
