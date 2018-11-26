import os, re

dir = os.listdir('../BakaBot/storage/sets')
os.chdir('../BakaBot/storage/sets')

for file in dir:
    if file.endswith('.set'):
        open_file = open(file, 'r')
        read_file = open_file.read()
        patterns = [
            # First, remove all newlines for consistency
            ('\n', ''),
            # Remove double opening and closing brackets
            (r'\[\[', ''),
            (r'\]\]', ''),
            # Remove varieties of separators
            (r'\]\,\[', '\n'),
            (r'\]\, \[', '\n'),
            # Remove the rest
            ('"', ''),
            (r'\,', ''),
        ]
        for pattern in patterns:
            regex = re.compile(pattern[0])
            read_file = regex.sub(pattern[1], read_file)

        write_file = open(file, 'w')
        write_file.write(read_file)
