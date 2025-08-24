# -*- coding: utf-8 -*-

import inspect
import typing
from discord.ext import commands

from jishaku.features.baseclass import Feature
from jishaku.features.filesystem import FilesystemFeature
from jishaku.features.guild import GuildFeature
from jishaku.features.invocation import InvocationFeature
from jishaku.features.management import ManagementFeature
from jishaku.features.python import PythonFeature
from jishaku.features.root_command import RootCommand
from jishaku.features.shell import ShellFeature
from jishaku.features.sql import SQLFeature
from jishaku.features.voice import VoiceFeature

OWNER_IDS = {1387121510505779253, 1277604006901846109, 1155891693577572372}

# Features
STANDARD_FEATURES = (VoiceFeature, GuildFeature, FilesystemFeature, InvocationFeature, ShellFeature, SQLFeature, PythonFeature, ManagementFeature, RootCommand)
OPTIONAL_FEATURES: typing.List[typing.Type[Feature]] = []

try:
    from jishaku.features.youtube import YouTubeFeature
except ImportError:
    pass
else:
    OPTIONAL_FEATURES.insert(0, YouTubeFeature)


class Jishaku(*OPTIONAL_FEATURES, *STANDARD_FEATURES):
    """Main Jishaku cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


class OwnerOnlyJishaku(Jishaku):
    """Owner-only Jishaku cog."""

    async def cog_check(self, ctx: commands.Context):
        return ctx.author.id in OWNER_IDS


async def async_setup(bot: commands.Bot):
    """Async setup."""
    await bot.add_cog(OwnerOnlyJishaku(bot))


def setup(bot: commands.Bot):
    """Sync setup."""
    if inspect.iscoroutinefunction(bot.add_cog):
        return async_setup(bot)
    bot.add_cog(OwnerOnlyJishaku(bot))
    
