#init python:
#    from wilson/Scene import SceneManager
#    config.developer = True
    # config.debug = True
#    config.log = 'active_speaker_logs.txt'
#    scene_manager = SceneManager(renpy)

#label campus:
#    scene amphitheater
#    # Add the character to the scene manager and they will be rendered every time "scene_say" is called.
#    $ scene_manager.add_character("mSmile", [left, walk_in_from_left])
#    # scene_say is a Creator-Defined Statement to help with handling the active speaker without
#    # having to show and hide characters yourself.
#    scene_say c "I'm {i}so{/i} late!"
#    scene_say c "I wonder where tasha is... I'm pretty sure we agreed to meet here."
#    scene_say c "Oh well, I'll wait for a few minutes."
#    $ scene_manager.add_character("mSmile", [right, walk_in_from_right])
#    scene_say m "Hey Circe! How's it going?"
#    scene_say c "Hey Morg! You look like you're in a hurry!"
#    scene_say m "I'm late for class! Got to go! Bye!!"
#    scene_say c "Bye!!"
#    $ scene_manager.add_transform("mSmile", walk_off_right_from_right_fast)
#    # Manually render the scene to trigger the movement transforms.
#    scene_say "{i}She's always in such a hurry!{/i}"
#    $ scene_manager.remove_character("mSmile")
#    $ scene_manager.add_character("silvia", [right, walk_in_from_right])
#    scene_say t "Hey! Sorry I'm late. Professor Hilden just kept talking."
#    scene_say t "I came as soon as I could."
#    scene_say c "It's no big deal, what did you want to do?"
#    scene_say t "Did you want to grab some food? I'm starving!"
#    scene_say c "Yeah! Let's go!"
#    scene_say t "Rain Forest Cafe it is! Come on!"
#    # We are going to walk the characters off the screen, so we no longer want active speaker triggering
#    $ scene_manager.ignore_speaking_flag = True
#    # toggle the flip Silvia flag so she faces the correct direction.
#    $ s.flip_flag = True
#    # Add the walking transforms.
#    $ scene_manager.add_transform("mSmile", walk_off_right_from_left)
#    $ scene_manager.add_transform("mSmile", walk_off_right_from_right)
#    scene_say "[s.name] and [c.name] head to the {b}Rain Forest Cafe{/b} just outside of campus."
#    # Clear the scene character list when you are done with the scene.
#    $ scene_manager.clear_character_list()

label campus:
    scene amphitheater1
    show morganaSmile
    m "I'm {i}so{/i} late!"
    m "I wonder where tasha is... I'm pretty sure we agreed to meet here."
    m "Oh well, I'll wait for a few minutes."
    show morganaSmile at left with move
    show circeNeutral at right with dissolve
    show cNeutral_inactive at right
    m "Hey Circe! How's it going?"
    show mSmile_inactive at left
    hide cNeutral_inactive
    show circeNeutral at right
    k "Hey Morg! You look like you're in a hurry!"
    show cNeutral_inactive at right
    hide mSmile_inactive
    show morganaSmile at left
    m "I'm late for class! Got to go! Bye!!"
    show mSmile_inactive at left
    hide circeNeutral
    show circeNeutral at right
    k "Bye!!"