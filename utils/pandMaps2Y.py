import os, re

dir = os.listdir('../BakaBot/storage/maps')
os.chdir('../BakaBot/storage/maps')

for file in dir:
    if file.endswith('.map'):
        open_file = open(file, 'r')
        read_file = open_file.read()
        patterns = [
            # First, remove all newlines for consistency
            ('\n', ''),
            # Remove double opening and closing brackets
            (r'\[\[', ''),
            (r'\]\]', r''),
            # Replace separators
            (r'"\, "', ':'),
            # Add newlines
            (r'\],', '\n'),
            # Remove the rest
            ('"', ''),
            (r'\,', ''),
            (r'\[', ''),
        ]
        for pattern in patterns:
            regex = re.compile(pattern[0])
            read_file = regex.sub(pattern[1], read_file)

        # print(read_file)
        write_file = open(file, 'w')
        write_file.write(read_file)
