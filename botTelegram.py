#https://www.youtube.com/watch?v=2TCkaJdcicQ Passo a passo criar bot
import telepot
from pprint import pprint

# Bot telegram
chave = 'AUTENTICAÇÃO BOT'
bot = telepot.Bot(chave)
resposta = bot.getUpdates()

pprint(resposta)
#bot.sendMessage(-0000000, 'aksjdklajsdlkjaskldjaksljdklajskd')

