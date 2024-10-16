import json
from yars.yars import YARS
from yars.utils import display_results, download_image

# Initialize the YARS Reddit miner
miner = YARS()
filename = "subreddit_data3.json"


# Function to display search results, subreddit posts, and user data
def display_data(miner, subreddit_name, reddit_username, limit=search_limit, time_setting):
    search_results = miner.search_reddit(reddit_search, limit=search_limit)
    display_results(search_results, "SEARCH")

    # Scrape post details for a specific permalink
    permalink = permalink_name.split("reddit.com")[1]
    post_details = miner.scrape_post_details(permalink)
    if post_details:
        display_results(post_details, "POST DATA")
    else:
        print("Failed to scrape post details.")

# Scrape user data
def scrape_user_data(reddit_username="", limit=5):
    user_data = miner.scrape_user_data(reddit_username, limit=userdata_limit)
    display_results(user_data, "USER DATA")

             
# Scrape top posts from a subreddit
def scrape_subreddit_or_user(reddit_username, subredditname, subreddit_or_user="subreddit", limit=5, category="new", time_setting="week"): 
    if subreddit_or_user == "user":
        subreddit_posts = miner.fetch_subreddit_posts(reddit_username, limit=limit, category=subreddit_category, time_filter=time_setting)
    else:
        subreddit_posts = miner.fetch_subreddit_posts(subreddit_name, limit=limit, category=subreddit_category, time_filter=time_setting)
    display_results(subreddit_posts, "Posts")
    # Attempt to download images from specified number of posts
    for idx, post in enumerate(subreddit_posts[:dl_images]):
        try:
            image_url = post.get("image_url", post.get("thumbnail_url", ""))
            if image_url:
                download_image(image_url)
        except Exception as e:
            print(f"Error downloading image from post {idx}: {e}")


# Function to scrape subreddit post details and comments and save to JSON
def scrape_subreddit_to_json(subreddit_name, limit=5, time_setting="all", subreddit_category="new", filename=filename):
    try:
        subreddit_posts = miner.fetch_subreddit_posts(
            subreddit_name, limit=limit, category=subreddit_category, time_filter=time_setting
        )

        # Load existing data from the JSON file, if available
        try:
            with open(filename, "r") as json_file:
                existing_data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Scrape details and comments for each post
        for i, post in enumerate(subreddit_posts, 1):
            permalink = post["permalink"]
            post_details = miner.scrape_post_details(permalink)
            print(f"Processing post {i}")

            if post_details:
                post_data = {
                    "title": post.get("title", ""),
                    "author": post.get("author", ""),
                    "created_utc": post.get("created_utc", ""),
                    "num_comments": post.get("num_comments", 0),
                    "score": post.get("score", 0),
                    "permalink": post.get("permalink", ""),
                    "image_url": post.get("image_url", ""),
                    "thumbnail_url": post.get("thumbnail_url", ""),
                    "body": post_details.get("body", ""),
                    "comments": post_details.get("comments", []),
                }

                # Append new post data to existing data
                existing_data.append(post_data)

                # Save the data incrementally to the JSON file
                save_to_json(existing_data, filename)
            else:
                print(f"Failed to scrape details for post: {post['title']}")

    except Exception as e:
        print(f"Error occurred while scraping subreddit: {e}")


# Function to save post data to a JSON file
def save_to_json(data, filename=filename):
    try:
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to JSON file: {e}")


# Main execution / Settings
if __name__ == "__main__":

    #Not sure what all the options are - possibly now, today, week, year, all
    time_setting ="all"
    
    #name for the subreddit and/or user we will be working with
    subreddit_name = "mildlyinfuriating"
    reddituser_name = "redditor's username"
    
    #Do a simple reddit search
    do_search = true
    reddit_search = "heartwarming news"
    search_limit = 5

    #Scrape post details from a reddit permalink
    do_permalink = true
    permalink_name = "https://www.reddit.com/r/OneOrangeBraincell/comments/1g4go9v/this_is_his_face_every_time_i_leave_the_house/"

    #Scrape a subreddit or user for posts
    do_subreddit_or_user = true
    #Number of posts to scrape
    posts limit = 5
    #Number of images to download from the scrape
    image_limit = 50
    #Choose if the scrape is for a user or a subreddit
    subreddit_or_user = "subreddit"
    #Scrape categories, for subreddit use 'new', 'hot', or 'top' - for user use 'usernew', 'userhot', or 'usertop'
    subreddit_category = "new"
        
    #Scrape basic user data / posts limit
    do_userdata = true
    userdata_limit = 5

    #scrape subreddit to json file / posts limit
    do_json = true
    json_limit = 5
    
    # Display data for various functionalities
    if 
    display_data(miner, subreddit_name, reddituser_name, limit=posts_limit, time_setting)
    
    # Scrape and save subreddit post data to JSON
    if do_json:
        scrape_subreddit_data(subreddit_name, json_limit, time_setting, subreddit_category)

    if do_subreddit_or_user:
        scrape_subreddit_or_user(reddit_username, subreddit_name, subreddit_or_user, subreddit_category, post_limit, image_limit, time_setting)

    if do_userdata:
        
