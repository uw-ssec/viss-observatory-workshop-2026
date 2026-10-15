---
type: Decision
title: "Block 3 example: agent-driven FITS to Zarr, verified, then used for moment 0"
description: "Block 3 converts a forward-modeled DSA FITS cube to Zarr with an agent and the fits-to-zarr skill, verifies it, then makes a moment-0 map and spectrum shown in astrowidget over DSS."
tags: [block-3, fits, zarr, astrowidget, curriculum]
generated: { by: "claude-code:claude-opus-5-5", at: "2026-10-15T21:00:02Z" }
status: stable
code_refs: ["blocks/03-research-loop/**"]
---

## Decision (2026-10-06/08, reaffirmed 2026-10-13/14)

- Replace the HCI text-entry example in Block 3 with an astronomy example:
  a participant uses an agent and a **fits-to-zarr skill** to convert a small
  FITS image cube into a Zarr store in their working directory.
- Center the pedagogy on FITS: everyone in the audience knows FITS; Zarr is
  "the better way" they have heard of but not learned.
- End with an **optional astrowidget visualization** projecting the Zarr image
  onto celestial coordinates, as a satisfying conclusion. A further optional
  stretch: load and display an image via natural language.
- Ship it in both **tutorial and completed forms**, and keep an
  `expected-artifacts/` fallback so people can follow along if live runs fail.
- Keep it a simple, sequential, self-contained example: the goal is
  understanding the mechanism, which participants then apply to their own data.
- Write a **new, bounded notebook in this repo**. Do not point participants
  at ovro-lwa-portal or its notebooks (in active development; too unbounded);
  `source_review.ipynb` is a reference pattern, not participant material.
- Block 4 tie-in: after the workshop a participant should be able to build a
  skill like the fits-to-zarr skill.

## Decision (2026-10-15, after Casey's review of the notebook)

- Section 4 becomes "use the cube": a **moment-0 map** (sum over frequency,
  Jy/beam km/s, radio-convention velocity from the HI rest frequency, LSRK)
  and a **whole-field spectrum** in Jy (pixel sum / beam area from the cube's
  `BEAM`), both computed lazily from the verified Zarr. The integrated map is
  the headline astrowidget view over DSS; channel maps at the two spectral
  horns follow, showing the disk's rotation. This cashes in the "lazy
  slicing" promise in the intro instead of adding a new thread.
- No continuum subtraction for the map: the line fills nearly the whole band;
  the notebook says so. The spectrum removes a continuum level from the band
  edges.
- Server-side compute stays one sentence (same code against Zarr in object
  storage), not a section; a real remote-compute demo would overrun the slot.
- Wording: the data is a **forward-modeled DSA** cube, not OVRO-LWA data.
  OVRO-LWA stays only as the converter's and astrowidget's provenance.
- Audience for the science framing: experienced astronomers, postdocs and grad
  students, so units and conventions are stated, not simplified. Stretch
  prompt: have the agent estimate the HI mass and check its constants.
- Flow is unchanged: profile, convert with the skill, verify, then use.

## Alternatives considered

- Keep the HCI example: rejected for a domain-specific audience.
- Cross-matching sources across the four Schmidt observatory telescopes with
  a spherical-geometry trap (from 2026-09-11/18 notes): not pursued; the
  verification idea carries over into the fits-to-zarr skill's WCS checks.
- Bring-your-own FITS cell: open stretch goal, needs Schmidt approval and
  image support.

## Sources

Granola meetings 2026-09-11, 2026-09-18, 2026-10-06, 2026-10-08,
2026-10-13, 2026-10-14.

# Related Concepts
- [How the workshop material evolved, and why](../facts/content-evolution.md): replaces the HCI skills loop in Block 3
- [OVRO-LWA FITS-to-Zarr and astrowidget: the backstory](../facts/ovro-lwa-origin-story.md): the real project that motivates the example
- [fits-to-zarr skill: wrap a minimal converter, then verify the output](fits-to-zarr-skill.md): the skill at the heart of the example
- [Block 3 data must be small and stay off git](../requirements/block3-data.md): data constraints for the example
