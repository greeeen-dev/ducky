# ducky's quack hammer (aka moderation commands)

import discord
from discord.ext import commands

def timetoint(t,timeoutcap=False):
    try:
        return int(t)
    except:
        pass
    if not type(t) is str:
        t = str(t)
    total = 0
    t = t.replace('mo','n')
    if t.count('n')>1 or t.count('d')>1 or t.count('h')>1 or t.count('m')>1 or t.count('s')>1:
        raise ValueError('each identifier should never recur')
    t = t.replace('n','n ').replace('d','d ').replace('h','h ').replace('m','m ').replace('s','s ')
    times = t.split()
    for part in times:
        if part.endswith('n'):
            multi = int(part[:-1])
            if timeoutcap:
                total += (2419200 * multi)
            else:
                total += (2592000 * multi)
        elif part.endswith('d'):
            multi = int(part[:-1])
            total += (86400 * multi)
        elif part.endswith('h'):
            multi = int(part[:-1])
            total += (3600 * multi)
        elif part.endswith('m'):
            multi = int(part[:-1])
            total += (60 * multi)
        elif part.endswith('s'):
            multi = int(part[:-1])
            total += (multi)
        else:
            raise ValueError('invalid identifier')
    return total

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command('quack')
    async def mute(self,ctx,user,duration,reason=''):
        msgparts = ctx.message.content.split()
        msgparts.pop(0)
        msgparts.pop(0)
        msgparts.pop(0)
        if not len(msgparts)==0:
            reason = ' '.join(msgparts)
        try:
            target1 = user.replace('<@', '')
            target1 = target1.replace('!', '')
            target1 = target1.replace('>', '')
            target1 = int(target1)
            await ctx.guild.query_members(limit=1, user_ids=[target1], cache=True)
            target = ctx.guild.get_member(target1)
            try:
                if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.moderate_members:
                    if ctx.author.id==target1:
                        return await ctx.send('**quack...**\nquack quack...quack (you cannot mute yourself)')
                    if ctx.author.top_role > target.top_role:
                        import datetime
                        ct = datetime.datetime.utcnow().timestamp()
                        try:
                            toadd = timetoint(duration,timeoutcap=True)
                        except:
                            return await ctx.send('**quack...**\nquack quack quack... (i can\'t understad the mute duration. please give it in the form of \'1d2h\', \'1mo\', \'1h\', \'6d9h4m20s\', etc.)')
                        if toadd > 2419200:
                            return await ctx.send('**quack...**\nquack! (i can\'t mute someone for more than 28 days)')
                        et = datetime.datetime.fromtimestamp(ct + toadd)
                        if reason=='':
                            action_reason = 'no reason given'
                        else:
                            action_reason = reason
                        await target.edit(communication_disabled_until=et,reason=f'quack\'d by moderator {ctx.author} - {action_reason}')
                        return await ctx.send(f'**Quack!**\nquack\'d {target}')
                    else:
                        return await ctx.send('**quack...**\nquack quack...quack quack (you cannot mute someone with a higher role)')
                else:
                    return await ctx.send('**quack...**\nq u a c k . (no permissions. nice try.)')
            except:
                return await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')
        except:
            raise

    @mute.error
    async def svr_mute_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f'**quack...**\nquack quack??? (some argument seems to be missing. it\'s probably `<{error.param}>`)')
        else:
            await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')

    @commands.command(name="quackn't", aliases=["unquack"])
    async def unmute(self,ctx,user,reason=''):
        msgparts = ctx.message.content.split()
        msgparts.pop(0)
        msgparts.pop(0)
        if not len(msgparts)==0:
            reason = ' '.join(msgparts)
        try:
            target1 = user.replace('<@', '')
            target1 = target1.replace('!', '')
            target1 = target1.replace('>', '')
            target1 = int(target1)
            await ctx.guild.query_members(limit=1, user_ids=[target1], cache=True)
            target = ctx.guild.get_member(target1)
            try:
                if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.moderate_members:
                    if ctx.author.id==target1:
                        return await ctx.send('**quack...**\nquack quack...quack (you cannot unmute yourself)')
                    if ctx.author.top_role > target.top_role:
                        if target.communication_disabled_until==None:
                            return await ctx.send('**quack...**\nquack quack...quack quack? (this person isn\'t muted?)')
                        if reason=='':
                            action_reason = 'no reason given'
                        else:
                            action_reason = reason
                        await target.edit(communication_disabled_until=None,reason=f'unquack\'d by {ctx.author} - {action_reason}')
                        return await ctx.send(f'**Quack!**\nunquack\'d {target}')
                    else:
                        return await ctx.send('**quack...**\nquack quack...quack quack (you cannot unmute someone with a higher role)')
                else:
                    return await ctx.send('**quack...**\nq u a c k . (no permissions. nice try.)')
            except:
                return await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')
        except:
            raise

    @unmute.error
    async def unmute_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f'**quack...**\nquack quack??? (some argument seems to be missing. it\'s probably `<{error.param}>`)')
        else:
            return await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')

    @commands.command(name="QUACK")
    async def quackhammer(self,ctx,user,reason=''):
        msgparts = ctx.message.content.split()
        msgparts.pop(0)
        msgparts.pop(0)
        if not len(msgparts)==0:
            reason = ' '.join(msgparts)
        try:
            target1 = user.replace('<@', '')
            target1 = target1.replace('!', '')
            target1 = target1.replace('>', '')
            target1 = int(target1)
            await ctx.guild.query_members(limit=1, user_ids=[target1], cache=True)
            target = ctx.guild.get_member(target1)
            try:
                if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.moderate_members:
                    if ctx.author.id==target1:
                        return await ctx.send('**quack...**\nquack quack...quack (you cannot kick/ban yourself)')
                    if ctx.author.top_role > target.top_role:
                        if reason=='':
                            action_reason = 'no reason given'
                        else:
                            action_reason = reason
                        lst = []
                        ButtonStyle = discord.ButtonStyle
                        lst.append(discord.ui.Button(style=ButtonStyle.grey, label="quack", custom_id='noquack'))
                        lst.append(discord.ui.Button(style=ButtonStyle.blurple, label="Quack", custom_id='quackem'))
                        lst.append(discord.ui.Button(style=ButtonStyle.red, label="QUACK", custom_id='quackhammer'))
                        btns = discord.ui.ActionRow(lst[0],lst[1],lst[2])
                        msg = await ctx.send("quack quack?",components=discord.ui.MessageComponents(btns))
                        lst = []
                        def check(interaction):
                            return interaction.user.id==ctx.author.id and interaction.message.id==msg.id
                        try:
                            interaction = await self.bot.wait_for("component_interaction", check=check, timeout=30.0)
                        except:
                            lst.append(discord.ui.Button(style=ButtonStyle.grey, label="quack", custom_id='noquack',disabled=True))
                            lst.append(discord.ui.Button(style=ButtonStyle.blurple, label="Quack", custom_id='quackem',disabled=True))
                            lst.append(discord.ui.Button(style=ButtonStyle.red, label="QUACK", custom_id='quackhammer',disabled=True))
                            btns = discord.ui.ActionRow(lst[0],lst[1],lst[2])
                            await interaction.response.edit_message(content="quack quack?",components=discord.ui.MessageComponents(btns))
                            return await ctx.send("quack (never mind i guess)")
                        lst.append(discord.ui.Button(style=ButtonStyle.grey, label="quack", custom_id='noquack',disabled=True))
                        lst.append(discord.ui.Button(style=ButtonStyle.blurple, label="Quack", custom_id='quackem',disabled=True))
                        lst.append(discord.ui.Button(style=ButtonStyle.red, label="QUACK", custom_id='quackhammer',disabled=True))
                        btns = discord.ui.ActionRow(lst[0],lst[1],lst[2])
                        await interaction.response.edit_message(content="quack quack?",components=discord.ui.MessageComponents(btns))
                        if interaction.component.custom_id=='noquack':
                            return await ctx.send('quack. (no quack then i guess)')
                        elif interaction.component.custom_id=='quackem':
                            await target.kick(reason=f'Quack\'d {ctx.author} - {action_reason}')
                            return await ctx.send(f'**quack quack quack**\nQuack\'d {target}')
                        if interaction.component.custom_id=='quackhammer':
                            await target.ban(delete_message_days=0,reason=f'QUACK\'d {ctx.author} - {action_reason}')
                            return await ctx.send(f'**QUACK QUACK QUACK <:duckyban:1072571104264204288>**\nQUACK\'d {target}')
                    else:
                        return await ctx.send('**quack...**\nquack quack...quack quack (you cannot kick/ban someone with a higher role)')
                else:
                    return await ctx.send('**quack...**\nq u a c k . (no permissions. nice try.)')
            except:
                return await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')
        except:
            raise

    @quackhammer.error
    async def quack_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f'**quack...**\nquack quack??? (some argument seems to be missing. it\'s probably `<{error.param}>`)')
        else:
            await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')

    @commands.command(name="QUACKn\'t", aliases=["unQUACK"])
    async def unquackhammer(self,ctx,user,reason=''):
        msgparts = ctx.message.content.split()
        msgparts.pop(0)
        msgparts.pop(0)
        if not len(msgparts)==0:
            reason = ' '.join(msgparts)
        try:
            target2 = user
            target1 = user.replace('<@', '')
            target1 = target1.replace('!', '')
            target1 = target1.replace('>', '')
            try:
                if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.ban_members:
                    if ctx.author.id==target1:
                        return await ctx.send('**quack...**\nquack quack...quack (you cannot unban yourself)')
                    if reason=='':
                        action_reason = 'no reason given'
                    else:
                        action_reason = reason
                    banlist = await ctx.guild.bans()
                    for ban in banlist:
                        userid = '%s' % ban.user.id
                        if target1 in ban.user.name:
                            user = ban.user
                            break
                        if target1 in userid:
                            user = ban.user
                            break
                        if target2 in '%s' % ban.user:
                            user = ban.user
                            break
                    await ctx.guild.unban(user,reason=f'unQUACK\'d by {ctx.author} - {action_reason}')
                    return await ctx.send(f'**Quack!**\nunQUACK\'d {user}')
                else:
                    return await ctx.send('**quack...**\nq u a c k . (no permissions. nice try.)')
            except:
                return await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')
        except:
            raise

    @unquackhammer.error
    async def unquack_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f'**quack...**\nquack quack??? (some argument seems to be missing. it\'s probably `<{error.param}>`)')
        else:
            await ctx.send('**quack...**\nquack!!! (something went wrong. please check my permissions. if they\'re all good, check your parameters)')

def setup(bot):
    bot.add_cog(Moderation(bot))
