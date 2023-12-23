from discord_webhook import DiscordWebhook, DiscordEmbed
from poll_config import RedditConfig, DiscordConfig, BASE_TEXT
import praw
from typing import Optional


def get_meme(reddit_config: RedditConfig):
    """[summary]

    Returns:
        [type]: [description]
    """
    reddit = praw.Reddit(
        client_id=reddit_config.username,
        client_secret=reddit_config.secret,
        password=reddit_config.password,
        user_agent=reddit_config.useragent,
        username=reddit_config.username,
    )
    subreddit = reddit.subreddit(reddit_config.sub)
    posts = subreddit.top("week")
    post = next(posts)
    image = post.url
    title = post.title
    link = post.permalink
    if link[:3].lower() == "/r/":
        link = "https://reddit.com" + link

    meme = DiscordEmbed(title=title, url=link)
    meme.set_image(url=image)
    return meme


def lambda_handler(event: Optional[dict] = None, context: Optional[dict] = None):
    if event["source"] == "local":
        env_file = "C:/Users/jon_h/Documents/Codes/TuningFork/.env"
    else:
        env_file = None

    reddit_config = RedditConfig(
        _env_file=env_file,
        _env_prefix="REDDIT_",
        _case_sensitive=False,
    )

    discord_config = DiscordConfig(
        _env_file=env_file,
        _env_prefix="DISCORD_",
    )

    webhook = DiscordWebhook(url=discord_config.webhook_url, content=BASE_TEXT)
    embed = get_meme(reddit_config)
    webhook.add_embed(embed)
    response = webhook.execute()


if __name__ == "__main__":
    event = {"source": "local"}
    lambda_handler(event=event)
