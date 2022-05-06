label day2Stella:
    "Through the mist, a tall, stone door grows in front of me."
    "On it, the crest of the Star is engraved into it."
    "Stepping forward, I push the door open."
    ##scene schoolExterior with Fade (1.0, 0.0, 1.0)
    "I'm finally here... a new witch at Luminoire Academy!"
    "The main hall of the school is lined with portraits of witches renown through the land."
    "I won't take this opportunity for granted..."
    "I'm going to make the most of my time at Luminoire Academy!"

    ##show circeNeutral
    k "Greetings! You wouldn't happen to be [name]?"
    char "No way! You're Professor Circe."

    menu:
        "The most experienced sorceress at Luminoire. I'm honored!":
            jump StellaNeu1
        "I loved your piece on the history of fey arcana!":
            jump StellaGood1

label StellaNeu1:
    ##show circeUpset
    k "What are you suggesting about my age?"
    jump continuingStella1

label StellaGood1:
    ##show circeSmile
    k "I appreciate that, but the article is outdated - by about 3000 years!"

label continuingStella1:
    ##show circeNeutral
    k "I'd like to introduce you to my protégeé."
    #"[[Celeste enters]"
    ##show circeNeutral at left
    ##show celesteNeutral at right
    c "Hello. I'm Celeste. Congratulations on your enrollment."
    "She seems so... static."
    k "Celeste here is one of the brightest students in Luminoire."
    k "Or at least she would be if she didn't spend ALL her time in my library..."
    ##"Celeste blushes and squeezes her book."
    ##show celesteUpsetB at right
    c "Thank you, Professor."
    k "I'll see you two tomorrow to discuss preparations for the Moonlight Ritual."
    k "Celeste, please show [name] to the Commons."
    ##show celesteNeutral at right
    c "Of course, ma'am."
    #"[[Circe leaves]"
    ##hide circeNeutral with dissolve
    ##show celesteNeutral at center with move

    "Celeste gestures for me to follow her down the main hall."
    "She stares down the hallway without turning to check if I'm following her."
    ##hide celesteNeutral with dissolve
    "It doesn't seem like she would enjoy small talk, so I keep to myself."
    ##scene Commons with Fade(2.0,0.0,2.0)
    ##with Pause(2.0)
    "We quietly walk into a smaller hall - the Commons."
    ##show celesteNeutral with dissolve
    c "These will be our lodgings for the rest of our term."
    c "I usually use this space to pass time between classes..."

    c "[name], what's something you do to kill time?"
    menu:
        "Exploring places that I've never been!":
            ##"A small, knowing smile cracks on Celeste's face."
            ##show celesteSmile
            "Her attention turns towards me with a hint of excitement."
            c "Exploring the unknown is exactly what House Stella is all about."
            ##show celesteNeutral
            c "Not... that there's anything unknown here."
            "Celeste's demeanor reverts back to being closed off, but her charming smile remains at the corner of her cheek."
        "Visiting museums that are rich with history.":
            ##show celesteSmile
            c "Thankfully, you won't have to spend the money to go somewhere like that."
            "Her demeanor shifts a little."
            "It's as though she has become less tense than when we introduced ourselves."
            c "Luminoire Academy is already so rich in the history of witches."
            c "In fact, I'd happily give you a tour of our oldest facilities."
            ##show celesteNeutral
            c "If you'd like."
            "I nod eagerly."
            char "That would be amazing!"
            "My enthusiasm amuses her and she leans against the wall."
        "Cracking open a book about folktales and fables.":
            ##show celesteSmile
            c "Really? I couldn't agree more."
            ##"Celeste's face brightens."
            " As she begins to elaborate, I take a seat and lean forward, listening to her carefully."
            c "We can learn as much from tall tales about history as artifacts or ancient text!"
            c "Folklore reveals to the present the way that the past was perceived,"
            c "In terms of culture, politics, and relationships."
            c "It's just a matter of translating the ancient language to bring visions of the past to life."

    ##show celesteNeutral
    c "You seem pretty... trustworthy."
    "Celeste becomes inquisitive, as though observing my response."
    ##show celesteSmile
    c "And by that I mean reliable!"
    "Her awkward laugh comes out again, but much less forced than earlier."
    ##show celesteNeutral
    c "We should get some rest before tomorrow."
    c "I'll see you at the library - Goodnight."
    ##hide celesteNeutral with dissolve
    "She waves goodnight and enters the room across from mine."
    "I'm thankful that I made a decent first impression."
    "Hopefully I'll make a better one after a good night's rest."
    ##jump dayTwoStella