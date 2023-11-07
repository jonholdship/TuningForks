REDDIT_ID = "xxxxxxxxxx"
REDDIT_SECRET = "xxxxxxxxxx"
REDDIT_PASSWORD = "xxxxxxxxxx"
REDDIT_USERAGENT = "twoforksmemebot"
REDDIT_USERNAME = "twoforksmemebot"
REDDIT_SUB = "pathfindermemes"

WEBHOOK_URL = "your_discord_webhook"


DISCORD_TOKEN = "token_for_discord"
DISCORD_CHANNEL = DISCORD_CHANNEL_ID

DAYS = [
    ":crescent_moon: Monday",
    ":crossed_swords: Tuesday",
    ":eagle: Wednesday",
    ":hammer: Thursday",
    ":ring: Friday",
    ":ringed_planet: Saturday",
    ":sun_with_face: Sunday",
]

EMOJIS = [day.split(":")[1] for day in DAYS]
BASE_TEXT = (
    "**Another week, another poll. When are you available for Pathfinder this week?**\n"
)
BASE_TEXT += "\n".join(DAYS)

# tuning forks channel for testing
DISCORD_CHANNEL = 888739175958974504
