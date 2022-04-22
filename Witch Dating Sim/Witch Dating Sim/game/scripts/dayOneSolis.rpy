define s = Character('Summer', color='#f7c039')
define t = Character('Tasha', color='#ba1230')
define char = Character("name", dynamic=True, color='#f933ff')

label day1Solis:
    "Through the mist, a tall, stone door grows in front of me."
    "On it, the crest of the Sun is engraved into it."
    "Stepping forward, I push the door open."
    ##scene Schoolgrounds
    "I'm finally here... a new witch at Luminoire Academy!"
##    "The main hall of the school is lined with portraits of witches renown through the land."
    "I won't take this opportunity for granted..."
    "I'm going to make the most of my time at Luminoire Academy!"

    t "Salutations! You must be [name]."
    ##show tashaNeutral with dissolve
    "This tall woman approaches and circles me as though I were a new specimen."
    char "Dr. Tasha. It's an honor to meet you."

    menu:
        "Luminoire Academy has made so many accomplishments thanks to your research in alchemy." :
            jump Schoice1neutral
        "I'm really looking forward to alchemy in the Greenhouse - I'm excited to see what your lab has to offer." :
            jump Schoice1good

label Schoice1neutral:
    ##hide tashaNeutral
    ##show tashaUpset
    "Tasha sighs, almost disappointed at the response."
    t "Those are only stepping stones to a real {i}"accomplishment."{/i}"
    ##hide tashaUpset
    ##show tashaNeutral
    jump continuing1

label Schoice1good:
    ##hide tashaNeutral
    ##show tashaSmile
    t "Very interesting..."
    t "Choose your words carefully, otherwise my expectations of you will grow."
    ##hide tashaSmile
    ##show tashaNeutral
    jump continuing1

label continuing1:
    t "I look forward to seeing you in class, [name]."
    t "I'd like for you to meet my lab assistant."
    ##show tashaNeutral at left with move
    ##show summerSmile at right
    s "Hi there! I'm Summer."
    ##hide summerSmile
    ##show summerNeutral at right
    "Wow... As soon as she spoke, it was like she radiated kindness."
    s "[name], you'll be working with House Solis on a big project this week, so keep your head up, okay?"
    t "Despite being a first-year like you, she has made quite an impression."
    t "I've hand-picked her for her sharp eye for botany and animal-handling."
    ##hide summerNeutral
    ##show summerSmile at right
    s "Aww, Doctor. You don't have to flatter me like that."
    ##hide summerSmile
    ##show summerNeutral at right
    s "It's like you always say:"
    s "Great magic comes from the world around us. We just have to tap into it."
    ##hide tashaNeutral
    ##show tashaSmile at left
    t "Well put, Summer."
    ##hide tashaSmile
    ##show tashaNeutral at left
    t "Unfortunately, I have research to attend to at the moment, so Summer will give you the Luminoire tour."
    ##hide tashaNeutral
    ##show tashaSmile at left
    t "I'll see you in the Greenhouse soon, young alchemists!"
    ##hide tashaSmile with dissolve
    ##show summerNeutral at center with move
    s "Hope you don't mind it just being the two of us."
    "I definitely do not mind..."
    s "Let's head over to our dormitory!"
    "I follow Summer down the main hall into a living area."
    ##hide summerNeutral with dissolve
    ##hide Schoolgrounds
    ##scene Commons with Fade(2.0,0,2.0)
    ##show summerNeutral with dissolve
    s "Welcome to the Commons!"
    ##hide summerNeutral
    ##show summerSmile
    s "Get comfy, because we'll be here all year."
    ##hide summerSmile
    ##show summerNeutral
    jump summerAsk

label summerAsk:
    s "Hey, [name]. What's something you do to decompress?"
    menu:
        "I would brew a hot cup of tea.":
            ##hide summerNeutral
            ##show summerSmile
            s "Dang... Are you reading my mind or something?"
            ##hide summerSmile
            ##show summerNeutral
            s "I always brew myself a cup after a hard day's work with Dr. Tasha."
            "I notice a stove in the commons area."
            s "I see you've noticed the gas stove."
            ##hide summerNeutral
            ##show summerSmile
            s "If you ever want to join me for tea, let me know!"
            ##hide summerSmile
        "Take care of animals, big and small.":
##            "Summer's face lights up."
            ##hide summerNeutral
            ##show summerSmile
            s "For real?"
            s "Then you should come to my family's farm sometime!"
            ##hide summerSmile
            ##show summerNeutral
            s "Unfortunately pets aren't allowed unless they're familiars."
            ##hide summerNeutral
            ##show summerUpset
            s "I wish I could bring all of my babies to school..."
            ##hide summerUpset
        "I love to cook, especially with home-grown ingredients!":
            ##hide summerNeutral
            ##show summerSmile
            s "No way, you can cook, too?!"
            s "We need to exchange recipes. I'd love to try yours, sometime."
            ##hide summerSmile
##    "Summer blushes and plays with her right braid."
    ##show summerNeutralBlush
    s "Sorry... I won't let you listen to me ramble the evening away."
    s "We have a lot to do tomorrow, so we need as much rest as possible!"
    s "Night night, [name]."
    ##fade summerNeutral with dissolve
    "She disappears into a room next to mine."
    "I wonder what we'll be doing tomorrow..."

##jump dayTwoSolis