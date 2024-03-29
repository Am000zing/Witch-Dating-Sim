label day1Solis:
    "Through the mist, a tall, stone door appears in front of me."
    scene solisDoor with Fade(1.0,0.0,1.0)
    "The crest of the Sun is engraved into it."
    show tea at my_center with Dissolve(2.0)
    "An ethereal voice speaks:"
    unknown "{i}The Sun gifts you the tea leaves of amelioration.{/i}"
    unknown "{i}May it soothe the pain that comes with time.{/i}"
    hide tea with Dissolve(2.0)
    unknown "{i}House of the Sun...{/i}"
    stop music fadeout 6.0
    unknown "{i}May your journey be guided by patience.{/i}"

    "Stepping forward, I push the door open..."
    scene schoolExterior with Fade(2.0,2.0,2.0)
    "I'm finally here... a new witch at Luminoire Academy!"
    "A grand facade beneath an even taller tree stands before me."
    "I won't take this opportunity for granted..."
    "I'm going to make the most of my time here at Luminoire Academy!"

    t "Salutations! You must be [name]."
    play sound walkProf volume 0.2 fadein 3.0
    show tasha Neutral with dissolve
    play music overworldMusic fadein 6.0
    #volume 0.5
    "This tall woman approaches me, circling around me as if I were a new specimen for her to study."
    char "Professor Tasha! It's an honor to meet you."

    menu:
        "\"Luminoire Academy has accomplished so much thanks to your research in alchemy.\"" :
            jump Schoice1neutral
        "\"I'm really looking forward to alchemy in the Greenhouse - I'm excited to see what your lab has to offer.\"" :
            jump Schoice1good

label Schoice1neutral:
    show tasha Upset
    "Professor Tasha sighs, almost disappointed at the response."
    t "Those are merely stepping stones to the real {i}\"accomplishment.\"{/i}"
    show tasha Neutral
    jump continuing1

label Schoice1good:
    show tasha Smile
    t "Very interesting..."
    t Neutral "Choose your words carefully, otherwise my expectations of you will grow steeper."
    jump continuing1

label continuing1:
    t Neutral "I look forward to seeing you in class, [name]."
    t "I'd like for you to meet my lab assistant."
    show tasha Neutral at left with move
    show summer Neutral at right with dissolve
    show t inactive at left with dissolve
    s Smile "Hi there! I'm Summer."
    "Wow...from the moment she first spoke, she felt as if she was just radiating kindness."
    s Neutral "[name], you'll be working with House Solis on a big project this week, so keep your head up, okay?"
    hide t inactive
    show s inactive at right
    t "Despite being a first-year, much like you, she has already made quite an impression."
    t "I've hand-picked her for her sharp eye for botany and animal-handling."
    hide s inactive
    show t inactive at left
    s Smile "Aww, Doctor. You don't have to flatter me like that."
    s Neutral "It's like you always say:"
    s "Great magic comes from the world around us. We just have to tap into it."
    hide t inactive
    show s inactive at right
    t Smile "Well put, Summer."
    t Neutral "Unfortunately, I have research to attend to at the moment, so Summer will give you the Luminoire tour."
    t Smile "I'll see you in the Greenhouse soon, young alchemists!"
    hide tasha Smile with dissolve
    hide s inactive with dissolve
    show summer Neutral at center with move
    s "Hope you don't mind it just being the two of us."
    "I definitely do not mind..."
    s Smile "Great! Then let's head over to our dormitory!"
    "Did she just-?"
    hide summer Neutral
    "Summer darts off immediately."
    "I follow her down the main hall into a living area."
    stop music fadeout 6.0
    scene nCommons with Fade(2.0,1.0,3.0)
    show summer Neutral with dissolve
    s "Welcome to the Commons!"
    s Smile "Get comfy, because we'll be here all year."
    s Neutral "Each term can get real intense from the get-go..."
    jump summerAsk

label summerAsk:
    s "Hey, [name]. What's something you do to decompress?"
    menu:
        "\"I would brew a hot cup of tea.\"":
            $ summerAP += 2
            s Smile "Dang... Are you reading my mind or something?"
            s Neutral "I always brew myself a cup after a hard day's work with Dr. Tasha."
            "My attention is directed to a stove in the commons area."
            s "Ah! I see you've noticed the gas stove."
            s Smile "If you ever want to join me for tea, let me know!"
        "\"Take care of animals, big and small.\"":
##          "Summer's face lights up."
            $ summerAP += 2
            s Smile "For real?"
            s "You should come to my family's farm sometime, then!"
            s Neutral "Pets aren't allowed here unless they're familiars, unfortunately."
            s Upset "I wish I could bring all of my babies to school..."
        "\"I love to cook, especially with home-grown ingredients!\"":
            $ summerAP += 2
            s Smile "No way, you can cook, too?!"
            s "We need to exchange recipes then! I'd love to try yours sometime."
    ##show summerNeutralBlush
    s Neutral "Sorry... I shouldn't let you listen to me ramble the evening away."
    s "We have a lot to do tomorrow, so we need as much rest as possible!"
    s "Night night, [name]."
    hide summer Neutral with dissolve
    "She disappears into a room next to mine."
    "I wonder what we'll be doing tomorrow..."
    ##hide Commons with Fade(1.0,1.0,1.0) 
    scene black with Dissolve(3.0)
    show text "Day 2" with dissolve
    play sound dingDong1 fadein 3.0 volume 0.25
    with Pause(3.0)
    show text "3 Days Until the Full Moon Ritual..." with dissolve
    with Pause (3.0)
    jump day2Solis