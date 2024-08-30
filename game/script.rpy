


## EYECATCH VARIABLES
### RELATED TO LILSTEA'S EYECATCH
default pink = True
image pink_bloop:
    "cm11"
    pause 0.05
    "cm12"
    pause 0.05
    "cm13"
    pause 0.05
    "cm14"
    pause 0.05
    "cm15"
    pause 0.05
    "cm16"
    pause 0.05
    "cm17"
    pause 0.05
    "cm18"
    pause 0.05
    "cm19"
    pause 0.05
    "cm1a"
    pause 0.05
    "cm1b"
    
image blue_bloop:
    "cm21"
    pause 0.05
    "cm22"
    pause 0.05
    "cm23"
    pause 0.05
    "cm24"
    pause 0.05
    "cm25"
    pause 0.05
    "cm26"
    pause 0.05
    "cm27"
    pause 0.05
    "cm28"
    pause 0.05
    "cm29"
    pause 0.05
    "cm2a"
    pause 0.05
    "cm2b"

image white_flash:
    "cms1"
    pause 0.1
    "cms2"
    pause 0.1
    "cms3"
    pause 0.1
    "cms4"
    pause 0.1
    "cms5"
    pause 0.1
    "cms6"
    pause 0.1
    "cms7"
    pause 0.1
    "cms8"
    pause 0.1
    "cms9"
    pause 0.1
    "cmsa"
    pause 0.1
    "cmsb"
    pause 0.1
    
image cmc1_b = im.MatrixColor("cmc1.png", im.matrix.brightness(0.1))


## CHARACTER DEFINITION
define n = Character("Nitori", color="#659296")
define i = Character("Irisu", color="#DDABC6")


label start:
    
    $ persistent.game_ended = False
    
    scene black with dissolve
    
    play music monika

    n "Hello!"
    
    show nit1:
        align(0.5, -0.25)
    
    n "Ahem. I'm here!"
    
    show nit2 as nit1

    n "Welcome to a {font=mikachan.otf}simple web demo!{/font}"
    
    show nit3 as nit1
    
    n "Alright, let's show a CG!"
    
    scene cg1 with Dissolve(1)
    
    n "This is a CG."
    
    stop music fadeout 1
    
    n "Let's meet {b}{font=ammys.ttf}\"Irisu\"{/font}{/b}!"
    
    play music quircky_shop fadein 1
    
    scene bg1 with fade
    pause 0.25
    show irisu with dissolve:
        align(0.5, 0.25) zoom 0.925
    
    i "{b}{font=ammys.ttf}Hi.{/font}{/b}"
    
    n "{font=mikachan.otf}I forgot to show myself!{/font}"
    
    show irisu as irisu:
        xalign 0.5
        ease 1.0 xalign 0.1
        
    show nit3 with Dissolve(1):
        align(0.8, -0.25)
        
    show irisu_blackout as irisu with Dissolve(0.25)
    
    n "Here I am!"
    
    show irisu_empty as irisu
    show nit2 as nit3
    with dissolve
    
    n "Okay. Maybe that's it for now!"
    
    hide osage with dissolve
    
    n "See ya!"
    
    stop music fadeout 2
    
    scene black with Dissolve(1.25)
    
    pause 2
    
    
    ## Test frame by frame animation
    ## Lilstea's Eyecatch!
    
    $ quick_menu = False
    
    "- ANIMATION TEST -"
    window hide
    window auto True
    
    play sound musmus026
    show pink_bloop
    pause 0.6
    show white_flash
    pause 1.2
    
    show cmc2
    show cmt1
    with Dissolve(0.9)
    pause 0.6
    
    show cmt1 as cmt1:
        subpixel True
        #linear 1.2 zoom 0.5 align(0.275, -0.1)
        linear 1.2 zoom 0.5 align(0.375, 0.45)
    show cmc1_b as cmc2 with Dissolve(1.2)
    
    pause 0.6
    
    show cmt4 behind cmt1:
        zoom 0.5 align(0.275, -0.1)
    show cmm1
    with Dissolve(1.2)
        
    pause
    stop sound fadeout 2
    scene black with Dissolve(1.5)
    pause
    
    ### Blue
    
    play sound musmus026
    show blue_bloop
    pause 0.6
    show white_flash
    pause 1.2
    
    show cmc4
    show cmt1
    with Dissolve(0.9)
    pause 0.6
    
    show cmt1 as cmt1:
        subpixel True
        linear 1.2 zoom 0.5 align(0.375, 0.45)
    show cmc3 as cmc4 with Dissolve(1.2)
    
    pause 0.6
    
    show cmt4 behind cmt1:
        zoom 0.5 align(0.275, -0.1)
    show cmm2
    with Dissolve(1.2)
    
    pause
    stop sound fadeout 2
    scene black with Dissolve(1.5)
    pause
    
    $ quick_menu = True
    
    "- END OF ANIMATION TEST -"
    
    "- BILL WURTZ VIDEO TEST -\nClick to end the video."
    
    $ renpy.movie_cutscene("test.mp4", loops=-1)
    
    "Video 2 to video 3."
    
    $ renpy.movie_cutscene("i%20write%20stupid%20music.mp4")
    
    $ renpy.movie_cutscene("jazzstarbucks.mp4", loops=-1)
    
    "- END OF VIDEO TEST -"
    
    $ persistent.game_ended = True
    
    return
