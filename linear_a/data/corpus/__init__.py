"""
Linear A Corpus
================
Complete corpus of Linear A inscriptions organized by findsite.
Data sourced from GORILA (Godart & Olivier), Younger's transcriptions,
and published scholarship.

Each inscription is a dict with:
  - site: findspot
  - type: tablet/roundel/libation_table/stone_vessel/pithos/nodule/etc
  - period: MM II, MM III, LM IA, LM IB, etc
  - lines: list of line transcriptions (phonetic, using Linear B values)
  - signs: raw sign sequences (AB numbers)
  - ideograms: commodity ideograms present
  - numbers: numeric values recorded
  - condition: complete/fragmentary/damaged
  - notes: scholarly commentary
"""

CORPUS = {}

def _merge(module_corpus):
    """Merge a sub-corpus into the main CORPUS."""
    CORPUS.update(module_corpus)

# Import sub-corpora - works both as package import and standalone script
import importlib
import os as _os

def _load_sub_corpora():
    """Load all sub-corpus modules, handling both package and standalone execution."""
    _sub_corpora = [
        ('libation_formulas', 'LIBATION_CORPUS'),
        ('haghia_triada', 'HT_CORPUS'),
        ('haghia_triada_2', 'HT_CORPUS_2'),
        ('zakros', 'ZA_CORPUS'),
        ('khania', 'KH_CORPUS'),
        ('phaistos', 'PH_CORPUS'),
        ('other_sites', 'OTHER_CORPUS'),
    ]

    for module_name, corpus_var in _sub_corpora:
        try:
            # Try relative import first (package mode)
            mod = importlib.import_module(f'.{module_name}', package=__package__ or 'linear_a.data.corpus')
        except (ImportError, ModuleNotFoundError):
            try:
                # Fall back to direct import (standalone mode)
                import sys
                corpus_dir = _os.path.dirname(_os.path.abspath(__file__))
                if corpus_dir not in sys.path:
                    sys.path.insert(0, corpus_dir)
                mod = importlib.import_module(module_name)
            except (ImportError, ModuleNotFoundError):
                continue
        sub_corpus = getattr(mod, corpus_var, None)
        if sub_corpus:
            _merge(sub_corpus)

_load_sub_corpora()


# === HELPER FUNCTIONS ===

def get_all():
    """Return the complete corpus."""
    return CORPUS

def get_by_site(site_prefix):
    """Get all inscriptions from a site (e.g., 'HT', 'ZA', 'KH')."""
    return {k: v for k, v in CORPUS.items() if k.startswith(site_prefix)}

def get_by_type(doc_type):
    """Get all inscriptions of a type (e.g., 'tablet', 'libation_table')."""
    return {k: v for k, v in CORPUS.items() if v.get('type') == doc_type}

def get_libation_formulas():
    """Get all inscriptions containing the libation formula."""
    return {k: v for k, v in CORPUS.items()
            if v.get('type') in ('libation_table', 'stone_vessel')
            or 'libation' in v.get('notes', '').lower()}

def get_words():
    """Extract all unique words (sign sequences between dividers) from the corpus."""
    words = []
    for entry in CORPUS.values():
        for line in entry.get('lines', []):
            # Split on word dividers (dots, spaces, |)
            parts = line.replace('|', '.').replace('  ', '.').split('.')
            for part in parts:
                w = part.strip()
                if w and not w.startswith(('GRA', 'OLE', 'VIN', 'FIC', 'OVIS',
                    'CAP', 'SUS', 'BOS', 'TELA', 'AES', 'HORD', 'OLIV',
                    'AROM', 'CYP', 'VIR', 'MUL', '[', ']')):
                    try:
                        float(w)
                    except ValueError:
                        if len(w) > 1:
                            words.append(w)
    return words

def get_unique_words():
    """Get sorted unique words with frequency counts."""
    from collections import Counter
    return Counter(get_words())

def search_sequence(seq):
    """Find all inscriptions containing a sign sequence."""
    results = {}
    seq_lower = seq.lower()
    for k, v in CORPUS.items():
        for line in v.get('lines', []):
            if seq_lower in line.lower():
                results[k] = v
                break
    return results

def corpus_stats():
    """Return basic corpus statistics."""
    total_lines = sum(len(v.get('lines', [])) for v in CORPUS.values())
    total_words = len(get_words())
    unique = len(get_unique_words())
    sites = set()
    for k in CORPUS:
        prefix = k.split(' ')[0] if ' ' in k else k[:2]
        sites.add(prefix)
    return {
        'total_inscriptions': len(CORPUS),
        'total_lines': total_lines,
        'total_words': total_words,
        'unique_words': unique,
        'sites': sorted(sites),
    }


if __name__ == '__main__':
    stats = corpus_stats()
    print(f"Linear A Corpus")
    print(f"{'='*40}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"\nTop 20 most frequent words:")
    for word, count in get_unique_words().most_common(20):
        print(f"  {word}: {count}")
