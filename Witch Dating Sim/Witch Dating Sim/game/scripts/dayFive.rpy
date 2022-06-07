label day5:
    scene dCommons with Fade (2.0, 1.0, 2.0)
    with Pause (2.0)
    "Tonight's the night: the Full Moon Ritual!"
    "House Stella, Luna, and Solis come together to celebrate tonight."
    "I can't lose rhythm now!"
    play sound chatter volume 0.2 fadein 6.0
    "Excitement fills the air of the Commons."
    student1 "I heard Eluna of House Luna is going to be performing the rites!"
    student2 "I bet she's going to be incredible!"
    student1 "She's always incredible."
    student3 "Well, I heard Summer of House Solis prepared a super sweet offering."
    student4 "Too bad we can't try whatever she's made..."
    student5 "I saw Celeste of House Stella running around Academy campus a lot this week."
    student5 "She left the library a few times!"
    student6 "I wonder if she has something up her sleeve..."

    "Everyone seems pretty excited for tonight."
    play sound doorslam
    "The doors to the Commons open."
    "Shoulder-to-shoulder, the three professors of each House enter."
    #show all 3 professors lined up
    show morgana Neutral at right 
    show tasha Neutral at center 
    show circe Neutral at left
    with dissolve
    m "Witches!"
    m "I hope you all are as excited for tonight's Full Moon Ritual as I am."
    m "I'd like to ask all of you to join us at the Amphitheater half past noon."
    t "We'll be working together to decorate and prepare for tonight's ritual."
    t "Don't worry, we'll have snacks."
    t Smile "We're not interested in working you to the bone."
    k Upset "Unless..."
    k Smile "I jest, of course."
    k Neutral "Now, everyone can go get ready-"
    k "Prepare your offering for the Full Moon ritual."
    k "We'll see you all soon."

    scene amphitheater1 with Fade(2.0, 0.0, 2.0)
    "I arrive at the Amphitheater."
    "It's filled with the hustle and bustle of witches of all houses anticipating tonight's event."
    "Caught up in the excitement of the ritual, I feel a light tap on my shoulder -"
    if(solis == True):
        show summer Neutral with dissolve
        s Smile "Heya, [name]!"
        s "I'm happy to see you."
        s Neutral "What do you think of the Amphitheater?"
        s "I hope everyone likes it."
        if(day4solisGood == True):
            s Smile "Thank to you and the other Luna students, we were able to finish decorating in no time!"
        else:
            s "We spent all of yesterday getting the decorations done, so it better be worth it!"
        s Neutral "What are you most excited for in tonight's event?"
        menu:
            "\"Hanging out with you, of course!\"":
                $ summerAP += 2
                s Smile "Aww, that's sweet of you to say."
                s Neutral "Just a heads up: I'll be splitting my attention tonight."
                s "Between serving the students at the banquet table, handling the cloying crumble, and ensuring the ritual goes smoothly..."
                char "I didn't realize how busy you were going to be..."
                s Upset "No no no! I'm fine."
                s Smile "I promise I can find time and fit you in."
                "She's already spread thin."
                "Am I getting in the way?"
                hide summer Smile with dissolve
            "\"Sneaking a bite from the banquet table.\"":
                $ summerAP += 2
                s Smile "Honestly, I wouldn't mind sneaking a little either..."
                s "I usually get my dinner while I'm making it!"
                s "I love snacking."
                s Neutral "But let's make sure that everyone has a chance to grab a bite."
                hide summer Neutral with dissolve
            "\"I'm not completely sure what to expect.\"":
                $ summerAP += 3
                s Smile "That's alright!"
                s "Actually, that's my favorite part of tonight."
                s Neutral "Whatever you offer to the altar determines the course of the year..."
                s Smile "Surely, House Solis will have a good year with the cloying crumble!"
                s "That way, Dr. Tasha, the Solis students, and you will be -"
                "Summer's expression shifts."
                s Neutral "All the people I care about will prosper from our hard work."
                "She turns away, covering the side of her face."
                s Smile "You know what I mean?"
                hide summer Smile with dissolve

    elif(luna == True):
        show eluna Neutral with dissolve
        e "[name], glad to see you here already."
        e "I hope you're feeling better prepared for the Ritual performance."
        e Smile "I'll be there with you, of course."
        "She squeezes my shoulder lightly."
        if(day4lunaGood == True):
            char "Are you okay?"
            e Neutral "Just some stage-fright."
            e Smile "Everyone gets it - even Professor Morgana."
            e Neutral "I'm less nervous now."
        else:
            e Upset "Yesterday was... weird right?"
            "I flinch a little, but turn to her."
            char "What do you mean?"
        "When our eyes meet, she reaches out and touches my arm."
        e Upset "About yesterday..."
        e Neutral "I didn't want you to feel like I was blowing you off or something."
        "Collecting my thoughts, I turn away to try to think of a response."
        menu:
            "\"You mean so much to me.\"":
                $ elunaAP += 1
                e Smile "That's very sweet of you."
                hide eluna Smile with dissolve
            "\"I don't want to be a distraction.\"":
                $ elunaAP += 1
                e Upset "Why would you think you'd be a distraction to me?"
                e "I believe I'm qualified enough to know what it is I want for myself-"
                e "-And to what extent I can handle my own personal troubles."
                hide eluna Upset with dissolve
            "\"You've been working so hard for this day.\"":
                $ elunaAP += 2
                e "I know."
                e Smile "It feels like I've been preparing myself for this moment this whole time."
                e Neutral "I've always seen the rites performed, but I've never done it myself."
                hide eluna Neutral with dissolve

    elif(stella == True):
        show celeste Neutral with dissolve
        c "I thought it was you, [name]."
        c "I hope you've been enjoying yourself so far."
        if(celesteAP == 11):
            c Smile "I've been enjoying myself these past few days, thanks to you."
            c Neutral "I've always preferred doing research solo-"
            c "-But so far I've actually quite enjoyed having a fellow partner."
            c Upset "I hope you haven't been overthinking how the Full Moon Ritual goes."
            c Neutral "Typically nothing crazy happens, although it'd be nice if something interesting actually occurred this time."
        else:
            c "You don't need to be too nervous about the banquet."
            c Smile "They often play out a fancy ritual, say some words, and then sometimes something interesting happens."
            c Neutral "I hope something interesting happens this time..."
        char "Interesting?"
        c "Well, similar to to the story, the ritual is to maintain favor of the fae."
        c "After all, they play quite the role in how the school came to be."
        c Smile "I guess I hinted at them since the beginning, huh?"
        menu:
            "\"It wasn't much of a secret.\"":
                $ celesteAP += 3
                c Smile "I suppose you're right."
                c Neutral "After all, there's no such thing as secrets."
                c "Only undiscovered truths."
                hide celeste Neutral with dissolve
            "\"I thought you were just dragging me along.\"":
                $ celesteAP += 1
                c Upset "That would be an incredibly callous way of having someone keep me company."
                c "You wouldn't think me that shallow, would you?"
                hide celeste Upset with dissolve
            "\"You were more of a mystery than the fae.\"":
                $ celesteAP += 2
                c "I guess I really keep to myself a lot."
                c "It's been easy being around you, though."
                c Smile "It's nice when someone truly listens to me and returns feedback."
                hide celeste Smile with dissolve
    
    "From a distance, the professors call for all the students to commune at the amphitheater."
    show morgana Neutral at right 
    show tasha Neutral at center 
    show circe Neutral at left
    with dissolve
    t "Alright, students, we've got a whole itinerary of activities for you all to do!"
    m "Don't get too ahead of yourself though!"
    m "Make sure you have enough energy to be awake for the banquet tonight."
    m "Our very own Eluna of House Luna will be performing them!"
    t "Well, we should also thank Summer of House Solis for setting up the amphitheater so nicely."
    k "Alright, enough of bragging about your own students."
    k "Away you all go!"
    scene amphitheater1 with dissolve
    if(solis == True):
        show summer Neutral with dissolve
        s Smile "Come on, [name]!"
        s "There's an awesome fishing game that I love playing."
        s "Let's go check it out!"
    if(luna == True):
        show eluna Neutral with dissolve
        e "[name]?"
        e "Would you like to spend some time with me before the Ritual begins?"
        char "It would be my pleasure."
        e Smile "Splendid."
        e Neutral "There's an arts and crafts area where we can make our own lantern."
        e "Let's go there first!"
    if(stella == True):
        "I feel a tap on my shoulder."
        show celeste Neutral with dissolve
        "Celeste quietly stares at me, as if she means to say something..."
        char "Did you want to go check out the fair?"
        c Smile "That would be really nice..."
        c Neutral "I've never really taken part in it very actively-"
        if(celesteAP == 15):
            c Smile "-So I'd prefer if I were with you the whole time."
            c Neutral "If that's alright of course."
        else:
            c Neutral "If you're okay with it, I'd like to stick with you."
        char "Of course that's alright."
        char "Which activity did you want to check out first?"
        c "Maybe the whack-the-rabbit game?"
        c Smile "Seems like a great way to destress."
        char "Let's go!"
    
    # "Time-skip:"
    scene darkAmphitheater with Fade(2.0, 2.0, 3.0)
    if(solis == True):
        "I had so much fun with Summer that I didn't notice the day passing into the night."
    if(luna == True):
        "I had so much fun with Eluna that I didn't notice the day passing into the night."
    if(stella == True):
        "I had so much fun with Celeste that I didn't notice the day passing into the night."
    "The professors call the students over to commune at the Amphitheater."
    "As if on cue, the clouds blew by and parted to show the moonlight."
    scene amphitheater2 with Dissolve(2.0)
    if(luna == True):
        "Eluna squeezes my hand."
        show eluna Neutral with dissolve
        e "Will you come with me?"
        hide eluna Neutral with dissolve
        "We approach center stage."
        show morgana Neutral at left with dissolve
        show eluna Neutral at right with dissolve
        show e inactive at right
        m "Are you ready, Eluna?"
        hide e inactive
        show m inactive
        e Smile "Ready as ever."
        hide m inactive with dissolve
        hide eluna Smile with dissolve
        "Eluna begins to enter the stage, but as I walk towards her-"
        m "[name]."
        show morgana Neutral at center with move
        "Professor Morgana puts her hand on my shoulder."
        m "Eluna will be performing solo."
        m "Thank you, though, for having helped her rehearse for this moment."
        m Smile "I'm sure Eluna greatly appreciates it too."
        m Neutral "I already discussed this with her, so just sit down and watch."
        m "Sound good?"
        menu:
            "\"I'll be cheering her on.\"":
                $ elunaAP += 3
                #points: 16
                m Smile "Good."
                m Neutral "Go take a seat."
                hide morgana Neutral with dissolve
            "\"I suppose so.\"":
                $ elunaAP += 2
                #points: 15
                m Upset "You suppose so?"
                m Neutral "Well, I suppose you should go take a seat."
                "Professor Morgana briskly walks away."
                hide morgana Neutral with dissolve
    else:
        "Eluna of House Luna approaches the center stage of the amphitheater."
        show morgana Neutral at left with dissolve
        show eluna Neutral at right with dissolve
        show e inactive at right 
        m "Eluna, are you ready?"
        hide e inactive
        show m inactive at left
        e "It would be my honor."
        hide m inactive
        hide morgana Neutral
        with dissolve
        show eluna Neutral at center with move
    
    "Eluna poises herself, posed under the moonlight."
    "She takes a deep breath."
    e "The Full Moon is representative of the cycles of life."
    "Eluna brings her arms up, and slowly twirls in place."
    "Purple specks of light crackle around her."
    e "The waxing and waning of the moon are a reminder to every individual-"
    e "-to every witch-"
    e "-that our magic is only as great as the person."
    e "That our magic is only as persistent as the individual who practices."
    e "Under the moonlight did Luminoire sacrifice herself for our safety."
    e "And under the moonlight we thank the fae for assisting the protection and longevity of the witches of Luminoire."
    e "Faeries of the North, with the power of ocean waves and quick running streams, continue to protect us."
    e "Faeries of the East, with the cunning of thorns along beautiful roses, continue to protect us."
    e "Faeries of the South, with the knowledge like the perfect balance Earth provides for those living, continue to protect us."
    e "Faeries of the West, with the gentleness of tall grass, a bed of flowers, a mossy path-"
    if(elunaAP == 16):
        "Eluna peers over at me."
        e Smile "-a good friend-"
        e Neutral "-please continue to protect us!"
    else:
        e "-please continue to protect us!"
    
    hide eluna Neutral with dissolve
    "Eluna takes a deep breath."
    "The amphitheater is quiet."
    "All the students-"
    "-myself included-"
    "-are in awe of her performance."
    "Then, little lights start pulsing in the Amphitheater."
    scene amphitheater3 with Dissolve(3.0)
    "What are they...?"
    if(solis == True):
        s "I don't believe my eyes!"
        s "Faeries!"
        "A gentle light bobs on my hand."
        s "Aww, one's taken a liking to you!"
        "The light shape weaves and bobs around me, and then takes off away towards other students."
        s "They're so beautiful."
        s "..."
        s "[name], thanks for being here with me these past couple of days."
        s "It's been a lot of fun!"
        s "It's important also to focus on your studies."
        s "I hope you continue to visit me in the Greenhouse though!"
        s "I'll catch you later."
    if(luna == True):
        "A gentle light bobs on my hand."
        "Is it...?"
        e "Thank you faeries, for visiting us."
        e "We are indebted to you."
        "The light shape weaves and bobs around me, and then takes off away towards other students."
        "Eluna bows, exits stage, and walks towards me."
        e "What do you think of the faeries?"
        e "I'm going to miss seeing them every Full Moon Ritual."
        e "..."
        e "Thank you, by the way, for having been with me these past few days."
        e "I hope you continue to focus on your studies-"
        e "-and one day you'll catch up to me."
        e "I'm always around until graduation to help out in any way I can."
        e "I'll always be within reach."
        e "I'm going to converse with the professors for a bit, and then head off."
        e "Don't be a stranger."
    if(stella == True):
        c "Faeries..."
        "A gentle light bobs on my hand."
        c "They're here."
        "I attempt to make sense of the light shape on my hand."
        c "They take the appearance of what is most comprehensible to the perceiver."
        c "Much like angels, their true form cannot be coherently perceived by humans."
        c "Even humans with magic in our blood cannot comprehend faeries."
        "The light shape weaves and bobs around me, and then takes off away towards other students."
        c "Fascinating."
        c "..."
        c "[name]..."
        c "Thanks for hanging out with me these past few days."
        c "I really appreciate it."
        c "However, after tonight, we're going to have to go back to normalcy."
        c "I'm usually studying in the library, if you ever want to talk or hang out."
        c "I'll see you around."
    "She leaves, and I'm left standing around in the Amphitheater alone."
    "A bright light approaches me..."
    "It's like it's asking for something..."
    "Should I give it something?"
    menu:
        "Tea imbued with leaves that have healing properties" if solis == True:
            "I hand the gift provided for me when I was selected into House Solis."
        "A candle that, when lighted, never burns out" if luna == True:
            "I hand the gift provided for me when I was selected into House Luna."
        "The quill, made from a phoenix feather, used to write tomes" if stella == True:
            "I hand the gift provided for me when I was selected into House Stella."
        "Nothing":
            "The light angrily bobs against my hand, and flits away."
        