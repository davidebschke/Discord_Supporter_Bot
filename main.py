from discord.ext import commands

from groupFeatures.member_join_system import DiscordToken, bot

if __name__ == "__main__":
   if DiscordToken:
       bot.run(DiscordToken)
   else:
       print("FEHLER: Kein Token in der .env Datei gefunden!")