import pandas as pd

def barkote_send_sms(event,context):

    data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
    }

#load data into a DataFrame object:
    df = pd.DataFrame(data)



    return {
        'message':"df"
    }