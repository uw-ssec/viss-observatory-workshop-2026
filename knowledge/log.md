## 2026-10-15
* **Update**: Updated concept `requirements/block3-data.md`.
* **Update**: Updated concept `decisions/block3-fits-to-zarr-example.md`.
* **Update**: Updated concept `facts/astrowidget-usage.md`.
* **Update**: Linked `requirements/block3-data.md` to `bugs/converter-equinox-and-wcs.md` (the DSA data's ICRS frame triggers the EQUINOX bug).
* **Update**: Linked `bugs/astrowidget-update-slice-resets-scale.md` to `facts/astrowidget-usage.md` (quirk of the astrowidget API).
* **Update**: Linked `bugs/converter-equinox-and-wcs.md` to `decisions/fits-to-zarr-skill.md` (workarounds live in the skill's convert.py).
* **Creation**: Documented concept `bugs/astrowidget-update-slice-resets-scale.md` (astrowidget: update_slice resets the colour scale).
* **Creation**: Documented concept `bugs/converter-equinox-and-wcs.md` (fits_to_zarr_xradio: EQUINOX crash on ICRS input; WCS not stored for astrowidget).
* **Update**: Updated concept `requirements/env-pins-zarr-v2.md`.
* **Update**: Updated concept `requirements/block3-data.md`.
* **Update**: Updated concept `decisions/delivery-on-jupyterhub.md`.
* **Update**: Updated concept `decisions/fits-to-zarr-skill.md`.
* **Update**: Updated concept `facts/source-review-notebook.md`.
* **Update**: Linked `architecture/llmoxie-gateway.md` to `facts/connected-projects.md` (LLMoxie is a connected SSEC project).
* **Update**: Linked `requirements/llm-data-consent.md` to `architecture/llmoxie-gateway.md` (data collected by the gateway).
* **Update**: Linked `requirements/audience-and-pedagogy.md` to `decisions/block3-fits-to-zarr-example.md` (shapes the example's scope).
* **Update**: Linked `requirements/audience-and-pedagogy.md` to `facts/observatory-event.md` (audience and format of the event).
* **Update**: Linked `facts/workshop-roles.md` to `facts/observatory-event.md` (who delivers the event).
* **Update**: Linked `facts/astrowidget-usage.md` to `facts/connected-projects.md` (published package from ovro-lwa).
* **Update**: Linked `facts/source-review-notebook.md` to `facts/connected-projects.md` (lives in ovro-lwa-portal).
* **Update**: Linked `requirements/env-pins-zarr-v2.md` to `decisions/delivery-on-jupyterhub.md` (same pins must land in the hub image).
* **Update**: Linked `requirements/env-pins-zarr-v2.md` to `facts/astrowidget-usage.md` (astrowidget's zarr v2 requirement drives the pins).
* **Update**: Linked `decisions/fits-to-zarr-skill.md` to `facts/astrowidget-usage.md` (output layout must match what astrowidget reads).
* **Update**: Linked `decisions/fits-to-zarr-skill.md` to `facts/source-review-notebook.md` (reference converter and notebook pattern).
* **Update**: Linked `decisions/block3-fits-to-zarr-example.md` to `requirements/block3-data.md` (data constraints for the example).
* **Update**: Linked `decisions/block3-fits-to-zarr-example.md` to `decisions/fits-to-zarr-skill.md` (the skill at the heart of the example).
* **Update**: Linked `decisions/block3-fits-to-zarr-example.md` to `facts/ovro-lwa-origin-story.md` (the real project that motivates the example).
* **Update**: Linked `decisions/block3-fits-to-zarr-example.md` to `facts/content-evolution.md` (replaces the HCI skills loop in Block 3).
* **Update**: Linked `decisions/delivery-on-jupyterhub.md` to `architecture/llmoxie-gateway.md` (models reach the hub through the gateway).
* **Update**: Linked `decisions/delivery-on-jupyterhub.md` to `facts/observatory-event.md` (infrastructure chosen for this event).
* **Update**: Linked `facts/stale-event-references.md` to `decisions/delivery-on-jupyterhub.md` (text that assumes the superseded Codespaces delivery).
* **Update**: Linked `facts/stale-event-references.md` to `facts/repo-lineage.md` (leftovers from earlier deliveries).
* **Update**: Linked `facts/repo-lineage.md` to `facts/content-evolution.md` (history of the repos where these content decisions were made).
* **Update**: Linked `facts/workshop-timeline.md` to `facts/observatory-event.md` (deadlines leading up to the event).
* **Creation**: Documented concept `architecture/llmoxie-gateway.md` (LLMoxie gateway as used by the workshop).
* **Creation**: Documented concept `requirements/llm-data-consent.md` (Disclose LLM data collection to participants).
* **Creation**: Documented concept `requirements/env-pins-zarr-v2.md` (Environment pins for astrowidget (zarr v2)).
* **Creation**: Documented concept `requirements/block3-data.md` (Block 3 data must be small and stay off git).
* **Creation**: Documented concept `requirements/audience-and-pedagogy.md` (Teaching requirements for the observatory audience).
* **Creation**: Documented concept `decisions/fits-to-zarr-skill.md` (fits-to-zarr skill: wrap a minimal converter, then verify the output).
* **Creation**: Documented concept `decisions/block3-fits-to-zarr-example.md` (Block 3 example: agent-driven FITS to Zarr, ending in astrowidget).
* **Creation**: Documented concept `decisions/delivery-on-jupyterhub.md` (Deliver the Florence tutorial on the Schmidt JupyterHub, not Codespaces).
* **Creation**: Documented concept `facts/workshop-roles.md` (Who does what for the observatory workshop).
* **Creation**: Documented concept `facts/astrowidget-usage.md` (astrowidget input format and API).
* **Creation**: Documented concept `facts/source-review-notebook.md` (What ovro-lwa-portal source_review.ipynb actually does).
* **Creation**: Documented concept `facts/ovro-lwa-origin-story.md` (OVRO-LWA FITS-to-Zarr and astrowidget: the backstory).
* **Creation**: Documented concept `facts/connected-projects.md` (External projects this workshop depends on).
* **Creation**: Documented concept `facts/stale-event-references.md` (Stale text to fix for the observatory event).
* **Creation**: Documented concept `facts/content-evolution.md` (How the workshop material evolved, and why).
* **Creation**: Documented concept `facts/repo-lineage.md` (Repository lineage and past deliveries).
* **Creation**: Documented concept `facts/workshop-timeline.md` (Observatory workshop timeline and deadlines (Oct-Nov 2026)).
* **Creation**: Documented concept `facts/observatory-event.md` (Observatory workshop event: Florence, Nov 3-5 2026).
* **Creation**: Initialized OKF v0.2 knowledge bundle.
