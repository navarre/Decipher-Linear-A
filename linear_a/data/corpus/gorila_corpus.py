"""
GORILA Corpus - Imported from lineara.xyz
==========================================
1,721 Linear A inscriptions from the complete GORILA publication
(Godart & Olivier, Recueil des Inscriptions en Linéaire A).

Source: github.com/mwenge/lineara.xyz (based on George Douros' tabulation)
License: CC BY-NC-SA 4.0

Each inscription is converted to match the project's standard format:
  - site, type, period, lines, condition, notes
"""

import json
import os

_DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'external', 'lineara_xyz_corpus.json'
)

# Map lineara.xyz support types to our type conventions
_TYPE_MAP = {
    'Tablet': 'tablet',
    'Nodule': 'nodule',
    'Roundel': 'roundel',
    'Stone vessel': 'stone_vessel',
    'Clay vessel': 'clay_vessel',
    'Metal object': 'metal_object',
    'Stone object': 'stone_object',
    'Lames (short thin tablet)': 'lame',
    'Sealing': 'sealing',
    'Inked inscription': 'inked_inscription',
    'Architecture': 'architecture',
    '3-sided bar': 'bar',
    '4-sided bar': 'bar',
    'Graffito': 'graffito',
    'Label': 'label',
    'ivory object': 'ivory_object',
    'clay vessel': 'clay_vessel',
    'Loom weight': 'loom_weight',
    'Triton': 'triton',
}

# Map lineara.xyz context strings to period labels
_PERIOD_MAP = {
    'MMII': 'MM II',
    'MMIII': 'MM III',
    'MMIIIA': 'MM IIIA',
    'MMIIIB': 'MM IIIB',
    'MMIII-LMIA': 'MM III - LM IA',
    'LMIA': 'LM IA',
    'LMIA-B': 'LM IA-B',
    'LMIB': 'LM IB',
    'LMI': 'LM I',
    'LMII': 'LM II',
    'LMIII': 'LM III',
    'LMIIIA': 'LM IIIA',
}


def _transliterated_words_to_lines(tw):
    """Convert a transliteratedWords list to our lines format.

    Input: ['QE-RA₂-U', '𐄁', '\\n', 'KI-RO', '197', ...]
    Output: ['QE-RA₂-U . KI-RO 197', 'ZU-SU 70', ...]
    """
    lines = []
    current_parts = []

    for token in tw:
        if token == '\n':
            if current_parts:
                lines.append(' . '.join(current_parts) if len(current_parts) > 1
                             else current_parts[0])
                current_parts = []
        elif token == '𐄁':
            # Word divider - already handled by joining with ' . '
            continue
        else:
            current_parts.append(token)

    if current_parts:
        lines.append(' . '.join(current_parts) if len(current_parts) > 1
                     else current_parts[0])

    return lines


def _normalize_name(name):
    """Normalize inscription names: 'HT1' -> 'HT 1', 'KH5' -> 'KH 5'."""
    import re
    m = re.match(r'^([A-Z]+)(\d.*)$', name)
    if m:
        return f'{m.group(1)} {m.group(2)}'
    return name


def _convert_entry(name, entry):
    """Convert a lineara.xyz entry to our corpus format."""
    tw = entry.get('transliteratedWords', [])
    lines = _transliterated_words_to_lines(tw)

    context = entry.get('context', '')
    period = _PERIOD_MAP.get(context, context)

    support = entry.get('support', '')
    doc_type = _TYPE_MAP.get(support, support.lower())

    notes_parts = []
    if entry.get('scribe'):
        notes_parts.append(f"Scribe: {entry['scribe']}")
    if entry.get('findspot'):
        notes_parts.append(f"Findspot: {entry['findspot']}")

    return {
        'site': entry.get('site', ''),
        'type': doc_type,
        'period': period,
        'lines': lines,
        'condition': 'fragmentary' if '𐝫' in entry.get('parsedInscription', '') else 'complete',
        'notes': '. '.join(notes_parts) if notes_parts else '',
        'source': 'GORILA via lineara.xyz',
        'unicode_inscription': entry.get('parsedInscription', ''),
        'unicode_words': entry.get('words', []),
    }


def load_gorila_corpus():
    """Load and convert the full GORILA corpus from JSON."""
    with open(_DATA_PATH, 'r') as f:
        raw = json.load(f)

    corpus = {}
    for name, entry in raw.items():
        normalized = _normalize_name(name)
        corpus[normalized] = _convert_entry(name, entry)

    return corpus


GORILA_CORPUS = load_gorila_corpus()
