from discord.ext import commands
from jishaku.cog import Jishaku

OWNER_IDS = {1387121510505779253, 1277604006901846109, 1155891693577572372, 1375433723083755590}


class OwnerOnlyJishaku(Jishaku):
    """Custom Jishaku restricted to owners."""

    async def cog_check(self, ctx: commands.Context):
        return ctx.author.id in OWNER_IDS
      
