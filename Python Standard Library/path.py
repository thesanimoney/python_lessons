from pathlib import Path
from time import ctime
import shutil

source = Path('D:\Python Lessons\Eccommerce\__init__.py')
target = Path() / '__init__.py'

shutil.copy(source, target)
# print(path.exists())
# print(path.is_file())

path1 = Path('D:\Python Lessons\Eccommerce')

# paths = [p for p in path1.iterdir() if p.is_dir()]
# py_files = [p for p in path1.glob('*.py')]

# print(paths)
# print(py_files)
#
# path.exists()
# path.rename('init.txt')
# path.unlink()
# print(ctime(path.stat().st_ctime))