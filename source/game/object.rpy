######################
init offset = 20
######################

default player_name = "Player"

define p = Character('player_name', color = "#2bff00", dynamic=True)
define a = Character("Ameno", color = "#FF3E3F")
define n = Character("Notifikasi")
define warga = Character("Warga")
define mahyun = Character("Mahyun", color = "#FFF")

define subtitle = Character(
    None,

    what_size=28,
    what_outlines=[( 1, "#FF3E3F", 0, 0 )],
    what_xalign=0.5,
    what_yalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')
define credits_text = Character(what_xalign=0.5, what_textalign=0.5)

#displayable
define fall_overlay = At("fall overlay.png", fullsize)
image fall_overlay_scrollable = Frame(fall_overlay, 0, 0, None, None, tile=True)
image ameno_fullarmored_full = At("ameno fullarmored.png", fullsize)
image bg hitam = "#000000"
image bg langitbiru = At("bg langitbiru.jpg", fullsize)

#screen object
screen input_screen():
    vbox:
        xalign 0.5
        yalign 0.4

        text "{color=#FFFFFF}Tuliskan Namamu:{/color}"
        input:
            value VariableInputValue("player_name", default=True, returnable=True)
            length 10