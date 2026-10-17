#!/usr/bin/env bash
set -euo pipefail

# --- Output styling -------------------------------------------------------
# Colors are emitted unconditionally (not gated on a tty) because the
# devcontainer "starting container" log renders ANSI codes.
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BOLD="\033[1m"
RESET="\033[0m"

STAGE="post-start"
TOTAL_STEPS=1

say()  { printf "%b\n==> [%s] (%s/%s) %s%b\n" "${BOLD}${GREEN}" "${STAGE}" "$1" "${TOTAL_STEPS}" "$2" "${RESET}"; }
info() { printf "      %s\n" "$1"; }
warn() { printf "%b  !   %s%b\n" "${YELLOW}" "$1" "${RESET}"; }

say 1 "Checking LLMoxie gateway credentials"
if [ -n "${LITELLM_BASE_URL:-}" ]; then
  info "LITELLM_BASE_URL: configured"
else
  warn "LITELLM_BASE_URL is not set"
fi

if [ -n "${LITELLM_API_KEY:-}" ]; then
  info "LITELLM_API_KEY: detected"
else
  warn "LITELLM_API_KEY is not set"
fi

printf "%b\n==> [%s] complete — container is ready.%b\n" "${BOLD}${GREEN}" "${STAGE}" "${RESET}"
