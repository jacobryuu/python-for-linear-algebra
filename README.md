# python-base-template

Python 開発向けテンプレートです。`uv` で依存管理し、`ruff`、`pyright`、`pytest`、`pytest-cov`、`pre-commit` を標準搭載しています。

## Setup

```bash
make install
make pre-commit-install
```

## Daily commands

```bash
make format
make lint
make typecheck
make test
make check
```
