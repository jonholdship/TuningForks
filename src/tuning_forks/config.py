from pydantic_settings import BaseSettings


class DiscordConfig(BaseSettings):
    webhook_url: str
    token: str
    channel: int


discord_config = DiscordConfig(
    _env_file="C:/Users/jon_h/Documents/Codes/TuningForks/.env",
    _env_prefix="DISCORD_",
)
