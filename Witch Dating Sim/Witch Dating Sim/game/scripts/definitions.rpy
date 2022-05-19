define e = Character('Eluna', color='#ff94c1')
define m = Character('Morgana', color='#52e5ff')
define s = Character('Summer', color='#ff94c1')
define t = Character('Tasha', color='#52e5ff')
define c = Character('Celeste', color='#ff94c1')
define k = Character('Circe', color='#52e5ff')
define char = Character("name", dynamic=True, color='#fff4ff')
define unknown = Character("unknown", color= '#ffa9a6')

image lunaDoor = "BackgroundCG/lunaDoor.png"
image solisDoor = "BackgroundCG/solisDoor.png"
image stellaDoor = "BackgroundCG/stellaDoor.png"
image schoolExterior = "BackgroundCG/schoolExterior.PNG"
image greenhouse = "BackgroundCG/greenhouse.png"
image amphitheater1 = "BackgroundCG/dayAmphitheater.png"
image amphitheater2 = "BackgroundCG/nightAmphitheater.png"
image amphitheater3 = "BackgroundCG/night2Amphitheater.png"

image morganaNeutral = "Morgana/morganaNeutral.png"
image mNeutral_mask = AlphaMask("the_darkness_70", "Morgana/morganaNeutral.png")
image mSmile_inactive = Composite(
    (1000,1000),
    (0,0), "Morgana/morganaNeutral.png",
    (0,0), "mSmile_mask"
)

image cNeutral_mask = AlphaMask("the_darkness_70", "Circe/circeNeutral.png")
image cNeutral_inactive = Composite(
    (1000,1000),
    (0,0), "Circe/circeNeutral.png",
    (0,0), "cNeutral_mask"
)

image tNeutral_mask = AlphaMask("the_darkness_70", "Circe/tashaNeutral.png")
image tNeutral_inactive = Composite(
    (1000,1000),
    (0,0), "Tasha/tashaNeutral.png",
    (0,0), "tNeutral_mask"
)

image morganaSmile = "Morgana/morganaSmile.png"
image morganaUpset = "Morgana/morganaUpset.png"
image tashaNeutral = "Tasha/tashaNeutral.png"
image tashaUpset = "Tasha/tashaUpset.png"
image tashaSmile = "Tasha/tashaSmile.png"
image circeNeutral = "Circe/circeNeutral.png"
image circeSmile = "Circe/circeSmile.png"
image circeUpset = "Circe/circeUpset.png"

