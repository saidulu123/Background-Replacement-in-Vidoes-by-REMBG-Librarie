import os

# Directory containing the images
directory = 'D:/Mukesh/Work Files/Project/Frames Merging to form a video/frames/'

# List all files in the directory
files = os.listdir(directory)

# Filter only JPG files
jpg_files = [file for file in files if file.endswith('.jpg')]

# Sort the files based on the numeric part of their name
jpg_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

# Rename the files to frame001.jpg, frame002.jpg, ...
for i, filename in enumerate(jpg_files, start=1):
    new_filename = f'frame{i:03d}.jpg'
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
