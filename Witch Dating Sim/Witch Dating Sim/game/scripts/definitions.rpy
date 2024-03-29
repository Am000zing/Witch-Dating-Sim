###########################################################################################################

define e = Character('Eluna', color='#ff94c1', image = "eluna")
define m = Character('Morgana', color='#52e5ff', image = "morgana")
define s = Character('Summer', color='#ff94c1', image = "summer")
define t = Character('Tasha', color='#52e5ff', image = "tasha")
define c = Character('Celeste', color='#ff94c1', image = "celeste")
define k = Character('Circe', color='#52e5ff', image = "circe")
define char = Character("name", dynamic=True, color='#db7fee')
define unknown = Character("unknown", color= '#ffa9a6')
define student1 = Character("Student 1", color='#3419ca')
define student2 = Character("Student 2", color='#ca19a1')
define student3 = Character("Student 3", color='#3419ca')
define student4 = Character("Student 4", color='#ca19a1')
define student5 = Character("Student 5", color='#3419ca')
define student6 = Character("Student 6", color='#ca19a1')

###########################################################################################################

image dampmask = AlphaMask("the_darkness_70", "BackgroundCG/nightAmphitheater.png")
image darkAmphitheater = Composite(
    (1920,1080),
    (0,0), "BackgroundCG/nightAmphitheater.png",
    (0,0), "dampmask"
)

image lunaDoor = "BackgroundCG/lunaDoor.png"
image solisDoor = "BackgroundCG/solisDoor.png"
image stellaDoor = "BackgroundCG/stellaDoor.png"
image schoolExterior = "BackgroundCG/schoolExterior.PNG"
image greenhouse = "BackgroundCG/greenhouse.png"
image amphitheater1 = "BackgroundCG/dayAmphitheater.png"
image amphitheater2 = "BackgroundCG/nightAmphitheater.png"
image amphitheater3 = "BackgroundCG/Amphitheater3.png"
#image Commons = "BackgroundCG/commonsHolder.png"
image dCommons = "BackgroundCG/dayCommons.png"
image nCommons = "BackgroundCG/nightCommons.png"
image library = "BackgroundCG/LibraryV4.png"
image black = "BackgroundCG/black.png"
image titleArtBig = "BackgroundCG/titleArtBig.png"
image titleArt = "BackgroundCG/titleArt.png"
image titleArtSmall = "BackgroundCG/titleArtSmall.png"

image p1 = "BackgroundCG/Page_1.png"
image p2a = "BackgroundCG/Page_2a.png"
image p2b = "BackgroundCG/Page_2b.png"
image p3a  = "BackgroundCG/Page_3a.png"
image p3b = "BackgroundCG/Page_3b.png"
image p3c = "BackgroundCG/Page_3c.png"
image p4a = "BackgroundCG/Page_4a.png"
image p4b = "BackgroundCG/Page_4b.png"
image p4c = "BackgroundCG/Page_4c.png"
image p5a = "BackgroundCG/Page_5a.png"
image p5b = "BackgroundCG/Page_5b.png"
image p5c = "BackgroundCG/Page_5c.png"
image p6 = "BackgroundCG/Page_6.png"
image p7 = "BackgroundCG/Page_7.png"
image p8 = "BackgroundCG/Page_8.png"

image quill = "graphics/quill.png"
image candle = "graphics/candle.png"
image tea = "graphics/teaLeaves.png"
image sunflowers = "graphics/sunflowers.png"
image violet = "graphics/violet.png"
image hairclip = "graphics/hairclip.png"
image owlQuill = "graphics/owlQuill.png"
image credits = "graphics/credits.png"

###########################################################################################################

image mNeutral_mask = AlphaMask("the_darkness_70", "Morgana/morganaNeutral.png")
image m inactive = Composite(
    (1000,1000),
    (0,0), "Morgana/morganaNeutral.png",
    (0,0), "mNeutral_mask"
)

image kNeutral_mask = AlphaMask("the_darkness_70", "Circe/circeNeutral.png")
image k inactive = Composite(
    (1000,1000),
    (0,0), "Circe/circeNeutral.png",
    (0,0), "kNeutral_mask"
)

image tNeutral_mask = AlphaMask("the_darkness_70", "Tasha/tashaNeutral.png")
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
    (1100,1073),
    (0,0), "Eluna/elunaNeutral.png",
    (0,0), "eNeutral_mask"
)

image cNeutral_mask = AlphaMask("the_darkness_70", "Celeste/celesteNeutral.png")
image c inactive = Composite(
    (950,950),
    (0,0), "Celeste/celesteNeutral.png",
    (0,0), "cNeutral_mask"
)

image sNeutral_mask = AlphaMask("the_darkness_70", "Summer/summerNeutral.png")
image s inactive = Composite(
    (950,943),
    (0,0), "Summer/summerNeutral.png",
    (0,0), "sNeutral_mask"
)

image eluna Neutral = "Eluna/elunaNeutral.png"
image eluna Smile = "Eluna/elunaSmile.png"
image eluna Upset = "Eluna/elunaUpset.png"
image eluna NeutralB = "Eluna/elunaNeutralB.png"
image eluna SmileB = "Eluna/elunaSmileB.png"
image eluna UpsetB = "Eluna/elunaUpsetB.png"

image summer Neutral = "Summer/summerNeutral.png"
image summer Upset = "Summer/summerUpset.png"
image summer Smile = "Summer/summerSmile.png"
image summer NeutralB = "Summer/summerNeutralB.png"
image summer UpsetB = "Summer/summerUpsetB.png"
image summer SmileB = "Summer/summerSmileB.png"

image celeste Neutral = "Celeste/celesteNeutral.png"
image celeste Smile = "Celeste/celesteSmile.png"
image celeste Upset = "Celeste/celesteUpset.png"
image celeste NeutralB = "Celeste/celesteNeutralB.png"
image celeste SmileB = "Celeste/celesteSmileB.png"
image celeste UpsetB = "Celeste/celesteUpsetB.png"

############################################################songs_and_all_that_bizazz#############

define introQuizMusic = "..//audio//MUSIC//IntroQuiz.mp3"
define conflictMusic = "..//audio//MUSIC//Conflict.wav"
define overworldMusic = "..//audio//MUSIC//OverworldMusic.mp3"
define cgMusic = "..//audio//MUSIC//CGMusic_M1.mp3"

define bee = "..//audio//SFX//BeeBuzzBuzz.wav"
define bird = "..//audio//SFX//BirdChirp.wav"
define clink = "..//audio//SFX//Clink.wav"
define doorslam = "..//audio//SFX//DoorBoom.wav"
define sparkle = "..//audio//SFX//ElectricCrackle.wav"
define clap = "..//audio//SFX//PoliteApplause.wav"
define potion = "..//audio//SFX//PotionBrew.wav"
define walkProf = "..//audio//SFX//ProfWalk.wav"
define dingDong1 = "..//audio//SFX//SchoolBell1.wav"
define dingDong2 = "..//audio//SFX//SchoolBell2.wav"
define chatter = "..//audio//SFX//StudentsTalking.wav"
define text1 = "..//audio//SFX//TextBoxSelection1.wav"
define text2 = "..//audio//SFX//TextBoxSelection2.wav"
define whoosh = "..//audio//SFX//WindyWhoosh.wav"

###################################################################AP#############################

transform my_center:
    xalign 0.5
    yalign 0.5

transform my_right:
    xalign 0.7
    yalign 0.5