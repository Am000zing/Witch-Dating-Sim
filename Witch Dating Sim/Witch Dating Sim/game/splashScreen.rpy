label splashscreen:
    # scene black
    # with Pause(2.0)
    show text "Tangy's Taiwan presents..." with dissolve
    play music conflictMusic volume 0.5 fadein 6.0
    with Pause (2.0)

    scene titleArtBig with Fade(2.0, 1.0, 2.0)
    # play music conflictMusic volume 0.5 fadein 6.0
    with Pause(2.0)

    scene titleArt with Dissolve(5.0)

    return