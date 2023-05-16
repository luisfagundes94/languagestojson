import json
import chardet
import uuid

input_file = 'languages.json'
output_file = 'languages.json'

# Detect the encoding of the input file
with open(input_file, 'rb') as file:
    raw_data = file.read()
    detected_encoding = chardet.detect(raw_data)['encoding']

# Load the input file using the detected encoding
data = json.loads(raw_data.decode(detected_encoding))

languages = []
available_languages = ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hu", "it", "ja", "lt", "lv", "mt", "nl", "pl", "pt", "ro", "ru", "sk", "sl", "sv", "zh"]

# filter only the available languages given an array of data
for language in data:
    if language['code'] in available_languages:    
        languages.append(language)

print(len(languages) == len(available_languages)) 


with open(output_file, 'w', encoding=detected_encoding) as file:
    json.dump(languages, file, indent=2, ensure_ascii=False)
