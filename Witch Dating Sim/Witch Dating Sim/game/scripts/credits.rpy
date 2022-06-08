label credits:
    play music cgMusic fadein 6.0
    scene titleArtSmall with Fade(2.0, 1.0, 3.0)

    $ credits_speed = 100
    show credits at Move((0.78, 1.0), (0.78, -3.0), credits_speed, xanchor=0.78, yanchor=0)
    
    
    with Pause(credits_speed+2)
    stop music fadeout 5.0
    scene black with Dissolve(6.0)
