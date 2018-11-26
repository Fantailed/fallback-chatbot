import os
from pathlib import Path

dir = os.listdir('../BakaBot/storage/maps')
os.chdir('../BakaBot/storage/maps')

for file in dir:
    p = Path(file)
    p.rename(p.with_suffix('.txt'))
