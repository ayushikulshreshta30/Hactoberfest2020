import time
import requests

quotes=['When the angels ask what I most loved about life, I’ll say you',
        'Love isn’t complicated, people are',
        'I will never regret loving you, only believing you loved me too',
        'Your cute smile is all I need to battle all struggles in my life.',
        'One Boy- Thousand Feelings',
        'Some love one, some love two. I love one that is you',
        'I am catastrophically in love with you',
        'Kiss me, and you may see stars, love me and I will give them to you.',
        'Close your eyes and I’ll kiss you, Tomorrow I’ll miss you',
        'Love is heat. You are sweet. When two Lips are meet. Love is completed.',
        'Dreams do come true, I know, because I found you',
        'Like the ocean finds the shore, I’ll always find you',
        'You are my sun, my moon and all my stars!']

print(quotes)
for quote in quotes:
  print(quote)
  base_url='https://api.telegram.org/bot1287485128:AAGGVxcj6yKOgffHBPp8ibZxN79ZQkJiTqI/sendMessage?chat_id=-1001289065791&text="{}"'.format(quote)

  print(base_url)
  requests.get(base_url)
  time.sleep(15)
