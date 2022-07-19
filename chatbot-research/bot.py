# importing libraries
# from utils.summarization import summarize
from utils.chatbot import intro
# from utils.read_files import read_docx
# from utils.question_answering import question_answer
from utils.speech_synthesis import speech_to_text, text_to_speech
import time

intro()
# text_to_speech(" Please enter your resource file name:")
# filename = input("\nPlease enter your resource file name: \n")
# text = input("\nPlease enter your resource text folder name: \n")
print("Data is loaded...")
time.sleep(3)
text_to_speech("So how can I help you?")
# question = input("\nPlease enter your question: \n")
text1 = speech_to_text()
time.sleep(10)
text_to_speech("Hello ryan?")
text_to_speech('Ok, before we move forward, I like to know whether you like to do potty train your child?')
# text_to_speech(
#     'Would I have your permission to gather some basic information?')

time.sleep(5)

text_to_speech("Before beginning schedule training, ensure that your child is ready for potty training. Your child should have some bowel control, indicated by extended periods of dryness and should be willing to sit on the toilet. Scheduled training is the technique used most often with typically developing children, and within early childhood classrooms. Scheduled training involves taking your child to the restroom at pre-determined times of the day and providing reinforcement for successes.")
time.sleep(5)
text_to_speech("We start training tomorrow morning. When child awakes take note of if they have wet themselves during the night. Regardless of condition take them to the potty and have them sit the entire 5 minute duration. If we have a successful session praise the child ... if not remind (chid) that using the restroom results in getting up off the potty.  you can update me with the results after you have completed the first morning of training. Just wake me up with  Childis awake, and we will document the results.  ")
time.sleep(15)
text_to_speech("Is child awake?")
time.sleep(5)
text_to_speech("Did (child) successfully use the potty? ")
time.sleep(5)
text_to_speech("Very good! ")
text_to_speech("scheduled training involves taking your chils to the restroom at pre-determined times of the day and providing reinforcement for successes. I will remind you 10 mins before (child name) next scheduled time which every to hours")
# text_to_speech("I am now ready to review the forms that we will need to connect with your service coordinator to obtain authorization for the services you are interested in.")

# text_to_speech("Now all the documents will display on your screen..")
# text_to_speech(
#     'Can I have your full name')
# name = speech_to_text()
# text_to_speech(
#     'what is your child’s full name')
# child_name = speech_to_text()
# text_to_speech(
#     'what is your child’s birthdate')
# child_bday = speech_to_text()

# text_to_speech(
#     'what is your phone number, starting with the area code')
# phone = speech_to_text()
# text_to_speech(
#     'what is your email address')
# email = speech_to_text()

# text_to_speech(
#     'what is your reigon? NorCal or SoCal?')
# reg = speech_to_text()
# print(reg)
# # if reg == 'norcal':
# text_to_speech(
#     'On a Monday thru Saturday basis, what time are you most available? We have three-time frames available: ')
# text_to_speech(
#     '1.	Morning(8 am-11 am) ? 2. Mid-day(11 pm-3 pm)? 3. Afternoon(3 pm-6 pm) ?')
# text_to_speech(
#     'Tell me 1, 2 or 3 for related time slots according to date or no if you are not available')
# text_to_speech(
#     'Are you available on Mondays for session')
# text_to_speech(
#     'Are you available on Tuesday for session')
# text_to_speech(
#     'Are you available on Wednesday for session')
# text_to_speech(
#     'Are you available on Thursday for session')
# text_to_speech(
#     'Are you available on Friday for session')
# text_to_speech(
#     'Are you available on Saturday for session')


# elif reg == 'socal':
#     text_to_speech(
#         'On a Monday thru Saturday basis, what time are you most available? We have three-time frames available: ')
#     text_to_speech(
#         '	1. Morning(8 am-11 am) ?  2. Mid-day(11 pm-3 pm)? 3. Afternoon(3 pm-6 pm) ? 4.	Evening (6 pm- 8 pm)')
#     text_to_speech(
#         'Tell me 1, 2 , 3 or 4 for related time slots according to date or no if you are not available')
#     text_to_speech(
#         'Are you available on Mondays for session')
#     text_to_speech(
#         'Are you available on Tuesday for session')
#     text_to_speech(
#         'Are you available on Wednesday for session')
#     text_to_speech(
#         'Are you available on Thursday for session')
#     text_to_speech(
#         'Are you available on Friday for session')
#     text_to_speech(
#         'Are you available on Saturday for session')


# text_to_speech(
#     'Please tell me your address, city and zip code')
time.sleep(10)
text_to_speech(
    'Please know that we take your confidential information very seriously and will always follow HIPAA guidelines to secure your information.')
time.sleep(5)

# text_to_speech(
#     'I have all the information I need. Do you have any questions  ')
# time.sleep(5)

# text_to_speech(
#     'Ok, this information is stored in our database so we can better assist you in the future.')

print("Information saved...")
# time.sleep(45)
# time.sleep(10)
# print("Conversation saved succesfully!")
# time.sleep(3)
# print("Conversation text is summarized and saved succesfully!")
# time.sleep(3)
# text_to_speech('Sometimes it\'s not about the food itself that they are being picky over, it\'s about having a sense of control. There are different ways to help a child feel like they have some control over their food. Relax and enjoy mealtimes, and realize that not every meal is going to be perfect.')
# text_to_speech(" Do you have more questions? ")
# question = speech_to_text()
# text_to_speech("There are a few things that you can do if your child has a hard time drinking from a bottle. Play soft calming music, sit somewhere you can gently rock your child as you feed them. You can also try and give your child a different type of bottle or nipple.")
# text_to_speech(" Do you have more questions? ")
# question = speech_to_text()
# time.sleep(10)
# text_to_speech("The autism spectrum includes a range of neurodevelopmental differences. Autistic people are said to have difficulties with social interactions, and to show rigid and repetitive behaviours and interests. They are also likely to have unusual responses to sensory input, including high or low sensitivity, auditory processing, sensory discrimination, and motor impairments. While psychiatry traditionally classifies autism as a neurodevelopmental disorder, some see autism as part of neurodiversity. This relatively positive view of autism has sometimes led to friction between autistic individuals and charities. Scientists are still trying to determine what causes autism; it is highly heritable and believed to be mainly genetic.")
# text_to_speech(" Do you have more questions? ")

# question = speech_to_text()
# text_to_speech(" Have a nice day! ")

# Sometimes it's not about the food itself that they are being picky over, it's about having a sense of control. There are different ways to help a child feel like they have some control over their food. Relax and enjoy mealtimes, and realize that not every meal is going to be perfect.

# There are a few things that you can do if your child has a hard time drinking from a bottle. Play soft calming music, sit somewhere you can gently rock your child as you feed them. You can also try and give your child a different type of bottle or nipple.
