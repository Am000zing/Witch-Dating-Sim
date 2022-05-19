python early:
    def parse_smartline(lex):
        who = lex.name()
        what = lex.string()
        return (who, what)

    def execute_smartline(o):
        who, what = o
        person = None
        if config.debug:
            renpy.log("who: " + str(who) + " | " + "what:" + str(what))
        if who is not None:
            try:
                person = eval(who)
            except:
                renpy.error("Character not defined: %s" % who)

        scene_manager._say(person, what, True)

    def lint_smartline(o):
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)
    renpy.register_statement("scene_say", parse=parse_smartline, execute=execute_smartline, lint=lint_smartline)
