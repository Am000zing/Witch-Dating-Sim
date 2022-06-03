label day3Luna:
    play sound "..\\audio\\SFX\\SchoolBell1.wav"
    "Yesterday was quite eventful."
    "Hopefully, things will get better soon."
    "I already feel the keen scrutiny of Professor Morgana..."
    e "Hey, [name]."
    ##show elunaNeutral with move right

    "It's Eluna."
    e "Let's go run lines today."
    "Right, she had asked if I could run lines with her yesterday."
    "I definitely need the practice."
    char "Yeah, of course! I kept the script in my bag so I wouldn't forget."

    e "Good! You're prepared."
    e "Where would you like to go practice today?"
    e "We can go to either the Greenhouse or the Library"

    menu:
        "Let's go to the Greenhouse.":
            jump greenhousePath
        "Let's go to the Library.":
            jump libraryPath
    
label greenhousePath:
    e "Sounds good. Let's head on over to the Greenhouse then."

    "We arrive at the Greenhouse."
    "I see someone that I remember passing by in the commons."
    ##show summerSmile with fade 
    unknown "Hey, Eluna! How are you?"
    e "Hello, Summer. How has work in the Greenhouse been?"
    unknown "Just as lovely as ever!"
    "The greenhouse girl peers over at me."
    unknown "You must be the new Luna student!"

    "I look at her, stunned."
    char "Ah, yeah! I am, yeah."
    s "Nice to meet you! I'm Summer."
    e "I was thinking we could stay here for a little bit to practice lines for the Ritual."
    s "Of course! It's closed to students today, but I can make an exception."
    s "Professor Tasha won't mind."
    e "Thank you, Summer."

    "Eluna turns to me."
    e "I need to go check on something outside the Greenhouse."
    e "Could you wait a little bit for me?"
    char "Oh, yeah, that's no problem."
    e "Thank you."
    e "I'll be right back."
    "Eluna briskly walks away."

    s "So..."
    ##show summerNeutral 
    s "What do you think of the Academy so far?"
    s "I've heard stories about how Professor Morgana can give new witches a hard time."
    s "I hope that isn't the case!"
    menu:
        "Well...":
            char "Professor Morgana definitely hasn't been giving me an easy time."
            s "Ahaha! Sounds like her."
            s "At least you're working closely with Eluna."
        "It's been fine.":
            s "That's good!"
            s "Although, you shouldn't feel pressured to appear like everything's okay when it's not."
            s "You're lucky you get to work with Eluna, though."

    s "Eluna always gives herself a lot of work."
    s "So I hope you can continue to take care of her."
    char "What do you mean by that?"

    e "Sorry for taking so long."
    "Eluna walks into the Greenhouse."
    char "Oh, it's no problem."
    s "Welcome back! We were just chatting about school experiences so far."
    e "Ah, I see."
    e "Well, I hope you two had a good time."
    e "Let's get to running our lines together."
    e "There should be no distractions or interruptions since it's closed, so this should go smoothly."
    ##Fade scene
    jump day3FinalPathLuna

label libraryPath:
    e "Sounds good! Let's head on over to the library then."

    "We show up at the Library."
    "I see someone that I remember briefly passing by in the Commons."
    e "Hello, Celeste. How are you?"
    ##show celesteNeutral 
    unknown "Oh! Hi, Eluna."
    e "I'm sorry, I shouldn't have snuck up on you like that."
    unknown "Oh, um, it's not a problem."
    e "Have you said hi to [name] yet? They're the new Luna student."
    "I swallow hard and prepare to speak…"
    unknown "Oh… of course I know them."
    unknown "You must be [name]."
    char "Oh, yeah, I am!"
    c "I'm Celeste."

    e "We were going to stay in the library for a little bit to practice lines for the Ritual."
    c "You're at the perfect place for some pure concentration."
    ##show elunaSmile 
    e "Heheh. Of course you'd find the library to be the perfect place…"
    ##show celesteUpsetB 
    c "..."
    e "I'm just teasing, of course."
    "It feels a little warm in here..."

    e "Sorry, [char], I need to go check on something by the Greenhouse for a little bit."
    e "I'll be right back."
    "Eluna briskly walks away."

    c "How has your time been with House Luna so far?"
    c "To my understanding, Professor Morgana is one of the more stricter professors here at Luminoire."
    c "I hope she hasn't been giving you a hard time."
    menu:
        "Well...":
            char "Professor Morgana hasn't been giving me the easiest time so far."
            c "I see."
            c "That's understandable, although it's interesting that she's chosen you to be Eluna's supporting lead."
            char "How did you...?"
            c "News spreads quite quickly across the Academy."
            c "Especially news about Eluna."
            char "Well, Eluna seems like quite the popular student."
        "It's been fine so far.":
            c "You don't need to lie about your experience, most of us know the trust anyways."
            char "Lying? I-"
            "I stumble over my words to defend myself."
            c "It's understandable though."
            c "Interesting, though, that Professor Morgana chose you to be Eluna's supporting lead."
            "How did she know? That happened just yesterday!"
            c "News spreads quite quickly across the Academy, you know?"
            c "Especially news about Eluna."
            char "Eluna seems like quite the popular student."
    
    c "For good reason, too."
    c "Although it might be expected a student pending to graduate would already be quite knowledgeable-"
    c "Eluna has always been at the top of her class."
    c "She might come off as distant when you first meet her, but she means well."
    c "She's always valued family and community, and it's really admirable how hard-working she is."
    e "[name], sorry for taking so long."
    "Eluna enters quickly into the library."
    c "Oh!"
    ##show celesteNeutralB
    e "What were you two up to?"
    c "N-nothing!"
    c "You both need to go practice for the Ritual right?"
    c "I should go study. Professor Circe must be expecting me anyways."
    "Celeste runs out of the library."
    e "Hm..."
    e "Well, [name], let's run our lines."
    e "It's nice and quiet in the library, so this should go smoothly without interruptions."
    ##fade Scene
    jump day3FinalPathLuna

label day3FinalPathLuna:
    #Scene with Fade 
    e "It's getting late."
    e "Let's clean up and call it a day, okay?"
    e "You've practiced hard today."
    char "Thanks for helping me!"
    e "Of course, anytime."
    e "..."
    e "By the way, I do appreciate you accepting my request to come practice with me."
    e "And I also appreciate you socializing a bit with my friends."
    char "Oh, it's no problem, really."
    e "Ah...yes, of course. Not a problem."
    "...Did I say something off?"
    char "I'm sorry if I said something-"
    e "No!"
    e "No, you didn't say anything wrong."
    e "I wanted to ask you if you wanted to watch my rehearsal tomorrow at the Amphitheater."
    char "Yeah, of course I'll be there."
    "Isn't all of House Luna going to be there?"
    e "Great!"
    e "I'll see you tomorrow then."
    char "Alright!"
    char "See you then."
    "Eluna glides across the library/greenhouse and exits."
    "That was...interesting."
    "Well, I should get going anyways."
    "I gotta make sure I'm at the Amphitheater a little earlier anyways."
    ##hide Scene with Fade
    show text "Day 4 Solis" with dissolve
    show text "1 Day Until the Blood Moon Ritual..." with dissolve
    jump day4Luna