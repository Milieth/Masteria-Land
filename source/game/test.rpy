######################
init offset = 30
######################

#TEST
image cursor:
    "windows cursor"
    xpos 800 ypos 160
    linear 3.0 xpos 640 ypos 500

label ameno_test:
    show ameno fullarmored at half_left
    pause
    show ameno fullarmored at half_center
    pause
    show ameno fullarmored at half_right
    pause
    hide ameno
    show ameno_fullarmored_full
    pause
    hide ameno_fullarmored_full
    show ameno cheers at half_left
    pause
    show ameno cheers at half_center
    pause
    show ameno cheers at half_right
    pause
    show ameno cheers at half_center, grayscale
    pause

    return

label cursor_move_test:
    show cursor
    pause
