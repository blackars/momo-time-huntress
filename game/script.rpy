# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.


label start:

  # continúa al label principal
    play movie "images/backgrounds/forest1.webm"
    $ renpy.pause()   # espera hasta que el video termine
    stop movie
    with dissolve


    
    scene forest2
    with dissolve
    show mfb_back with dissolve
    mo "Beautiful place..."
    hide mfb_back
    show mfb_neutral with dissolve
    mo "Come on, Casiopeia..."
    mo "You have to checkout the view..."
    hide mfb_neutral with dissolve
    show mfb_back with dissolve 
    scene black with dissolve
    
    scene forest3
    with dissolve
    show mmb_back with dissolve
    mo "..."
    mo "its so beautiful here..."
    mo "..."
    mo "We can see the castle from the road..."
    mo "I found a shorter path in this steep descent "
    scene black with dissolve

    
    scene black with dissolve

    play movie "images/backgrounds/forest4.webm"
    $ renpy.pause()   # espera hasta que el video termine
    stop movie
    with dissolve

    scene forest5
    with dissolve
    show mfb_back with dissolve
    mo "bla bla bla"
    hide mfb_back 
    show mfb_neutral 
    mo "We have a long road ahead..."
    mo "blaa bla bla"
    hide mfb_neutral 
    show mfb_smile 
    mo "To enjoy the moonlight and the warmth of the fire..."
    hide mfb_smile 
    show mfb_back 
    mo "bla bla bla"
    hide mfb_back 
    show mfb_neutral 
    mo "come on, casiopeia..."
    mo "I will fish somenthin for you..."
    show cas_right at enter_right with dissolve
    ca "..."
    scene black with dissolve


    scene forest6
    with dissolve
    show mmb_neutral with dissolve
    mo "This road reminds me of the one in my dream..."
    mo "I wonder where it leads to."
    hide mmb_neutral
    show mmb_smile
    mo "What do you think about it?" 
    show cas_right at enter_right with dissolve
    ca "..."
    hide mmb_smile
    show mmb_neutral
    mo "Really?"
    ca "..."    
    mo "Why?"
    ca "..."
    mo "Then we must hurry up..."
    hide mmb_neutral with dissolve
    hide cas_right with dissolve
    scene black with dissolve


    scene forest7
    with dissolve
    "... and many times blah bla blah"
    show mfb_neutral with dissolve
    show cas_right at enter_right with dissolve
    mo "But already have this feeling of deja vu... or something like that"
    ca "..."
    mo "I'm sure I've been here before"
    mo "maybe I'm just imagining it..."
    mo "or maybe in a past life..."
    mo "or maybe I'm just crazy..."
    ca "..."
    hide mfb_neutral
    show mfb_smile
    mo "but not the only one here..."
    scene black with dissolve


    scene forest8
    with dissolve
    show mfb_neutral with dissolve
    show cas_right at enter_right with dissolve
    mo "Look at this ruins..."
    hide mfb_neutral
    show mfb_back
    ca "..."
    mo "Is like home..."
    mo "before they arrived..."
    ca "..."
    hide mfb_neutral
    show mfb_back 
    # hide cas_right
    with dissolve
    "between the fragments of the past, they found a way that never should have been found..."
    with dissolve

    scene forest9
    with dissolve
    show mmb_back with dissolve
    mo "looks like a good place to build a fire..."
    mo "we can rest here..."
    mo "And in few hours we can reach the castle..."
    hide mmb_back 
    show mmb_neutral
    mo "It's a good idea?"

    menu:
        "Yes, its time to rest":
            jump build_fire
        "No, we should continue":
            jump no_build_fire
    scene black with dissolve

    label build_fire:
        scene forest10
        with dissolve
        show mmb_neutral at left
        show cas_mb_right at enter_right with dissolve
        hide mmb_neutral at left
        show mmb_smile at left
        mo "Its a great opportunity..."
        ca "..."
        mo "To enjoy the moonlight and the warmth of the fire..."
        mo "I'll going to read a little more about Clock City..."
        hide mmb_smile at left
        show mmb_neutral at left
        mo "Maybe we can find a way to destroy that horrible place..."
        hide mmb_neutral at left
        show mmb_smile at left
        mo "Come on Casiopeia..."
        mo "Grab some wild berries for us"
        ca "..."
        hide mfb_smile 
        hide cas_right
        jump read_story



    label no_build_fire:
        scene forest9
        show mfb_neutral 
        show cas_right at enter_right 
        hide mfb_neutral
        show mfb_smile
        mo "Come on Casiopeia..."
        mo "No time to waste..."
        ca "..."
        jump go_to_castle

    label go_to_castle:
        scene ruins1
        with dissolve
        show mfb_back with dissolve
        show cas_right at enter_right with dissolve
        hide mfb_back
        show mfb_neutral
        mo "We are here..."
        mo "The castle is just ahead..."
        ca "..."
        hide mfb_neutral
        hide cas_right
        with dissolve
        scene black with fade

        play movie "images/backgrounds/graygshout.webm"
        $ renpy.pause()   # espera hasta que el video termine
        stop movie
        with dissolve

        scene ruins1
        with dissolve 
        show mmb_angry with dissolve
        mo "Its time..."

        scene ruins2
        with dissolve  
        show mmb_neutral with dissolve
        mo " dsfsdfsf"
        ca "..."

        scene ruins6
        with disolve
        show mfb_neutral with dissolve
        show cas_left at enter_left with dissolve
        mo "I can smell it from here..."
        ca "..."
        mo "Whats wrong?"
        ca "   "
        
        play movie "images/backgrounds/casnox.webm"
        $ renpy.pause()
        stop movie
        with dissolve
        
        scene ruins6
        with dissolve
        show mfb_surprised at right with dissolve
        show cas_left at left with dissolve 
        mo "That symbols, you never use them before"
        ca "..."
        mo "Are you okay?"
        mo "What was that?"
        ca " ? "
        mo "What kind of premonition supposed to be it"  
        ca "..."
        hide mfb_surprised at right with dissolve
        show mfb_neutral at right with dissolve
        mo "With that dammed bug around here its not good time to try to undertand that"
        ca "..."
        mo "Let's hurry, it's close to us, I can feel it"


        scene ruins3
        with dissolve
        show mmb_angry
        mo "SHOW YOURSELF FUCKING DEMON!"
        mo "We are preparing a grave hole for you!"
        hide mmb_angry
        show mmb_back
        pause 1.5
        hide mmb_back
        jump ruins_way

    label read_story:
        scene forest10
        with dissolve
        show mmb_neutral with dissolve 
        # NVL mode: las líneas se acumulan en pantalla
        
        book "You are reading the story of the castle..."
        book "The castle is a big castle..."
        book "We can see the castle from the road..."
        book "The castle is a big castle..."
        book "We can see the castle from the road..."
        book "The castle is a big castle..."


        mo "..."
        mo "Casiopeia, you feel it..."
        scene black with dissolve

        jump hear_noise


    label hear_noise:

        play movie "images/backgrounds/graygshout.webm"
        $ renpy.pause()   # espera hasta que el video termine
        stop movie
        with dissolve

        scene forest10
        with dissolve
        show mmb_angry at left 
        show cas_mb_right at enter_right with dissolve 
        mo "Thats sounds like..."
        mo "...this fucking bugs..."
        mo "Always on time"
        ca "..."
        mo "Its time to revenge the stolen time..."
        ca "..."
        hide mmb_angry at left 
        show mmb_neutral at left 
        mo "We will set up an ambush..."
        mo "We need to move across the river..."
        ca "..."
        hide mmb_neutral at left with dissolve
        hide cas_mb_right at right with dissolve
        scene black with fade
        jump river_way


label river_way:
    scene forest11
    with dissolve
    ############## RIVER SOUNDS
    show mmb_neutral with dissolve
    mo "We can hide our trace going to river..."
    mo "In this direction we can reach de ruins..."
    mo "And find a way below these.."
    mo "Come on Casiopeia..."
    hide mmb_neutral 
    show mmb_smile
    mo "This time you're really going fish"
    hide mmb_smile with dissolve
    scene black with dissolve

    scene river1
    with dissolve
    #RIVER SOUNDS
    show mmb_neutral at enter_left with dissolve
    show cas_mb_rigth at enter_right with dissolve
    mo "Following the riverbed can hide our scent and muffle our noise."
    mo "We’ll sneak up on that bug from behind"
 


    scene river2
    with dissolve
    show mmb_neutral at enter_left with dissolve
    show cas_mb_rigth at enter_right with dissolve
    mo "Following the riverbed can hide our scent and muffle our noise."
    mo "We’ll sneak up on that bug from behind"

    scene river3
    with dissolve
    show mmb_neutral at enter_left with dissolve
    show cas_mb_rigth at enter_right with dissolve
    mo "lorem bla bla"
    mo "lorem bla bla"
    ca "..."
    mo "lorem bla bla"
    mo "lorem bla bla"
    mo "lorem bla bla"

    scene ruins7
    with dissolve

    scene ruins8
    with dissolve

    scene ruins9
    with dissolve

    scene ruins6
    with disolve
    show mfb_neutral with dissolve
    show cas_left at enter_left with dissolve
    mo "I can smell it from here..."
    ca "..."
    mo "Whats wrong?"
    ca "   "
    
    play movie "images/backgrounds/casnox.webm"
    $ renpy.pause()
    stop movie
    with dissolve
    
    scene ruins6
    with dissolve
    show mfb_surprised at right with dissolve
    show cas_left at left with dissolve 
    mo "That symbols, you never use them before"
    ca "..."
    mo "Are you okay?"
    mo "What was that?"
    ca " ? "
    mo "What kind of premonition supposed to be it"  
    ca "..."
    hide mfb_surprised at right with dissolve
    show mfb_neutral at right with dissolve
    mo "With that dammed bug around here its not good time to try to undertand that"
    ca "..."
    mo "Let's hurry, it's close to us, I can feel it"


    scene ruins3
    with dissolve
    show mmb_angry
    mo "SHOW YOURSELF FUCKING DEMON!"
    mo "We are preparing a grave hole for you!"
    hide mmb_angry
    show mmb_back
    pause 1.5
    hide mmb_back
    jump ruins_way






label ruins_way:

    play movie "images/backgrounds/ruins3.webm"
    $ renpy.pause()
    stop movie
    with dissolve

    scene ruins3
    with dissolve
    show mmb_angry at enter_right with dissolve
    mo "Cover my back Casiopeia"
    mo "Me encargare de este maldito bicho.."
    show grayg_mb_left at enter_left with dissolve
    gr "AGRRRRR!"
    mo "Your time here its finished"
    gr "MOOOOOO-MOOOOOOOO"
    hide mmb_angry at enter_right
    show mmb_surprised at right
    mo "What that hell! Sounds like my name..."
    gr "WE NEED...HELPPPP"
    mo "No eres el mas grande que he enfrentado"
    mo "Pero si el primero que puede hablar"
    hide mmb_surprised at right
    show mmb_angry at right
    mo "PEro tus trucos baratos no te libraran de tu castigo"
    gr "DOOON'T WANT FIGGHT..."
    gr "WEE NEEED SAAAVEE UNIVERSEEEE..."
    mo "I DON'T CARE!"
    hide mmb_agry at right
    show mmb_fight at right with dissolve
    gr "LEEETT EEXXPLAAAAIINN!!"
    show grayg_mb_left at exit_left with dissolve
    mo "I, see..." 
    mo "You wanna make the hunt more interesting..."

    scene ruins5




    return
