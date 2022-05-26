label day4Stella:
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
    "I lean in and gently tap on her shoulder."
    "Celeste jumps slightly and turns her head towards me."
    c "Oh, [name], I didn't notice you there."
    jump day4StellaCont

label day4StellaBad:
    char "Celeste!"
    k "Shush, don't you remember where we are?"
    "Celeste's face turns a shade of pink."
    "She looks in my direction."
    c "We're in a library. Please don't do that again."
    char "A-ah, sorry."
    jump day4StellaCont

label day4StellaCont:
    "Celeste glances over to Circe examining a novel."
    c "We should talk about our research somewhere else."
    c "Come with me."
    "After waving a quick bye to our professor, Celeste leads me through the winding corridors."
    "We end up outside where a huge circular stage stands at the center."
    c "Have you been to the Amphitheater yet?"
    char "No... is this it?"
    c "Precisely, I thought it would be perfect to talk about it here."

    c "This is where they have the Ritual."
    c "I thought it might be best that you see it before your very eyes."
    c "Since you're already aware that this school is so rich in history."
    "Celeste gestures towards the stage."

    c "There are stories of the origins of the Academy."
    "Some stories you might hear about the school might tell you that it was constructed by several different magical beings and the high witches of Luminoire."
    "But that's not really the case."
    #scene Black Fade(1.0,0.0,1.0) 
    "You see, I ended up in some restricted area in the archives, and I found a notebook written by a faerie."
    "It took some time to decipher, but I found some information about how the school came to be."

    #scene CG_1 Fade(1.0,0.0,1.0) The gist is that our founder of Luminoire Academy desired a safe space for her lover and for future witches who felt outcasted.
    "They both lived in a small village."
    "But it wasn't something like a village of only witches."
    "Magic was more of an afterthought, not something to be trained and harnessed."
    "When their love was discovered, the villagers demanded they be burned."
    "They were being hunted down, and at the moment of capture her lover decided to sacrifice herself to save our fellow founder."
    "Since they weren't fully trained on their magic, they both had no idea what she was capable of."

    "A forest bloomed to hide themselves from the hunters, but the magic was so powerful that she crumbled into bright sand."
    "The faeries of the region, despite being peeved that there was now a large forest covering their homes, were so moved by the act that they helped construct our school now known as Luminoire Academy."
    "The realm of Luminoire was named after her lover."

    c "It's kind of romantic, don't you think?"
    c "The motivation to create something so grand and so powerful because of something like love?"
    c "I wonder what it's like to love someone so strongly."

    c "Ah, I can't believe telling that story took so much time!"
    c "I really should get going to the rites prep for the Ritual."
    c "You don't need to stay with me for this."
    menu:
        "I'd be willing to help.":
            c "That's very kind of you, but Professor Circe tasked me with this."
            c "I'll catch you in the Commons later."
        "Are you sure?":
            c "Don't worry!"
            c "Professor Circe tasked me with this."
            c "I'll catch you in the Commons later."

    #If CelesteAP == perfect
    c "[name], wait, before you go!"
    "She shuffles through her bag then offers the item to me."
    "It's a quill."
    char "Oh, thank you, Celeste!"
    c "I thought you might like it."
    c "It's a quill made out of an owl's feather."
    c "After all this time, I had a really wonderful time hanging out with you."
    c "It's the least I could do to thank you."
    c "Alright, I have to go back to prep."
    c "I'll see you at the Common soon."