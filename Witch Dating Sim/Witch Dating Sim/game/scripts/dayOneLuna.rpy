label day1Luna:
    "Through the mist, a tall, stone door grows in front of me."
    scene lunaDoor with Fade(1.0,0.0,1.0)
    "On it, the crest of the Moon is engraved into it."
    "Stepping forward, I push the door open..."
    scene schoolExterior with Fade (2.0, 0.0, 2.0)
    "I'm finally here... a new witch at Luminoire Academy!"
    "A grand facade beneath an even taller tree stands before me."
    "I won't take this opportunity for granted..."
    "I'm going to make the most of my time at Luminoire Academy!"

    m "Excuse me, witchling."
    show morgana Neutral with dissolve
    "The door that you entered through has disappeared."
    "Instead, a witch emanating raw magical power towers over you."
    m "You're in my way."
    "It's Professor Morgana. The most talented spellcaster in the entire world."

    "She's a major part in the reason I enrolled in Luminoire."
    "I can already feel my knees buckling from the pressure of even standing in the same hall as this great witch..."
    menu:
        "I bend over and take a deep bow before her.":
            char "I apologize! You are an inspiration to a generation of witches like me!"
            "After about five seconds of my issued apology, I peek up at her for approval."
            "Her face looks puffed up, as though holding back her amusement."
            #show morganaSmile
            m Smile "Stand up, child. I should apologize."
            m "I should be kinder to the next generation if they're ever going to be as great as mine."
        "I correct my posture and compose myself.":
            char "It's an honor to stand beside great witches like you, professor."
            show morgana Upset
            ##"An annoyed look streaks across her face."
            "She looks down at me."
            "My legs shake in spite of my best efforts to stay calm."
            "She utters under her breath."
            m "{i}If you knew anything about this academy, you'd know that I'm the only \"great witch\" here.{/i}"
            show morgana Neutral
    unknown "Please excuse our beloved professor."
    "Someone walks up from behind Professor Morgana."
    show morgana Neutral at left with move
    show eluna Neutral at right with dissolve
    "Her energy, while as intoxicating as Morgana's, is as calming as it is energizing."

    show m inactive at left
    unknown "She gets a kick out of keeping the students on their toes."
    hide m inactive
    show e inactive at right
    m Neutral "Eluna, not everyone can be as talented as my star pupil."
    m "Everyone just needs a little... push."
    "Morgana turns to me and stares me down menacingly."
    m Upset "[name], this is Eluna."
    m "Think of her as your superior from now on."


    show eluna Upset at right
    "Eluna rolls her eyes, just out of the professor's view."
    "Morgana continues to glare at me as I hold my breath nervously."
    show e inactive at right
    m Neutral "She is this class's pride and joy..."
    m "...so she can't be held back supporting other witchlings—"
    show m inactive at left
    hide e inactive
    e Upset "Thank you, Professor Morgana."
    "Eluna steps between me and Professor Morgana."

    show m inactive at left
    e Neutral "As the head witch for the Luna house I feel it's my responsibility to..."
    "Eluna turns to me and winks."
    #not entirely sure where to put this part (before or after the wink)
    e Smile "...be a role model for my junior witches."
    "Morgana sighs and places her hands on Eluna's shoulders as a proud parent would."

    hide m inactive
    show e inactive at right
    m Smile "Then I won't stand in your way either."
    show morgana Upset at left
    "Morgana shoots a piercing glance at me."
    m Neutral "I'll see the both of you tomorrow at the amphitheater."
    "She lifts her hands and walks down the hall."
    hide morgana Neutral with dissolve
    hide e inactive with dissolve
    show eluna Neutral at right
    "As soon as the professor turns the corner, Eluna lets out a soft, exasperated groan." #mindmup stops here

    show eluna Upset at right
    show eluna Upset at center with move



    e Upset "I'm sorry about that."
    e Neutral "Let me show you to the Commons now..."
    hide eluna Neutral with dissolve
    scene Commons with Fade(2.0, 1.0, 2.0)
    with Pause(2.0)
    "We walk quietly into the Commons."
    show eluna Neutral with dissolve

    "She hasn't really said a word to me after Professor Morgana's encounter."
    e "..."
    e Smile "So, [name], what do you do in your spare time?"
    menu:
        "\"Making weekend plans with my friends.\"":
            e "That sounds really fun."
            e "It's definitely important to maintain the relationships around you."
            e "You never know when you might be in a pinch and need help."
        "\"Writing serenades for...well...\"":
            e "Oh?"
            e "For whom I wonder."
            char "Oh, uh, I mean- it's not-"
            e Smile "I won't pry."
        "\"Dancing alone in my room.\"":
            e "There's nothing quite like the comfort of being in your own space."
            e "I enjoy being House Luna's primary student representative-"
            e Upset "-but it can be hard to keep things secretive when it comes to news about me."
    e Neutral "Here we are at the Commons by the way."
    e "If you ever need assistance, I'd be more than happy to help."
    char "Sounds great, thank you!"
    e "I'll see you at the Amphitheater tomorrow."
    hide eluna Neutral with dissolve

    jump day2Luna
