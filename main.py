import requests


def get_quote():
  response = requests.get('https://api.quotable.io/random')

  if response.status_code == 200:
    data = response.json()
    return data['content']
  else:
    return 'Failed to retrieve a quote'


print(get_quote())
