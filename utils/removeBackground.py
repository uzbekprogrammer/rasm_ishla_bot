import requests


async def remove_background(img_url):
    response = requests.post(
        'https://sdk.photoroom.com/v1/segment',
        headers={'x-api-key': '1e352e0fb19099fe2984cdc43d90614da96d1840'},
        files={'image_file': open(f'{img_url}', 'rb')},
    )

    response.raise_for_status()
    with open(f'{img_url}', 'wb') as f:
        f.write(response.content)
