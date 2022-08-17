from operator import truediv
import profile
import login1
import speech_recognition as sr
import json
import spotipy
import webbrowser

class Main():
    name = "Hackathon"
    password = "Hackathon"
    a = True
    n = login1.username.get()
    p = login1.password.get()
    while(a):
        if(p != password):
            p = input("Incorrect password, please try again: ")
        else:
            a = False   
    print("the password is correct")
    
def voice_assistant():
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Whatsup?")
            audio = r.listen(source)
            input_text = r.recognize_google(audio)
            final_text = input_text.lower()
    except sr.RequestError as e:
        print("Could not proccess that because: ", e)
    except sr.UnknownValueError:
        print("unknown error occured")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def Spotify():
    song_index = final_text.index('play')
    artist_index = final_text.index('by')
    song_input = final_text[song_index + 5:artist_index - 1]
    artist_input = final_text[artist_index + 3:]
    print(song_input)
    print(artist_input)
    print(song_input)
    username = '7ypcjyjdabk6uetsmoe7awkc4'
    clientID = '3e14d3868db34328bfaddc9d47fb7fcd'
    clientSecret = '05c2e3a4e6a14c91a9d8e0ec1902d818'
    redirect_uri = 'http://google.com/'

    oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()

    # To print the response in readable format.
    print(json.dumps(user_name, sort_keys=True, indent=4))
    user_input = 1
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    if user_input == 1:
        search_song = song_input
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        song_id = (results['tracks']['items'][0]['id'])
        print('Song has opened in your browser.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
    else:
        print("Please enter valid user-input.")
         
