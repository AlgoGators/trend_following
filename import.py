import requests
import os

# Base URL without the chapter number and file extension
base_url = "https://gitfront.io/r/user-4000052/iTvUZwEUN2Ta/AFTS-CODE/raw/chapter"

# Directory to save the downloaded chapters
save_dir = "downloaded_chapters"

# Make directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# array of needed chapters
# taking user input for the last chapter needed
last_chapter = int(input("Enter the last chapter needed: "))
# Loop through chapter numbers
for i in range(1, last_chapter + 1):
    # Construct the full URL for each chapter
    url = f"{base_url}{i}.py"
    
    # Make the GET request to download the file
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a file in the specified save directory
        filename = f"chapter{i}.py"
        filepath = os.path.join(save_dir, filename)
        
        with open(filepath, 'wb') as file:
            file.write(response.content)
        
        print(f"Downloaded {filename} successfully.")
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")

print("Download complete.")

