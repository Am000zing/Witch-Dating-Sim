define e = Character('Eluna', color='#f7c039')
define m = Character('Morganna', color='#ba1230')
define char = Character("name", dynamic=True, color='#f933ff')

label day1Luna:
    "Through the mist, a tall, stone door grows in front of me."
    "On it, the crest of the Moon is engraved into it."
    "Stepping forward, I push the door open."
    ##scene schoolExterior with Fade (1.0, 0.0, 1.0)
    "I'm finally here... a new witch at Luminoire Academy!"
    "The main hall of the school is lined with portraits of witches renown through the land."
    "I won't take this opportunity for granted..."
    "I'm going to make the most of my time at Luminoire Academy!"

    m "Excuse me, witchling."
    ##show morganaNeutral with dissolve
    "The door that you entered through has disappeared."
    "Instead, a witch emanating raw magical power towers over you."
    m "You're in my way."
    "It's Professor Morgana. The most talented spellcaster in the entire world."

    "She's a major part in the reason I enrolled in Luminoire."
    "I can already feel my knees buckling from the pressure of even standing in the same hall as this great witch."
    menu:
        "I bend over and take a deep bow before her. \"I apologize! You are an inspiration to a generation of witches like me!\"":
            "After about five seconds of my issued apology, I peek up at her for approval."
            "Her face looks puffed up, as though holding back her amusement."
            ##show morganaSmile
            m "Stand up, child. I should apologize."
            m "I should be kinder to the next generation if they're ever going to be as great as mine."
        "I correct my posture and compose myself. \"It's an honor to stand beside great witches like you, professor.\"":
            ##show morganaUpset
            ##"An annoyed look streaks across her face."
            "My legs shake from it as she looks down at me, in spite of my best efforts to stay calm."
            "She utters under her breath."
            m "If you knew anything about this school, you'd know that I'm the only great witch here."
    e "Please excuse our beloved professor."
    ##show morganaNeutral at left with move
    ##show elunaNeutral at right with move
    ##"A gorgeous girl walks up from behind Professor Morgana."
    ##"Her energy, while as intoxicating as Morgana's, is as calming as it is energizing."
    e "She gets a kick out of keeping the students on their toes."
    m "Eluna, not everyone can be as talented as my star pupil."
    m "Everyone just needs a little push."
    ##show morganaUpset at left
    "Morgana turns to me and stares me down menacingly."
    m "[name], this is Eluna."
    m "Think of her as your superior from now on."
    ##show elunaUpset at right
    "Eluna rolls her eyes, just out of the professor's view."
    "Holding my breath nervously, Morgana stares me down."
    ##show morganaNeutral at left
    m "She is this class's pride and joy..."
    m "...so she can't be held back supporting witchlings such as you —"
    e "Thank you, Professor Morgana."
    "Eluna steps between me and Professor Morgana."
    ##show elunaNeutral at right
    e "As the head witch for the Luna house I feel it's my responsibility to..."
    "Eluna turns to me and winks."
    ##show elunaSmile at right  #not entirely sure where to put this part (before or after the wink)
    e "...serve as a role model for my junior witches."
    "Morgana sighs and places her hands on Eluna's shoulders as a proud parent would."
    ##show morganaSmile at left
    m "Then I won't stand in your way either."
    ##show morganaUpset at left
    "Morgana shoots a piercing glance at me."
    m "I'll see the both of you tomorrow at the amphitheater."
    ##hide morganaUpset with dissolve
    "She lifts her hands and walks down the hall."
    "As soon as the professor turns the corner, Eluna lets out a soft, exasperated groan." #mindmup stops here
    ##show elunaUpset at center with move
    e "I'm sorry about that."
    ##show elunaNeutral
    e "Let me show you to the Commons now..."
    ##hide elunaNeutral with dissolve
    ##scene Commons with Fade(2.0, 1.0, 2.0)
    ##with Pause(2.0)
    ##show elunaNeutral
    e "So, [name], what do you do in your spare time?"
    menu:
        "Making weekend plans with my friends":
            e "That sounds really fun."
            e "It's definitely important to maintain the relationships around you."
            e "You never know when you might be in a pinch and need help."
        "Writing serenades for... well...":
            e "Oh?"
            e "For whom I wonder."
            char "Oh, uh, I mean- it's not-"
            ##show elunaSmile
            e "I won't pry."
        "Dancing alone in my room.":
            e "There's nothing quite like the comfort of being in your own space."
            e "I enjoy being House Luna's primary student representative-"
            ##show elunaUpset
            e "-but it can be hard to keep things secretive when it comes to news about me."
    ##show elunaNeutral
    e "Here we are at the Commons by the way."
    ##e "I'm afraid I never introduced myself formally."
    ##e "I'm Eluna, representative of House Luna."
    e "If you ever need assistance, I'd be more than happy to help."
    char "Sounds great, thank you!"
    e "I'll see you at the Amphitheater tomorrow."
    ##hide elunaNeutral with dissolve
    ##jump dayTwoLuna
