import discord
 
class Bot(discord.Client):
    server = None
    welcome = None
 
    def suffix_gen(self, number):
        tld = number % 100
        ld = number % 10
        if ld == 1 and tld != 11:
            return 'st'
        if ld == 2 and tld != 12:
            return 'nd'
        if ld == 3 and tld != 13:
            return 'rd'
        return 'th'
 
    async def on_ready(self):
        self.server = self.get_guild(568448415793676299)
        self.welcome = self.get_channel(568452409421201418)
 
    async def on_member_join(self, member):
        await self.welcome.send('Welcome %(username)s to **Spirit - Support Server**. You are the **%(number)i%(suffix)s** member on the server.' %
        {'username': member.mention, 'number': self.server.member_count, 'suffix': self.suffix_gen(self.server.member_count)})
 
bot = Bot()
bot.run('token')
