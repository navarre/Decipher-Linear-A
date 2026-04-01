#!/usr/bin/env python3
"""
Build script: export Python corpus data to JSON for the static site.

Run this to regenerate docs/data.json from the canonical Python sources.
The dashboard JS can then fetch this file for live data.

Usage:
    python3 docs/build_data.py
"""

import json
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from linear_a.data.signs import (
    SYLLABOGRAMS, LOGOGRAMS, NUMERALS, FRACTIONS,
    TRANSACTION_SIGNS, RECURRING_SEQUENCES, signs_by_confidence
)
from linear_a.data.corpus import corpus_stats, get_unique_words, CORPUS

# Try to import recent discoveries extras
try:
    from linear_a.data.corpus.recent_discoveries import (
        ACTIVE_EXCAVATIONS, ONLINE_DATABASES, KEY_PAPERS_2023_2026
    )
except ImportError:
    ACTIVE_EXCAVATIONS = {}
    ONLINE_DATABASES = {}
    KEY_PAPERS_2023_2026 = {}


def build():
    stats = corpus_stats()
    top_words = get_unique_words().most_common(30)

    # Site distribution
    from collections import Counter
    site_counts = Counter()
    type_counts = Counter()
    period_counts = Counter()
    for k, v in CORPUS.items():
        site_counts[v.get('site', 'unknown')] += 1
        type_counts[v.get('type', 'unknown')] += 1
        period_counts[v.get('period', 'unknown')] += 1

    data = {
        'generated': True,
        'corpus': {
            'total_inscriptions': stats['total_inscriptions'],
            'total_lines': stats['total_lines'],
            'total_words': stats['total_words'],
            'unique_words': stats['unique_words'],
            'sites_count': len(stats['sites']),
            'top_words': [{'word': w, 'count': c} for w, c in top_words],
            'by_site': dict(site_counts.most_common()),
            'by_type': dict(type_counts.most_common()),
            'by_period': dict(period_counts.most_common()),
        },
        'signs': {
            'syllabograms': len(SYLLABOGRAMS),
            'logograms': len(LOGOGRAMS),
            'numerals': len(NUMERALS),
            'fractions': len(FRACTIONS),
            'confidence': {
                'high': len(signs_by_confidence('high')),
                'medium': len(signs_by_confidence('medium')),
                'low': len(signs_by_confidence('low')),
                'none': len(signs_by_confidence('none')),
            },
            'transaction_signs': len(TRANSACTION_SIGNS),
            'recurring_sequences': len(RECURRING_SEQUENCES),
        },
        'recurring_sequences': {
            k: {'freq': v.get('freq', 0), 'context': v.get('context', ''), 'notes': v.get('notes', '')}
            for k, v in RECURRING_SEQUENCES.items()
        },
        'active_excavations': ACTIVE_EXCAVATIONS,
        'online_databases': ONLINE_DATABASES,
        'key_papers': KEY_PAPERS_2023_2026,
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json')
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2, default=str)

    print(f"Exported to {out_path}")
    print(f"  Corpus: {data['corpus']['total_inscriptions']} inscriptions, "
          f"{data['corpus']['unique_words']} unique words")
    print(f"  Signs: {data['signs']['syllabograms']} syllabograms "
          f"({data['signs']['confidence']['high']} high confidence)")
    print(f"  Excavations: {len(ACTIVE_EXCAVATIONS)}")
    print(f"  Databases: {len(ONLINE_DATABASES)}")


if __name__ == '__main__':
    build()
