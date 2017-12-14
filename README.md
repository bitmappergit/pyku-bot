# pyku-bot
A discord bot that polices haiku channels and deletes incorrect haikus.

This will be accurate almost 99.9% of the time. It uses a pronunciation dictionary for all common and semi-uncommon words (not including names and brands) and uses a Regex to guess how many syllables are in the word if the word is not in the dictionary.

* Required Libraries:
  * Natural Language Tool Kit (NLTK)
  * discord.py
