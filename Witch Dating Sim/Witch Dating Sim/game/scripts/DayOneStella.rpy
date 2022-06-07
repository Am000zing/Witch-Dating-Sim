label day1Stella:
    "Through the mist, a tall, stone door grows in front of me."
    scene stellaDoor with Fade(1.0,0.0,1.0)
    "On it, the crest of the Star is engraved into it."
    show quill at my_center with Dissolve(2.0)
    "An ethereal voice speaks:"
    unknown "{i}The Stars gift you the phoenix feather.{/i}"
    unknown "{i}May it write the stories for generations upon generations of witches.{/i}"
    hide quill with Dissolve(2.0)
    unknown "{i}House of the Stars...{/i}"
    stop music fadeout 6.0
    unknown "{i}May your journey be guided by knowledge.{/i}"

    "Stepping forward, I push the door open."
    scene schoolExterior with Fade(2.0,2.0,2.0)
    "I'm finally here... a new witch at Luminoire Academy!"
    "A grand facade beneath an even taller tree stands before me."
    "I won't take this opportunity for granted..."
    "I'm going to make the most of my time at Luminoire Academy!"
    play sound walkProf volume 0.2 fadein 3.0
    show circe Neutral with dissolve
    play music overworldMusic fadein 6.0
    k "Greetings! You wouldn't happen to be [name]?"
    char "No way! You're Professor Circe."

    menu:
        "The most experienced sorceress at Luminoire. I'm honored!":
            jump StellaNeu1
        "I loved your piece on the history of fey arcana!":
            jump StellaGood1

label StellaNeu1:
    ##show circeUpset
    k Upset "What are you suggesting about my age?"
    jump continuingStella1

label StellaGood1:
    ##show circeSmile
    k Smile "I appreciate that, but the article is outdated - by about 3000 years!"

label continuingStella1:
    k Neutral "Nevertheless, I'm flattered."
    k "I'd like to introduce you to my protégeé."
    show circe Neutral at left with move
    show celeste Neutral at right with dissolve
    show k inactive at left
    c "Hello. I'm Celeste."
    c "Congratulations on your enrollment."
    "She seems so... static."
    hide k inactive
    show c inactive at right
    k "Celeste here is one of the brightest students in Luminoire."
    k Smile "Though I think she seems to spend a little too much time in the library..."
    ##"Celeste blushes and squeezes her book."
    ##show celesteUpsetB at right
    hide c inactive
    show k inactive at left
    c Upset "Thank you, Professor."
    show c inactive at right
    hide k inactive
    k Neutral "I'll see you two tomorrow to discuss preparations for the Moonlight Ritual."
    k "Celeste, please show [name] to the Commons."
    show k inactive at left
    hide c inactive
    c Neutral "Of course, ma'am."
    #"[[Circe leaves]"
    hide k inactive with dissolve
    hide circe Neutral with dissolve
    show celeste Neutral at center with move
    ##hide circeNeutral with dissolve
    ##show celesteNeutral at center with move
    stop music fadeout 6.0
    "Celeste gestures for me to follow her down the main hall."
    "She stares down the hallway without turning to check if I'm following her."
    hide celeste Neutral with dissolve
    "It doesn't seem like she would enjoy small talk, so I keep to myself."
    scene nCommons with Fade(2.0,0.0,2.0)
    with Pause(2.0)
    "We quietly walk into a smaller hall - the Commons."
    show celeste Neutral with dissolve
    c "These will be our lodgings for the rest of the term."
    c "I usually use this space to pass time between classes..."

    c "[name], what's something you do to kill time?"
    menu:
        "\"Exploring places that I've never been!\"":
            ##"A small, knowing smile cracks on Celeste's face."
            $ celesteAP += 2
            show celeste Smile
            "Her attention turns towards me with a hint of excitement."
            c "Exploring the unknown is exactly what House Stella is all about."
            c Neutral "Not... that there's anything unknown here."
            "Celeste's demeanor reverts back to being closed off, but her charming smile remains at the corner of her cheek."
        "\"Visiting museums– they're rich with history!\"":
            $ celesteAP += 2
            c Smile "Luckily for you, you won't have to spend the money to go somewhere like that."
            "It's as though she has become less tense than when we introduced ourselves."
            c "Luminoire Academy is already so rich in the history of witches."
            c "In fact, I'd happily give you a tour of our oldest facilities."
            c Neutral "If you'd like, of course..."
            "I nod eagerly."
            char "That would be amazing!"
            "My enthusiasm amuses her and she leans against the wall."
        "\"Cracking open a book about folktales and fables.\"":
            $ celesteAP += 2
            c Smile "Really? I couldn't agree more."
            ##"Celeste's face brightens."
            "As she continues, I take a seat and lean forward, listening to her carefully."
            c "We can learn as much from historical tall tales as artifacts or ancient text!"
            c "Folklore reveals to the present the way that the past was perceived,"
            c "In terms of culture, politics, and relationships."
            c Neutral "It's just a matter of translating the ancient language to bring visions of the past to life."

    c Neutral "You seem pretty... trustworthy."
    "Celeste becomes inquisitive, as though observing my response."
    c Smile "And by that I mean reliable!"
    "Her awkward laugh comes out again, but much less forced than earlier."
    c Neutral "We should get some rest before tomorrow."
    c "I'll see you at the library - Goodnight."
    hide celeste Neutral with dissolve
    "She waves goodnight and enters the room across from mine."
    "I'm thankful that I made a decent first impression."
    "Hopefully I'll make an even better second impression after a good night's rest."
    scene black with Dissolve(3.0)
    show text "Day 2" with dissolve
    play sound dingDong1 fadein 3.0 volume 0.25
    with Pause(3.0)
    show text "3 Days Until the Full Moon Ritual..." with dissolve
    with Pause (3.0)
    jump day2Stella