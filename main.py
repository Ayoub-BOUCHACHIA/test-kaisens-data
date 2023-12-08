
import argparse
import os
from crawler import crawl_page
from scraper import Post
from config_mongdb import get_cnx_database


def read_page():
    if os.path.exists('./results.html'):
        with open('./results.html', 'r', encoding='utf-8') as file_data:
            return file_data.read()
    return None

def scrape():
    # the endpoint for the posts lookup
    ENDPOINT = "https://www.facebook.com/"

    # Setting up the arg parser to parse argument when the script called 
    parser = argparse.ArgumentParser(prog="FACEBOOK COLLECTOR",description='Collect facebook posts related to a specific subject.')
    parser.add_argument("-s","--subject",default="le décès du président Jacques Chirac") # for subject selection 
    
    args = parser.parse_args()
    print(f"Starting Crawling Process for topic = {args.subject}")
    url = f"{ENDPOINT}/search/posts/?q={args.subject}"

    page_source = crawl_page(url) 

    return page_source



if __name__ == "__main__":

    print("Connecting to DB ...")
    db = get_cnx_database()

    page_source = read_page() or scrape()

    posts = Post.scrape_posts(page_source)
    print("Extracing and Saving data to DB ...", (posts))
    for post in posts:
        post.serialize() # serialize the object
        post.save(db) # save to the database DB

    print("Finished Successfully !")

