label start:
$renpy.music.stop(fadeout = 5.0)
python:
    name = renpy.input("Before we begin our journey, what is your name?")
    name.strip()
#if name == "Leilia" or name == "leilia":
#    $ name = "Master"
#    menu:
#        "Which day do you want to jump to?"
#            "Day One":
#                jump dayOne
#            "Day Two":
#                jump dayTwo

if name == "Gamespawn" or name == "gamespawn":
    $ name = "Great Grandmaster"
    menu:
        "Which path do you want to jump to?"
        "Luna House":
            jump lunaHouseOptions
        "Stella House":
            jump stellaHouseOptions
        "Solis House":
            jump solisHouseOptions

menu:
    "Your name is [name], correct?"
    "Yes":
        jump quiz
    "No":
        jump start



label lunaHouseOptions:
    menu:
        "1 Luna":
            $ solis = False
            $ stella = False
            $ luna = True
            jump day1Luna
        "2 Luna":
            $ solis = False
            $ stella = False
            $ luna = True
            jump day2Luna
        "3 Luna":
            $ solis = False
            $ stella = False
            $ luna = True
            jump day3Luna
        "4 Luna":
            $ solis = False
            $ stella = False
            $ luna = True
            jump day4Luna
        "5 Luna":
            $ solis = False
            $ stella = False
            $ luna = True
            jump day5

label stellaHouseOptions:
    menu:
        "1 Stella":
            $ luna = False
            $ solis = False
            $ stella = True
            jump day1Stella
        "2 Stella":
            $ luna = False
            $ solis = False
            $ stella = True
            jump day2Stella
        "3 Stella":
            $ luna = False
            $ solis = False
            $ stella = True
            jump day3Stella
        "4 Stella":
            $ luna = False
            $ solis = False
            $ stella = True
            jump day4Stella
        "5 Stella":
            $ luna = False
            $ solis = False
            $ stella = True
            jump day5

label solisHouseOptions:
    menu:
        "1 Solis":
            $ luna = False
            $ stella = False
            $ solis = True
            jump day1Solis
        "2 Solis":
            $ luna = False
            $ stella = False
            $ solis = True
            jump day2Solis
        "3 Solis":
            $ luna = False
            $ stella = False
            $ solis = True
            jump day3Solis
        "4 Solis":
            $ luna = False
            $ stella = False
            $ solis = True
            jump day4Solis
        "5 Solis":
            $ day4lunaGood = True
            $ luna = False
            $ stella = False
            $ solis = True
            jump day5

label quiz:
play music introQuizMusic  fadein 10.0
#volume 0.5
"Thank you. A name is important for witches, as names may hold great power."
"Before further embarking on this magical journey, I'd like to know a few things about you."

#scene

label q1:
"Where do you draw your strength?"
menu:
        "My kindness":
            $ solisPoint += 1
            jump q2
        "My knowledge":
            $ stellaPoint += 1
            jump q2
        "My charm":
            $ lunaPoint += 1
            jump q2

label q2:
"You need to clear your head after a long day. What do you do?"
menu:
        "Walk through the gardens":
            $ solisPoint += 1
            jump q3
        "Read a book":
            $ stellaPoint += 1
            jump q3
        "Confide in a friend":
            $ lunaPoint += 1
            jump q3

label q3:
"What is most important to you?"
menu:
        "Community":
            $ lunaPoint += 1
            jump q4
        "Creation":
            $ solisPoint += 1
            jump q4
        "Truth":
            $ celesteAP += 1
            jump q4

label q4:
"You come across an ancient altar. What do you offer to it?"
menu:
        "Tea imbued with leaves that have healing properties":
            $ solisPoint += 1
            jump q5
        "A candle that, when lighted, never burns out":
            $ lunaPoint += 1
            jump q5
        "The quill, made from a phoenix feather, used to write tomes":
            $ stellaPoint += 1
            jump q5

label q5:
"What do you fear the most?"
menu:
        "Isolation":
            $ lunaPoint += 1
            jump quizEnd
        "Darkness":
            $ stellaPoint += 1
            jump quizEnd
        "Destruction":
            $ solisPoint += 1
            jump quizEnd

label quizEnd:
"The witch house you will be a part of is..."
#if most points is elunaAP, then jump houseLuna
#if most points is celesteAP, then jump houseStella
#if most points is summerAP, then jump houseSolis
#if tied, choose random between the two options
if lunaPoint >= 3:
    jump houseLuna

elif solisPoint >= 3:
    jump houseSolis

elif stellaPoint >= 3:
    jump houseStella

elif lunaPoint == solisPoint:
    $ SLrandom = renpy.random.choice(['solis', 'luna'])
    if SLrandom == 'solis':
        jump houseSolis
    if 'luna':
        jump houseLuna

elif lunaPoint == stellaPoint:
    $ SLrandom = renpy.random.choice(['stella', 'luna'])
    if SLrandom == 'stella':
        jump houseStella
    if 'luna':
        jump houseLuna

elif solisPoint == stellaPoint:
    $ SLrandom = renpy.random.choice(['stella', 'solis'])
    if SLrandom == 'stella':
        jump houseStella
    if 'solis':
        jump houseSolis


label houseSolis:
    "House Solis!"
    $ luna = False
    $ stella = False
    $ solis = True

    jump day1Solis

label houseLuna:
    "House Luna!"
    $ solis = False
    $ stella = False
    $ luna = True

    jump day1Luna

label houseStella:
    "House Stella!"
    $ luna = False
    $ solis = False
    $ stella = True
    jump day1Stella
