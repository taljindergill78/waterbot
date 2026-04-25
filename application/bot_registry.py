from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BotConfig:
    bot_id: str
    display_name: str
    persona_prompt: str
    chatbot_type: str
    legacy_page: str
    enabled: bool = True


RELATIONAL_BOTS: dict[str, BotConfig] = {
    "riverbot": BotConfig(
        bot_id="riverbot",
        display_name="RiverBot",
        persona_prompt="You are River. Answer as a river would.",
        chatbot_type="riverbot",
        legacy_page="riverbot.html",
    ),
    "oceanbot": BotConfig(
        bot_id="oceanbot",
        display_name="OceanBot",
        persona_prompt="You are Ocean. Answer as an ocean would.",
        chatbot_type="oceanbot",
        legacy_page="oceanbot.html",
    ),
    "mountainbot": BotConfig(
        bot_id="mountainbot",
        display_name="MountainBot",
        persona_prompt="You are Mountain. Answer as a mountain would.",
        chatbot_type="mountainbot",
        legacy_page="mountainbot.html",
    ),
}


def get_relational_bot(bot_id: str) -> BotConfig | None:
    config = RELATIONAL_BOTS.get((bot_id or "").lower())
    if not config or not config.enabled:
        return None
    return config
