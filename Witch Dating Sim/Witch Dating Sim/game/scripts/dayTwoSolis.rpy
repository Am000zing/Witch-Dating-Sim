label day2Solis:
    "I wonder what today has in store for me."
    "Coming out of my room, I'm met eye-to-eye with..."
    ##show summerNeutral
    s "Good morning, sunshine!"
    s "Hope you had a restful sleep."
    s "We have a lot to get done before the Banquet!"
    s "Come with me. I want to show you something special."

    "Summer eagerly takes me by the wrist as we travel from the Commons to an unfamiliar part of the academy."
    "We enter a room contained by shimmering glass."
    "Summer happily does a little twirl."
    ##scene Greenhouse with Fade(2.0,2.0,2.0)
    ##show summerSmile
    s "Welcome to the Greenhouse!"
    s "You and I will be working on cultivating and gathering ingredients."
    s "All in preparation for the Full Moon Ritual!"
    "Summer guides me to a wall in the Greenhouse covered in magical plants of all kinds."
    s "For the ritual, we use only the finest ingredients."
    ##show tashaNeutral behind summerSmile with dissolve
    t "…all provided to the academy per my request."
    ##show summerSmile at left with move
    ##show tashaNeutral at right

    "Tasha rounds the corner from behind the wall, caressing the large leaves of the potted plants."
    t "House Solis is responsible for tending to the Greenhouse with the utmost care."
    s "And todaaay… you'll be harvesting leaves from the rare hare basil."
    s "While endangered in most parts of the realm, the academy provides a haven for all living things."
    t "And in return, the gardens provide the magic we use to sustain the ritual."
    t "Summer, I trust you'll do well to train our new witch."
    t "I have much to attend to before the ritual."
    s "You can always count on me!"
    t "Lovely. I leave it to you."
    ##hide tashaNeutral
    
    "Tasha leaves."
    s "I'm going to harvest the other ingredients from the gardens."
    s "I'll be keeping an eye on you, but no pressure!"
    "Summer tends to another pocket of greenery elsewhere."
    ##hide summerSmile

    "You examine the basil plant before you."
    "Its stems shoot out from the pot."
    "There are large leaves crumpled on the soil, but even bigger ones growing from the plant."
    "How should I harvest it?"
    menu:
        "Cut it at the root.":
            "From a tray nearby, I take a pair of shears and go for the base of the stem."
            ##show summerUpset
            s "WHAT ARE YOU DOING?!"
            "Summer snatches the shears from my hands."
            s "Be careful with these!"
            s "You could have killed the poor thing…"
            s "Here. I'll do it."
        "Collect the fallen leaves.":
            "It looks like there are enough fallen leaves. I don't want to hurt the plant."
            "I take the few that I see and bring them over to Summer."
            ##show summerNeutral
            s "Oh!"
            s "These look a little... crumpled. Don't you think?"
            s "We should probably grab the larger leaves from the basil plant."
            s "That way it'll give it more room to grow out the younger, smaller leaves."
        "Pluck the largest ones.":
            "The large leaves on the plant look enticing."
            "I carefully pluck them from the stem, making sure not to accidentally grab the small and young ones."
            ##show summerSmile
            s "Good job!"
            s "These look great - you have an eye for harvesting."
            "I give the leaves to her."

    ##show summerNeutral
    "Summer takes the leaves and ties them into a bundle."
    "In a mortar and pestle, she grinds it into a fine powder."
    "The atmosphere of the Greenhouse transforms as a fragrance fills the air."
    "At the end of the delicate process, Summer pours the powder into a mesh strainer and tosses it into a cauldron."
    ##show summerSmile
    s "At the banquet, we'll be serving this as a beverage for the ritual!"
    ##show summerNeutral
    s "Now that we're done here, let's head back to the Commons."
    "I follow Summer back to the Commons."
    jump day3Solis