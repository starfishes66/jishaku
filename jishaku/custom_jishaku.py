from discord.ext import commands
from jishaku.cog import Jishaku

OWNER_IDS = {1387121510505779253, 1277604006901846109, 1155891693577572372, 1375433723083755590}

class OwnerOnlyJishaku(Jishaku):
    """Custom Jishaku restricted to owners."""

    def __init__(self, bot: commands.Bot):
        # Important: pass the bot to the superclass
        super().__init__(bot)
        self.bot = bot  # ensures self.bot exists

    async def cog_check(self, ctx: commands.Context):
        # Only allow owners
        return ctx.author.id in OWNER_IDS
        
