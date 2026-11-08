"""Deterministic fair-entry rating; value-band reconciliation remains analyst work."""
import math


def rate_entry(entry, lower, upper, coverage='limited'):
    """Return a 1–5 estimate from an independently supported as-is band.

    A verified no-viable-use rating of zero requires separate factual analysis.
    This function neither produces value bands nor measures their reliability.
    """
    for value in (entry, lower, upper):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError('Entry and value bounds must be finite positive numbers')
    if lower > upper:
        raise ValueError('As-is value lower bound exceeds upper bound')
    if coverage not in ('limited', 'moderate', 'strong'):
        raise ValueError('Coverage must be limited, moderate or strong')
    if entry > upper:
        raw = 2 if entry <= upper * 1.15 + 1e-8 else 1
    elif entry <= lower * .80 + 1e-8:
        raw = 5
    elif entry <= lower * .95 + 1e-8:
        raw = 4
    else:
        raw = 3
    cap = {'limited': 3, 'moderate': 4, 'strong': 5}[coverage]
    return {'rating': min(raw, cap), 'uncapped_rating': raw, 'coverage_cap': cap,
            'lower_bound_discount_pct': (lower - entry) / lower * 100,
            'upper_bound_premium_pct': (entry - upper) / upper * 100}
