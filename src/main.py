import time
import logging
from github_api import get_latest_commit_sha, get_stars_count
from bluesky_api import post_to_bluesky
from config import CHECK_INTERVAL, STAR_INCREMENT, OWNER, REPO

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info(f"Starting monitoring of GitHub repository: {OWNER}/{REPO}")
    logging.info(f"Check interval: {CHECK_INTERVAL} seconds")
    logging.info(f"Star increment threshold: {STAR_INCREMENT}")

    # Initialize variables to track initial state
    initial_stars_count = get_stars_count()
    initial_commit_sha = get_latest_commit_sha()

    if initial_stars_count is not None:
        initial_message = f"RecruitBot is now automatically tracking {OWNER}/{REPO}. This repository currently has {initial_stars_count} stars."
        logging.info(f"Initial message: {initial_message}")
        post_to_bluesky(initial_message)
    
    try:
        while True:
            logging.info("Resting...")
            time.sleep(5)  # Simulate resting period
            
            logging.info("Polling GitHub data...")
            current_stars_count = get_stars_count()
            current_commit_sha = get_latest_commit_sha()
            
            # Log the current stars count and check against initial stars count
            logging.info(f"Current stars count: {current_stars_count}, Initial stars count: {initial_stars_count}")

            # Check if stars count has changed
            if current_stars_count != initial_stars_count:
                stars_change = current_stars_count - initial_stars_count
                logging.info(f"Detected change in stars: {initial_stars_count} -> {current_stars_count}")
                if stars_change >= STAR_INCREMENT:  
                    message = f"{OWNER}/{REPO} has reached {current_stars_count} stars."
                    logging.info(message)
                    post_to_bluesky(message)
                    initial_stars_count = current_stars_count  # Update initial stars count
            
            # Check if there's a new commit
            if current_commit_sha != initial_commit_sha:
                message = f"New commit just published on {OWNER}/{REPO}. Commit SHA: {current_commit_sha}"
                logging.info(message)
                post_to_bluesky(message)
                initial_commit_sha = current_commit_sha  # Update initial commit SHA
            
            logging.info("Back to resting...")
            time.sleep(CHECK_INTERVAL - 5)  # Subtracting the resting time from the check interval

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")

if __name__ == "__main__":
    main()
