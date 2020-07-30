from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def ouvir_microfone():
	frase = ""
	microfone = sr.Recognizer()
	with sr.Microphone() as source:
		microfone.adjust_for_ambient_noise(source)
		print('Microfone...')
		audio = microfone.listen(source)
	try:
		frase = microfone.recognize_google(audio, language='pt-BR')
		print("Humano: "+frase)
	except sr.UnknownValueError:
		print('bot: Isso não funcionou')
	return frase


def cria_audio(audio):
	tts = gTTS(audio, lang="pt-BR")
	tts.save('bot.mp3')
	playsound('bot.mp3')


bot = ChatBot("Chatbot")

conversa = ['Oi', 'Ola']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
	try:
		quest = ouvir_microfone()
		if quest != "":
			resposta = bot.get_response(quest)
			if float(resposta.confidence) > 0.5:
				cria_audio(str(resposta))
				print('Bot: ',resposta)
			else:
				cria_audio('Ainda não sei responder esta pergunta')
				print('Bot: Ainda não sei responder esta pergunta')
		else:
			print("[Erro:fala vazia]")
	except:
		print('Erro')


