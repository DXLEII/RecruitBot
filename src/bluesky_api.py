import logging
from atproto import Client


from config import BLUESKY_USERNAME, BLUESKY_PASSWORD

# BlueSky API URLs
bluesky_auth_url = "https://bsky.social/xrpc/com.atproto.server.createSession"
bluesky_post_url = "https://bsky.social/xrpc/com.atproto.repo.createRecord"

def get_bluesky_client():
    client = Client(base_url='https://bsky.social/xrpc')
    client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)
    return client

def post_to_bluesky(message):
    try:
        client = get_bluesky_client()
        post = client.send_post(message)
        logging.info(f"Successfully posted to BlueSky: {message}")
    except Exception as e:
        logging.error(f"Error posting to BlueSky: {e}")

def get_bluesky_access_token():
    try:
        client = get_bluesky_client()
        return client.get_access_token()
    except Exception as e:
        logging.error(f"Error getting BlueSky access token: {e}")
        return None

