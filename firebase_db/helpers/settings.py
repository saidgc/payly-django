import pyrebase

config = {
    "apiKey": "AIzaSyBuWVQCJ18DRxkTeashOjwiBEisN_wLsiI",
    "authDomain": "payly-e968a.firebaseapp.com",
    "databaseURL": "https://payly-e968a.firebaseio.com",
    "storageBucket": "payly-e968a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
