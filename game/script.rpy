﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define pen = Character('Penguin King', color="#c8ffc8")
define narrator = Character(None, kind=nvl)
define game = Character(None, color="#e8ffe8")
define player = Character(None, color="#c8c8c8")
 
image bg blank = "empty_Street.png"
image penguin normal = "penguin_Looking_Left.png"
image penguin backwards = "turned_around_penguin"

image deathFilter:
    "red_screen.png"
    alpha 0.3
    
image bloodSplatter:
    choice:
        "blood_spatter2.png"
        zoom .9
    #choice:
        #"blood_spatter3.png"
        #zoom .6
    #choice:
        #"blood_spatter4.png"
        #zoom .6
    alpha 0.6
    
    

# The game starts here.
label start:
    play music "bg_music.mp3"
    scene bg blank at right:
        zoom 0.18
    #show penguin backwards at center:
    #   zoom 0.5
    narrator "You had a long day at work.\n ...\nIt's now several hours past midnight\n
    ...\n \n*more narration*\n \n..."
    narrator "The roads are Dark and Dangerous\nAnd now you have to get home.\n"
    narrator "Try not to get mugged."
    
    pen "Who's there!"
    nvl clear
    
    show penguin normal at center:
        zoom 0.5
    pen "I don't recognize you. What are you doing in my neighborhood?"

label penguinChoice:
    menu:
        "I'm just trying to get home":
                jump penguinMugging
        
        "Your neighborhood? You mean MY neighborhood":
                jump penguinDeath
                
        "I've heard of a great King in this neighborhood and had come to see if the legends where true ":
                jump penguinPass
                
label penguinMugging:
    pen "You're not passing through my domain for free"
    game "Animation of the Penguin King mugging the player"
    
    show penguin backwards:
        zoom .2
        yalign .55
        xalign .4
    pen "Don't come back here again"
    
    hide penguin
    game ".:. Bad End"
    return
    
label penguinDeath:
    pen "You have a lot of nerve"
    show deathFilter
    show bloodSplatter at top
    game "*Animation of the Penguin King killing player*"
    
    hide penguin
    game ".:. Game Over"
    return
    
label penguinPass:
    pen "That's understandable, My greatness is so grand that it seems unbelievable"
    pen "Well, do you believe the legends now?"
    player "The Legends don't do your grace justice. You're far more impressive a king in person"
    pen "But of course."
   
    show penguin backwards:
        zoom .2
        yalign .55
        xalign .4
    pen "I have decided you aren't completely unworthy of my pressence.
    you may pass"
    
    hide penguin
    
    game ".:. Good end"
    return
   
