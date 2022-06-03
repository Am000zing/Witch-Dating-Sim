label day3Solis:
    play sound "..\\audio\\SFX\\SchoolBell1.wav"
    scene Commons with Fade (2.0, 1.0, 2.0)
    with Pause(1.0)
    "Todays the day. I have to do well, I can't disappoint Summer now."
    "After getting ready, I stumble out of the commons, hastily making my way to the grand library."
    scene Library with Fade(2.0, 0.0, 2.0)

    "From the front desk, Summer spots me and waves cheerily, standing next the history instructor, Professor Circe."
    show summer Neutral with dissolve
    s "Morning, sunshine."
    s "Got enough sleep yesterday?"
    s Smile "Prepare to be worked to the bone."
    s Neutral "Today, we're hitting the books!"
    show summer Neutral at right with move
    show circe Neutral at left with dissolve
    show s inactive at right
    k Neutral "Good morning, [name]."
    k "I've heard from Dr. Tasha that you'll be researching magical dishes."
    k "I'm here to offer my guidance in any way I can."
    k "Follow me to the arcane cuisine section."
    hide s inactive
    hide summer Neutral with dissolve
    hide circe Neutral with dissolve
    "Summer and I follow Circe through the towering aisles of bookshelves"
    "Circe suddenly stops in the middle of the aisle."
    show circe Neutral with dissolve
    k "Typically, the Library is reserved to my studious Stella witches..."
    k Smile "But I'll gladly make an exception for the both of you"
    "Casting a spell on the books, they begin to flow and float from the shelves, encircling, Circe, Summer, and I in the air."
    k Neutral "Besides, finding recipes for the banquet is an exciting task!"
    k "We have recipe books from ages past..."
    show circe Neutral at left with move
    show summer Neutral at right with dissolve
    show k inactive at left
    s Neutral "Oh, I think what we're looking for is much simpler than you think."
    hide k inactive
    "The books begins to spin faster and faster."
    "I try to look at the titles but my eyes can't keep up."
    "I'm about to fall over from being dizzy when Summer takes my hand and raises her hand politely to Professor Circe."
    show k inactive at left
    s "Professor, we're specifically looking for arcane desserts."
    "Summer squeezes my hand, and lets go trying to elaborate."
    s "Do you have a book containing a dish known as \"Cloying Crumble.\""
    hide k inactive
    show s inactive at right
    k "Cloying Crumble?"
    k Smile "How curious..."
    k Neutral "That's an *interesting* choice for the centerpiece of the banquet, Summer."
    "Summer squeezes her hands into ambitious fists."
    hide s inactive
    show k inactive at left
    s Upset "One thing you should know about us Solis witches, Professor Circe..."
    s Smile "... Is that we're always up for a challenge!"
    hide k inactive
    show s inactive at right
    k "Oh, my!"
    k Smile "I can see why Doctor Tasha speaks so highly of her personal assistant."
    "A large recipe book titled Dorothy's Desserts descends gently into Summer's hands."
    k Neutral "I believe this book contains the recipe you seek."
    hide s inactive
    show k inactive at left
    s Neutral  "Thank you, Professor!"
    hide k inactive
    show s inactive at right
    k Neutral "Do be careful, it's a complicated dish."
    hide s inactive
    hide circe Neutral with dissolve
    hide summer Neutral with dissolve

    scene greenhouse with Fade (2.0, 0.0, 2.0)
    "After retrieving Volume 106 of Dorothy's Desserts, Summer and I travel back to the Greenhouse."
    "In the corner of the laboratory, Summer flips to a page titled \"Cloying Crumble.\""
    show summer Neutral with dissolve
    s "[name], do you know what \"cloying\" means?"
    s "It means sickeningly sweet."
    s "The key to making this crumble is a very special ingredient..."
    "Summer points to a red note at the end of the page."
    "{i}WARNING TO THE CHEF:{/i}"
    "{i}Harvest the honeycomb within the hour of the harvest.{/i}"
    s "The Greenhouse received a shipment of haunted honeycomb recently."
    s "However, in order to protect it's delicate sweetness the guard bees protect the honeycomb."
    s Smile "I'm going to go look for it. I'm sure I left it around here."
    s Neutral "I'll be right back!"
    hide summer Neutral with dissolve
    "Summer disappears around a corner to look for the shipment."
    "I hear a faint buzzing sound growing from underneath the lab bench."
    "Ducking under the table I notice a small wooden box"
    "Across the lid of the crate is the label \"HAUNTED HONEYBEES.\""

    "Pulling out the box I ponder what to do next."
    "Summer isn't back yet. This could be my chance to really help her."
    "But what even are *haunted* honeybees?"
    "I should be careful about opening this box..."
    menu:
        "Lift the lid from the crate to get a good look inside to investigate.":
            $ summerAP += 3
            "In the darkness of the crate, tiny, glowing bees float to the top."
            "They suspend themselves at the top of the crate, gently flying around my face."
            s "Oh! I see you're already two steps ahead of me."
            show summer Neutral with dissolve
            "Spinning around, I see Summer had returned."
            s "I forgot that I already unloaded the shipment."
            s "Thank you for opening the lid - I'm sure they wanted a little bit of space to fly around."
            s Smile "And it looks like they've taken fondly to you."
            s "Good thing you didn't use any magic, these guys hate that stuff."
            s "Tasks like these require a kind touch."
        "Cast a spell of telekinesis and collect honeycomb without touching the box.":
            $ summerAP += 1
            "A relatively simple spell, the lid slowly floats off the crate."
            "The inside of the crate begins to glow red. The ight from the inside begins to flicker."
            s "Put the lid down!"
            show summer Upset with dissolve
            "Summer comes bursting in, breaking my concentration, the lid drops to the ground, knocking over the crate."
            "Summer fumbles and slides next to the crate, catching it before it spills over."
            "She sets it back up and looks into the crate worriedly."
            s "This is all my fault."
            s "I should have told you that this breed of bees are sensitive to all types of magic..."
            s "I'll take care of this..."
            "Summer pulls the crate away from me."
            s Neutral "You know, magic can't solve all of our problems."
        "Don some gardening gloves, open the lid, and feel around the inside of the box.":
            $ summerAP += 2
            "After slipping on some thick gloves, I lift the lid and set it down gently next to the crate."
            "The crate is dark, and it seems that there are only honeycombs inside."
            "But no honeybees."
            "With the gloves on, I go into to pick up a loose piece of honeycomb."
            "As I go into grab one, a vivid, red light flashes against my glove and zaps my finger."
            "I pull my hand out, and more red lights flash from inside, lighting up and going out."
            s "[name] take those off!"
            show summer Upset with dissolve
            "Summer catches me off guard, gesturing towards the gloves."
            s Neutral "The bees will think they're being attacked by a non-living entity and retaliate."
            "I take my gloves off and peer back into the crate."
            "The once flashing red lights dissolve into gentle, blue lights."
            s Smile "Perfect! Looks like they're calm now."

    "Summer, with her bare hands, scoops out a piece of the haunted honeycomb."
    "The honeybees glow a gently blue light, hovering around her hands."
    "In a hushed voice, Summer whispers something to the bees."
    "Honeycomb in hand, the bees follow her to the cauldron as she drops the ingredients in."
    s Neutral "The honeybees need to protect the honeycomb-"
    s Smile "-otherwise it'll be too sweet and throw off the whole crumble."
    s Neutral "Now we have our dessert and the bees have more than enough for their hive."
    # menu:
    #     "I consume a piece of the honeycomb myself":
    #         s "[name], NOOOOO!"
    "We watch as the Cauldron bubbles mixing in the ingrediencies delicately."
    s "You know, [name], I'm glad you came to help me out today."
    "As I turn to look at her, Summer takes a hold of my hand."
    s Upset "I... don't have too many friends at the academy, they're always a little hesitant with how giddy I am."
    s "So when you first agreed to come with me I was really worried, maybe you'd think the same way as everyone else."
    s Neutral "But I'm glad that wasn't the case."
    s Smile "Thanks [name]."
    s Neutral "We should head back to the Commons."
    s "It's been a long day, and you must be tired."
    s "Do you wanna grab a bite with me on the way though?"
    s "There won't be any bees to deal with."
    "I feel a small rumble in my stomach."
    "I could really go for some food before heading back to my room."
    char "That sounds like a great idea."
    s Smile "Great!"
    hide summer Smile with dissolve
    show text "Day 4 Solis" with dissolve
    show text "1 Day Until the Blood Moon Ritual..." with dissolve
    jump day4Solis