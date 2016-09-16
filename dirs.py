import os

file_dir = os.path.dirname(__file__)
print file_dir
new_dir = os.path.join(file_dir, 'dev')
print new_dir