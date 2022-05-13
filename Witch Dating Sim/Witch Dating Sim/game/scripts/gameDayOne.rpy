label start:
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

menu:
    "Your name is [name], correct?"
    "Yes":
        jump quiz
    "No":
        jump start

if name == "Gamespawn" or name == "gamespawn":
    $ name = "Great Grandmaster"
    menu:
        "Luna House":
            jump lunaHouseOptions
        "Stella House":
            jump stellaHouseOptions
        "Solis House":
            jump solisHouseOptions


label lunaHouseOptions:
    menu:
        "1 Luna":
            jump day1Luna
        "2 Luna":
            jump day2Luna
        "3 Luna":
            jump day3Luna
        "4 Luna":
            jump day4Luna
        "5 Luna":
            jump day5Luna

label stellaHouseOptions:
    menu:
        "1 Stella":
            jump day1Stella
        "2 Stella":
            jump day2Stella
        "3 Stella":
            jump day3Stella
        "4 Stella":
            jump day4Stella
        "5 Stella":
            jump day5Stella

label solisHouseOptions:
    menu:
        "1 Solis":
            jump day1Solis
        "2 Solis":
            jump day2Solis
        "3 Solis":
            jump day3Solis
        "4 Solis":
            jump day4Solis
        "5 Solis":
            jump day5Solis

label quiz:
play music introQuizMusic volume 0.5
"Thank you. A name is important for witches, as names may hold great power."
"Before further embarking on this magical journey, I'd like to know a few things about you."

#scene

label q1:
"Where do you draw your strength?"
menu:
        "My kindness":
            $ summerAP += 1
            jump q2
        "My knowledge":
            $ celesteAP += 1
            jump q2
        "My charm":
            $ elunaAP += 1
            jump q2

label q2:
"You need to clear your head after a long day. What do you do?"
menu:
        "Walk through the gardens":
            $ summerAP += 1
            jump q3
        "Read a book":
            $ celesteAP += 1
            jump q3
        "Confide in a friend":
            $ elunaAP += 1
            jump q3

label q3:
"What is most important to you?"
menu:
        "Community":
            $ elunaAP += 1
            jump q4
        "Creation":
            $ summerAP += 1
            jump q4
        "Truth":
            $ celesteAP += 1
            jump q4

label q4:
"You come across an ancient altar. What do you offer to it?"
menu:
        "Tea imbued with leaves that have healing properties":
            $ summerAP += 1
            jump q5
        "A candle that, when lighted, never burns out":
            $ elunaAP += 1
            jump q5
        "The quill, made from a phoenix feather, used to write tomes":
            $ celesteAP += 1
            jump q5

label q5:
"What do you fear the most?"
menu:
        "Isolation":
            $ elunaAP += 1
            jump quizEnd
        "Darkness":
            $ celesteAP += 1
            jump quizEnd
        "Destruction":
            $ summerAP += 1
            jump quizEnd

label quizEnd:
"The witch house you will be a part of is..."
#if most points is elunaAP, then jump houseLuna
#if most points is celesteAP, then jump houseStella
#if most points is summerAP, then jump houseSolis
#if tied, choose random between the two options
if elunaAP >= 3:
    jump houseLuna

elif summerAP >= 3:
    jump houseSolis

elif celesteAP >= 3:
    jump houseStella

elif elunaAP == summerAP:
    $ SLrandom = renpy.random.choice(['solis', 'luna'])
        if SLrandom = solis:
            jump houseSolis
        if luna:
            jump houseLuna


label houseSolis:
"House Solis!"
$ solis = true
jump intro

label houseLuna:
"House Luna!"
$ luna = true
jump intro

label houseStella:
"House Stella!"
$ stella = true
jump intro


label intro:
"nice."
jump day1Solis
jump day1Luna
