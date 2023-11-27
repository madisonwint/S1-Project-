# what beabadoobee songs should you listen to?

#questions.
questions = [
    "Have you listened to Beabadoobee before", 
    "Do you feel like listening to a whole album right now",
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

print("Answer these yes or no questions to see what Beabadoobee songs you should listen to! ₊˚⊹♡ ")

userResponse1 = input( questions[ 0 ] + "? " )
if userResponse1[ 0 ].lower() == "y":
    print("Cool!")
else:
    print("Yeah, not everyone is a Beabadoobee fan ...")


# starting the quiz
def apple(): #function definition
    bool = True 
    while bool == True:
        
        #"Do you feel like listening to a whole album right now",
        userResponse2 = input( questions[ 1 ] + "? " )
        if userResponse2[ 0 ].lower() == "y":
            print( f"{rec1} I hope you enjoy it! *ੈ✩‧₊˚" ) # entire album

        else:
            # "How about a few songs",
            userResponse3 = input( questions[ 2 ] + "? " )
            if userResponse3[ 0 ].lower() == "n":
                print("You listen to: nothing. Enjoy!*ੈ✩‧₊˚")
            else:
                #if userResponse3[ 0 ].lower() == "y": # asking about songs
                #"Do you have a preference",
                userPreference = input( questions[ 3 ] + "? " ) # prefrence
                if userPreference[ 0 ].lower() == "n": # any
                    print(f"{rec4} I hope you enjoy your songs! *ੈ✩‧₊˚")
                else:

                    #"Do you want to listen to fast songs or slow songs"
                    userSongSpeed = input( questions[ 4 ] + "? " )
                    if userSongSpeed[ 0 ].lower() == "f": # fast songs
                        print(f"{rec5} I hope you enjoy your songs! *ੈ✩‧₊˚")   
                    if userSongSpeed[ 0 ].lower() == "s": # slow songs
                        print(f"{rec3} I hope you enjoy your songs! *ੈ✩‧₊˚")

        check = input("⊹˙⋆ Would you like to try again? ⋆˙⊹ ")

    if check[ 0 ].lower() != "y":
        bool = False       
apple() #calling function  
