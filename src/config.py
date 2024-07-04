import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Extract necessary configurations from .env
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
BLUESKY_USERNAME = os.getenv('BLUESKY_USERNAME', '')
BLUESKY_PASSWORD = os.getenv('BLUESKY_PASSWORD', '')
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', '20'))  
STAR_INCREMENT = int(os.getenv('STAR_INCREMENT', '1'))   
OWNER = os.getenv('OWNER', 'DXLEII')
REPO = os.getenv('REPO', 'RecruitBot')