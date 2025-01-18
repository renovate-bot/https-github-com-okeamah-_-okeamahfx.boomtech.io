import requests
import base64
import json

# Replace with your GitHub details
GITHUB_TOKEN = 'your_github_token'
REPO_OWNER = 'DAVID OKEAMAH'  # Your GitHub username
REPO_NAME = 'Okeamahfx.boomtech.io'  # Your repository name
FILE_PATH = 'path_to_your_file.txt'  # Path to the file you want to upload
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/'

# Function to create and upload a file to GitHub repository
def create_and_upload_file(file_path, file_name, commit_message):
    # Open the file and read its contents
    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    # Encode the content in base64 (GitHub API requires base64 encoding for file contents)
    encoded_content = base64.b64encode(file_content).decode('utf-8')
    
    # Define the payload for the GitHub API request
    data = {
        'message': commit_message,  # Commit message
        'content': encoded_content,  # Base64 encoded file content
        'branch': 'main'  # Or any other branch you want to upload the file to
    }
    
    # API request headers
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # GitHub API URL for creating/uploading file
    url = GITHUB_API_URL + file_name

    # Make the API request to upload the file
    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        print(f'File uploaded successfully to {file_name}')
    else:
        print(f'Failed to upload file. Status code: {response.status_code}')
        print(response.json())

# Usage example
file_name = 'uploaded_file.txt'  # Name you want for the file on GitHub
commit_message = 'Initial commit: Upload file'

create_and_upload_file(FILE_PATH, file_name, commit_message)
