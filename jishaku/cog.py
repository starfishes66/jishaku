# -*- coding: utf-8 -*-

"""
jishaku.cog
~~~~~~~~~~~~

The Jishaku debugging and diagnostics cog implementation.

:copyright: (c) 2021 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

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
# jishaku/custom_cog.py

# Remove it entirely if you're defining Jishaku in this file
# or ensure you import Jishaku only from the right module, e.g.:
# if you put the original in another file



        

__all__ = (
    "Jishaku",
    "STANDARD_FEATURES",
    "OPTIONAL_FEATURES",
    "setup",
)

STANDARD_FEATURES = (VoiceFeature, GuildFeature, FilesystemFeature, InvocationFeature, ShellFeature, SQLFeature, PythonFeature, ManagementFeature, RootCommand)

OPTIONAL_FEATURES: typing.List[typing.Type[Feature]] = []

try:
    from jishaku.features.youtube import YouTubeFeature
except ImportError:
    pass
else:
    OPTIONAL_FEATURES.insert(0, YouTubeFeature)


class Jishaku(*OPTIONAL_FEATURES, *STANDARD_FEATURES):
    """The frontend subclass that mixes in to form the final Jishaku cog."""

    def __init__(self, bot: commands.Bot):
        # Pass the bot to all the mixins
        self.bot = bot
        super().__init__()
            


async def async_setup(bot: commands.Bot):
    """
    The async setup function defining the jishaku.cog and jishaku extensions.
    """

    await bot.add_cog(Jishaku(bot=bot))  # type: ignore


def setup(bot: commands.Bot):  # pylint: disable=inconsistent-return-statements
    """
    The setup function defining the jishaku.cog and jishaku extensions.
    """

    if inspect.iscoroutinefunction(bot.add_cog):
        return async_setup(bot)

    bot.add_cog(Jishaku(bot=bot))  # type: ignore[reportUnusedCoroutine]
    
