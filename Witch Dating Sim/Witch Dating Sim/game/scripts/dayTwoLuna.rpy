label day2Luna:
    scene Commons with Fade(2.0,1.0, 2.0)
    pause 1.0
    "The reality of being at Luminoire Academy is really starting to hit me."
    "I'm not sure whether or not I got off the wrong foot with Professor Morgana, but surely I can still make a good impression!"
    "House Luna is supposed to be meeting at the amphitheater..."
    "I should really get going!"
    scene amphitheater1 with Fade(2.0, 0.0, 2.0)
    "I arrive at the amphitheater, nearly out of breath."
    "The academy's layout is so puzzling with all its twists and turns, so many different entrances with just as many exits."
    show morganaNeutral with dissolve
    m "You've barely made it on time."
    "I try to stand up straight and lighten my breathing."
    "So far, Professor Morgana has not pulled any punches with her sharp tongue."
    show morganaNeutral at left with move
    show elunaNeutral at right with dissolve
    e "Oh, Professor, don't be so hard on her..."
    e "It's only her first day! I remember feeling confused navigating the halls on my first day here."
    m "Well, on your first day you also perfectly performed the introductory enchantment. On your first try, no less!"
    show morganaSmile at left
    m "...but we'll see what our new Luna witchling is capable of."
    "Damn, Profesor Morgana is seriously giving me a hard time."

    #I need a better key for this color coding  :sob:
    hide morganaSmile
    show morganaNeutral at center with move
    hide elunaNeutral with dissolve
    "Profesor Morgana claps her hands with a flourish."
    m "Alright class! We will now begin the auditions for the Full Moon Ritual."
    m "It is of  utmost importance that you take this seriously, and when the Ritual begins, the rites are performed {i}perfectly{/i}." 
    m "For this year's Ritual, I will be having Eluna leading the rites."
    m "Eluna, would you like to demonstrate to them what is expected in the Ritual?" 
    e "It would be my pleasure, Professor."
    hide morganaNeutral
    hide elunaNeutral
    scene elunaDanceCG with Fade (1.0, 0.0, 1.0)
    #CG OPTION: Eluna singing/dancing
    "Everyone in the class stares at Eluna with wonder."
    "It's like she's enchanted everyone in the room."
    "She certainly is quite... beautiful."
    m "Thank you, Eluna. You may go sit down."
    scene amphitheater1 with Fade (1.0, 0.0, 1.0)
    "Eluna grabs the empty seat next to mine."
    "I sit up a little straighter in my chair."
    "Maybe I should say something to her...."
    menu:
        "Your performance was amazing!":
            show elunaNeutral with dissolve
            e "Aha, thank you. That is very kind of you you to say."
            "She stares back at where Professor Morgana is lecturing the students about the ritual."
        "You looked really pretty on stage.":
            show elunaUpset with dissolve
            e "Ah, thank you."
            "She seems a little uncomfortable by that remark."
            char "I'm sorry, I didn't mean to come off as shallow or anything."
            show elunaNeutral
            e "Ah, oh no, it's fine. Thank you for the compliment."
            "She stares back at where Profesor Morgana is lecturing the students about the ritual."

    hide elunaNeutral with dissolve
    show morganaNeutral with dissolve
    m "No one has signed up to be Eluna's supporting lead for the Ritual."
    m "I'd like for you all to be as involved as possible with the Ritual, as we are the house responsible for the rites."
    m "Hm..."
    show morganaSmile
    m "[name], why don't you take supporting role for now?"
    "..."
    "What?"
    show morganaNeutral
    m "You're conveniently next to her, might as well run lines together."
    "Professor Morgana shoves a stack of papers into my hands."
    m "Here, read... this part of the script with her."
    e "..."
    "Oh boy, this has been a hell of a day."

    "I've never done plays before, nor do I have experience running lines with a partner!"
    "What should I do..."
    menu: 
        "Read the lines while looking at Eluna":
            "While reading, I stumble over a line."
            "Eluna is completely straight-faced."
            m "You just need some more practice, but I'm sure you'll get the hang of it."            
        "Focus on reading the lines directly from the page.":
            "I managed to get through the lines, but it didn't really feel very impactful."
            "Eluna looks a bit annoyed."
            m "Bit dry of a performance, but I'm sure with practice you'll get the hang of it." 
        "Cast a spell on your throat that will amplify your voice!":
            "I haven't shown Professor Morgana my magical prowess."
            "Maybe now is the time!"
            "I cast the spell and-"
            char "{i}THE FULL MOON IS REPRESENTATIV- {/i}"
            "Oh no, my voice was too loud!"
            m "Alright, enough of that now..."
            char "I'M SORRY PROFESSOR! I DIDN'T REALIZE IT WOULD TURN OUT THIS WAY!"
            m "{i}*Sigh*{/i), of course you didn't."
            "Professor Morgana waves her hands and my vocal chords feel less tense."
            "Professor Morgana looks peeved, but Eluna looks pretty amused."   

    m "Since there isn't anyone else brave enough to be supporting lead, [name], you shall be supporting lead for Eluna."
    m "You all are excused for today."
    "Everyone starts packing up and getting out of their seats."
    m "[name]."
    "I look up at Professor Morgana peering over at me from across the room."
    m "Practice well."
    ##Morgana leaves the scene
    "Ugh..."

    e "Hey, [name]?"
    char "Oh! Hey, sorry for messing up today."
    e "No, it's really no big deal."
    e "I wanted to ask if you'd like to run lines with me tomorrow afternoon?"
    e "Some practice might help you feel a bit more confident perfoming."
    char "oh, of course! Yes, that'd be great."
    e " Perfect! I'll find you in the Commons tomorrow afternoon."
    char "S-sounds good!"
    char "I'll see you then!"
    e "Yes, goodbye."
    "She promptly leaves the room."

    "I slump back into my seat."
    "What a day."
    "I guess I'll be meeting Eluna tomorrow then."
    "I should go back and get some rest."
    ## ##Scene fade out, jump LunaDayThree