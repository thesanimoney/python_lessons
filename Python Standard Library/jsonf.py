import json
from pathlib import Path


file = Path('movies.json').read_text()
movies = json.loads(file)
print(movies[0]['title'])

