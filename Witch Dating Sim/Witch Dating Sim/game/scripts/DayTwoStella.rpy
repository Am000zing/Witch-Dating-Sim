label day2Stella:
    "I'm still processing the fact that I've managed to make it into Luminoire Academy."
    "I'm in awe at everything I've seen here thus far…"
    "I've been constantly curious to learn more about this school's history."

    "I run into Circe upon entering the Commons."
    ##"She greets me with a wave, happy to see me."
    k "Oh, [name]! Good morning!"
    k "I hope you've been getting comfortable here."
    menu: 
        "Ah… I'm still getting used to it…":
            k "That's understandable. It's only your first day, after all."
            k "But you'll do great! I just know it."

        "I'm eager to learn more about everything!":
            k "That's the spirit! I assure you that you'll take much interest in some of my lessons."
            k "It'll be fun! I can hardly wait myself…"

    k "Ah, that's right. I'd like to invite you to the library."
    k "I believe Celeste's already there, as per usual."
    k "It's practically a second home to her in there…"
    k "Anyways, I'd like to discuss the Moonlight Ritual with the both of you."
    "Circe leads me though one of the school's many hallways, and we make it to an ornate door."
    k "Well, don't just stand there…"
    k "Come see the library for yourself."

    "I push the door open and and the first thing I see is rows upon rows of books."
    ##"Celeste notices me enter."
    c "Ah, good morning."
    ##"Circe flashes a smile at me."
    k "Ah, I need to attend to other duties. I'll leave you two to research."
    k "I'll see you both later then!"
    ##[[Circe leaves]
    "Now it's just me and Celeste. And the big pile of books between us."
    "Many of these books contain historical accounts of Luminoire Academy."
    "We both quietly shuffle through the pages, seldom making any eye contact."

    char "What are we looking for, exactly?"
    c "Anything about the Moonlight Ritual, really."
    c "We all know about the ritual's proceedings…"
    c "But I think it's strange how none of these relate to Luminoire Academy's founding."
    ##"Celeste places the book on the table, lips pursed."
    "Her attention then shifts to me."

    c "Besides that, don't you think that there seemed to be an… emphasis on the Florae language?"
    c "These accounts would refer to it every so often."
    c "There must be some reason why the faerie language is so intertwined with this school…"
    menu:
        "Don't you know fairies don't exist?":
            jump StellaBad1
        "I sit and quietly listen to Celeste's lecture.":
            jump StellaNeu2
        "The language is so ancient, it might have been connected to the school since it's very founding.":
            jump StellaGood2

label StellaBad1:
    c "Celeste tenses up for a moment, taken aback."
    c "If you’re going to be a part of Stella, you have to take your studies seriously."
    c "There has been evidence regarding the existence of fairies."
    c "We'd need to find out for sure."
    jump continuingStella2

label StellaNeu2:
    "Celeste takes one of the books and flips through the pages."
    c "Look in this book, for instance. This page has the ancient language written on it."
    c "Witches used to often be hunted in an era past."
    c "Some believe they used this language to communicate with each other in secret."
    c "I can't seem to find any sources quite yet, but it's also believed that they used it to announce important things."
    c "As witches learned Florae, the general public dismissed their messages as myths."
    "Celeste blinks and gently places the book back on the table. She laughs sheepishly."
    c "Sorry, I’ve been rambling on and on, and we haven’t even gotten started on the Full Moon ritual history research!"
    jump continuingStella2

label StellaGood2:
    "Celeste leans closer to me with a brightened expression."
    c "That’s exactly my hypothesis as well, and I’m hoping the research we’re doing will help with answering further questions!"
    c "If we know about the \"when\", then we'll soon be able to figure out the \"why\" too."
    jump continuingStella2

label continuingStella2:
    c "There's so many secrets within the language of the Florae."
    "She stares at the pile of books."
    c "I think it would be a good place to start for building up our research."
    c "The Florae language has been here for as long as the fairies have been mentioned."
    c "We need to see where it leads us."
    ##"Celeste's purses her lips once more."
    "My instincts tell me she knows a bit more than what she is letting on…"
    "She offers me a book."
    c "Let's look into it some more."

