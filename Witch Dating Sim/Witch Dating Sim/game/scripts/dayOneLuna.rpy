define e = Character('Eluna', color='#f7c039')
define m = Character('Morganna', color='#ba1230')
define char = Character("name", dynamic=True, color='#f933ff')

label day1Luna:
    "Through the mist, a tall, stone door grows in front of me."
    "On it, the crest of the Sun is engraved into it."
    "Stepping forward, I push the door open."
    "I'm finally here... a new witch at Luminoire Academy!"
    "The main hall of the school is lined with portraits of witches renown through the land."
    "I won't take this opportunity for granted..."
    "I'm going to make the most of my time at Luminoire Academy!"

    m "Excuse me, witchling."
    "[[Morgana enters]"
    "The door that you entered through has disappeared."
    "Instead, a witch emanating raw magical power towers over you."
    m "You're in my way."
    "It's Professor Morgana. The most talented spellcaster in the entire world."

    "She's a major part in the reason I enrolled in Luminoire."
    "I can already feel my knees buckling from the pressure of even standing in the same hall as this great witch."
    menu:
        "I bend over and take a deep bow before her. \"I apologize! You are an inspiration to a generation of witches like me!\"":
            "After about five seconds of my issued apology, I peak up at her for approval."
            "Her face looks puffed up, as though holding back her amusement."
            m "Stand up, child. I should apologize."
            m "I should be kinder to the next generation if they're ever going to be as great as mine."
        "I correct my posture and compose myself. \"It's an honor to stand beside great witches like you, professor.\"":
            "An annoyed look streaks across her face."
            "My legs shake from it as she looks down at me, in spite of my best efforts to stay calm."
            "She utters under her breath."
            m "If you knew anything about this school, you'd know that I'm the only great witch here."
    "[[Eluna enters]"
    e "Please excuse our beloved professor."
    "A gorgeous girl walks up from behind Professor Morgana."
    "Her energy, while as intoxicating as Morgana's, is as calming as it is energizing."
    e "She gets a kick out of keeping the students on their toes."
    m "Eluna, not everyone can be as talented as my star pupil."
    m "Everyone just needs a little push."
    "Morgana turns to me and stares me down menacingly."
    m "[name], this is Eluna."
    m "Think of her as your superior from now on."

    "Eluna rolls her eyes, just out of the professor's view."
    "Holding my breath nervously, Morgana stares me down."
    m "She is this class's pride and joy..."
    m "...so she can't be held back supporting witchlings such as you —"
    e "Thank you, Professor Morgana."
    "Eluna steps between me and Professor Morgana."
    e "As the head witch for the Luna house, I feel it's my responsibility to..."
    "Eluna turns to me and winks."
    e "... serve as a role model for my junior witches."

    "Morgana sighs and places her hands on Eluna's shoulders as a proud parent would."
    m "Then I won't stand in your way either."
    "Morgana shoots a piercing glance at me."
    m "I'll see the both of you tomorrow at the amphitheater."
    "She lifts her hands and walks down the hall."
    "As soon as the professor turns the corner, Eluna lets out a soft, exasperated groan."
            