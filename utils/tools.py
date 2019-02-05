from collections import OrderedDict

import discord

from settings.config import VOICE_CHANNEL_DIVIDER
import more_itertools


# If we get an array of 2 (or more, somehow) then it's splittable
from settings.constants import INFO_COLOR, ERROR_COLOR


def splittable(name):
    return len(name.split(" {} ".format(VOICE_CHANNEL_DIVIDER))) >= 2


# "Name | Lang" -> "Name"
def get_original_name(name):
    return name.split(" {} ".format(VOICE_CHANNEL_DIVIDER))[0]


# Return true if the bot has "manage channel" permission, otherwise false
def can_edit_channel(bot, channel):
    return channel.permissions_for(channel.server.get_member(bot.user.id)).manage_channels


# Return true if given user in VC
def user_in_vc(user, vc):
    if user is None or vc is None:
        return False
    return True


# Divides list into N evenly-sized chunks
def create_chunks(list_to_divide, number_of_chunks):
    return [list(c) for c in more_itertools.divide(number_of_chunks, list_to_divide)]


# Add a … symbol if the is longer than "limit"
def add_dots(string, limit):
    # "…" " " - 3 dots + 2x unbreakable spaces (alt+0160)
    return (string[:limit] + '…  ') if len(string) > limit else string


# Just a convenient way to make error boxes
def error_embed(message):
    embed = discord.Embed(description=message, colour=discord.Colour(ERROR_COLOR))
    return embed

# Just a convenient way to make info boxes
def info_embed(message):
    embed = discord.Embed(description=message, colour=discord.Colour(INFO_COLOR))
    return embed


def make_role_list(input_str):
    # Dividing roles to a list, removing unnecessary spaces and making it lowercase
    # "  native english,    fluent english " -> ["native english", "fluent english"]
    result = [role.strip().lower() for role in " ".join(input_str).split(",") if role.strip() != ""]
    return list(OrderedDict.fromkeys(result))


def get_role(server, role_name):
    return discord.utils.find(lambda m: m.name.lower() == role_name.lower(), server.roles)
