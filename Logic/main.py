# what beabadoobee song(s) should you listen to?

#questions
questions = [
    "Have you listened to Beabadoobee before",
    "Do you feel like listening to a whole album right now",
    "*******Leave this",
    "How about a few songs",
    "Do you have a preference",
    "Do you want to listen to fast songs or slow songs"
]

userAnswers = []

# reccomendations 
rec1 = "Listen to fake it flowers!"
rec2 = "You listen to: Nothing."
rec3 = "I recommend you listen to: Ripples, pictures of us or disappear."
rec4 = "I recommend you listen to: Sorry, the perfect pair or the way things go."
rec5 = "I recommend you listen to: 10:36, Cologne or Charlie Brown."

print("Answer these (yes or no) questions to find out what Beabadoobee songs you should listen to!")

#first question
userResponse1 = input( questions[ 0 ] + "? " )

if userResponse1[0].lower() == "y":
    print("Hmm I see...")
else:
    print("Yeah, not everyone is a Beabadoobee fan ...")

#question2
userResponse2 = input( questions[ 1 ] + "? " )
if userResponse2[ 0 ].lower() == "y":
    print( f"{rec1}" ) # entire album

else:
    userResponse3 = input( questions[ 3 ] + "? " )
    if userResponse3[ 0 ].lower() == "n":
        print("You listen to: nothing.")
    if userResponse3[0].lower() == "y": # asking about songs
        userPreference = input( questions[ 4 ] + "? " ) # prefrence
    if userPreference[ 0 ].lower() == "n": # any
        print(f"{rec4}")
            
    if userPreference[ 0 ].lower() == "y":
        userSongSpeed = input( questions[ 5 ] + "? " ) # speed
            
            
        if userSongSpeed[ 0 ].lower() == "f": # fast songs
            print(f"{rec5}")   
        if userSongSpeed[ 0 ].lower() == "s": # slow songs
            print(f"{rec3}")

print("I hope you enjoy your song recomendations!₊˚⊹♡")
#end