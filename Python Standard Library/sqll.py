import sqlite3
import json
from pathlib import Path

data = Path('movies.json').read_text()
movies = json.loads(data)

with sqlite3.connect('db.sqlite3') as conncetion:
    select_command = 'SELECT * FROM MOVIES'
    cursor = conncetion.execute(select_command)
    print(cursor.fetchall())
