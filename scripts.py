import subprocess

completed = subprocess.run(['python', 'csv1.py'], capture_output=True, text=True)
print(completed.stdout)
