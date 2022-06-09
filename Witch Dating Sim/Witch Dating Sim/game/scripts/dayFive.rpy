label day5:
    scene dCommons with Fade (2.0, 1.0, 2.0)
    with Pause (2.0)
    "Tonight's the night: the Full Moon Ritual!"
    "House Stella, Luna, and Solis come together to celebrate tonight."
    "I can't lose rhythm now!"
    play sound chatter volume 0.2 fadein 6.0
    "Excitement fills the air of the Commons."
    play music overworldMusic fadein 6.0
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
    show circe Neutral at right 
    show morgana Neutral at center 
    show tasha Neutral at left
    with dissolve
    show t inactive at left
    show k inactive at right
    with dissolve
    m "Witches!"
    m "I hope you all are as excited for tonight's Full Moon Ritual as I am."
    m "I'd like to ask all of you to join us at the Amphitheater half past noon."
    hide t inactive
    show m inactive at center
    t "We'll be working together to decorate and prepare for tonight's ritual."
    t "Don't worry, we'll have snacks."
    t Smile "We're not interested in working you to the bone."
    show t inactive at left
    hide k inactive
    k Upset "Unless..."
    k Smile "I jest, of course."
    k Neutral "Now, everyone can go get ready-"
    k "Prepare your offering for the Full Moon ritual."
    stop music fadeout 5.0
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
                s SmileB "Aww, that's sweet of you to say."
                s Smile "Just a heads up: I'll be splitting my attention tonight."
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
            e SmileB "Everyone gets it - even Professor Morgana."
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
                e UpsetB "Why would you think you'd be a distraction to me?"
                e Upset "I believe I'm qualified enough to know what it is I want for myself-"
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
            c NeutralB "-But so far I've actually quite enjoyed having a fellow partner."
            c Upset "I hope you haven't been overthinking how the Full Moon Ritual goes."
            c Neutral "Typically nothing crazy happens, although it'd be nice if something interesting actually occurred this time."
        else:
            c "You don't need to be too nervous about the banquet."
            c Smile "They often play out a fancy ritual, say some words, and then sometimes something happens."
            c Neutral "I hope something interesting occurs this time..."
        char "Interesting?"
        c "Well, similar to to the story, the ritual is to maintain favor of the fae."
        c "After all, they play quite the role in how the school came to be."
        c Smile "I guess I hinted at them since the beginning, huh?"
        menu:
            "\"It wasn't much of a secret.\"":
                $ celesteAP += 3
                c SmileB "I suppose you're right."
                c Neutral "After all, there's no such thing as secrets."
                c "Only undiscovered truths."
                hide celeste Neutral with dissolve
            "\"I thought you were just dragging me along.\"":
                $ celesteAP += 1
                c UpsetB "That would be an incredibly callous way of having someone keep me company."
                c "You wouldn't think me that shallow, would you?"
                hide celeste UpsetB with dissolve
            "\"You were more of a mystery than the fae.\"":
                $ celesteAP += 2
                c "I guess I really keep to myself a lot."
                c "It's been easy being around you, though."
                c SmileB "It's nice when someone truly listens to me and returns feedback."
                hide celeste SmileB with dissolve
    
    "From a distance, the professors call for all the students to commune at the amphitheater."
    show circe Neutral at right 
    show morgana Neutral at center 
    show tasha Neutral at left
    with dissolve
    show m inactive at center
    show k inactive at right
    with dissolve
    t "Alright, students, we've got a whole itinerary of activities for you all to do!"
    hide m inactive
    show t inactive at left
    m "Don't get too ahead of yourself though!"
    m "Make sure you have enough energy to be awake for the banquet tonight."
    m Smile "Our very own Eluna of House Luna will be performing them!"
    hide t inactive
    show m inactive at center
    t "Well, we should also thank Summer of House Solis for setting up the amphitheater so nicely."
    hide k inactive
    show t inactive at left
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
        e SmileB "Splendid."
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
            c SmileB "-So I'd prefer if I were with you the whole time."
            c NeutralB "If that's alright of course."
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
        show morgana Neutral at left 
        show eluna Neutral at right 
        with dissolve
        show e inactive at right with dissolve
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
    play sound sparkle volume 0.4 fadein 3.0
    "Purple specks of light crackle around her."
    play music conflictMusic fadein 3.0
    e "The waxing and waning of the moon are a reminder to every individual-"
    stop sound fadeout 3.0
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
        e SmileB "-a good friend-"
        e Neutral "-please continue to protect us!"
    else:
        e "-please continue to protect us!"
    
    hide eluna Neutral with dissolve
    stop music fadeout 3.0
    "Eluna takes a deep breath."
    "The amphitheater is quiet."
    "All the students-"
    "-myself included-"
    "-are in awe of her performance."
    play music cgMusic fadein 10.0
    "Then, little lights start pulsing in the Amphitheater."
    scene amphitheater3 with Dissolve(3.0)
    "What are they...?"
    if(solis == True):
        show summer Neutral with dissolve
        s "I don't believe my eyes!"
        s Smile "Faeries!"
        "A gentle light bobs on my hand."
        s Smile "Aww, one's taken a liking to you!"
        "The light shape weaves and bobs around me, and then takes off away towards other students."
        s Neutral "They're so beautiful."
        s "..."
        s "[name], thanks for being here with me these past couple of days."
        s SmileB "It's been a lot of fun!"
        s Smile "It's important also to focus on your studies."
        s "I hope you continue to visit me in the Greenhouse though!"
        s Neutral "I'll catch you later."
        hide summer Neutral with Dissolve(2.0)
    if(luna == True):
        "A gentle light bobs on my hand."
        "Is it...?"
        show eluna Neutral with dissolve
        e "Thank you faeries, for visiting us."
        e "We are indebted to you."
        "The light shape weaves and bobs around me, and then takes off away towards other students."
        "Eluna bows, exits stage, and walks towards me."
        e "What do you think of the faeries?"
        e Smile "I'm going to miss seeing them every Full Moon Ritual."
        e Neutral "..."
        e "Thank you, by the way, for having been with me these past few days."
        e "I hope you continue to focus on your studies-"
        e "-and one day you'll catch up to me."
        e Smile "I'm always around until graduation to help out in any way I can."
        e "I'll always be within reach."
        e Neutral "I'm going to converse with the professors for a bit, and then head off."
        e "Don't be a stranger."
        hide eluna Neutral with dissolve
    if(stella == True):
        show celeste Neutral with dissolve
        c "Faeries..."
        "A gentle light bobs on my hand."
        c "They're here."
        "I attempt to make sense of the light shape on my hand."
        c Upset "They take the appearance of what is most comprehensible to the perceiver."
        c "Much like angels, their true form cannot be coherently perceived by humans."
        c "Even humans with magic in our blood cannot comprehend faeries."
        "The light shape weaves and bobs around me, and then takes off away towards other students."
        c Neutral "Fascinating."
        c "..."
        c "[name]..."
        c "Thanks for hanging out with me these past few days."
        c SmileB "I really appreciate it."
        c Upset "However, after tonight, we're going to have to go back to normalcy."
        c Neutral"I'm usually studying in the library, if you ever want to talk or hang out."
        c "I'll see you around."
        hide celeste Neutral with dissolve
    "She leaves, and I'm left standing around in the Amphitheater alone."
    "A bright light approaches me..."
    "It's like it's asking for something..."
    stop music fadeout 5.0
    "Should I give it something?"
    menu:
        "Tea imbued with leaves that have healing properties" if solis:
            show tea at my_center with dissolve
            "I hand the gift provided for me when I was selected into House Solis."
            hide tea with dissolve
            jump genEnd
        "A candle that, when lighted, never burns out" if luna:
            show candle at my_center with dissolve
            "I hand the gift provided for me when I was selected into House Luna."
            hide candle with dissolve
            jump genEnd
        "The quill, made from a phoenix feather, used to write tomes" if stella:
            show quill at my_center with dissolve
            "I hand the gift provided for me when I was selected into House Stella."
            hide quill with dissolve
            jump genEnd
        "A bouquet of dried sunflowers" if sunflower:
            show sunflowers at my_center with dissolve
            "I hand Summer's gift to the faerie."
            hide sunflowers with dissolve
            jump solisEnd
        "A violet from the Evergarden" if violet:
            show violet at my_center with dissolve
            "I hand Celeste's gift to the faerie."
            hide violet with dissolve
            jump stellaEnd
        "A quill from an owl's feather" if owl:
            show owlQuill at my_center with dissolve
            "I hand Celeste's gift to the faerie."
            hide owlQuill with dissolve
            jump stellaEnd
        "A hairclip adorned with the sun, moon, and stars" if hairclip:
            show hairclip at my_center with dissolve
            "I hand Eluna's gift to the faerie."
            hide hairclip with dissolve
            jump lunaEnd
        "Nothing":
            jump badEnd
    
    label badEnd:
        "The light angrily bobs against my hand, and flits away."
        "..."
        "It's quiet around me."
        "..."
        "The faeries have departed, and most of the students have left."
        scene amphitheater2 with Dissolve (2.0)
        "I sit in silence."
        "It's been an interesting first couple days."
        "I should head back to the Commons."
        "I wonder what will come upon me tomorrow..."
        jump credits
    
    label genEnd:
        "..."
        "It's quiet around me."
        "Then a light voice speaks:"
        unknown "{i}Your generous offering...{/i}"
        unknown "{i}The gift from Luminoire...{/i}"
        unknown "{i}...{/i}"
        unknown "{i}May your House be blessed upon the coming year.{/i}"
        jump theEnd
    
    label solisEnd:
        "..."
        "It's quiet around me."
        "Then a light voice speaks:"
        unknown "{i}Your generous offering...{/i}"
        unknown "{i}Solis...{/i}"
        unknown "{i}The gift from one who has their entire faith in you...{/i}"
        unknown "{i}...{/i}"
        unknown "{i}May your bonds be strengthened upon the coming year.{/i}"
        jump theEnd

    label lunaEnd:
        "..."
        "It's quiet around me."
        "Then a light voice speaks:"
        unknown "{i}Your generous offering...{/i}"
        unknown "{i}Luna...{/i}"
        unknown "{i}The gift from one who seeks their support in you...{/i}"
        unknown "{i}...{/i}"
        unknown "{i}May your bonds be strengthened upon the coming year.{/i}"
        jump theEnd

    label stellaEnd:
        "..."
        "It's quiet around me."
        "Then a light voice speaks:"
        unknown "{i}Your generous offering...{/i}"
        unknown "{i}Stella...{/i}"
        unknown "{i}The gift from one who absolutely trusts you...{/i}"
        unknown "{i}...{/i}"
        unknown "{i}May your bonds be strengthened upon the coming year.{/i}"
        jump theEnd

    label theEnd:
        "..."
        "The faeries have departed, and most of the students have left."
        scene amphitheater2 with Dissolve (2.0)
        "I sit in comfortable silence."
        "It's been an interesting first couple days."
        "I hope I can continue to make good memories."
        "I should head back to the Commons."
        "I wonder what will happen tomorrow..."
        jump credits