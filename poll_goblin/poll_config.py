from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class RedditConfig(BaseSettings):
    id: str
    secret: str
    password: str
    useragent: str
    username: str
    sub: Optional[str] = "dndmemes"


class DiscordConfig(BaseSettings):
    webhook_url: str
    token: str
    channel: int


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
