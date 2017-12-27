'''Ch13 : JSON problem'''

import json

datafull = '''[{"id":"001","x":"2","name":"Chuck"},{"id":"009","x":"7","name":"Chuck"}]'''    

tree = json.loads(datafull)
print('User count: ', len(tree))

for item in tree:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item["x"])