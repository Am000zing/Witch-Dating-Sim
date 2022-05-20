define e = Character('Eluna', color='#ff94c1', image = "eluna")
define m = Character('Morgana', color='#52e5ff', image = "morgana")
define s = Character('Summer', color='#ff94c1', image = "summer")
define t = Character('Tasha', color='#52e5ff', image = "tasha")
define c = Character('Celeste', color='#ff94c1')
define k = Character('Circe', color='#52e5ff')
define char = Character("name", dynamic=True, color='#db7fee')
define unknown = Character("unknown", color= '#ffa9a6')

image lunaDoor = "BackgroundCG/lunaDoor.png"
image solisDoor = "BackgroundCG/solisDoor.png"
image stellaDoor = "BackgroundCG/stellaDoor.png"
image schoolExterior = "BackgroundCG/schoolExterior.PNG"
image greenhouse = "BackgroundCG/greenhouse.png"
image amphitheater1 = "BackgroundCG/dayAmphitheater.png"
image amphitheater2 = "BackgroundCG/nightAmphitheater.png"
image amphitheater3 = "BackgroundCG/night2Amphitheater.png"

image mNeutral_mask = AlphaMask("the_darkness_70", "Morgana/morganaNeutral.png")
image m inactive = Composite(
    (1000,1000),
    (0,0), "Morgana/morganaNeutral.png",
    (0,0), "mSmile_mask"
)

image kNeutral_mask = AlphaMask("the_darkness_70", "Circe/circeNeutral.png")
image k inactive = Composite(
    (1000,1000),
    (0,0), "Circe/circeNeutral.png",
    (0,0), "kNeutral_mask"
)

image tNeutral_mask = AlphaMask("the_darkness_70", "Circe/tashaNeutral.png")
image t inactive = Composite(
    (1000,1000),
    (0,0), "Tasha/tashaNeutral.png",
    (0,0), "tNeutral_mask"
)

image morgana Neutral = "Morgana/morganaNeutral.png"
image morgana Smile = "Morgana/morganaSmile.png"
image morgana Upset = "Morgana/morganaUpset.png"
image tasha Neutral = "Tasha/tashaNeutral.png"
image tasha Upset = "Tasha/tashaUpset.png"
image tasha Smile = "Tasha/tashaSmile.png"
image circe Neutral = "Circe/circeNeutral.png"
image circe Smile = "Circe/circeSmile.png"
image circe Upset = "Circe/circeUpset.png"

###########################################################################################################

image eNeutral_mask = AlphaMask("the_darkness_70", "Eluna/elunaNeutral.png")
image e inactive = Composite(
    (1000,1000),
    (0,0), "Eluna/elunaNeutral.png",
    (0,0), "eNeutral_mask"
)

# image cNeutral_mask = AlphaMask("the_darkness_70", "Celeste/celesteNeutral.png")
# image c inactive = Composite(
#     (1000,1000),
#     (0,0), "Celeste/celesteNeutral.png",
#     (0,0), "cNeutral_mask"
# )

image sNeutral_mask = AlphaMask("the_darkness_70", "Summer/summerNeutral.png")
image s inactive = Composite(
    (1000,1000),
    (0,0), "Summer/summerNeutral.png",
    (0,0), "sNeutral_mask"
)

image eluna Neutral = "Eluna/elunaNeutral.png"
image eluna Smile = "Eluna/elunaSmile.png"
image eluna Upset = "Eluna/elunaUpset.png"
image summer Neutral = "Summer/summerNeutral.png"
image summer Upset = "Summer/summerUpset.png"
image summer Smile = "Summer/summerSmile.png"
# image celeste Neutral = "Celeste/celesteNeutral.png"
# image celeste Smile = "Celeste/celesteSmile.png"
# image celeste Upset = "Celeste/celesteUpset.png"
