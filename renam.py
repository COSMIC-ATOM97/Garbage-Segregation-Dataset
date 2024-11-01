import os

# Path to the directory containing the images
directory = 'Garbage\original_images\cardboard'

# Start numbering from 595
start_num = 595

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename starts with 'cardboard_'
    if filename.startswith('cardboard_'):
        # Create the new filename by replacing 'cardboard_' with 'paper_' and adding the new number
        new_filename = f'paper_{start_num:03d}' + os.path.splitext(filename)[1]  # Retain the original file extension
        
        # Get the full file path for the old and new filenames
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)

        print(f'Renamed: {filename} -> {new_filename}')
        
        # Increment the numbering for the next file
        start_num += 1

print('Renaming completed!')
