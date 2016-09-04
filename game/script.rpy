﻿# Create special transitions
define updownTransHelper = ComposeTransition(slideup,
    after=Fade(0.4, 0.35, 0.6, color="#00001a"))
define updownTrans = ComposeTransition(slideawayup,
    before = Fade(0.4, 0.35, 1.0, color="#00001a"), after=updownTransHelper)

define quickFade = Fade(0.5, 0.2, 0.5)
define longFade = Fade(1, 1, 1)
define shakeScreen = ComposeTransition(vpunch, before=hpunch)
    
# Define npc characters used by this game.
# Penguin King
define pen = Character('Penguin King', color="#c8ffc8")
image penguin normal = "penguin_Looking_Left.png"
image penguin backwards = "turned_around_penguin"
# Tutorial character
define tut = Character("Nervous Man", color ="#a22342" )
image tutMug normal:
    "lousy_mugger.png"
    zoom 0.7
    yalign 0.48
image tutMug shocked:
    "batless_other_mugger.png"
    zoom 0.7
    yalign 0.48
image tutMug batless:
    "batless_mugger.png"
    zoom 0.7
    yalign 0.48
# Double mugging rash character
define doubleRash = Character('Mugger', color="#c8f4d8")
define doubleStalker = Character('Stalker', color="#2ce438")
# Define text baised characters
define narrator = Character(None, kind=nvl)
define game = Character(None, color="#e8ffe8")
define player = Character(None, color="#c8c8c8")
define player_nar = Character(None, kind=nvl, color="#c231d4")
 
# background images
image bg city:
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
image bg trap_door:
    "trap_door.jpg"
    zoom 1.6
image bg dev_men:
    "moon.jpg"
    zoom 1.7
image bg intersection = "city_intersection.jpg"
image bg black = "black_screen.png"
image bg brown = "brown_screen.png"
image bg white = "white_screen.png"
image bg gray = "gray_screen.png"

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

    
init:
    # create Varaibles
    $ money = 18.41  
    $ observed = False
    $ inspected = False
    $ forestCleared = False
    $ townCleared = False
    $ lost_bat = True
    
label start:
    stop music fadeout 2.0
    queue music "music/bg_music.mp3"
    jump chapterMenu
label chapterMenu: # developer menu
    scene bg dev_men at top
    menu:
        "Intro":
            jump intro
        "tutorialEncounter":
            jump preTut
        "Starting point":
             jump endTutorial
        "Double Mugging":
            scene bg forest
            jump doubleMugging
        "Forest Clear":
            $ forestCleared = True
            jump endTutorial
        "Penguin King":
            jump penguinEncounter
        "Ending":
            jump forestBaseDoor

    
############## The game starts here.
label intro:    
    scene bg black
    narrator "…"
    show headache
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
    player "I don’t remember a goddamned thing about myself..."
 
label firstChoice:
    scene bg cornfield
    if observed and inspected:
        pause
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
    the elements, but the bright lit moon gives you a clear vantage point of your
    surroundings.\n"
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
    scene bg cornfield
    play sound "audio/gust.mp3"
    game "A sudden gust of wind blows, violently swaying the corn around me.
    To my surprise, the overgrowth reveals a stout looking man crouched over, hiding
    with a baseball bat."
    
    show tutMug normal
    game "Realizing that his cover is blown, the man slowly steps out from his hiding
    spot and approaches you, bat held in an awkward striking stance."
    
label tutorialEncounter:
    tut "H-H-hey, you there."
    show tutMug normal
    tut "Ya you. G-gimme everything you've got"
    game "*Is this guy serious? He looks like he's only capable of mugging old ladies.
    Still, it would be quite troublesome getting hit by that bat.*"

label tutorialChoice:
    menu:
        "Drop the bat, before you hurt yourself":
            jump tutTrick
        "Look man, I don't want any trouble":
            jump tutFight
        "*Approach the man menacingly*":
            jump tutFrighten

            
label tutTrick:
    tut "W-w-whaddaya mean, hurt myself?"
    player "You don’t know? Approximately one out of ten people hurt themselves holding onto
    a baseball bat. Every minute, a person dies from blunt trauma to the head from a flying bat.
    In 1946, the NSA deemed the bat ‘The second most dangerous household object’, after
    the portable guillotine, of course."
    player "If you’re not careful with that death machine, you might even end up…"
    player "*You pause dramatically*"
    player "...DEAD" with hpunch
    tut "Whaaaaaaa!!! Get this deathtrap away from me!"
    hide tutMug
    game "With a start, the man tosses the bat into the air, whizzing through the trees before
    disappearing into the dark forest."
    show tutMug batless
    tut "T-t-thank you for saving me from that terrible thing. I’ll make sure to use
    something safer next time. You can keep your $[money]."
    player "Wait how do you know exaclty how much money I have on me"
    tut "You must not be from around here. E-E-everone in this town can smell m-m-m-money. 
    I wonder if you'll survive. I wish you G-g-g-good luck"
    jump endTutorial
    
label tutFight:
    $ lost_bat = False
    play sound "audio/Witches_Laugh.mp3"
    tut "Hahahahaha, Y-Y-You're in the wrong county if you didn't want any t-t-trouble"
    #rushing animation
    game "The man rushes you "
    #scene bg cornfield with 
    game "You roll to the side and manage to get out of the way before the bat strikes the
    ground where you were just standing. The man staggers from the recoil of the bat.
    As your feet touch the ground you spring onto the now vulerable man."
    #toppled man
    show tutMug shocked
    game "You miss judged the distance and the man is able to back off before you can
    knock him to the ground. He immediately regains his balance and.... runs away."
    hide tutMug
            
    game "You catch your breath and look at the baseball bat he left behind.  There is a
    crack running down the center of the bat making it completely useless. Suprised you
    walk over to it to get a closer look."
    game "Upon inspection you notice that the there is a strudy rock in the location
    where the man stuck the ground surrounded by tiny wooden splinters. It seems you
    lucked out this time but you should be catious. In the future you might not
    get a second chance."
    jump endTutorial

label tutFrighten:
    tut "D-D-Don’t come any closer! I’ll club ya tah death!"
    game "You continue to approach"
    tut "I-I-I m-mean it"
    game "You are withing arms reach of the man now"
    game "The man let's out a cry as he swings the bat towards you"
    tut "AAARRRHH!"
    game "You where able to block the swinging motion of the mans arms with your own."
    game "You stuggle with each other over control of the bat but in a swift motion you
    relinquish control of the bat and slam your body into the mans chest"
    
    show tutMug batless
    game "As the man tumbles to the floor his grip on the bat weakens and the bat is sent
    flying into the forest with astonishing speed."
    
    
    game "The man, now defenseless, sprints of out of sight"
    hide tutMug
    game "As the man leaves you let out a small sigh of relief"
    player "Glad I got rid of him"
    jump endTutorial
    
label endTutorial:
    scene bg cornfield
    menu:
        game "You are still standing in the middle of a corn field. Where will you go?"
        "Forest":
            if forestCleared:
                jump forestContinuation
            jump forestEnterance
        "Into Town":
            if townCleared:
                jump townContinuation
            jump townEnterance  

######################### Forest Enterance 
label forestEnterance:
     scene bg forest with longFade
     narrator "Narration occurs describing the forest"
     narrator "Naration of you walking into the forest and"
     narrator "Narration of being in the forest"
     narrator "Narration of moving to a new location"
     nvl clear
     
     scene bg white with wipeleft
     pause 0.75
     scene bg forest with wipeleft
     narrator "Narration new locations description. The old mugging trap spot"
     show headache
     narrator "Narration of what you can infer from the location"
     narrator "Narration of suspitous activity causing you to think someone might be
     following you but you brush it off"
     nvl clear
     
     scene bg white with blinds
     pause 0.75
     scene bg forest with blinds
     narrator "Narration of another possible old mugging trap spot"
     show headache
     narrator "Narration of what you think happened here"
     nvl clear
     game "Thoughts of you connecting the dots and what possibly happened in the forest.
     (also Possible time range i.e. withing the last 24 hours)"
     
################# Double Mugging Encounter
label doubleMuggingIntro:
     game "The prelude to a suprise attack"
     # Rash mugger appears centre screen
     game "Single mugger apearing"
     doubleRash "Threating dialouge"
     doubleRash "Muggin dialouge"
     game "susicious sounds from before"
     doubleRash "Huh, What's that?"
     # move the Rash mugger to the far right of the screen 
     game "You turn to the source of the sound and the second mugger comes from his
     hiding spot"
     # stalker mugger appears on the far left of the screen
     doubleStalker "Hold it."
     doubleStalker "Explains how he was following you to see if you would lead him to any
     other objects of value before muggin you but now his plan is ruined"
     doubleStalker "But that's okay I won't take your life, if you give me all the money you have"
     doubleRash " wait don't give him your money give it to me"
   
label doubleMugging:
    $forestCleared = True
    menu:
        "you guys got me but I can't give my money to both of you":
            jump dMugPass
        "Option 2":
            jump dMugPass
        "Option 3":
            jump dMugPass
        "None of you guys are getting anything":
            jump dMugFail
            
label dMugPass:
    game "The men are arguing amonst themselves. You hear them talk about the
    ogrinization and how they were both breaking rules in there confrontation."
    game "as they argue you start to slowly slip away into the forest behind you"
    game "One of the men swings his knife at the other and they break out into a knife fight"
    game "Not wanting to learn which man gets the honour of mugging you.
    You hastily escape from the muggers and run of into the forest"
    scene bg forest with quickFade
    game "You keep runnning until you're sure you've created enough distance"
    game "You expertly hide your tracks in a manner that suggests you have a lot of
    experience running away from dangerous people"
    game "After a few more minutes you begin to feel that you've succesfully escaped the
    muggers and are not in any danger of being tracked"
    jump forest
    
label dMugFail:
    doubleStalker "Hah, there isn't any sense in keeping you alive if you're going to resist"
    doubleRash "Hey, you're try to take all the money for yourself"
    doubleStalker "You can go kill him then. We can argue about the money later"
    # hide stalker mugger
    doubleRash "Hahahaa"
    game "The mugger rans at you with his knife laughing as he charges"
    show deathFilter
    show bloodSplatter at top
    game "*Animation of the man the killing player*"
    game ".:. Game Over"
    return

label forest:
    scene bg white with squares
    pause 0.75
    scene bg forest with squares
    narrator "You continue wandering through the forest, additional descriptions"
    if lost_bat:
        narrator "description of a loction in the forest. You find an object sticking out"
        narrator "As you get closer you realize it's a base ball bat. And not just any baseball bat.
        It was the baseBall bat the first mugger tried to use against you!"
        narrator "With all these muggers in town you decide it's best to hold on to the bat."
        # add bat to inventory
    else:
        narrator "you don't find anything else of particular interest as you walk through
        the forest"
    
    nvl clear
    scene bg white with quickFade
    scene bg forest with quickFade
    
    narrator "As you begin to feel that you're approaching the end of the forest your eye
    catches on an oddity near one fo the bushes"
    narrator "It seems the bushes wouldn't naturaly form this way. What amazing preception
    you must have in order to notice this irregularity."
    nvl clear
    
    scene bg trap_door with quickFade
    game  "You move the bushes aside to reveal a stone trapdoor behind the bushes"
    jump forestBaseDoor
        
################# Forest Continuation
label forestContinuation:
         scene bg forest with longFade
         narrator "Narration about walking back into the forest"
         narrator "going through where you thought you went last time and after a few minutes
         of uncertainty, you find your self back to the enterance of the base"
         jump forestBaseDoor
         
label forestBaseDoor:
    scene bg trap_door with quickFade
    game "You approach the Door and notice the lock"
    game "Looks like you won't be able to open this door unless you have a key."
    game "Looking up you realise you also can't go any deeper into the forest"
    menu:
    #if inv.has("base_key"):
        "use the iron key on the door" if True:
            jump enteringBase
        "Leave the forest":
            #play sound ""
            scene bg black with longFade
            scene bg cornfield with quickFade
            jump endTutorial
        
label enteringBase:
    game "Narration of unlocking the door with the key you pull from your pockets and
    opening it"
    play sound "audio/stone_door.wav"
    pause 0.65
    
    scene bg white with Dissolve(2.35)
    narrator "You step through the open trap door"
    nvl clear
    
    #For now
    narrator "Thank you for playing Part 1 of Don't get mugged. We hope you enjoyed it."
    narrator "Wait for Part 2 to complete the story."
    return
         
######################### Town Enterance
label townEnterance:
    scene bg park with quickFade:
        xalign 0.2
    player "Let's take a look in the town"
    scene bg park:
        xpos  -0.3
        easein 0.5 xpos -1.0
    narrator "narration about walking past the sign in the directions of town"
    nvl clear
    jump penguinEncounter
    
################# Penguin Encounter
label penguinEncounter:
    scene bg city at right with longFade
    narrator "Narration about the lights and city"
    narrator "The feeling of walking throuhg this town before "
    nvl clear
    pen "Who's there!"
    
    show penguin normal at center:
        zoom 0.5
    pen "I don't recognize you. What are you doing in my neighborhood?"

    menu:
        "I'm just trying to get home":
                jump penguinMugging
        
        "Your neighborhood? You mean MY neighborhood":
                jump penguinDeath
                
        "I've heard of a great King in this neighborhood and had come to see if the legends
        where true ":
                jump penguinPass
                
label penguinMugging:
    
    $ money = 0
    pen "Who do you think your are. Thinking you can enter my domain without
    paying a price."
    
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
    game "A minute after you see the Penguin King walk out of sight you move your hands
    under your body to try and pick yourself of the street and onto your feet"
    game "The moment you begin pushing with your arms you feel strong surge of pain go
    through your body. You groan but somehow manage to get onto your two feet. After
    wobbling a few times you take inventory of what you still have on you.\n"
    pen "The penguin King made sure to steal all the money you had on you but at least you
    still have your shoes "
    
    $ money = 0
    jump penguinsDomain
    
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
    player "The Legends don't do your grace justice. You're far more impressive a king in
    person"
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
    $ townCleared = true
    narrator ""
    scene bg intersection with quickFade
    
################# Town Continuation
label townContinuation:    
