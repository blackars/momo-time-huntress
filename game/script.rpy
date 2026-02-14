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
    mo "Come on Casiopeia..."
    mo "You must see the views.."
    hide mfb_neutral with dissolve
    show mfb_back with dissolve
    
    scene forest3
    with dissolve
    show mfb_back with dissolve
    mo "..."
    mo "its so beautiful here..."
    mo "..."
    mo "We can see the castle from the road..."
    mo "I found a shorter path in this steep descent "
    hide mfb_back with dissolve
    
    scene black with fade

    play movie "images/backgrounds/forest4.webm"
    $ renpy.pause()   # espera hasta que el video termine
    stop movie
    with dissolve

    scene forest5
    with dissolve
    show mfb_back with dissolve
    mo "bla bla bla"
    hide mfb_back with dissolve
    show mfb_neutral with dissolve
    show cas_right at enter_right with dissolve
    mo "We have a long road ahead..."
    mo "blaa bla bla"
    hide mfb_neutral with dissolve
    show mfb_smile with dissolve
    mo "To enjoy the moonlight and the warmth of the fire..."
    hide mfb_smile with dissolve
    show mfb_back with dissolve
    mo "bla bla bla"
    hide mfb_back with dissolve
    show mfb_neutral with dissolve
    mo "come on, casiopeia..."
    mo "I will fish somenthin for you..."
    show cas_right at enter_right with dissolve
    ca "..."


    
    scene forest6
    with dissolve
    show mfb_neutral with dissolve
    mo "This road reminds me of the one in my dream..."
    mo "I wonder where it leads to."
    hide mfb_neutral
    show mfb_smile
    mo "What do you think about it?" 
    show cas_right at enter_right with dissolve
    ca "..."
    show mfb_neutral
    mo "Really?"
    ca "..."    
    mo "Why?"
    ca "..."
    mo "Then we must hurry up..."
    hide mfb_neutral and cas_right

    scene forest7
    with dissolve
    "... and many times blah bla blah"
    show mfb_neutral
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
    show mfb_back with dissolve #MIDDLE BODY
    mo "looks like a good place to build a fire..."
    mo "we can rest here..."
    mo "And in few hours we can reach the castle..."
    hide mfb_back #MIDDLE BODY
    show mfb_neutral
    mo "It's a good idea?"

    menu:
        "Yes, its time to rest":
            jump build_fire
        "No, we should continue our journey":
            jump no_build_fire

    label build_fire:
        scene forest9
        with dissolve
        show mfb_neutral with dissolve
        show cas_right at enter_right with dissolve
        hide mfb_neutral with dissolve
        show mfb_smile with dissolve
        mo "Maybe we can find a treasure here..."
        ca "..."
        mo "To enjoy the moonlight and the warmth of the fire..."
        mo "I'll going to read a little more about Clock City..."
        hide mfb_smile with dissolve
        show mfb_neutral with dissolve
        mo "Maybe we can find a way to destroy that horrible place..."
        hide mfb_neutral
        show mfb_smile with dissolve
        mo "Come on Casiopeia..."
        mo "Grab some wild berries for us"
        ca "..."
        hide mfb_smile with dissolve
        hide cas_right with dissolve
        jump read_story



    label no_build_fire:
        scene forest9
        with dissolve
        show mfb_neutral with dissolve
        show cas_right at enter_right with dissolve
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
        # REPRODUIR VIDEO DEL BOSQUE ALTERADO POR EL EFECTO DE LA RUIDO
        scene ruins1
        with dissolve
        show mfb_neutral with dissolve
        show cas_right at enter_right with dissolve
        mo "Its time..."
        ca "..."


    label read_story:
        scene forest9
        with dissolve

        show mfb_neutral with dissolve # MEDIO CUERPO

        # NVL mode: las líneas se acumulan en pantalla
        
        book "You are reading the story of the castle..."
        book "The castle is a big castle..."
        book "We can see the castle from the road..."
        book "The castle is a big castle..."
        book "We can see the castle from the road..."
        book "The castle is a big castle..."

        hide mfb_neutral
        show mfb_smile

        mo "I hear something..."

        jump hear_noise


    label hear_noise:
    # REPRODUIR VIDEO DEL BOSQUE ALTERADO POR EL EFECTO DE LA RUIDO
        scene ruins1
        with dissolve
        show mfb_neutral with dissolve
        show cas_right at enter_right with dissolve
        mo "Thats sounds like..."
        mo "...this fucking bugs..."
        ca "..."
        hide mfb_neutral with dissolve
        show mfb_angry with dissolve
        mo "Its time to revenge the loss time..."
        ca "..."
        hide mfb_angry


label river_way:
    scene forest11
    with dissolve
    
    scene river1
    with dissolve 

    scene river2
    with dissolve

    scene river3
    with dissolve

    jump ruins_way





label ruins_way:
    scene ruins2
    with dissolve

    play movie "images/backgrounds/ruins3.webm"
    $ renpy.pause()
    stop movie
    with dissolve

    scene ruins3
    with dissolve







    return
