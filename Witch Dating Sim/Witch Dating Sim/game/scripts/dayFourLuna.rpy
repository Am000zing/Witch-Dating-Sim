label day4Luna:
    #"Today is the final rehearsal for the Full Moon Ritual"
    scene dCommons with Fade(2.0, 1.0, 2.0)
    with Pause(2.0)
    "It's nice and early, about 30 minutes before I need to be at the Amphitheater"
    "Today is supposed to be the final rehearsal for the Full Moon Ritual"
    "Even though it's only been a few days for me at Luminoire Academy..."
    "It's been quite the experience so far!"
    "I head over to the Amphitheater..."
    scene amphitheater1 with Fade(2.0,0.0,2.0)
    "Eluna's already here, practicing her lines."
    "A few other students are already here too..."
    "Uh oh... did I arrive late somehow?"
    m "No, you didn't."
    show morgana Neutral with dissolve
    char "Professor Morgana! I didn't notice you there."
    m Smile "It's alright."
    m Neutral "There was something I wanted to talk to you about."
    play music conflictMusic fadein 6.0
    m "I know you aren't aware of Eluna's family name and bloodline."
    m "She doesn't exactly make it clear with many of her peers"
    m "She's always preferred to be on the down-low about these matters."
    m "Eluna comes from a prestigious family line of witches."
    m "I was tasked to ensure that her magical prowess would be maximized."
    m Upset "-and to not allow any potential distractions to her success."
    m Neutral "I think it's good that you and Eluna have befriended each other and have become so close."
    m "I'm sure Eluna appreciates you as well."
    m "But she has been spending much of her free time with you instead of practicing her magic."
    m "[name], I know you mean well but-"
    m Upset "Do not distract Eluna from her destiny."
    m "Understood?"

    "I quietly stare back at Professor Morgana."
    "Am I... holding Eluna back?"
    "How would Professor Morgana know what's best for Eluna?"
    "Has she even bothered to ask Eluna?"
    "Before I could respond-"
    m Neutral "I know you must feel defensive over Eluna's autonomy."
    m Upset "If I had a choice, I would want Eluna to explore and have a richer experience of her youth."  
    m Neutral "However, both Eluna and I understand how important her role is to her family."
    m "I implore you to understand as well."
    
    char "I see..."
    "Seems like Eluna's under a lot of pressure nonetheless."
    "But I don't want to be an interference to Eluna's success-"
    "And her future."
    stop music fadeout 6.0
    play sound clap fadein 5.0
    "From behind me I hear applause."
    "Eluna must be done with her rehearsal"
    e "[name]!"
    "I turn and see her beeline towards me."
    "I can feel Professor Morgana's piercing gaze..."
    show morgana Neutral at left with move
    show eluna Neutral at right with dissolve
    show m inactive at left
    e Neutral "I noticed you arrived a little earlier today."
    e Smile "Worried Professor Morgana would give you a hard time?"
    hide m inactive
    show e inactive at right
    m Smile "That should hardly be an issue."
    m Neutral "I should go greet the rest of the class."
    hide morgana Neutral with dissolve
    "Professor Morgana begins to walk towards the rest of the class, but then pauses next to me." #Professor Morgana? Because in most of the other messages we address her as such
    hide e inactive
    hide eluna Smile with dissolve
    "She quietly speaks to me-"
    show morgana Upset with dissolve
    m "Remember what I told you."
    hide morgana Upset with dissolve
    "She heads towards the rest of the class briskly."
    play music cgMusic fadein 6.0
    show eluna Neutral with dissolve
    e "I hope Professor hasn't been giving you a hard time."
    e Smile "She really does mean well."
    e Neutral "Are you free soon?"
    e "I wanted to ask if you'd like to come with me after rehearsals to the Greenhouse."
    e "Or anywhere, really, if you don't feel like going to the Greenhouse."
    stop music fadeout 5.0
    "I can feel Professor Morgana's stare from here."
    menu:
        "\"You should prioritize practicing for the ritual since it's tomorrow.\"":
            $ elunaAP += 3
            $ day4lunaGood = True
            e Upset "I see..."
            "She sighs deeply."
            "I hope I didn't upset her."
            e Neutral "You're right."
            e "I can't get too distracted now."
            e Smile "I need to make sure the ritual runs smoothly!"
            e "Plus, we can always go out after it's over" #Copyedited says "... go out after the it's over."
            char "Go out?"
            e NeutralB "Ah!"
            e Neutral "I meant like-"
            e "Just go out somewhere to celebrate the successes of the Full Moon Ritual, you know?"
            e "I should go back and practice."
            e Smile "I'll catch you back at the Commons!"
            if elunaAP == 13:
                e Neutral "Before you go-"
                "Eluna hands me an object."
                show e inactive with dissolve
                show hairclip at my_center with Dissolve(2.0)
                with Pause(2.0)
                $ hairclip = True
                "It's a beautifully adorned hairclip."
                hide hairclip with dissolve
                hide e inactive with dissolve
                e Smile "It's a reminder that we're going to meet up later, okay?"
                e "I'm holding you to it."
            hide eluna Smile with dissolve
            "Eluna briskly walks away."
        "\"I actually have an assignment that I have to finish tonight.\"":
            $ elunaAP += 2
            $ day4lunaGood = False
            e Upset "Oh, okay."
            e Neutral "It's good to focus on your studies."
            e "I should focus on practicing for the ritual anyways."
            e "I can't get too distracted now."
            e Smile "I need to make sure it runs smoothly!"
            e Neutral "I should go back to rehearsing."
            e "I'll see you back at the Commons."
            char "Yeah I'll catch you later."
            hide eluna Neutral with dissolve
            "Eluna walks back to the Amphitheater stage."
        "\"I'd love to, but I can't. I'll meet you in the Commons.\"":
            $ day4lunaGood = False
            $ elunaAP += 1
            e UpsetB "But you just got here!"
            play sound sparkle volume 0.2 fadein 3.0
            e Upset "You still have an obligation to stay for class or do schoolwork."
            "The air around us feels like crackling electricity."
            e "Is there something going on?"
            stop sound fadeout 3.0
            m "That's quite enough, Eluna." #Added a comma
            show eluna Upset at left with move
            show morgana Neutral at right with dissolve
            "Professor Morgana appears besides us."
            show e inactive at left
            m "Eluna, you should go continue rehearsing for tomorrow evening's ritual."
            hide e inactive
            show m inactive at right 
            e Neutral "I'm sorry, Professor Morgana."
            e "I should focus on practicing."
            e Upset "I can't afford any distractions."
            hide eluna Upset with dissolve
            "Eluna walks off to the Amphitheater stage."
            "I sigh."
            hide m inactive
            show morgana Neutral at center with move
            m "You can leave early if you must."
            m "I must go back to attend to class."
            hide morgana Neutral with dissolve
            "Before I could respond, Professor Morgana strides away."

    "I guess I'll go back to my room to read or study for a little bit."
    "I need to clear my head."
    "I leave the Amphitheater and head towards the Commons."
    "I do want to continue watching and helping out Eluna-"
    "But I don't want to further distract her, and the Ritual must go well."
    "As I make my exit, I look back at the stage-"
    "Eluna glances at me, and waves."
    "I wave back, and make my way back to the Commons."

    scene black with Dissolve(3.0)
    show text "Day 5" with dissolve
    play sound dingDong1 fadein 3.0 volume 0.25
    with Pause(3.0)
    show text "0 Days Until the Full Moon Ritual..." with dissolve
    with Pause(3.0)
    jump day5
#perfect run: 13
    ##hide Scene with Fade