label day3Luna:
    scene dCommons with Fade(2.0,1.0, 2.0)
    "Yesterday was quite eventful."
    "Hopefully, things will get better soon."
    "I already feel the keen scrutiny of Professor Morgana..."
    e "Hey, [name]."
    show eluna Neutral with dissolve
    "It's Eluna."
    e Neutral "Let's go run lines today."
    "Right, she had asked if I could run lines with her yesterday."
    "I definitely need the practice."
    char "Yeah, of course! I kept the script in my bag so I wouldn't forget."

    e Smile "Good! You're prepared."
    e Neutral "Where would you like to go practice today?"
    e "We can go to either the Greenhouse or the Library"

    menu:
        "Let's go to the Greenhouse.":
            jump greenhousePath
        "Let's go to the Library.":
            jump libraryPath
    
label greenhousePath:
    e "Sounds good. Let's head on over to the Greenhouse then."
    hide eluna Neutral with dissolve
    scene greenhouse with Fade(2.0, 0.0, 2.0)
    "We arrive at the Greenhouse."
    "I see someone that I remember passing by in the Commons."
    show summer Neutral with dissolve 
    unknown "Hey, Eluna! How are you?"
    show summer Neutral at left with move
    show eluna Neutral at right with dissolve
    show s inactive at left
    e "Hello, Summer. How has work in the Greenhouse been?"
    hide s inactive
    show e inactive at right
    unknown "Just as lovely as ever!"
    "The greenhouse girl peers over at me."
    unknown "You must be the new Luna student!"

    "I look at her, stunned."
    char "Ah, yeah! I am, yeah."
    s Neutral "Nice to meet you! I'm Summer."
    hide e inactive
    show s inactive at left
    e "I was thinking we could stay here for a little bit to practice lines for the Ritual."
    hide s inactive
    show e inactive at right
    s Smile "Of course! It's closed to students today, but I can make an exception."
    s Neutral "Professor Tasha won't mind."
    hide e inactive
    show s inactive at left
    e "Thank you, Summer."

    "Eluna turns to me."
    e Upset "I need to go check on something outside the Greenhouse."
    e Neutral "Could you wait a little bit for me?"
    char "Oh, yeah, that's no problem."
    e Smile "Thank you."
    e Neutral "I'll be right back."
    "Eluna briskly walks away."
    hide eluna Neutral with Dissolve(2.0)
    s Neutral "So..."
    show summer Neutral at center with move
    s "What do you think of the Academy so far?"
    s Upset "I've heard stories about how Professor Morgana can give new witches a hard time."
    s Neutral "I hope that isn't the case!"
    menu:
        "Well...":
            $ lunaAP += 3
            char "Professor Morgana definitely hasn't been giving me an easy time."
            s Smile "Ahaha! Sounds like her."
            s Neutral "At least you're working closely with Eluna."
        "It's been fine.":
            $ lunaAP += 2
            s Smile "That's good!"
            s Neutral "Although, you shouldn't feel pressured to appear like everything's okay when it's not."
            s "You're lucky you get to work with Eluna, though."

    s Neutral "Eluna always gives herself a lot of work."
    s Smile "So I hope you can continue to take care of her."
    char "What do you mean by that?"
    e "Sorry for taking so long."
    show summer Neutral at left with move
    show eluna Neutral at right with dissolve
    "Eluna walks into the Greenhouse."
    char "Oh, it's no problem."
    show e inactive at right
    s Smile "Welcome back! We were just chatting about school experiences so far."
    hide e inactive
    show s inactive at left
    e "Ah, I see."
    e "Well, I hope you two had a good time."
    e "Let's get to running our lines together."
    e "There should be no distractions or interruptions since it's closed, so this should go smoothly."
    ##Fade scene
    jump day3FinalPathLuna

label libraryPath:
    e "Sounds good! Let's head on over to the library then."
    scene library with Fade(2.0, 0.0, 2.0)
    "We show up at the Library."
    "I see someone that I remember briefly passing by in the Commons."
    show eluna Neutral with dissolve
    e "Hello, Celeste. How are you?"
    ##show celesteNeutral 
    show eluna Neutral at left with move
    show celeste Neutral at right with dissolve
    unknown "Oh! Hi, Eluna."
    show c inactive at right
    e "I'm sorry, I shouldn't have snuck up on you like that."
    hide c inactive
    show e inactive at left
    unknown "Oh, um, it's not a problem."
    hide e inactive
    show c inactive at right
    e "Have you said hi to [name] yet? They're the new Luna student."
    "I swallow hard and prepare to speak…"
    hide c inactive
    show e inactive at left
    unknown "Oh… of course I know them."
    unknown "You must be [name]."
    char "Oh, yeah, I am!"
    c Neutral "I'm Celeste."
    hide e inactive
    show c inactive at right
    e "We were going to stay in the library for a little bit to practice lines for the Ritual."
    hide c inactive
    show e inactive at left
    c Smile "You're at the perfect place for some pure concentration."
    hide e inactive
    show c inactive at right
    e Smile "Aha, of course you'd find the library to be the perfect place…"
    ##show celesteUpsetB 
    hide c inactive
    show e inactive at left
    c Upset "..."
    hide e inactive
    show c inactive at right
    e Smile "I'm just teasing, of course."
    "It feels a little warm in here..."
    e Neutral "Sorry, [name], I need to go check on something by the Greenhouse for a little bit."
    e "I'll be right back."
    hide eluna Neutral with Dissolve(2.0)
    "Eluna briskly walks away."
    show celeste Upset at center with move
    c Neutral "How has your time been with House Luna so far?"
    c "To my understanding, Professor Morgana is one of the more stricter professors here at Luminoire."
    c "I hope she hasn't been giving you a hard time."
    menu:
        "Well...":
            $ elunaAP += 3
            char "Professor Morgana hasn't been giving me the easiest time so far."
            c "I see."
            c "That's understandable, although it's interesting that she's chosen you to be Eluna's supporting lead."
            char "How did you...?"
            c Smile "News spreads quite quickly across the Academy."
            c Neutral "Especially news about Eluna."
            char "Well, Eluna seems like quite the popular student."
        "It's been fine so far.":
            $ elunaAP += 2
            c "You don't need to lie about your experience, most of us know the truth anyways."
            char "Lying? I-"
            "I stumble over my words to defend myself."
            c "It's understandable though."
            c "Interesting, though, that Professor Morgana chose you to be Eluna's supporting lead."
            "How did she know? That happened just yesterday!"
            c Smile "News spreads quite quickly across the Academy, you know?"
            c Neutral "Especially news about Eluna."
            char "Eluna seems like quite the popular student."
    
    c Neutral "For good reason, too."
    c "Although it might be expected a student pending to graduate would already be quite knowledgeable-"
    c "Eluna has always been at the top of her class."
    c Smile "She might come off as distant when you first meet her, but she means well."
    c Neutral "She's always valued family and community, and it's really admirable how hard-working she is."
    e "[name], sorry for taking so long."
    c "Oh!"
    "Eluna enters quickly into the library."
    ##show celesteNeutralB
    show celeste Neutral at left with move
    show eluna Neutral at right with dissolve
    show c inactive at left
    e Neutral "What were you two up to?"
    hide c inactive
    show e inactive at right
    c Upset "N-nothing!"
    c "You both need to go practice for the Ritual right?"
    c "I should go study. Professor Circe must be expecting me anyways."
    hide celeste Neutral with dissolve
    "Celeste runs out of the library."
    hide e inactive with dissolve
    show eluna Neutral at center with move
    e "Hm..."
    e "Well, [name], let's run our lines."
    e Smile "It's nice and quiet in the library, so this should go smoothly without interruptions."
    ##fade Scene
    jump day3FinalPathLuna

label day3FinalPathLuna:
    #Scene with Fade
    scene library with Fade(3.0, 0.0, 2.0)
    with Pause(3.0)
    show eluna Neutral with dissolve
    e "It's getting late."
    e "Let's clean up and call it a day, okay?"
    e Smile "You've practiced hard today."
    char "Thanks for helping me!"
    e Neutral "Of course, anytime."
    e "..."
    e Smile "By the way, I do appreciate you accepting my request to come practice with me."
    e "And I also appreciate you socializing a bit with my friends."
    char "Oh, it's no problem, really."
    e Neutral "Ah...yes, of course. Not a problem."
    "...Did I say something off?"
    char "I'm sorry if I said something-"
    e Upset "No!"
    e Neutral "No, you didn't say anything wrong."
    e Smile "I wanted to ask you if you wanted to watch my rehearsal tomorrow at the Amphitheater."
    char "Yeah, of course I'll be there."
    "Isn't all of House Luna going to be there?"
    e "Great!"
    e Neutral "I'll see you tomorrow then."
    char "Alright!"
    char "See you then."
    hide eluna Neutral with dissolve(2.0)
    "That was...interesting."
    "Well, I should get going anyways."
    "I gotta make sure I'm at the Amphitheater a little earlier anyways."
    #perfect run: 10
    scene black with Dissolve(3.0)
    show text "Day 4" with dissolve
    play sound dingDong1 fadein 3.0 volume 0.25
    with Pause(3.0)
    show text "1 Day Until the Full Moon Ritual..." with dissolve
    with Pause(3.0)
    jump day4Luna