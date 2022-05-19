image mSmile_mask = AlphaMask("the_darkness_70", "Morgana/morganaSmile.png")
image mSmile_inactive = Composite(
    (1000,1000),
    (0,0), "Morgana/morganaSmile.png",
    (0,0), "mSmile_mask"
)

image cNeutral_mask = AlphaMask("the_darkness_70", "Circe/circeNeutral.png")
image cNeutral_inactive = Composite(
    (1000,1000),
    (0,0), "Circe/circeNeutral.png",
    (0,0), "cNeutral_mask"
)

image mSmile_flip = im.Flip("Morgana/morganaSmile.png", horizontal=True)
image mSmile_flip_mask = AlphaMask("the_darkness_70", "mSmile_flip")
image mSmile_flip_inactive = Composite(
    (730,1080),
    (0,0), "mSmile_flip",
    (0,0), "mSmile_flip_mask"
)

#image morgSmile = ConditionSwitch(
#    "(scene_manager.active_speaker == s.name or scene_manager.ignore_speaking_flag) and s.flip_flag == True", "silvia_flip",
#    "s.flip_flag == True", "silvia_flip_inactive", "scene_manager.active_speaker == s.name or scene_manager.ignore_speaking_flag", "Morgana/morganaSmile.png",
#    "True", "mSmile_inactive")

image mSmile = ConditionSwitch(
    "(scene_manager.active_speaker == s.name or scene_manager.ignore_speaking_flag) and s.flip_flag == True", "mSmile_flip",
    "mSmile.flip_flag == True", "mSmile_flip_inactive",
    "scene_manager.active_speaker == s.name or scene_manager.ignore_speaking_flag", "Morgana/morganaSmile.png",
    "True", "mSmile_inactive")
