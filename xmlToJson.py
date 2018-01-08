import json
import xmltodict

with open('sample.xml', 'r') as fileXML:
    xmlString = fileXML.read()
fileXML.close()

print('XML input (sample.xml):')
print(xmlString)

jsonString = json.dumps(xmltodict.parse(xmlString))

print('\nJSON output(output.json):')
print(jsonString)

with open('output.json', 'w') as fileJSON:
    fileJSON.write(jsonString)
fileJSON.close()
