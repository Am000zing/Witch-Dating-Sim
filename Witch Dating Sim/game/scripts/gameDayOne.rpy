from unittest import result


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



label quiz:
"Thank you. A name is important for witches, as names may hold great power."
"Before further embarking on this magical journey, I'd like to know a few things about you."

label q1:
menu:
    "Where you do draw your strength?"
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
menu:
    "You need to clear your head after a long day. What do you do?"
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
menu:
    "What is most important to you?"
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
menu:
    "You come across an ancient altar. What do you offer to it?"
        "Tea imbued with leaves that have healing properties":
            $ summerAP += 1
            jump q5
        "A candle that, when lighted, never burns out":
            $ elunaAP += 1
            jump q5
        "The quill, made from a phoenix feather, used to write tomes"
            $ celesteAP += 1
            jump q5

label q5:
menu:
    "What do you fear the most?"
        "Isolation":
            $ elunaAP += 1
            jump quizEnd
        "Darkness" (Celeste)
            $ celesteAP += 1
            jump quizEnd
        "Destruction" (Summer)
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
        if solis:
            jump houseSolis
        if luna:
            jump houseLuna


label houseSolis:
"House Solis!"

label houseLuna:
"House Luna!"

label houseStella:
"House Stella!"