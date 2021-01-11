# -*- coding: UTF8 -*-

import json

from nosql import NoSQL


db = NoSQL()
print('Created NoSQL database instance!')

print(f'Main table: {db.main_table}')

all_v = db.get_all()

if not all_v:
    # If the database is empty, we'll add some values.

    to_put = {
        'iPhone': {
            'color': 'white',
            'price': '1199€',
            'size': 'medium',
            'battery': 'low',
        },
        'Samsung': {
            'size': 'big',
            'price': '799€',
            'screen': 'QHD',
        },
        'Windows Phone': {
            'status': 'discontinued'
        },
        'Huawei': {
            'origin': 'China',
            'color': 'various',
            'price': '599€',
        },
    }

    for k, v in to_put.items():
        db.put({k: v})

all_v = db.get_all()


print(json.dumps(all_v, indent=4))
