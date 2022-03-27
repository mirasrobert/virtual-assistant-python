import speech_recognition as sr
import pyttsx3 as ts
import pywhatkit
import datetime
import wikipedia

# To Recognize
listener = sr.Recognizer()
engine = ts.init()
voices = engine.getProperty('voices')  # Get All Voices

maleVoice = voices[0].id
femaleVoice = voices[1].id

engine.setProperty('voice', femaleVoice)


# VA Talk
def talk(text):
    # Speak
    engine.say(text)
    engine.runAndWait()


# Take our command
def take_command():
    try:
        # Use Microphone as source
        with sr.Microphone() as source:

            talk('Hello Robert')
            talk('How can I help you today?')

            print('Listening...')

            # Our Voice
            voice = listener.listen(source)
            # Our Command To Our VA
            command = listener.recognize_google(voice)
            # Make our command voice lowercase
            command = command.lower()
            if 'alexa' in command:
                # Alexa will say;
                command = command.replace('alexa', '').lstrip()
            return command
    except:
        print("An exception occurred")
    return ""


# Run Virtual Assistant
def run_assistant():
    command = take_command()

    if command == "":
        talk('Sorry, I dont understand you')

    if 'play' in command:
        song = command.replace('play', '').lstrip()
        talk('Playing ' + song)
        # Play On YouTube
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Time is ' + time)
    elif 'info' in command or 'who is' in command or 'what is' in command:
        wiki = ''
        if 'what is' in command:
            wiki = command.replace('what is', '').lstrip()
        elif 'who is' in command:
            wiki = command.replace('who is', '').lstrip()
        elif 'info' in command:
            wiki = command.replace('info', '').lstrip()

        try:
            info = wikipedia.summary(wiki, 2)
            talk(info)
        except:
            pass


    else:
        talk('Please say your command again.')


while True:
    run_assistant()
