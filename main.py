# pip isntall openai
import openai
import os
import json
from base64 import b64decode

prompt = input('The prompt: ')
openai.api_key = os.getenv('API_KEY')

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size='256x256',
    response_format='b64_json'
)

with open('data.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

image_data = b64decode(response['data'][0]['b64_json'])
file_name = '_'.join(prompt.split(' '))

with open(f'{file_name}.png', 'wb') as file:
    file.write(image_data)
