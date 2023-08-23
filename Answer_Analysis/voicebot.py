import speech_recognition as sr
import tkinter as tk

# list of questions to be asked
questions = ["What is your name?", "What is your age?", "What is your favorite color?", "What is your favorite food?"]

# initialize the recognizer
r = sr.Recognizer()

# function to ask questions
def ask_question(question):
    # initialize the microphone
    with sr.Microphone() as source:
        # ask the question
        print(question)
        voice_output.config(text=question)
        audio = r.listen(source)
    try:
        # convert speech to text
        text = r.recognize_google(audio)
        # print the response
        print("You said:", text)
        response.config(text="You said: " + text)
    except sr.UnknownValueError:
        # handle unrecognized speech
        print("Sorry, I didn't understand that.")
        response.config(text="Sorry, I didn't understand that.")
    except sr.RequestError as e:
        # handle API request error
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        response.config(text="Could not request results from Google Speech Recognition service.")

# initialize the GUI
window = tk.Tk()
window.title("Voice Bot")

# create the UI elements
voice_output = tk.Label(window, text="")
voice_output.pack()
response = tk.Label(window, text="")
response.pack()

# create the "Ask Question" button
button = tk.Button(window, text="Ask Question", command=lambda: ask_question(questions[len(response['text'])]))
button.pack()

# start the GUI
window.mainloop()
