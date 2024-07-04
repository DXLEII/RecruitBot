This is a bot designed to help market yourself on social media accounts. 

This project will use github API alongside Bluesky api so that your bluesky account can automatically create posts when your github account reaches a certain milestone set by the user and provide updates on any git repository like when you make a push and instantly create a posts to social media to celebrate and help market your own milestones. 

This project is currently in development and has plans to go beyond just whats mentioned above. 

### Environment Variables

1. **Create `.env` File**:
   - Create a `.env` file in the root directory of the project.

2. **Add Environment Variables**:
   - Add the following environment variables to your `.env` file:

     ```plaintext
     GITHUB_TOKEN=your_github_api_token
     OWNER=your_github_username
     REPO=your_repository_name
     CHECK_INTERVAL=60
     STAR_INCREMENT=10
     BLUESKY_USERNAME=username.bsky.social
     BLUESKY_PASSWORD=YOURAPPPASSWORD
     ```

   Replace placeholders (`your_github_api_token`, `your_github_username`, `your_repository_name`, `username.bsky.social`, `YOURAPPPASSWORD`) with your actual GitHub API token, username, repository name, Bluesky username, and Bluesky app password.

### GitHub API Token

1. **Generate GitHub API Token**:
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
   - Click on `Generate new token`.
   - Select the scopes required, typically `repo` for repository access.
   - Copy the generated token and paste it as `GITHUB_TOKEN` in your `.env` file.

### Bluesky App Password

1. **Generate Bluesky App Password**:
   - Bluesky requires an app-specific password for API access.
   - Navigate to the Bluesky API settings or profile settings where app passwords are managed.
   - Generate a new app password specifically for this project.
   - Copy the generated password and paste it as `BLUESKY_PASSWORD` in your `.env` file.

### Installing Requirements

1. **Install Python Packages**:
   - Make sure Python is installed on your system.
   - Navigate to the project directory in your terminal.
   - Install the required Python packages using pip:

     ```bash
     pip install -r requirements.txt
     ```

   This command installs all dependencies listed in the `requirements.txt` file.

## Running the Project

1. **Run the Python Script**:
   - Once the `.env` file is configured and dependencies are installed, you can run the Python script to start the project:

     ```bash
     python main.py
     ```
