import os

# Set the path to the directory containing your images
directory = "images"  # Change this to the directory containing your images

# List all files in the directory
files = os.listdir(directory)

# Filter to only include image files (optional: can be expanded to other formats)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Sort the image files alphabetically (optional)
image_files.sort()

# Rename the files
for idx, filename in enumerate(image_files, start=1):
    # Create new name, e.g., house1, house2, etc.
    new_name = f"house{idx}{os.path.splitext(filename)[1]}"
    
    # Get the full path for the old and new filenames
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")

print("Renaming completed!")
