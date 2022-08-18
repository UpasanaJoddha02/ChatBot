
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import requests
import json

bot = ChatBot(
    'covid-19' ''',
   logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ]'''
)

chatLine = open('chats.txt', 'r').readlines()
trainer = ListTrainer(bot)
trainer.train(chatLine)
trainer_corpus = ChatterBotCorpusTrainer(bot)
trainer_corpus.train('covid19')



def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Me: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12))
        # res = chatbot_response(msg)
        res = bot.get_response(msg)
        # print(res)
        response = str(res)
        if response in ['TT', 'GJ', 'MH', 'TN', 'DL', 'RJ', 'MP', 'UP', 'WB', 'AP', 'PB', 'TG',
                        'KA', 'JK', 'BR', 'HR', 'OR', 'KL', 'CH', 'JH', 'TR', 'UT', 'HP', 'AS', 'CT',
                        'ML', 'PY', 'GA', 'MN', 'MZ', 'SK', 'NL', 'AP', 'DN', 'DD', 'LD', 'AN']:
            stringToDisplay = getRequestedData(response)
        else:
            stringToDisplay = response
        ChatLog.insert(END, "Bot: " + stringToDisplay + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


def who():
    url = "https://www.covid19india.org/"
    webbrowser.open_new_tab(url)


def getRequestedData(stateCode):
    print(stateCode)
    # Request URL: https://api.covid19india.org/state_district_wise.json
    # Request URL: https://api.covid19india.org/data.json

    URL = "https://api.covid19india.org/data.json"
    r = requests.get(url=URL)
    StateWiseData = json.loads(r.text)['statewise']
    searchedData = [x for x in StateWiseData if x['statecode'] == stateCode]
    return '\nActive Cases : ' + searchedData[0]['active'] + '\nConfirmed cases : ' + searchedData[0][
        'confirmed'] + '\nDeaths : ' + searchedData[0]['deaths'] + '\nRecovered Cases : ' + searchedData[0]['recovered']


base = Tk()
base.title("COVID-19 BOT")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
bg_image = ImageTk.PhotoImage(Image.open("corona.png"))
bg = Label(base, image=bg_image)
bg.pack()
#  Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(state=DISABLED)
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set
#  Button to send message
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=send)
#  box to enter message
EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")
# EntryBox.insert(END, "Enter the state name here.")
# Button for exit
button_quit = Button(base, font=("Verdana", 12, 'bold'), text="EXIT",  width="12", height=5,
                     bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=base.quit)
# who button
help_button = Button(base, font=("Verdana", 12, 'bold'), text="HELP!", width="12", height=5,
                     bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=who)
scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=6, y=401, height=40, width=265)
SendButton.place(x=278, y=401, height=40)
button_quit.place(x=6, y=450, height=40, width=122)
help_button.place(x=278, y=450, height=40, width=122)
base.mainloop()
'''import webbrowser
url = "http://www.google.com/"
webbrowser.open_new_tab(url)'''
'''while True:
    request = input('You: ')
    response = bot.get_response(request)
    print('Bot: ', response)'''
