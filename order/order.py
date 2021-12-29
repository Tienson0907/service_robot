#!/usr/bin/env python3

# import gtts
from playsound import playsound

import speech_recognition as sr
import pyttsx3
import rospy
from std_msgs.msg import String



# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
# def SpeakText(command):
# # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()

# Loop infinitely for user to
# speak
talk = True
while (talk):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            playsound("WhatOrder.mp3")
            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            playsound("Thanks.mp3")
            print("Did you say " + MyText)
            print("Send " + MyText + " to bartender")
            pub = rospy.Publisher('talker', String, queue_size=10)
            rospy.init_node('publish_node', anonymous=True)
            rate = rospy.Rate(10) # 10hz # fequency at which the publishing occurs
            while not rospy.is_shutdown():
                publishString = str(MyText) # varibale 
                rospy.loginfo("Data is being sent")  # to print on the terminal 
                pub.publish(publishString) # publishing 
                rate.sleep()
            if MyText != None :
                break
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        playsound("Sorry.mp3")

            # SpeakText(MyText)






