import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import cv2
import numpy as np
import pyautogui
import wikipedia
import pyjokes
import cv2
import winsound
import smtplib
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""

    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "jarvis" in command:
                command = command.replace("jarvis", "").strip()

            print(command)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")

    except sr.RequestError:
        print("Could not connect to the speech recognition service.")

    except Exception as e:
        print("Error:", e)

    return command


def send_email(reciver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('lvsnlohith@gmail.com', 'xucaefygdydmurfw')
    email = EmailMessage()
    email['From'] = 'lvsnlohith@gmail.com'
    email['To'] = reciver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)
    talk('you email is succesfully sent boss')
    talk('do you want to send more email boss')
    send_more = take_command()
    if 'yes' in send_more:
        get_email_command()
    if 'no' in send_more:
        talk('ok boss, call me if you want any help..')

email_list={
    'padmapriya': 'padmap816@gmail.com',
    'vishnu': 'kamalavishnulakkaraju@gmail.com',
    's sambasiva rao': 'ssambasivarao1939@gmail.com',
    
}

def get_email_command():
    talk('to whome should i send email boss')
    name = take_command()
    reciver = email_list[name]
    print(reciver)
    talk('okay,,,,what is the subject of your email boss')
    subject = take_command()
    talk('fine,,,,tell me the text in your mail boss')
    message = take_command()
    send_email(reciver, subject, message)

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'email' in command:
        email = get_email_command()
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'where is' in command:
        person = command.replace('where is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)   
    elif 'when is' in command:
        person = command.replace('when is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'when' in command:
        person = command.replace('when will', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'who am i' in command:
        name = command.replace('who am i', '')
        name = ('Neela Lohith')
        talk('you are my boss ' + name)
    elif 'english teacher name' in command:
        person = command.replace('where is my english teacher', '')
        name = ('venu gopal sir')
        print('you english teacher name is ' + name)
        talk('your english teacher name is ' + name)       
    elif 'my school name' in command:
        person = command.replace('what is my school name', '')
        name = ('The Crossword School')
        print(name)
        talk(name)
    elif 'tell me' in command:
        person = command.replace('tell me', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'director' in command:
        person = command.replace('director', '')
        name = ('channakasava reddy sir')
        print(name)
        talk(name)
    elif 'how are you' in command:
        talk('iam fine neela lohith boss,i think you are also fine')
    elif 'introduce' in command:
        talk('hi everyone. this is real life jarvis from iron mam movie. i can do anything like ok google and alexa. iam created by Neela lohith boss,and iam proude of my boss.')
    elif 'i am bored' in command:
        talk('ohh, shall i play a song sir')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'nice explanation' in command:
        talk('Thankyou boss')
    elif 'goodbye'in command:
        talk('Bye neela lohith boss . Have a nice day . Thankyou for asking me help . Bye')
    elif 'ok' in command:
        print('🤗')
    elif 'who created you' in command:
        talk('iam created by Neela lohith boss and iam proude of him.')
    elif 'no thanks' in command:
        talk('ok boss')
    elif 'hi' in command:
        talk('hai boss. jarvis on your command. how may i help you neela lohith boss')
    elif 'who are you' in command:
        talk('This is jarvis iam from iron man movie.... iam assistant od neela lohit boss..... jarvis service activated')
    elif 'cam' in command:
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, frame1 = cam.read()
            ret, frame2 = cam.read()
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
            for c in contours:
                if cv2.contourArea(c) < 5000:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2 )
                winsound.Beep(5000, 200)
            if cv2.waitKey(10) == ord('q'):
                break
            cv2.imshow('Lohith secrect cam', frame1)
    elif 'mouse' in command:
            cap = cv2.VideoCapture(0)

            lower_green = np.array([40, 40,40])
            upper_green = np.array([70, 255,255])
            prev_y = 0
            while True:
                ret, frame = cap.read()
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, lower_green, upper_green)
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for c in contours:
                    area = cv2.contourArea(c)
                    if area > 300:
                        x, y, w, h = cv2.boundingRect(c)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        if y < prev_y:
                            pyautogui.press('space')

                        prev_y = y
            
                cv2.imshow('frame', frame)
                if cv2.waitKey(10) == ord('l'):
                    break


            cap.relese()
            cv2.destroyAllWindows()
    
    else:
        talk('sorry, i didnt get you boss')
      
    
while True:
    run_jarvis()