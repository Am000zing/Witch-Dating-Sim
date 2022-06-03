label day2Solis:
    play sound "..\\audio\\SFX\\SchoolBell1.wav"
    scene Commons with Fade (2.0, 1.0, 2.0)
    with Pause(1.0)
    "I wonder what today has in store for me."
    "Coming out of my room, I'm met eye-to-eye with..."
    show summer Neutral with dissolve
    s Smile "Good morning, sunshine!"
    s "Hope you had a restful sleep."
    s Neutral "We have a lot to get done before the Banquet!"
    s "Come with me. I want to show you something special."
    hide summer Neutral with dissolve
    scene greenhouse with Fade(2.0,2.0,2.0)
    "Summer eagerly takes me by the wrist as we travel from the Commons to an unfamiliar part of the academy."
    "We enter a room contained by shimmering glass."
    "Summer happily does a little twirl."
    show summer Neutral with dissolve
    s Smile "Welcome to the Greenhouse!"
    s Neutral "You and I will be working on cultivating and gathering ingredients."
    s Smile "All in preparation for the Full Moon Ritual!"
    "Summer guides me to a wall in the Greenhouse covered in magical plants of all kinds."
    s Neutral "For the ritual, we use only the finest ingredients."
    ##show tashaNeutral behind summerSmile with dissolve
    t "...all provided to the academy per my request."
    show summer Neutral at left with move
    show tasha Neutral at right with dissolve
    ##show summerSmile at left with move
    ##show tashaNeutral at right

    "Tasha rounds the corner from behind the wall, caressing the large leaves of the potted plants."
    t Smile "House Solis is responsible for tending to the Greenhouse with the utmost care."
    s "And todaaay...you'll be harvesting leaves from the rare hare basil."
    s "While endangered in most parts of the realm, the academy provides a haven for all living things."
    t Neutral "And in return, the gardens provide the magic we use to sustain the ritual."
    t "Summer, I trust you'll do well to train our new witch."
    t "I have much to attend to before the ritual."
    s Smile "You can always count on me!"
    t "Lovely. I leave it to you."
    hide tasha Neutral with dissolve
    ##"Tasha leaves."
    show summer Neutral at center with move
    s Neutral "I'm going to harvest the other ingredients from the gardens."
    s "I'll be keeping an eye on you, but no pressure!"
    hide summer Neutral with dissolve
    "Summer tends to another pocket of greenery elsewhere."
    ##hide summerSmile

    "You examine the basil plant before you."
    "Its stems shoot out from the pot."
    "There are large leaves crumpled on the soil, but even bigger ones growing from the plant."
    "How should I harvest it?"
    menu:
        "Cut it at the root.":
            $ summerAP +=  1
            "From a tray nearby, I take a pair of shears and go for the base of the stem."
            show summer Upset with dissolve
            s "WHAT ARE YOU DOING?!"
            "Summer snatches the shears from my hands."
            s "Be careful with these!"
            s "You could have killed the poor thing..."
            s Neutral "Here. I'll do it."
        "Collect the fallen leaves.":
            $ summerAP += 2
            "It looks like there are enough fallen leaves. I don't want to hurt the plant."
            "I take the few that I see and bring them over to Summer."
            show summer Neutral with dissolve
            s "Oh!"
            s Upset "These look a little... crumpled. Don't you think?"
            s Neutral "We should probably grab the larger leaves from the basil plant."
            s "That way it'll give it more room to grow out the younger, smaller leaves."
        "Pluck the largest ones.":
            $ summerAP += 3
            "The large leaves on the plant look enticing."
            "I carefully pluck them from the stem, making sure not to accidentally grab the small and young ones."
            show summer Smile with dissolve
            s "Good job!"
            s Neutral "These look great - you have an eye for harvesting."
            "I give the leaves to her."

    "Summer takes the leaves and ties them into a bundle."
    "In a mortar and pestle, she grinds it into a fine powder."
    "The atmosphere of the Greenhouse transforms as a fragrance fills the air."
    "At the end of the delicate process, Summer pours the powder into a mesh strainer and tosses it into a cauldron."
    show summer Smile
    s "At the banquet, we'll be serving this as a beverage for the ritual!"
    ##show summerNeutral
    s Neutral "Now that we're done here, let's head back to the Commons."
    hide summer Neutral with dissolve
    "I follow Summer back to the Commons"
    scene Commons with Fade(2.0, 0.0, 2.0)
    show summer Neutral with dissolve
    s "Okay, [name]."
    s "You did alright today, but you'll have to bring your A-Game tomorrow!"
    s "Meet me in the Library tomorrow."
    s "We're going to do some sweet research on the basics of magical agriculture."
    s "Goodnight!"
    hide summer Neutral with dissolve
    show text "Day 3 Solis" with dissolve
    show text "2 Days Until the Blood Moon Ritual..." with dissolve
    jump day3Solis