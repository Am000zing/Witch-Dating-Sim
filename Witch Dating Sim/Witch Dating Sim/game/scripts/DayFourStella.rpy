label day4Stella:
    scene library with Fade(2.0, 3.0, 3.0)
    with Pause(1.0)
    "The library has slowly become more and more familiar."
    "Celeste said she would be here, so where is she?"
    "Then, before me sits a huge pile of books. Looking closer, there's a head peeking out."
    "Oh, there's Celeste."
    "She barely takes notice of me as she sticks her head within the mounds of pages."

    menu:
        "Tap on her shoulder":
            jump day4StellaNeu
        "Call out her name":
            jump day4StellaBad

label day4StellaNeu:
    $ celesteAP += 2
    #13
    "I lean in and gently tap on her shoulder."
    "Celeste jumps slightly and turns her head towards me."
    show celeste Neutral with dissolve
    c "Oh, [name], I didn't notice you there."
    jump day4StellaCont

label day4StellaBad:
    $ celesteAP += 1
    char "Celeste!"
    show circe Upset with dissolve
    k "Shush, don't you remember where we are?"
    hide circe Upset with dissolve
    "Celeste's face turns a shade of pink."
    "She looks in my direction."
    #blush
    show celeste Upset with dissolve
    c UpsetB "We're in a library. Please don't do that again."
    char "A-ah, sorry."
    jump day4StellaCont

label day4StellaCont:
    "Celeste glances over to Circe examining a novel."
    c Neutral "We should talk about our research somewhere else."
    c "Come with me."
    hide celeste Neutral with dissolve
    scene black with Dissolve(3.0)
    "After waving a quick bye to our professor, Celeste leads me through the winding corridors."
    scene amphitheater1 with Fade(2.0, 1.0, 2.0)
    play sound bird volume 0.2 fadein 3.0
    with Pause(2.0)
    "We end up outside where a huge circular stage stands at the center."
    show celeste Neutral with dissolve
    c "Have you been to the Amphitheater yet?"
    stop sound fadeout 6.0
    char "No..."
    char "Is this it?"
    c Smile "Precisely."
    c Neutral "I thought it would be perfect to talk about it here."

    c "This is where they have the Ritual."
    c "I thought it might be best that you see it before your very eyes."
    play music conflictMusic fadein 5.0
    c Smile "Since you're already aware that this school is so rich in history."
    "Celeste gestures towards the stage."
    c Neutral "There are stories of the origins of the Academy."
    c "Some stories you might hear about the school might tell you that it was constructed by several different magical beings and the high witches of Luminoire."
    c "But that's not really the case."
    hide celeste Neutral with dissolve
    scene black with Fade(2.0, 2.0, 2.0)
    with Pause (3.0)
    c "You see, I ended up in some restricted area in the archives, and I found a notebook written by a faerie."
    c "..."
    c "It took some time to decipher, but I found some information about how the school came to be."
    #scene CG_1 Fade(1.0,0.0,1.0)
    show p1 with Fade(1.0, 0.0, 1.0)
    #with Pause(3.0)
    "{i}The gist is that our founder of Luminoire Academy desired a safe space for her lover and for future witches who felt outcasted.{/i}"
    "{i}They both lived in a small village.{/i}"
    show p2a with Dissolve(2.0)
    "{i}But it wasn't something like a village of only witches.{/i}"
    "{i}Magic was more of an afterthought, not something to be trained and harnessed.{/i}"
    show p2b with Dissolve(2.0)
    show p3a with Dissolve(2.0)
    "{i}When their love was discovered-{/i}"
    #scene p3b with Dissolve(2.0)
    show p3c with Dissolve(1.0)
    "{i}-the villagers demanded they be burned.{/i}"
    show p4a with Dissolve(2.0)
    "{i}They were being hunted down, and at the moment of capture-"
    show p4b with Dissolve(2.0)
    "{i}-her lover decided to sacrifice herself to save our fellow founder.{/i}"
    "{i}Since they weren't fully trained on their magic-{/i}"
    show p4c with Dissolve(2.0)
    scene black with Dissolve(4.0)
    with Pause(2.0)
    "{i}-they both had no idea what she was capable of.{/i}"
    with Pause (2.0)
    stop music fadeout 10.0
    scene p5a with Fade(2.0, 0.0, 3.0)
    scene p5b with Dissolve(3.0)
    "{i}A forest bloomed to hide themselves from the hunters-{/i}"
    scene p5c with Dissolve(2.0)
    with Pause(3.0)
    "{i}-but the magic was so powerful-{/i}"
    scene p6 with Dissolve(3.0)
    "{i}-that she crumbled into bright sand.{/i}"
    play music cgMusic fadein 10.0
    show p7 with Dissolve(2.0)
    "{i}The faeries of the region, despite being peeved that there was now a large forest covering their homes-{/i}"
    "{i}-were so moved by the act that they helped construct our school now known as Luminoire Academy.{/i}"
    scene p8 with Fade(3.0, 0.0, 3.0)
    "{i}The realm of Luminoire was named after her lover.{/i}"
    scene amphitheater2 with Fade(2.0, 0.0, 2.0)
    with Pause(2.0)
    show celeste Neutral with dissolve
    c "It's kind of romantic, don't you think?"
    c "The motivation to create something so grand and so powerful because of something like love?"
    c NeutralB "I wonder what it's like to love someone so strongly."

    c Neutral "Ah, I can't believe telling that story took so much time!"
    c "I really should get going to the rites prep for the Ritual."
    c "You don't need to stay with me for this."
    stop music fadeout 6.0
    menu:
        "I'd be willing to help.":
            $ celesteAP += 2
            c "That's very kind of you, but Professor Circe tasked me with this."
            c "I'll catch you later."
        "Are you sure?":
            $ celesteAP += 2
            c "Don't worry!"
            c "Professor Circe tasked me with this."
            c "I'll catch you later."

    if celesteAP == 15:
        c "[name], wait, before you go!"
        "She shuffles through her bag then offers the item to me."
        show c inactive with dissolve
        show owlQuill at my_center with Dissolve(2.0)
        $ owl = True
        "It's a quill."
        hide owlQuill with dissolve
        char "Oh, thank you, Celeste!"
        c "I thought you might like it."
        c "It's a quill made out of an owl's feather."
        c "After all this time, I had a really wonderful time hanging out with you."
        c Smile "It's the least I could do to thank you."
        c Neutral "Alright, I have to go back to prep."
    else:
        c "See you at the Commons soon."
    scene black with Dissolve(3.0)
    show text "Day 5" with dissolve
    play sound dingDong1 fadein 3.0 volume 0.25
    with Pause(3.0)
    show text "0 Days Until the Full Moon Ritual..." with dissolve
    with Pause (3.0)
    #perfect: 15
    jump day5