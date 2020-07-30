from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Chatbot')

conversa = ['oi','olá']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot:não tenho certeza..:',resposta)



