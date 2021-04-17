# Final Project - An Interactive Conversational Agent with Added Features

This Project is a developed by Chinmay Gopal and is based on a chat-bot created by Sebi Unipan, Chinmay Gopal, Iwan Levin, Amritpal Aujla and Ali Ibrahim in a previous assignment.
## Description

This Project aims to implement additional features to an online chat-bot. More specifically, this chat-bot implements the Twitter API as well as the Bing translate API to allow additional functionality. 


This project was was developed entirely in Python using the Natural Language Processing library, Natural Language Toolkit(NLTK) and the Tweepy Library.

The program is made up of two classes: chatbot and main
>chatbot is the class that can has all the attributes of the chat bot and its methods

>main class is where a chatbot object gets created and is run to extract quotes from file as  
>well as running a loop to continuously ask the user for input with a loop in the class until  
>they enter an exit word.
>Both new features are directly implemented into main using their respective libraries.  

## Installation

To be able to run the chat bot, you need the nltk and sklearn Python packages.
Open up command prompt and type the following:  

`pip install nltk`  

`pip install -U scikit-learn` 

You should then open up a Python interactive console (IDLE) and download all nltk packages by:

`import nltk`  

`nltk.download()`

A GUI should pop up, select 'all | All packages' and press download, afterwards close the GUI.

Afterwards, you may run the main.pyw file and the bot should work accordingly.
***NOTE: When running the main.pyw file, a delay of 10-15 seconds is normal to train the model in the sentiment file***

## New features

Twitter functionality: Using the Tweepy library and Twitter's API recieved through my Twitter developer account I was able to add a "Tweet Conversation" button. The "Tweet Conversation" button I can instantly post a snippet of my converstion with the chat-bot. Due to twitter's tweet limit of 280 characters only a few lines of conversation can be posted. This feature is indented to allow users to post funny or informational moments from their conversation that might be memorable. After clicking the button Tweepy's library is used to post the tweet and am added message is added to the GUI.


Example:  
You: Presses Tweet Conversation Button  
Calm Bot: Solution: "Conversation Tweeted!"

~ It posted the tweet and informed the user using the GUI.

Bing Translate API: Using the documentation and the API key from the Microsoft website I was able to seamlessly add multiple language support to the chat-bot. The API allows me to detect the current spoken langauge and translate it to english for the NLTK library to untilize. In addition the program retranslates the NLTK output back to the detected language from the users' convenience. The chat-bot performs language detection continually in the while loop so that the user can use multiple languages as they desire. The chat-bot informs the user when the language they have translated is not recognized by the Bing API. 

Example:  
You: I feel stressed 
Calm Bot: Stress can sometimes be overwhelming, just know that you are not alone.
You: me odio a mí mismo
Calm Bot: A veces todos necesitamos hablar sobre nuestros problemas.

~ It correctly recognized the changing languages and responded appropriately.

