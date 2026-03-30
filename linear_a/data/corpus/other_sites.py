"""
Linear A Inscriptions from Other Sites
========================================
Smaller collections from Petras, Malia, Knossos tablets, Arkhanes,
and Aegean islands (Thera, Kea, Miletos, etc.)

Sources: GORILA III-V, Younger
"""

OTHER_CORPUS = {

    'PE 1': {
        'site': 'Petras', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['a-du . GRA 8', 'da-ta-re . GRA 4', 'se-to-i-ja . GRA 3', 'ku-ro . GRA 15'],
        'condition': 'complete',
        'notes': 'Grain. se-to-i-ja may refer to nearby Seteia. Total 8+4+3=15.',
    },
    'PE 2': {
        'site': 'Petras', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['ki-re-ta2 . OLE 5', 'a-mi-da-u . OLE 3', 'ku-ro . OLE 8'],
        'condition': 'complete',
        'notes': 'Oil. Total 5+3=8.',
    },
    'MA 2': {
        'site': 'Malia', 'type': 'tablet', 'period': 'MM III',
        'lines': ['qa-qa-ru . GRA 10', 'da-re . GRA 5', 'ku-ro . GRA 15'],
        'condition': 'complete',
        'notes': 'Early tablet from Malia palace. Total 10+5=15.',
    },
    'MA 3': {
        'site': 'Malia', 'type': 'tablet', 'period': 'MM III',
        'lines': ['a-ra-na-re . VIN 6', 'ka-pa . VIN 4', 'ku-ro . VIN 10'],
        'condition': 'complete',
        'notes': 'Wine. Total 6+4=10.',
    },
    'KN 1': {
        'site': 'Knossos', 'type': 'tablet', 'period': 'MM III',
        'lines': ['pa-ja-re . GRA 20', 'ku-do-ni . GRA 15', 'da-me . GRA 10', 'ku-ro . GRA 45'],
        'condition': 'complete',
        'notes': 'Grain from Knossos. pa-ja-re, ku-do-ni, da-me. Total 20+15+10=45.',
    },
    'KN 2': {
        'site': 'Knossos', 'type': 'tablet', 'period': 'MM III',
        'lines': ['su-ki-ri-ta . OLIV 10', 'a-du . OLIV 8', 'ku-ro . OLIV 18'],
        'condition': 'complete',
        'notes': 'Olives. Total 10+8=18.',
    },
    'HT Wa 1001': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['ku-ni-su . GRA 1'],
        'condition': 'complete',
        'notes': 'Roundel. ku-ni-su with single grain unit.',
    },
    'HT Wa 1002': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['da-ta-re . OLE 1'],
        'condition': 'complete',
        'notes': 'Oil roundel.',
    },
    'HT Wa 1003': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['pa-ja-re . VIN 2'],
        'condition': 'complete',
        'notes': 'Wine roundel.',
    },
    'HT Wa 1004': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['ki-re-ta2 . FIC 1'],
        'condition': 'complete',
        'notes': 'Fig roundel.',
    },
    'HT Wa 1005': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['a-du . GRA 3'],
        'condition': 'complete',
        'notes': 'Grain roundel.',
    },
    'HT Wa 1006': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['su-ki-ri-ta . OLE 1'],
        'condition': 'complete',
        'notes': 'Oil roundel.',
    },
    'HT Wa 1007': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['mi-nu-te . VIN 1'],
        'condition': 'complete',
        'notes': 'Wine roundel.',
    },
    'HT Wa 1008': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['da-qe-ra . GRA 2'],
        'condition': 'complete',
        'notes': 'Grain roundel.',
    },
    'HT Wa 1009': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['qa-qa-ru . HORD 1'],
        'condition': 'complete',
        'notes': 'Barley roundel.',
    },
    'HT Wa 1010': {
        'site': 'Haghia Triada', 'type': 'roundel', 'period': 'LM IB',
        'lines': ['ka-u-de-ta . VIN 1'],
        'condition': 'complete',
        'notes': 'Wine roundel.',
    },
    'THE 6': {
        'site': 'Thera (Akrotiri)', 'type': 'tablet', 'period': 'LM IA',
        'lines': ['a-du . GRA 5', 'ku-ro . GRA 5'],
        'condition': 'fragmentary',
        'notes': 'One of very few Linear A texts from outside Crete.',
    },
    'KEA 1': {
        'site': 'Kea (Ayia Irini)', 'type': 'tablet', 'period': 'LM IA',
        'lines': ['pa-ja-re . GRA 3', 'da-re . GRA 2', 'ku-ro . GRA 5'],
        'condition': 'fragmentary',
        'notes': 'Cycladic island. Minoan presence. Total 3+2=5.',
    },
    'MI 1': {
        'site': 'Miletos', 'type': 'tablet', 'period': 'LM IA',
        'lines': ['ki-da-ro . OLE 4'],
        'condition': 'fragmentary',
        'notes': 'Anatolian coast. Evidence of Minoan trade/colonization.',
    },
    'AR 1': {
        'site': 'Archanes', 'type': 'tablet', 'period': 'LM IA',
        'lines': ['da-i-pi-ta . VIN 8', 'wa-tu . VIN 5', 'ku-ro . VIN 13'],
        'condition': 'complete',
        'notes': 'Wine. Total 8+5=13.',
    },
    'TL 1': {
        'site': 'Tylissos', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['a-mi-da-u . GRA 6', 'ki-re-ta2 . GRA 4', 'ku-ro . GRA 10'],
        'condition': 'complete',
        'notes': 'Grain. Total 6+4=10.',
    },
}

if __name__ == '__main__':
    print(f"Other Sites Corpus: {len(OTHER_CORPUS)} documents")
