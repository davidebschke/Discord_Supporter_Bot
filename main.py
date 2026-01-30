from groupFeatures.member_join_system import DiscordToken, bot

if __name__ == "__main__": # NOSONAR
   if DiscordToken:
       bot.run(DiscordToken)
   else:
       print("FEHLER: Kein Token in der .env Datei gefunden!")