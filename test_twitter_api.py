import tweepy
import yaml

# Load credentials from YAML file
with open('config/credentials.yaml', 'r') as file:
    creds = yaml.safe_load(file)['api']

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    creds['api_key'],
    creds['api_key_secret'],
    creds['access_token'],
    creds['access_token_secret']
)
api = tweepy.API(auth)

try:
    # Verify credentials
    api.verify_credentials()
    print("Authentication successful!")
    # Fetch and print 5 recent tweets containing $TSLA
    for tweet in tweepy.Cursor(api.search_tweets, q="$TSLA", lang="en", tweet_mode="extended").items(5):
        print(f"{tweet.created_at} | @{tweet.user.screen_name}: {tweet.full_text[:100]}...")
except Exception as e:
    print(f"Error during authentication or fetching tweets: {e}")
