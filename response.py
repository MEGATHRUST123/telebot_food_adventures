# create a response file  to return suitable responses based on 
# input text

from datetime import datetime

def sample_response(input_text):
    # lower case input text
    s = str(input_text).lower()
    print(s)

    if s in ['hello','morning','yo','start']:
        return "Hey! how's it going?"

    if s in ['bye','goodbye']:
        return "Sad to see you go! see you again!"
    
    return "I don't understand you"
