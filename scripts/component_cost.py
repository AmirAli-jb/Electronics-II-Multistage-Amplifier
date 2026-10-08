#!/usr/bin/env python3
"""Estimate component cost in the archived Electronics II LTspice designs.

This simple calculator follows the course price list and excludes the external
R_L load by default, consistent with the submitted cost totals. Only SYMBOL
and SYMATTR lines are parsed; model definitions do not count as components.
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILES = [
    ROOT / "phase-1/circuit/Phase1_Amplifier.asc",
    ROOT / "phase-2/circuit/Phase2_Amplifier.asc",
]
COSTS = {"npn": 5, "pnp": 5, "nmos": 3, "pmos": 3, "res": 10, "cap": 40}


def components(path: Path):
    """Yield dicts with symbol type and name from an LTspice ASCII schematic."""
    active = None
    # LTspice ASCII schematic sources may arrive with different encodings.
    for encoding in ("utf-8-sig", "utf-16", "latin-1"):
        try:
            data = path.read_text(encoding=encoding)
            if not data.startswith("Version "):
                continue
            break
        except UnicodeError:
            continue
    else:
        raise ValueError(f"Not a recognized LTspice schematic: {path}")
    for line in data.splitlines():
        if line.startswith("SYMBOL "):
            if active is not None:
                yield active
            parts = line.split()
            active = {"type": parts[1].lower(), "name": ""}
        elif active is not None and line.startswith("SYMATTR InstName "):
            active["name"] = line[len("SYMATTR InstName "):].strip()
    if active is not None:
        yield active


def summarize(path: Path, include_load: bool = False):
    counted = [c for c in components(path)
               if include_load or c["name"].lower() not in {"r_l", "r_load", "rload"}]
    counts = Counter(c["type"] for c in counted if c["type"] in COSTS)
    return counts, sum(count * COSTS[typ] for typ, count in counts.items())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schematic", type=Path, nargs="*", help=".asc files to inspect")
    parser.add_argument("--include-load", action="store_true", help="Count the external load R_L")
    args = parser.parse_args()
    for schematic in args.schematic or DEFAULT_FILES:
        if not schematic.is_file():
            parser.error(f"File not found: {schematic}")
        counts, cost = summarize(schematic, args.include_load)
        items = ", ".join(f"{t}={counts.get(t, 0)}" for t in ("npn", "pnp", "nmos", "pmos", "res", "cap"))
        print(f"{schematic.name}: {cost} units ({items})")


if __name__ == "__main__":
    main()
