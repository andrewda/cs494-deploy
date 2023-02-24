import json
import os

if __name__ == '__main__':
  # Read and parse assignments.json file
  with open('assignments.json') as f:
    assignments = json.load(f)

  # Create build and repos directories
  os.system('mkdir -p build repos')

  # Create a directory for each assignment
  for assignment in assignments:
    clone_path = f'"repos/{assignment["name"]}"'
    build_path = f'"build/{assignment["name"]}"'

    # Get GitHub username and password from environment variables
    user = os.environ['GITHUB_USER']
    token = os.environ['GITHUB_PAT']

    # public_url = os.environ['PUBLIC_URL']
    public_url = f'https://dassonville.dev/cs494-deploy/{assignment["name"]}'
    basename = f'/cs494-deploy/{assignment["name"]}'

    # Clone repository with git:
    os.system(f'git clone https://{user}:{token}@github.com/{assignment["repo"]} {clone_path}')

    # CD into the cloned repository, install depeodencies and run build script
    os.system(f'cd {clone_path} && npm install && PUBLIC_URL={public_url} REACT_APP_BASENAME={basename} npm run build')

    # Copy the build folder to the build directory
    os.system(f'cp -r {clone_path}/build {build_path}')
