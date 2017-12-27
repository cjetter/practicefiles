'''Ch13 : XML ElementTree problem #2 - Looping through nodes'''

import xml.etree.ElementTree as ET

datafull = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
        <user x="19">
            <id>019</id>
            <name>George</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(datafull)
print(tree)
print(type)
lst = tree.findall('users/user')
print('User count: ', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))