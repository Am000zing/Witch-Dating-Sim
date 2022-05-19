class SceneManager(object):
    def __init__(self, renpy):
        self.characters = []
        self.active_speaker = None
        self.renpy = renpy

        #
        self.ignore_speaking_flag = False

    def clear_speaker(self):
        self.active_speaker = ""

    def _say(self, speaker, text, interact=False):
        if speaker is not None:
            self.active_speaker = speaker.name
        self.renpy.log("Currently Speaking: " + str(self.active_speaker))
        self.render_scene()
        self.renpy.say(speaker, text, interact)

    def add_character(self, char, loc):
        self.characters.append((char, loc))
        self.renpy.log("Added Char: " + char.__str__() + " - " + loc.__str__())

    def remove_character(self, char):
        char_in_scene = next((x for x in self.characters if x[0] == char), None)
        self.renpy.log("Possible character: " + char_in_scene.__str__())
        if char_in_scene is not None:
            self.characters.remove(char_in_scene)
            self.renpy.log("Removed Char: " + char.__str__())

    def add_transform(self, char, tform):
        char_in_scene = next((x for x in self.characters if x[0] == char), None)
        self.renpy.log("Possible character: " + char_in_scene.__str__())
        if char_in_scene is not None:
            char_in_scene[1].append(tform)
            self.renpy.log("Character updated!")

    def clear_character_list(self):
        self.characters = []

    def render_scene(self):
        self.renpy.log("Last person to speak: " + str(self.active_speaker))
        for char_tuple in self.characters:
            tlength = len(char_tuple[1])
            self.renpy.log("Length of transforms: " + str(tlength))
            if tlength > 1:
                transformer = [char_tuple[1].pop()]
            else:
                transformer = char_tuple[1]
            self.renpy.log("Showing Char: " + char_tuple[0].__str__() + " - " + transformer.__str__())
            self.renpy.show(char_tuple[0], at_list=transformer)
