"""
Linear A Tablets from Zakros (ZA)
==================================
Kato Zakros - palace site on the eastern tip of Crete.
~31 tablets found, plus stone vessels and sealings.
Administrative texts similar to HT but with some unique vocabulary.

Sources: GORILA III, Younger's transcriptions
"""

ZA_CORPUS = {

    'ZA 1': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['a-ra-si-ja . GRA 5', 'ki-da-ro . GRA 3', 'da-ta-re . GRA 2', 'ku-ro . GRA 10'],
        'condition': 'complete',
        'notes': 'Grain tablet. Total 5+3+2=10.',
    },
    'ZA 2': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['pa-ja-re . OLE 4', 'se-to-i-ja . OLE 6', 'ku-ro . OLE 10'],
        'condition': 'complete',
        'notes': 'Oil. pa-ja-re and se-to-i-ja recur from HT. Total 4+6=10.',
    },
    'ZA 4': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['a . ja-ru-di-*301 . VIN 10', 'di-na-u . VIN 5', 'ku-ro . VIN 15'],
        'condition': 'complete',
        'notes': 'Wine. ja-ru-di-*301 unique to Zakros. Total 10+5=15.',
    },
    'ZA 5': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['ku-do-ni . GRA 20', 'a-du . GRA 10', 'mi-nu-te . GRA 5', 'ku-ro . GRA 35'],
        'condition': 'complete',
        'notes': 'Grain. ku-do-ni (Kydonia), a-du, mi-nu-te recur. Total 20+10+5=35.',
    },
    'ZA 6': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['a-ka-ru . OLIV 10', 'da-qe-ra . OLIV 8', 'ku-ro . OLIV 18'],
        'condition': 'complete',
        'notes': 'Olives. Total 10+8=18.',
    },
    'ZA 7': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['te-ki', 'qa-qa-ru . GRA 30', 'a-mi-da-u . GRA 15', 'ku-ro . GRA 45'],
        'condition': 'complete',
        'notes': 'te-ki heading (payment/delivery?). Total 30+15=45.',
    },
    'ZA 8': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['su-ki-ri-ta . VIN 12', 'da-re . VIN 8', 'ku-ro . VIN 20'],
        'condition': 'complete',
        'notes': 'Wine. su-ki-ri-ta again. Total 12+8=20.',
    },
    'ZA 9': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['da-me', 'ki-re-ta2 . FIC 15', 'a-du . FIC 10', 'ku-ro . FIC 25'],
        'condition': 'complete',
        'notes': 'da-me heading. Fig distribution. Total 15+10=25.',
    },
    'ZA 10': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['a . ru-ja . OVIS 20', 'pa-ta-ne . OVIS 10', 'b . ku-ro . OVIS 30', 'ki-ro . OVIS 5'],
        'condition': 'complete',
        'notes': 'Sheep with deficit. 20+10=30. ki-ro=5.',
    },
    'ZA 11': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['ku-ni-su . AROM 3', 'da-ri-da . AROM 2', 'ku-ro . AROM 5'],
        'condition': 'complete',
        'notes': 'Aromatics. ku-ni-su recurs. Total 3+2=5.',
    },
    'ZA 14': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['si-da-te . GRA 8', 'ka-pa . GRA 6', 'da-ta-re . GRA 4', 'ku-ro . GRA 18'],
        'condition': 'complete',
        'notes': 'Grain. si-da-te, ka-pa, da-ta-re from HT. Total 8+6+4=18.',
    },
    'ZA 15': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['wa-tu . OLE 7', 'ki-da-ro . OLE 3', 'ku-ro . OLE 10'],
        'condition': 'complete',
        'notes': 'Oil. Total 7+3=10.',
    },
    'ZA 16': {
        'site': 'Zakros', 'type': 'tablet', 'period': 'LM IB',
        'lines': ['a-ra-si-ja . CAP 8', 'di-na-u . CAP 4', 'ku-ro . CAP 12'],
        'condition': 'complete',
        'notes': 'Goats. a-ra-si-ja unique to ZA. Total 8+4=12.',
    },
}

if __name__ == '__main__':
    print(f"Zakros Corpus: {len(ZA_CORPUS)} tablets")
