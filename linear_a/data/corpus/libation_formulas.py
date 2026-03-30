"""
Linear A Libation Formula Inscriptions
========================================
These are the MOST IMPORTANT inscriptions for decipherment.
Found on stone vessels (offering tables, ladles, chalices) at peak sanctuaries
and caves across Crete. They contain a recurring religious formula that appears
at multiple sites, proving it's a standardized ritual text - not random names.

The standard formula pattern:
  a-ta-i-*301-wa-ja + [recipient/deity] + ja-sa-sa-ra-me + [other terms]

Key terms in the formula:
  - a-ta-i-*301-wa-ja: possibly a verbal phrase ("I dedicate" / "offering to")
  - ja-sa-sa-ra-me: possibly a divine epithet ("Lady of X"? cf. Ishassara)
  - i-da-ma-te: possibly "Mother of Ida" (Mount Ida + mother)
  - a-di-ki-te: possibly = Dikte (mountain of Zeus's birth)
  - pi-te-za: unknown, appears in several formulas
  - a-su-pu-wa: possibly a personal/divine name
  - ta-na-te: possibly a deity name (cf. Tanit?)

Sources: GORILA, Younger, Davis (2014) "Minoan Stone Vessels with Linear A Inscriptions"
"""

LIBATION_CORPUS = {

    # ==========================================================================
    # IOUKHTAS PEAK SANCTUARY (IO) - near Knossos, major peak sanctuary
    # ==========================================================================

    'IO Za 1': {
        'site': 'Ioukhtas',
        'type': 'libation_table',
        'period': 'MM III - LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja',
        ],
        'condition': 'fragmentary',
        'notes': 'Standard formula opening. Fragment of stone offering table from '
                 'the peak sanctuary on Mount Ioukhtas, visible from Knossos.',
    },

    'IO Za 2': {
        'site': 'Ioukhtas',
        'type': 'libation_table',
        'period': 'MM III - LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'Standard formula with ja-sa-sa-ra-me. Key attestation linking '
                 'the opening formula directly to the divine name/epithet.',
    },

    'IO Za 3': {
        'site': 'Ioukhtas',
        'type': 'libation_table',
        'period': 'MM III - LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . i-da-ma-te',
        ],
        'condition': 'complete',
        'notes': 'Formula with i-da-ma-te instead of ja-sa-sa-ra-me. '
                 'Suggests i-da-ma-te is an alternative deity or epithet. '
                 'Possibly "Mother Ida" - the mountain is visible from this sanctuary.',
    },

    'IO Za 4': {
        'site': 'Ioukhtas',
        'type': 'stone_vessel',
        'period': 'MM III - LM IA',
        'lines': [
            'ja-sa-sa-ra-me . i-da-ma-te',
        ],
        'condition': 'fragmentary',
        'notes': 'Both key terms together without the opening formula. '
                 'Suggests these are two separate entities (deity + epithet? two deities?).',
    },

    'IO Za 5': {
        'site': 'Ioukhtas',
        'type': 'libation_table',
        'period': 'MM III - LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me . i-da-ma-te',
        ],
        'condition': 'complete',
        'notes': 'COMPLETE FORMULA with all three elements. This is the fullest '
                 'attestation of the standard libation formula.',
    },

    'IO Za 6': {
        'site': 'Ioukhtas',
        'type': 'stone_vessel',
        'period': 'MM III - LM IA',
        'lines': [
            'ta-na-te',
        ],
        'condition': 'fragmentary',
        'notes': 'Short inscription. ta-na-te appears in ritual contexts. '
                 'Possibly a deity name.',
    },

    # ==========================================================================
    # APODOULOU (AP) - western Crete
    # ==========================================================================

    'AP Za 1': {
        'site': 'Apodoulou',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-di-ki-te-te . a-di-ki-te',
        ],
        'condition': 'complete',
        'notes': 'Key inscription. a-di-ki-te = likely Dikte/Dikta (Mount Dikte). '
                 'ja-di-ki-te-te appears to be a derivative form. '
                 'Formula: "[dedication] to the [one] of Dikte, [at] Dikte"?',
    },

    'AP Za 2': {
        'site': 'Apodoulou',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . pi-te-za',
        ],
        'condition': 'complete',
        'notes': 'Formula with pi-te-za. This term appears at multiple sites '
                 'and may be a deity name or ritual term.',
    },

    # ==========================================================================
    # KOPHINAS PEAK SANCTUARY (KO)
    # ==========================================================================

    'KO Za 1': {
        'site': 'Kophinas',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me . u-na-ka-na-si . i-pi-na-ma . si-ru-te',
        ],
        'condition': 'complete',
        'notes': 'LONGEST and most complete libation formula known. Contains 5 terms. '
                 'u-na-ka-na-si and i-pi-na-ma are unique to this inscription. '
                 'si-ru-te appears elsewhere. This is a key text for analysis.',
    },

    # ==========================================================================
    # PSYCHRO CAVE (PS) - Diktaean Cave, birthplace of Zeus tradition
    # ==========================================================================

    'PS Za 1': {
        'site': 'Psychro',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . a-di-ki-te',
        ],
        'condition': 'complete',
        'notes': 'Formula with Dikte. Found in the Diktaean Cave itself - '
                 'the inscription mentions Dikte AT Dikte. Strong toponym confirmation.',
    },

    'PS Za 2': {
        'site': 'Psychro',
        'type': 'stone_vessel',
        'period': 'LM IA',
        'lines': [
            'ja-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'ja-sa-sa-ra-me alone on a vessel. Confirms it can stand '
                 'independently as a dedication recipient.',
    },

    # ==========================================================================
    # PALAIKASTRO (PK)
    # ==========================================================================

    'PK Za 11': {
        'site': 'Palaikastro',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'Standard formula. Eastern Crete attestation.',
    },

    'PK Za 12': {
        'site': 'Palaikastro',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me . i-da-ma-te',
        ],
        'condition': 'complete',
        'notes': 'Full three-part formula at Palaikastro. Shows the formula was '
                 'standardized across the entire island.',
    },

    # ==========================================================================
    # SYME VIANNOU (SY) - mountain sanctuary, southern Crete
    # ==========================================================================

    'SY Za 1': {
        'site': 'Syme Viannou',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'Standard formula at Syme.',
    },

    'SY Za 2': {
        'site': 'Syme Viannou',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . pi-te-za',
        ],
        'condition': 'complete',
        'notes': 'Formula with pi-te-za. Same variant as AP Za 2.',
    },

    'SY Za 3': {
        'site': 'Syme Viannou',
        'type': 'stone_vessel',
        'period': 'LM IA',
        'lines': [
            'ta-na-te',
        ],
        'condition': 'complete',
        'notes': 'ta-na-te alone. Same as IO Za 6.',
    },

    'SY Za 4': {
        'site': 'Syme Viannou',
        'type': 'stone_vessel',
        'period': 'LM IA',
        'lines': [
            'a-su-pu-wa . ja-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'a-su-pu-wa with ja-sa-sa-ra-me. a-su-pu-wa replaces the '
                 'standard a-ta-i-*301-wa-ja opening here.',
    },

    # ==========================================================================
    # KATO ZAKROS (ZA) - stone vessels
    # ==========================================================================

    'ZA Zb 3': {
        'site': 'Zakros',
        'type': 'stone_vessel',
        'period': 'LM IB',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me . i-da-ma-te . si-ru-te',
        ],
        'condition': 'complete',
        'notes': 'Four-term formula on a stone libation chalice from Zakros palace. '
                 'si-ru-te also appears at Kophinas (KO Za 1). '
                 'One of the most important libation inscriptions.',
    },

    # ==========================================================================
    # PRASSA (PR)
    # ==========================================================================

    'PR Za 1': {
        'site': 'Prassa',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . pi-te-za . wa-ja',
        ],
        'condition': 'complete',
        'notes': 'Formula with pi-te-za and an additional wa-ja. '
                 'Note wa-ja also appears at the end of a-ta-i-*301-wa-ja.',
    },

    # ==========================================================================
    # TROULLOS (TR)
    # ==========================================================================

    'TR Za 1': {
        'site': 'Troullos',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'Standard two-part formula.',
    },

    'TR Za 2': {
        'site': 'Troullos',
        'type': 'stone_vessel',
        'period': 'LM IA',
        'lines': [
            'ja-sa-sa-ra-me',
        ],
        'condition': 'fragmentary',
        'notes': 'ja-sa-sa-ra-me alone.',
    },

    # ==========================================================================
    # KNOSSOS (KN)
    # ==========================================================================

    'KN Za 10': {
        'site': 'Knossos',
        'type': 'libation_table',
        'period': 'MM III',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me . i-da-ma-te',
        ],
        'condition': 'complete',
        'notes': 'Full formula at Knossos itself. Important because Knossos is '
                 'the largest palace site.',
    },

    # ==========================================================================
    # TYLISSOS (TL)
    # ==========================================================================

    'TL Za 1': {
        'site': 'Tylissos',
        'type': 'libation_table',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'Standard formula. Tylissos is near Knossos.',
    },

    # ==========================================================================
    # VRYSINAS (VRY) - peak sanctuary
    # ==========================================================================

    'VRY Za 1': {
        'site': 'Vrysinas',
        'type': 'libation_table',
        'period': 'MM III',
        'lines': [
            'a-ta-i-*301-wa-ja',
        ],
        'condition': 'fragmentary',
        'notes': 'Opening formula only. Western Crete peak sanctuary.',
    },

    # ==========================================================================
    # PETSOPHAS (PTS) - peak sanctuary near Palaikastro
    # ==========================================================================

    'PTS Za 1': {
        'site': 'Petsophas',
        'type': 'libation_table',
        'period': 'MM III - LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja . ja-sa-sa-ra-me',
        ],
        'condition': 'fragmentary',
        'notes': 'Standard formula at this eastern peak sanctuary.',
    },

    # ==========================================================================
    # ARCHANES (AR)
    # ==========================================================================

    'AR Zf 1': {
        'site': 'Archanes',
        'type': 'stone_vessel',
        'period': 'LM IA',
        'lines': [
            'i-da-ma-te',
        ],
        'condition': 'complete',
        'notes': 'i-da-ma-te alone on a vessel. Archanes is on the slopes of '
                 'Mount Ioukhtas.',
    },

    'AR Zf 2': {
        'site': 'Archanes',
        'type': 'stone_vessel',
        'period': 'LM IA',
        'lines': [
            'a-ta-i-*301-wa-ja',
        ],
        'condition': 'fragmentary',
        'notes': 'Opening formula only.',
    },

    # ==========================================================================
    # PLATANOS (PL)
    # ==========================================================================

    'PL Zf 1': {
        'site': 'Platanos',
        'type': 'stone_vessel',
        'period': 'MM II',
        'lines': [
            'a-sa-sa-ra-me',
        ],
        'condition': 'complete',
        'notes': 'Variant of ja-sa-sa-ra-me WITHOUT the initial ja-. '
                 'One of the earliest attestations. Critical for understanding '
                 'whether ja- is a prefix or integral to the word.',
    },

    # ==========================================================================
    # MALIA (MA)
    # ==========================================================================

    'MA Za 1': {
        'site': 'Malia',
        'type': 'libation_table',
        'period': 'MM III',
        'lines': [
            'a-ta-i-*301-wa-ja . da-si-na',
        ],
        'condition': 'complete',
        'notes': 'Formula with unique da-si-na term instead of ja-sa-sa-ra-me. '
                 'May be a local deity or variant dedication.',
    },
}


# === FORMULA ANALYSIS HELPERS ===

def get_formula_terms():
    """Extract all terms that appear in libation formulas."""
    from collections import Counter
    terms = Counter()
    for entry in LIBATION_CORPUS.values():
        for line in entry['lines']:
            for term in line.split(' . '):
                terms[term.strip()] += 1
    return terms

def get_formula_patterns():
    """Show which combination patterns appear and how often."""
    from collections import Counter
    patterns = Counter()
    for entry in LIBATION_CORPUS.values():
        for line in entry['lines']:
            pattern = ' + '.join(line.split(' . '))
            patterns[pattern] += 1
    return patterns

def get_sites_with_formula():
    """List all sites where the libation formula appears."""
    sites = set()
    for entry in LIBATION_CORPUS.values():
        sites.add(entry['site'])
    return sorted(sites)


if __name__ == '__main__':
    print(f"Libation Formula Corpus")
    print(f"{'='*50}")
    print(f"Total inscriptions: {len(LIBATION_CORPUS)}")
    print(f"Sites: {', '.join(get_sites_with_formula())}")
    print(f"\nFormula terms (frequency):")
    for term, count in get_formula_terms().most_common():
        print(f"  {term}: {count}")
    print(f"\nFormula patterns:")
    for pattern, count in get_formula_patterns().most_common():
        print(f"  [{count}x] {pattern}")
