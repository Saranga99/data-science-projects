# importing libraries 
# from utils.summarization import summarize
from utils.chatbot import intro
from utils.read_files import read_docx
from utils.question_answering import question_answer
from utils.speech_synthesis import speech_to_text, text_to_speech


while True:
    intro()
    text_to_speech(" Please enter your resource file name:")
    # filename = input("\nPlease enter your resource file name: \n")
    text = input("\nPlease enter your resource text: \n")
    text_to_speech("Please enter your question")
    # question = input("\nPlease enter your question: \n")
    question = speech_to_text()

    answer = question_answer(question, text)
    text_to_speech(answer)
    
    flag = True
    flag_N = False
    
    while flag:
        text_to_speech(" Do you have more questions? ")
        response = speech_to_text()
        print(response)
        if response[0] == "yes":
            text_to_speech("Please enter your question")
            # question = input("\nPlease enter your question: \n")
            question = speech_to_text()
            flag = False
        elif response[0] == "no":
            text_to_speech("End of the program! Have a nice day!")
            # print("\nEnd of the program!")
            flag = False
            flag_N = True
            
    if flag_N == True:
        break
# text = input(" ENter your text here: ")
# print (summarize(text))