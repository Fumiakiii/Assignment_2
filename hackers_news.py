import requests
import time


def main():
    ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:30]

    for id in ids:
        story_info = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json").json()
        if "url" not in story_info:
            continue

        title = story_info["title"]
        url = story_info["url"]

        print(f"Title: {title}\nURL: {url}\n")
        time.sleep(1)


if __name__ == "__main__":
    main()
