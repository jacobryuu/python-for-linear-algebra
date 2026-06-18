UV ?= uv

.PHONY: install format lint lint-fix typecheck test check pre-commit-install pre-commit clean

install:
	$(UV) sync --all-groups

format:
	$(UV) run ruff format src tests

lint:
	$(UV) run ruff check src tests

lint-fix:
	$(UV) run ruff check --fix src tests

typecheck:
	$(UV) run pyright

test:
	$(UV) run pytest

check: lint typecheck test

pre-commit-install:
	$(UV) run pre-commit install

pre-commit:
	$(UV) run pre-commit run --all-files

clean:
	rm -rf .venv .pytest_cache .ruff_cache .pyright .coverage coverage.xml dist build *.egg-info
