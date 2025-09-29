######################
init offset = 10
######################

#Transition
define flashBub = Fade(0.1, 0.0, 0.5, color="#fff")
define white_fade = Fade(1.0, 0.0, 1.0, color="#fff")
define slow_dissolve = Dissolve(3.0)

#########################
#Positioning And Scaling
#########################
    #Half Size, Works special for Ameno style position
transform half_center:
    xpos 1500
    ypos 0
    xanchor 1.0
transform half_left:
    xpos 1080
    ypos 0
    xanchor 1.0
transform half_right:
    xpos 1930
    ypos 0
    xanchor 1.0

    #Scale displayable to fullsize
transform fullsize:
    xsize 1280
    ysize 720

    #Position fullsize image in right, center or left, only works for Ameno Style
transform fullsize_right:
    xpos 300
    xsize 1280
    ysize 720
transform fullsize_center:
    xpos 0
    xsize 1280
    ysize 720
transform fullsize_left:
    xpos -300
    xsize 1280
    ysize 720


transform grayscale:
    matrixcolor TintMatrix("#5c5c5c")

#########################
#Animation
#########################

#horizontal shaking effect
transform shaking:
    ease 0.05 xoffset 5
    ease 0.05 xoffset -5
    repeat 30

#fell down effect
transform fell_of:
    linear 3.0 ypos 720

#defeated in battle effect
transform defeated:
    shaking
    fell_of

#scroll down the background
transform parallax_scroll_down:
    ysize bg_height
    ypos 0
    parallel:
        linear time ysize 2*bg_height
    parallel:
        linear time ypos -bg_height
    repeat
define speed = 7000     #pixel per second
define bg_width = 1280
define bg_height = 720
define time = bg_height/speed

#falling from the sky animation
transform falling_animation:
    zoom 2.0
    pause 1.5
    linear 0.1 xpos -1280
    pause 0.5
    linear 0.1 xpos 0
    pause 1.0