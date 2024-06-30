This is a bot designed to help market yourself on social media accounts. 

This project will use github API alongside Bluesky api so that your bluesky account can automatically create posts when your github account reaches a certain milestone set by the user and provide updates on any git repository like when you make a push and instantly create a posts to social media to celebrate and help market your own milestones. 

This project is currently in development and has plans to go beyond just whats mentioned above. 

## SETUP

1. **Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables:

     ```
     GITHUB_TOKEN=your_github_api_token
     OWNER=your_github_username
     REPO=your_repository_name
     CHECK_INTERVAL=60
     STAR_INCREMENT=10
     ```

2. **GitHub API Token**:
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
   - Click on `Generate new token`.
   - Select the scopes required, typically `repo` for repository access.
   - Copy the generated token and paste it as `GITHUB_TOKEN` in your `.env` file.

## Usage

Once the .env has been configured you can now run the python script app.py.