# Bhagavad Gita Daily Learning App

A simple Python application that generates **one Bhagavad Gita learning per day**.

## Features
- Deterministic daily learning (same date always returns the same learning)
- Verse reference, theme, short lesson, and daily practice step
- Optional `--date` argument for checking any day

## Run
```bash
python gita_daily_app.py
```

Use a custom date:
```bash
python gita_daily_app.py --date 2026-02-27
```

## Test
```bash
python -m pytest -q
```
