######################
init offset = 40
######################

label splashscreen:
    $ isNoneLanguage = (_preferences.language == None)
    if isNoneLanguage:
        scene black
        menu:
            "English":
                $ renpy.change_language("English")
                return
            "Indonesia":
                $ renpy.change_language("Indonesia")
                return

    return

label input_name_text:
    window hide
    call screen input_screen()
    return

label start:
    #call ameno_test
    #call cursor_move_test
    call input_name_text from _call_input_name_text
    with fade
    jump prolog_rute_i

label prolog_rute_i:
    scene bg rumahawal
    with fade 
    pause

    scene bg ruanganrumah
    with dissolve
    pause

    play sound [    
    "computerMouseClick.mp3", 
    "<silence 2.0>",  # This is the 2-second delay
    "computerMouseClick.mp3"] loop
    "Ctiks.. Ctiks.. ."

    scene bg mousedanlayar
    with dissolve
    pause

    scene bg layarwelcome
    with fade
    stop sound

    "Welcome to Masteria Lαnd, we look for your success!"
    play sound "<to 1.0>airRush.mp3"
    queue sound "fallingWind.mp3" loop
    scene black
    with fade
    scene bg langitbiru at falling_animation
    with fade
    show fall_overlay_scrollable at parallax_scroll_down
    $ renpy.pause(3.0, hard=True)       # t > falling animation total time
    show bg langitbiru:
        zoom 1.0
    with dissolve



    p "Waaaaaaaa!!! What?! Where's my parachute?!"
    "[player_name] is falling from the sky"
    "From far away, an object in the sky moves towards [player_name] at lightning speed."
    p "I'm falling, I'm falliiiing"
    "Whoosh. ."

    scene bg langitbiru
    show ameno_fullarmored_full
    with flashBub
    stop sound
    pause

    scene bg pulau
    with dissolve
    pause 2

    show ameno cheers at half_center
    a "Don't worry, I am holding you. We'll land on that island in a moment."
    "They land on the island, which seems to be uninhabited"
    a "Mission complete."
    p "Sav-Saved~ Who knew I'd be dropped like that?"
    show ameno serious at half_center
    a "Who are you, actually? not only did you appear on my mission list, but you also showed up suddenly in the sky?!"
    menu:
        "I am a Master":
            jump job
        "My name is [player_name], nice to meet you":
            jump name

    label job:
        show ameno surprised at half_center
        a "Really?! So you came here like me, too."
        jump pulau
    label name:
        show ameno smile at half_center
        a "My name is Ameno Khroma. My task is to complete every mission that pops up on my notification screen."
        jump pulau

label pulau:
    show ameno blushing at half_center
    a "So, did you feel anything?"
    p "Feel anything? Hmm... yes, I think I feel-"
    a "Wait- wait, that doesn't count, because it was an emergency while I was holding you in the sky. I can't deny that my chest touched you."
    "[player_name] stared intently at Ameno's chest, wondering, \"What chest did she mean?\""
    p "Eh?!"
    p "chest? . . ."
    show ameno badmood at half_center
    a ". . . .!!"
    show ameno angry at half_center
    a "Say something?"
    "[player_name] hesitates to state their opinion"
    menu:
        "Well... flat":
            jump blakblakan
        "Ahaha~ of course, the sky is so bright, right?":
            jump alihkan

    label blakblakan:
        a "Hahaha, how many lives do you have, mister?"
        jump hutan
    label alihkan:
        a "Hoooh, so you didn't feel anything at all?!"
        jump hutan

label hutan:
    play sound "punch.mp3"
    scene bg pulau
    with hpunch
    pause 1.0

    scene bg hutan
    with fade

    show ameno smile at half_center
    a "Why are you following me? I have a mission to investigate the surrounding area!"
    p "This forest seems dangerous, so it's better if we go together than alone."
    a "Do you know where is this?"
    p "I'm not sure, but they briefly mentioned the words Masteria Land."
    a "It seems I can get some information from you."
    show ameno cheers at half_center
    a "Alright, I'll allow you to follow me."
    "Rustle. .rustle.. ."

    show ameno fullarmored at half_center
    stop sound
    pause

    scene bg hutan
    with flashBub

    show mahyun siluete at fullsize_right
    play sound "swordClashHit.mp3"
    "Trank! It was so fast. A fantasy monster suddenly appeared from behind [player_name], launching an unexpected ambush attack."
    "Ameno quickly protected [player_name], but because she didn't have time to activate the shield particle, her left weapon took a direct hit."
    show ameno fullarmored at half_left
    pause
    n "New mission! Defeat the monster that is ambushing you!"
    a "What kind of creature is that?!"

    scene bg judul0_putih
    with slow_dissolve
    subtitle "Prolog Rute I"

    scene bg judul1
    with slow_dissolve
    pause 3

label prolog_rute_ii:
    subtitle "Prolog Rute II"

    scene bg hitam
    with slow_dissolve
    pause 2

    scene bg rumahawal
    with fade
    pause

    scene bg ruanganrumah
    with dissolve
    pause

    play sound [    
    "computerMouseClick.mp3", 
    "<silence 2.0>",  # This is the 2-second delay
    "computerMouseClick.mp3"] loop
    "Ctiks.. Ctiks.. ."

    scene bg mousedanlayar
    with dissolve
    pause

    scene bg layarwelcome
    with fade
    stop sound

    "Welcome to Masteria Lαnd, we look for your success!"

    scene bg hitam
    with dissolve

    warga "Runnn! The Armed Ghost is attacking!"
    warga "Hey, wake up! Do you want to die! Hurry up and get up!"
    p "Ugh~ Who's attacking?"

    scene bg ujungterowongan
    with dissolve

    "[player_name] is still getting used to the bright light and glare."

    scene bg kotahancur
    with white_fade
    pause
    show armedghost as armedghost1 at fullsize_right
    pause 1
    show armedghost as armedghost2 at fullsize_center
    pause 1
    show armedghost as armedghost3 at fullsize_left
    pause 1

    warga "Waaaaa!!"
    "The armed ghost is attacking citizens indiscriminately. [player_name] slumped to the ground, trembling."
    "blar! blar! blar!"

    show mahyun siluete at fullsize_center
    with flashBub
    "Someone in full armor charges into the middle of the Armed Ghosts."
    play sound ["armorImpactFromSword.mp3",
    "<silence 2.0>",
    "armorImpactFromSword.mp3",
    "<silence 0.5>"] loop
    show armedghost as armedghost1 at defeated
    pause 1.0
    show armedghost as armedghost2 at defeated
    pause 1.0
    show armedghost as armedghost3 at defeated
    pause 8.0
    show screen ctc
    pause
    hide screen ctc
    stop sound
    scene bg mahyunatk

    warga "We're safe! The Queen has arrivedddd!"

    scene bg kotahancur

    show mahyun serious at fullsize_center
    mahyun "Evacuate immediately! This place is no longer safe."

    "The Queen continues to destroy the Armed Ghosts until none remain."
    "The Queen approaches [player_name], to help them stand up."
    show mahyun halfbody at fullsize_center
    p "Thank you."
    mahyun "Hold on! We're going to a safer place."

    scene bg permukiman

    show mahyun halfbody at fullsize_center
    mahyun "I don't recognize you, you don't seem to be from the shelter area, do you?"
    p "That's right, I'm not from here. Could this be..."
    mahyun "In that case, welcome to-"
    p "-Masteria Land!!"

    scene bg judul0_putih
    with slow_dissolve
    credits_text "{color=#FF3E3F}Project by:{/color}\nProgrammer: Milieth\nIllustration & Story: Byuha"
 
    return
