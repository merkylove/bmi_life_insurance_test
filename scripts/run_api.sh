#!/usr/bin/env bash

${HOME}/.poetry/bin/poetry run python -m aiohttp.web -H 0.0.0.0 -P 8080 src.life_insurance.api.app:init_func