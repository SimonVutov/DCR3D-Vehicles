import os
from datetime import datetime

# Get all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Filter for .car files and get their modified times
car_files = [
    (f, os.path.getmtime(f))
    for f in files if f.lower().endswith('.car')
]

# Sort by modified time (oldest first)
car_files.sort(key=lambda x: x[1])

lines = []
for car_file, mod_time in car_files:
    mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
    lines.append(f"{car_file} {mod_date}")

with open('car_files_list.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(lines) + '\n')