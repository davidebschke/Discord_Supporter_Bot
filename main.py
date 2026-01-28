from discord.ext import commands

from groupFeatures.memberJoinSystem import DiscordToken, bot

if __name__ == "__main__":
   if DiscordToken:
       bot.run(DiscordToken)
   else:
       print("FEHLER: Kein Token in der .env Datei gefunden!")