import os
import json
import discord
import datetime
from info import Info
from discord.ext import commands

class Show(commands.Cog):
    def __init__(self, bot: commands.Bot, info: Info):
        self.bot = bot

        self.info_obj = info
    
    @commands.command()
    @commands.has_role("Executives")
    async def showpuzz(self, ctx: commands.context.Context):
        puzz_info = self.info_obj.info["puzz"]
        puzz_text = self.info_obj.get_puzz_text(ctx, False)
        puzz_time = puzz_info["release_datetime"]
        puzz_channel = puzz_info["channel_id"]

        await ctx.send(f"The following will be released at {puzz_time} in <#{puzz_channel}>.")
        await ctx.send(puzz_text)
        for i in range(len(puzz_info["img_urls"])):
            await ctx.send(puzz_info["img_urls"][i])

    @commands.command()
    @commands.has_role("Executives")
    async def showsb(self, ctx: commands.context.Context):
        sb_info = self.info_obj.info["sb"]
        sb_text = self.info_obj.get_sb_text(ctx, False)
        sb_time = sb_info["release_datetime"]
        sb_channel = sb_info["channel_id"]

        await ctx.send(f"The following will be released at {sb_time} in <#{sb_channel}>.")
        await ctx.send(sb_text)

    @commands.command()
    @commands.has_role("Executives")
    async def showciyk(self, ctx: commands.context.Context):
        ciyk_info = self.info_obj.info["ciyk"]
        ciyk_text = self.info_obj.get_ciyk_text(ctx, False)
        ciyk_time = ciyk_info["release_datetime"]
        ciyk_channel = ciyk_info["channel_id"]

        await ctx.send(f"The following will be set at {ciyk_time} in <#{ciyk_channel}>.")
        await ctx.send(ciyk_text)

def setup(bot: commands.Bot):
    info = Info()
    bot.add_cog(Show(bot, info))