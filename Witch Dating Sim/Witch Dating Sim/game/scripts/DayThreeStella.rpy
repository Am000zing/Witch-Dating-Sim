label day3Stella:
    play sound "..\\audio\\SFX\\SchoolBell1.wav"
    scene black with Fade(2.0, 2.0, 2.0)
    with Pause(1.0)
    "Huh, I'm in my room."
    "The last thing I remember was studying with Celeste..."
    "Oh no, I must've fallen asleep!"
    "How did I get in my room anyways...?"
    c "Hello? [name]?"
    c "Are you alright in there?"
    char "Y-yes, give me a second."
    scene Commons with Fade(2.0, 1.0, 2.0)
    "I dash out to the Commons."
    char "I'm sorry, I'm not sure what happened."
    show celeste Neutral with dissolve
    c "Oh, no worries."
    c "You passed out after an hour of reading."
    c "You seemed to have really fallen asleep, so I took you back."
    "Did she carry me? Is she that strong?"
    c "I'm not as adept as Eluna in my magical prowess-"
    c "But I managed to do some short transportation hops across campus."
    char "I'm so sorry, that must've been really out of the way for you."
    c Smile "I actually thought it was really funny you fell asleep."
    c "You've gotta learn to keep up with me."
    c Neutral "Speaking of keeping up..."
    c "I wanted to go to the Greenhouse today to check out the flowers."
    c "Flower language can be quite important, and it may be useful in understanding Luminoire much better."
    char "Ah, I see."
    c Smile "Hurry up and get ready to go out."
    c Neutral "I'll wait here in the Commons for you."
    char "Got it, it'll only be a minute."
    "I scramble to get ready for the day."
    "I've already got a quest to do!"
    scene Commons with Fade(1.0, 0.0, 1.0)
    "After freshening up, I go find Celeste in the Commons."
    "When Celeste notices me, she closes the book she's reading."
    show celeste Neutral with dissolve
    c "Ready to go?"
    char "Ready when you are."
    c "Great!"
    c "Let's go to the Greenhouse."
    hide celeste Neutral with dissolve

    scene greenhouse with Fade(2.0, 0.0, 2.0)
    show celeste Neutral with dissolve
    c "Here we are!"
    c "Although the Greenhouse isn't as precisely organized as the library-"
    c Smile "-there's a certain charm to its...organized mess."
    unknown "Are you bad-mouthing my Greenhouse?"
    c Neutral "P-professor Tasha!"
    show celeste Neutral at left with move
    show tasha Neutral at right with dissolve
    show t inactive at right
    c Neutral "It's not bad-mouthing, it's just an observation I've made."
    hide t inactive
    show c inactive at left
    t "I'm just joking, no need to take me so seriously."
    t "I was just about to head out for lunch, so if you need anything, ask Summer."
    hide c inactive
    show t inactive at right
    c "Got it!"
    "Professor Tasha looks over at me."
    hide t inactive
    show c inactive at left
    t Neutral "Make sure her head is screwed on, alright?"
    hide tasha Neutral with dissolve
    hide c inactive with dissolve
    "Tasha leaves the Greenhouse, chuckling to herself."
    show celeste Neutral at center with move
    c Upset "I can't believe she heard me say that..."
    unknown "You're not exactly good at keeping all your observations to yourself, you know?"
    show celeste Neutral at left with move
    show summer Neutral at right with dissolve
    show c inactive at left with dissolve
    unknown "You really should work on that, some people can take it the wrong way."
    hide c inactive
    show s inactive at right
    c "The opinions of others are not of primary concern, Summer."
    hide s inactive
    show c inactive at left
    "Summer sighs deeply."
    s "It's not about being concerned of other people's opinions."
    s "Nevermind that, what're you up to in the Greenhouse?"
    hide c inactive
    show s inactive at right
    c "I wanted to do some research in flower language."
    "Celeste holds up the book she was reading earlier in the Commons."
    c "I found a book that explains a little bit on flower language, and wanted to do some research on what Luminoire's native flowers were."
    hide s inactive
    show c inactive at left
    s "Well, you're in luck!"
    s "The garden outside has just bloomed with some beautiful seasonals."
    s "You can go take a look-"
    s "-just don't fall over into the bushes again."
    hide c inactive
    show s inactive at right
    c Upset "You..."
    ##show celesteUpsetB
    char "Did something happen before?"
    hide s inactive
    show c inactive at left
    s "Well-"
    hide c inactive
    show s inactive at right
    c Upset "No!"
    c "Nothing happened."
    c "I'm going to be in the garden for a bit."
    hide celeste Upset with dissolve
    hide s inactive with dissolve
    "Celeste briskly leaves the Greenhouse."
    show summer Neutral at center with move
    s "Celeste is really something, isn't she?"
    menu:
        "\"She really is.\"":
            $ celesteAP += 2
            s "Oh?"
            s Smile "You'd better hope she didn't hear you say that."
            s Neutral "She normally isn't okay with teasing."
            s "We're pretty close, so I'm not so concerned with her perception of me-"
            s Upset "-as it's been established a while ago."
            "Summer looks out the window to where Celeste is and sighs."
            s "It's funny..."
            s "Despite Celeste and I being the same age and year-"
            s "- She puts {i}so{/i} much pressure on herself to be more knowledgeable than any other witch here."
            s Neutral "Make sure you watch over her, okay?"
            "Watch over her?"
            "I wonder what she means by that..."
        "\"What do you mean?\"":
            $ celesteAP += 3
            s Upset "She takes herself so seriously."
            s "I wish she'd think about just decompressing for a little bit."
            s Smile "I'm glad though that she's taken a liking to you."
            char "You think she has?"
            s Neutral "Oh yeah."
            s "It might seem like she's just dragging you along for her research-"
            s "-And you wouldn't be wrong on that presumption-"
            s "-but, much like research, consistency is key."
            s "I hope you continue to take care of her."
            "Take care of her?"
            "I wonder what she means by that..."
    
    c "[name]! [name]!"
    "Celeste dashes into the Greenhouse, nearly out of breath."
    show summer Neutral at left with move
    show celeste Neutral at right with moveinright
    show s inactive at left
    c "I've made some incredible observations!"
    c Smile "I've jotted them all down in my notebook, I'll show it to you later."
    hide s inactive
    show c inactive at right
    s "Well you certainly seem excited."
    hide c inactive
    show s inactive at left
    c "The garden was especially beautiful today."
    c "I've brought some flowers with me too."
    if celesteAP == 11:
        $ cperfect = true
        c Smile "Here, I picked one for you!"
        #show violet at center
        "She hands me a vibrant violet."
        c Neutral "Isn't this such a perfect flower?"
        char "Yeah, it's very pretty."
        "I can feel Summer peering over at us..."
        "My face feels really warm..."
        hide s inactive
        show c inactive at right
        s "That's very sweet of you to do, Celeste."
    else:
        hide s inactive
        show c inactive at right
        s Upset "Oh, you picked flowers from the garden?"
        hide c inactive
        show s inactive at left
        c "There were so many, I'm sure it's fine."
        hide s inactive
        show c inactive at right
        s Upset "Alright, but next time please as first."
        hide c inactive
        show s inactive at left
        c "Got it!"
        c Upset "Sorry, Summer. I know how much that bothers you."
        c Neutral "The results will be worth it, I swear!"
        hide s inactive
        show c inactive at right
        s Neutral "Alright..."
    
    hide c inactive
    show s inactive at left
    c "We should head back to the Commons."
    "Celeste tightens her grip on the book."
    c "There's a lot I need to tell you!"
    hide s inactive
    show c inactive at right
    s Neutral "Don't trip on your way back."
    hide c inactive
    hide celeste Neutral with dissolve
    "Celeste makes her way out of the Greenhouse."
    "I turn to follow her and-"
    show summer Neutral at center with move
    s "Remember what I told you."
    "I look back at Summer."
    "Her stare is unwavering."
    s Smile "Have fun!"
    hide summer Smile with dissolve 
    "Summer briskly leaves the Greenhouse as well, making her way to the garden."
    "Well, that was an eventful day."
    "I need to catch up with Celeste..."
    char "Wait up!"

    jump day4Stella