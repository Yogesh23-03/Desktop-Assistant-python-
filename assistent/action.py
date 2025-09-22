import txt_to_spch
import speech_to_text
import datetime
import webbrowser as web
import weather
def Action(indata):
    user_data=indata.lower()
    if 'what is your name ' in user_data:
        txt_to_spch.text_to_spch('my name is merlin your assistent')
        return 'my name is merlin your assistent'
    elif'hello' in user_data or 'hye' in user_data:
        txt_to_spch.text_to_spch('hello how can i assist you today')
        return 'hello how can i assist you today'
    elif 'good morning' in user_data:
        txt_to_spch.text_to_spch('good morning dear')
        return 'good morning dear'
    elif 'time now' in user_data:
        time=datetime.datetime.now().strftime('%I:%M %p')
        txt_to_spch.text_to_spch(time)
        return time
    elif 'shutdown' in user_data:
        txt_to_spch.text_to_spch('ok dear')
        return 'ok dear'
    elif 'play music' in user_data:
        web.open('https://gaana.com/')
        txt_to_spch.text_to_spch('gaana.com is ready for you')
        return 'gaana.com is ready for you'
    elif 'open youtube' in user_data:
        web.open(' https://www.youtube.com/')
        txt_to_spch.text_to_spch('youtube is ready for you') 
        return 'youtube is ready for you'
    elif 'open google' in user_data:
        web.open('https://www.google.com/')
        txt_to_spch.text_to_spch('google.com is ready for you')
        return 'google.com is ready for you'
    elif 'open vscode' in user_data:
        web.open('https://code.visualstudio.com/')
        txt_to_spch.text_to_spch('vscode is ready for you')
        return 'vscode is ready for you'
    elif 'open jupyternotebook' in user_data:
        web.open('https://jupyter.org/')
        txt_to_spch.text_to_spch('jupyter notebook is ready for you')
        return 'jupyter notebook is ready for you'
    elif 'weather' in user_data:
        result=weather.weather()
        txt_to_spch.text_to_spch(result)
        return result

    else:
        txt_to_spch.text_to_spch('sorry i did not understand what you said')
        return 'sorry i did not understand what you said'