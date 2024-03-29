label day4Solis:
    scene dCommons with Fade (2.0, 1.0, 2.0)
    with Pause (2.0)
    "I can't imagine having to deal with those bees again."
    #"After leaving the herbs to marinate for the night it was now time to go see how they've developed."
    "Stumbling out of my room, I begin to make my way to the Greenhouse."
    #"Half way there, I stumble into Summer who'd seem to have been waiting for me."
    "I run into Summer who'd seem to have been waiting for me."
    #"I greet Summer, nervously as I had realized I had been late to our agreed time."
    show summer Upset with dissolve
    s Upset "[name], you're up late. What took you so long?"
    #"I try to explain to her how the demons had attacked me in my bed, while in truth I had just slept past my alarm."
    char "Uhh..."
    "What's my excuse..."
    play music overworldMusic fadein 5.0
    char "I was attacked in bed!"
    "I try to explain to her that demons attacked me in my bed, while in truth I had just slept past my alarm."
    s Neutral "Demons?"
    s "Are you okay? Are you hurt?"
    s "Why didn't you tell me earlier?"
    "A sense of guilt washes over me as I hesitate from her sudden concern."
    char "Oh, uh..."
    char "I was just joking, there weren't any demons."
    char "I just overslept."
    #"I admit the truth, and she sighs."
    s Upset "Don't worry me like that again, okay?"
    s "I really thought you got harassed by demons."
    #"I chuckle, telling her how demons aren't real. She looks at me with concern."
    char "Haha, but demons aren't real though!"
    "My laughter trails off as she continues to look at me with concern."
    s Neutral "What do you mean..."
    s Upset "Demons {i}are{/i} real..."
    char "..."
    s "..."
    #"There's a silence between us for a moment."
    char "..."
    s "..."
    stop music fadeout 5.0
    s Smile "Anyways, lets go back to the greenhouse."
    s Neutral "There are fermenting herbs waiting for me there."
    hide summer Neutral with dissolve
    scene greenhouse with Fade (2.0, 0.0, 2.0)
    #"We head towards the green house."
    "When we enter the green house, we notice a figure inspecting Summer's herbal experiment."
    #"I had seen her in the green house before, though I wasn't too sure who she was."
    #"A little cautious, I began to approach her. Ready to confront her meddling."
    show summer Neutral with dissolve
    s "Professor Tasha!"
    play music overworldMusic fadein 5.0
    #"Tasha turns around, smiling as she noticed the two of us."
    show summer Neutral at left with move
    show tasha Neutral at right with dissolve 
    show s inactive at left with dissolve
    t "Well, well, well."
    t Smile "If it isn't my dear sunshine. How's it going?"
    "She smiles and hugs Summer, who returns the embrace."
    hide s inactive
    show t inactive at right
    s Smile "Hey professor Tasha, we're doing-"
    "Summer struggles to breath."
    s Neutral "-great!"
    "Tasha releases Summer, who inhales a deep breath."
    hide t inactive
    show s inactive at left
    t "I was just looking over your results."
    t Smile "Your herbs are perfect! You've even managed to get all the chlorophyll out."
    "Summer and I look at the leaves, which now appeared transparent."
    t "And your concoction as well, I haven't seen a Cloying crumble this perfect in centuries."
    #"Summer blushes a little, the waves of compliments lighting up her cheeks."
    #show summer Neutral blush at left
    t Neutral "Since you've seemed to have completed your project, could I ask a small favor of you, Summer?"
    #hide summer Neutral blush
    hide s inactive
    show t inactive at right
    s "Sure thing, Professor Tasha!"
    s "What can I help you with?"
    hide t inactive
    show s inactive at left
    #"Tasha explains how the mandrakes she had sent to set up for the Amphitheater had withered and how she needs help setting up for the banquet."
    t Upset "The mandrakes I had sent over to the Amphitheater have withered."
    t "I'd bring over the rest of the decor and supplies-"
    t "-but that would take away time from me reviving the mandrakes."
    t Neutral "Could you possibly bring the supplies over from the greenhouse to the amphitheater?"
    hide s inactive
    show t inactive at right
    s Smile "Of course!"
    s Neutral "I'll get on it right away."
    hide t inactive
    show s inactive at left
    t Smile "Thank you, Summer."
    t Neutral "I must go attend to the mandrakes at once."
    hide tasha Neutral
    hide s inactive 
    hide summer Neutral
    with dissolve
    "Professor Tasha briskly leaves the greenhouse."
    "Summer eyes a set of boxes in the corner, and begins making her way to them."
    "She wholeheartedly agreed to Professor Tasha's request..."
    "-but made no effort in asking for help."
    "What should I do?"
    stop music fadeout 5.0
    "On the one hand, Summer hadn't directly asked me for help..."
    "But on the other, it would take her the whole day to set up for the banquet."
    menu:
        "\"I'll be right back.\"":
            $ day4solisGood = True
            $ summerAP += 3
            scene amphitheater1 with Fade (2.0, 0.0, 2.0)
            "I head towards the Amphitheater."
            play sound clap volume 0.2 fadein 6.0
            "There's a performance that seems to be wrapping up at the theater."
            play sound walkProf volume 0.3 fadein 3.0
            m "Hello fellow Solis student."
            show morgana Neutral with dissolve
            "Professor Morgana of House Luna appears behind me."
            char "Ah, Professor Morgana!"
            m "May I help you?"
            char "Well, actually we need help setting up for the banquet-"
            char "-and that requires bringing a lot of boxes and items over here."
            unknown "We?"
            show morgana Neutral at left with move
            show eluna Neutral at right with dissolve
            "The performer who had been on stage shows up beside Professor Morgana."
            show m inactive at left
            unknown "I bet it's Summer trying to work on arrangements by herself."
            hide m inactive
            show e inactive at right
            m Smile "I suppose it's quite in character for her."
            m Neutral "You'd know best, Eluna."
            jump day4SolisExtraPath
        "\"Do you need any help?\"":
            $ summerAP += 2
            s "Thanks [name], though I'm not sure how much we can do with just the two of us."
            s "But I really appreciate that you're willing to help me."
            scene amphitheater1 with Fade(2.0, 1.0, 2.0)
            "It took a decent amount of time, but we got the work done early."
            "The sun's nearly set as we finish loading the final pot onto the cart."
            s "Oof, I think that was the last of them, it took longer then expected didn't it."
            s "Thanks for helping me out [name]."
            #"Summer mumbles to herself-"
            s "{i}-though it would've been faster if I had better magical abilities.{\i}"
            "My body is seriously killing me after all that."
            jump day4SolisEnd
        "\"Good luck, Summer!\"":
            $ summerAP += 1
            "Summer smiles at you, sighing as she prepares to get back to work."
            "Ah, she didn't take it as a joke."
            "I quickly go to help her out."
            scene amphitheater1 with Fade(2.0, 1.0, 2.0)
            "We worked diligently."
            "We barely spoke a word the whole time."
            "As we finish setting up for the banquet we hear the performers over at the Amphitheater."
            s "That must've been the folks of the Luna House."
            #"I realize that perhaps I could've asked them for help, but it was too late for that."
            s "Well, thanks for your help [name] I couldn't have done this without you."
            jump day4SolisEnd

label day4SolisExtraPath:
    hide e inactive
    show m inactive at left
    e "Where is Summer right now?"
    e "I've just about wrapped up rehearsal, I can manage helping out a friend."
    hide m inactive
    show e inactive at right
    m "Go with [name] to manage with Summer."
    hide e inactive
    show m inactive at left
    e "Let's go."
    e "I assume she's at the Greenhouse?"
    "I nod, startled by the intensity of Eluna's call to action."
    hide e inactive
    hide eluna Neutral 
    hide morgana Neutral 
    with dissolve
    "Eluna walks off briskly."
    "I trail after her."
    scene greenhouse with Fade(1.0, 0.0, 1.0)
    with Pause(2.0)
    "We show up at the Greenhouse."
    "I'm nearly out of breath, but Eluna is steady."
    "Summer grunts, lifting heavy pots onto a small wagon."
    show eluna Neutral with dissolve
    e "Summer!"
    play music overworldMusic fadein 6.0
    show eluna Neutral at left with move
    show summer Neutral at right with dissolve
    show e inactive at left with dissolve
    s "Oh! Hiya Eluna! What brings you here?"
    hide e inactive
    show s inactive at right
    e "What brings me here? I'm here to help you."
    e Upset "What gives you the idea that you need to be doing all this heavy lifting yourself!?"
    hide s inactive
    show e inactive at left
    s "It's not a big deal, really."
    hide e inactive
    show s inactive at right
    e Neutral "You're going to break your back lifting all these pots and decor alone."
    e Upset "You're here at the academy now."
    e Neutral "You don't have to keep doing things alone."
    hide s inactive
    show e inactive at left
    s "..."
    hide e inactive
    show s inactive at right
    e "Come on, [name], let's lift these together."
    stop music fadeout 5.0
    scene amphitheater1 with Fade(2.0, 1.0, 2.0)
    "Summer and I wave goodbye to Eluna and the other Luna students who came to help."
    "Summer sighs in exhaustion."
    show summer Neutral with dissolve
    s "Well, I sure am glad at least we managed to finish all the preparations today."
    s "I really have to go thank Eluna and the other students of Luna."
    s Upset "..."
    s "Hey, [name]?"
    char "Yeah?"
    s Smile "I really appreciate you reaching out to the Luna students and helping me out."
    s "I guess I have a bad habit of not really asking for help."
    s Neutral "You see..."
    s Upset "I didn't grow up glamorous or with a lot of magical abilities to spare."
    if summerAP >= 11:
        play music conflictMusic fadein 6.0
        s Neutral "It felt like all of our family's magical talent went to my sister."
        s "She was perfect in every way."
        s "Strong, magical, beautiful..."
        s "I'm just..."
        "Summer gestures towards herself."
        s Upset "...this."
        s "She was kind to me, but I can't say the same about my parents."
        s Neutral "They only ever saw her."
        s "I would wonder if I ever was related to the family."
        s "I was worried that if I didn't work hard enough-"
        s Upset "..."
        "Summer takes a shaky breath."
        s "If I were able to do everything by myself..."
        s "If I could succeed at tasks without assistance..."
        s Smile "...that meant that I was just as good, right?"
        "Summer shuffles her feet from side to side."
        s Neutral "Eluna and I have known each other since childhood."
        s "She used to help me out anytime I'd try to do anything alone."
        s "Eluna was kind of like my second older sister."
        s Upset "She had to move away though when I was 10."
        s Neutral "Kind of a miracle though that we got to see each other again at Luminoire Academy."
        s "She's just as kind as I remembered her."
        #"Summer begins to cry as she recounts the countless of times she's felt like a failure, even though it's clearly she's pushing herself past her limit."
        "Summer's eyes glisten, but she keeps a steady breath."
        s "I guess what I wanted to say was..."
        s Smile "...thank you."
        s Neutral "I would've probably just worked the entire day without actually considering asking for help."
        s Smile "It sounds a little weird when you really think about it."
        s Neutral "I'm aware it's a bad habit, but I can't seem to change it."
        #s "But as a token of thanks, I wanted to give you this."
        "She hands you a bouquet of dried flowers, all still perfectly preserved with their beauty."
        $ sunflower = True
        show s inactive with dissolve
        show sunflowers at my_center with dissolve
        "It's sunflowers."
        hide sunflowers with dissolve
        hide s inactive
        s Smile "They're my favorite flower."
        s Neutral "Sunflowers are so bright and lovely."
        s "They stand so tall and unrelenting, always facing the sun."
        s "I used to imagine being a sunflower when I was little..."
        stop music fadeout 5.0
    else:
        s Upset "..."
        s Neutral "Actually, never mind, this isn't the right time to tell you"


label day4SolisEnd:
    s Neutral "Let's go grab some food, I'm starving after all that work!"
    hide summer Neutral with dissolve
    #transition to Commons
    scene nCommons with Fade (2.0, 1.0, 2.0)
    with Pause (2.0)
    "Summer and I had a big meal in the cafeteria."
    "We were so exhausted by the events of the day that we had walked back to the Commons in peaceful silence."
    show summer Neutral with dissolve
    s "..."
    s Smile "[name], I'll see you tomorrow for the Full Moon Ritual!"
    hide summer Smile with dissolve
    "Summer and I bid our goodbyes, and leave to our respective rooms."
    scene black with Dissolve(3.0)
    show text "Day 5" with dissolve
    play sound dingDong1 fadein 3.0 volume 0.25
    with Pause(3.0)
    show text "0 Days Until the Full Moon Ritual..." with dissolve
    with Pause(3.0)
    jump day5
    #perfec : 11