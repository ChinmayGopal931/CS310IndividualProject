from chatbot.chatbot import ChatBot
from chatbot.spellcheck import SpellCheck
from chatbot import translator
import PySimpleGUI as sg
import sys
import json
import subprocess
import tweepy

auth = tweepy.OAuthHandler("8yjR2kRNfQJ2vacpu9P76plSt", "YCZ9JMR8kyAFyGjizGGMeWle4RhrnyyHy3shdFecf8cJaRz7wH")
auth.set_access_token("1379398552430895105-xSB9aoZKZtnBNLBOvHZ941DMUowbWp", "lIL7bOAymECDFfeGz8wzynImnsu4hs1T8mRcDtxzoXlFd")
api = tweepy.API(auth)
# Define the window's contents
sg.theme('Dark2')
layout = [[sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(80,10))],
          [sg.Text('Your Input')],
          [sg.InputText(key='i', size=(40, 2))],
          [sg.Button('Tweet Conversation')],
          [sg.Button('SUBMIT', bind_return_key=True), sg.Button('EXIT')]]

def __main__():

    # Create the window
    window = sg.Window('Calm Bot', layout, default_element_size=(50, 3),finalize=True)
    cb = ChatBot() 
    sc = SpellCheck()
    window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot: Hello, my name is Calm Bot and I'm here to help you!")
    cb.extractQuotes('posQuotes.txt') #we establish the posQuotes in the object
    cb.extractQuotes('negQuotes.txt') #we establish the negQuotes in the object
    exitWords = ['bye', 'quit', 'exit', 'see ya', 'good bye'] #Exit the chat bot with common salutations

    exitError = sc.errorHandlingArray(exitWords) # correcting for errors
    try:
        stack = []
        while(True):    #run a loop to keep prompting the user for input
            event, values = window.read()
            print("You: "+ values['i'])
            translatoroutput = translator.translateme(values['i'])
            language=(json.dumps(translatoroutput["detectedLanguage"]["language"],ensure_ascii=False)).replace('"', '')
            userInput= (json.dumps(translatoroutput["translations"][0]["text"], ensure_ascii=False)).replace('"', '')
            rating= int(float(json.dumps(translatoroutput["detectedLanguage"]["score"])))

            if len(stack) > 8:
                stack.pop()
            else:
                stack.append("You: "+ userInput)

            window.FindElement('i').Update('')
            window['-ML1-' + sg.WRITE_ONLY_KEY].print(translator.translator(("You: "+userInput), language), end='\n')

            if event == sg.WIN_CLOSED or event == 'EXIT':
                break
            if event == 'Tweet Conversation':
                results=""
                print(stack)
                for x in stack:
                    results+=stack.pop()+"\n"
                api.update_status(status=results)
                window['-ML1-' + sg.WRITE_ONLY_KEY].print(translator.translator("Calm Bot: Conversation Tweeted!", language), end='\n')
                continue


            if sc.errorHandlingArray(userInput.lower()) in exitError: #allows for words like "exiting" or "exited" to work, as well as many other cases
                window['-ML1-' + sg.WRITE_ONLY_KEY].print(translator.translator("Calm Bot: It was really nice talking to you!",language), end='\n')
                stack.append("Calm Bot: It was really nice talking to you!")
                print("Calm Bot: It was really nice talking to you!")
                break
            if rating<0.65:
                print("rating too low")
                window['-ML1-' + sg.WRITE_ONLY_KEY].print("Calm Bot:I'm sorry I couldn't quite understand you", end='\n')
                stack.append("Calm Bot: I'm sorry I couldn't quite understand you")
                continue
            else:
                if cb.helloMessage(userInput) != None:  #if hello returns nothing, output a quote
                    out=("Calm Bot: " + cb.helloMessage(userInput))
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print(translator.translator(out, language), end='\n')
                    stack.append(out)
                else:
                    out = ("Calm Bot: " + cb.botResponse(userInput))
                    window['-ML1-' + sg.WRITE_ONLY_KEY].print(translator.translator(out, language), end='\n')
                    stack.append(out)
                    # See if user wants to quit or window was closed
                    if event == sg.WINDOW_CLOSED or event == 'EXIT':
                        break
    except Exception as e:
        print(e)
        window.close()
        sys.exit()
    window.close()
    sys.exit()
    
__main__()
