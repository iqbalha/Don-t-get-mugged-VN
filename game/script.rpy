# Create specail transitions
define updownTransHelper = ComposeTransition(slideup,
    after=Fade(0.4, 0.35, 0.6, color="#00001a"))
define updownTrans = ComposeTransition(slideawayup,
    before = Fade(0.4, 0.35, 1.0, color="#00001a"), after=updownTransHelper)

define quickFade = Fade(0.5, 0.2, 0.5)

# Define npc characters used by this game.
# Penguin King
define pen = Character('Penguin King', color="#c8ffc8")
image penguin normal = "penguin_Looking_Left.png"
image penguin backwards = "turned_around_penguin"
# Tutorial character
define tut = Character("some guy", color ="#a22342" )
image tutMug normal:
    "lousy_mugger.png"
    zoom 0.7
    yalign 0.48
image tutMug batless:
    "batless_other_mugger.png"
    zoom 0.7
    yalign 0.48
# Define text baised characters
define narrator = Character(None, kind=nvl)
define game = Character(None, color="#e8ffe8")
define player = Character(None, color="#c8c8c8")
define player_nar = Character(None, kind=nvl, color="#c231d4")
 
# background images
image bg blank:
    "empty_Street.png"
    zoom 0.18
image bg park:
    "park.jpeg"
    zoom 1.0
image bg cornfield:
    "cornField.jpg"
    zoom 1.5
image bg forest:
    "forest_path.jpg"
    zoom 0.6
image bg moon:
    "moon_over_forest.jpg"
    #"moon.jpg"
    zoom 0.25
image bg sky:
    "sky.jpg"
    zoom 1.3
image bg money:
    "money_screen.png"
    zoom 1.5
image bg black = "black_screen.png"
image bg brown = "brown_screen.png"

# Effect images
image headache:
    "red_screen.png"
    alpha 0
    linear 0.075 alpha 0.8
    #pause 0.1
    linear 0.4 alpha 0

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

label start:
    jump chapterMenu
label chapterMenu: # developer menu
    menu:
        "Intro":
            jump intro
        "tutorialEncounter":
            jump preTut
        "Penguin King":
            jump penguinEncounter
            
############## The game starts here.
label intro:    
    # create Varaibles
    $ money = 18.41  
    $ observed = False
    $ inspected = False

    play music "bg_music.mp3"
    scene bg black
    narrator "…"
    show headache
    narrator "*Pounding headache 'flinch'*"
    player_nar "Urgh… where I am?"
    nvl clear
    
    scene bg sky with Dissolve(2.0)
    narrator "You slowly open your eyes and gaze at the starry sky. The cool night air is crisp
    and cold, and you shiver as you realize you’ve awoken on a grassy patch of field."
    nvl clear
    
    scene bg cornfield with updownTrans
    pause
    game "Slowly, using your weak arms to push yourself upright, you gather your thoughts
    and attempt to recall how you arrived at this state."    
    show headache
    game "*Pounding headache 'flinch'*"
    player "I don’t remember a goddamned thing about myself..."
 
label firstChoice:
    scene bg cornfield
    if observed and inspected:
        player "It's time to head to town"
        jump preTut 
    menu:
        "{b}Observe your surroundings{/b}" if not observed:
            jump observe
        "{b}Inspect Self{/b}" if not inspected:
            jump inspectSelf
            
label observe:
    $ observed = True
    narrator "You suddenly have a strong urge to look around even though the thought of
    thinking brings immense pain.\n"
    scene bg moon at topright with quickFade
    narrator "You’re in the middle of a corn field. The corn provide little to no shelter from
    the elements, but the bright lit moon gives you a clear vantage point of your surroundings.\n"
    scene bg forest with quickFade:
        xalign 0.5
    narrator "Just behind you is a dark forested area, with a old trodden path that leads you
    into the looming darkness.\n"
    nvl clear
    
    scene bg park with quickFade:
        xalign 0.15
    narrator "In the distance resides a small picturesque town. Although its existence
    is seemingly peaceful, you reconsider this fact when you see the beaten up graffiti-ridden
    sign in front of the village. You step closer to make out the words.\n"
    narrator "“Stab… County? Population… 10.” You are also able to make out several phallic
    objects skirting the sign, and an absolutely filthy comment about someone’s mother.\n"
    narrator "You shudder to think what else might be written if you walk any closer."
    nvl clear
    jump firstChoice
    
label inspectSelf:
    $ inspected = True
    narrator "Strangely, you decide to check yourself out. Obviously, this is an odd quirk
    of yours, and you dread to remember other weird peculiarities about yourself. Although
    there are no mirrors in front of you, you are able to identify your attire and check your
    armaments in the well-lit moonlight.\n"
    narrator "You don a neon yellow polo shirt and baggy khaki pants. On your feet are rather
    childish shoes. Further examination shows that the shoes actually light up like a rave
    party when you walk in any direction. Worse, they make an obnoxious squeaking sound
    whenever you take a step.\n\n"
    narrator "Whoever you are, you have terrible fashion sense."
    nvl clear
    
    #scene bg brown with squares
    scene bg money at center with quickFade:
        yalign 0.5
    narrator "You also realize that although your baggy pants are ill-fitting, they are able to
    hold a large number of items. You find $[money] and scrunched up receipt.\n"
    narrator "You wonder why you have every type of legal tender on yourself, but based on
    all the other peculiar things you do, this does not surprise you. The change in your
    pocket jingles with every step, which parallels the noise from your unruly shoes.\n" 
    player_nar "It’s quite dangerous to walk around with all this change. I hope no one
    tries to mug me."
    nvl clear
    jump firstChoice
    
############### Tutorial Encounter 
label preTut:
    scene bg park:
        xalign 0.2
    narrator "You had a long day at work.\n ...\nIt's now several hours past midnight\n
    ...\n \n*more narration*\n \n..."
    narrator "The roads are Dark and Dangerous\nAnd now you have to get home.\n"
    narrator "Try not to get mugged."
    nvl clear
    
label tutorialEncounter:
    tut "H-H-hey, you there."
    scene bg park:
        xpos  -0.3
        easein 0.5 xpos -.8
    show tutMug normal
    tut "Ya you. G-gimme everything you've got"
    game "*Is this guy serious? He looks like he's only capable of mugging old ladies. But still
    getting hit by that baseball bat looks like troublesome.*"

label tutorialChoice:
    menu:
        "Drop the bat, before you hurt yourself":
            jump endTutorial
        "Look man, I don't want any trouble":
            play sound "Witches_Laugh.mp3"
            tut "Hahahahaha, Y-Y-You're in the wrong county if you didn't want any t-t-trouble"
            #rushing animation
            game "The man rushes you "
            # move and shake camera
            game "You roll to the side and manage to get out of the way before the bat strikes the
            ground where you were just standing. The man staggers from the recoil of the bat.
            As your feet touch the ground you spring onto the now vulerable man."
            #toppled man
            show tutMug batless
            game "You miss judged the distance and the man is able to back off before you can
            knock him to the ground. He immediately regains his balance and.... runs away."
            hide tutMug
            
            game "You catch your breath and look at the baseball bat he left behind.  There is a
            crack running down the center of the bat making it completely useless. Suprised you
            walk over to it to get a closer look."
            game "Upon inspection you notice that the there is strudy rock in the location
            where the man stuck the ground surrounded by tiny wooden splinters. It seems you
            lucked out this time but you should be catious. In the future you might not
            get a second chance."
            jump penguinEncounter
        "*Approach the man menacingly*":
            jump endTutorial
        
label endTutorial:
    tut "Y-You've some how convinved me not to m-m-mug you. You can keep your $[money]"
    player "Wait how do you know exaclty how much money I have on me"
    tut "You must not be from around here. E-E-everone in this town can smell m-m-m-money. 
    I wonder if you can survive in this town. I wish you G-g-g-good luck"
    
################# Penguin Encounter
label penguinEncounter:
    scene bg blank at right with dissolve    
    pen "Who's there!"
    
    show penguin normal at center:
        zoom 0.5
    pen "I don't recognize you. What are you doing in my neighborhood?"

    menu:
        "I'm just trying to get home":
                jump penguinMugging
        
        "Your neighborhood? You mean MY neighborhood":
                jump penguinDeath
                
        "I've heard of a great King in this neighborhood and had come to see if the legends where true ":
                jump penguinPass
                
label penguinMugging:
    
    $ money = 0
    pen "Who do you think your are. Thinking you can enter my domain without paying a price."
    
    show deathFilter:
        alpha 0.3
    game "Animation of the [pen.name] roughly mugging the player"
    pen "I'll be taking that as your penance for wasting a Kings time."
    
    show penguin backwards:
        zoom .2
        yalign .55
        xalign .4
    pen "Don't come back here again"
    
    hide penguin
    game "A minute after you see the Penguin King walk out of sight you move your hands under
    your body to try and pick yourself of the street and onto your feet"
    game "The moment you begin pushing with your arms you feel strong surge of pain go
    through your body. You groan but somehow manage to get onto your two feet. After
    wobbling a few times you take inventory of what you still have on you.\n"
    pen "The penguin King made sure to steal all the money you had on you but at least you still have
    your shoes "
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
    jump penguinsDomain
    
label penguinsDomain:
    game ".:. Good end"
    return
   
