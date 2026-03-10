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
    play music "forestambient.mp3" volume 0.35
    show mfb_back with dissolve
    mo "Beautiful place..."
    hide mfb_back
    show mfb_neutral with dissolve
    mo "Come on, Casiopeia..."
    mo "At least pretend you're impressed."
    mo "Even you must feel it, the air is different here."
    hide mfb_neutral with dissolve
    show mfb_back with dissolve 
    scene black with dissolve
    
    scene forest3
    with dissolve
    show mmb_back with dissolve
    mo "..."
    mo "It's too beautiful...it makes me uneasy."
    mo "..."
    mo "From the road, we should be able to see the castle."    
    mo "I found a shorter path down this slope."
    mo "Steep...but faster."
    mo "And we don't have time to waste."
    scene black with dissolve
    stop music fadeout 1.0

    
    scene black with dissolve

    play movie "images/backgrounds/forest4.webm"
    $ renpy.pause()   # espera hasta que el video termine
    stop movie
    with dissolve

    scene forest5
    with dissolve
    play music "forestambient.mp3" volume 0.35
    show mfb_back with dissolve
    mo "If we keep this pace, we'll reach the valley before nightfall."
    mo "You always slow down when I get excited..."
    hide mfb_back 
    show mfb_neutral 
    mo "We still have a long road ahead of us."
    hide mfb_neutral 
    show mfb_smile 
    mo "We'll sit under the moonlight."
    mo "I'll make a fire."
    mo "For a moment...we'll almost feel safe."
    hide mfb_smile 
    show mfb_back 
    hide mfb_back 
    show mfb_neutral 
    mo "Come on, Casiopeia..."
    mo "I'll catch something for you."
    mo "You pretend not to care, but I know you're hungry."
    show cas_right at enter_right with dissolve
    ca "..."
    scene black with dissolve


    scene forest6
    with dissolve
    show mmb_neutral at left with dissolve
    mo "This road...it feels like the one from my dream."
    mo "I wonder where it truly leads."
    hide mmb_neutral at left
    show mmb_smile at left
    mo "What do you think?"
    show cas_mb_right at enter_right with dissolve
    ca "..."
    hide mmb_smile at left
    show mmb_neutral at left
    mo "You think so?"
    ca "..."    
    mo "Why would you say that?"
    ca "..."
    mo "Then we must hurry up..."
    hide mmb_neutral with dissolve
    hide cas_mb_right with dissolve
    scene black with dissolve


    scene forest7
    with dissolve
    "... and often, time passes without us realizing what it has in store for us."
    show mfb_neutral with dissolve
    show cas_right at enter_right with dissolve
    mo "I have this strange sense of déjà vu..."
    mo "As if the forest remembers me."
    ca "..."
    mo "I'm certain I've stood here before."
    mo "Maybe I'm imagining it."
    mo "Or maybe it was another life."
    mo "Or maybe grief bends memory into strange shapes."
    mo "Or maybe I'm just crazy..."
    ca "..."
    hide mfb_neutral
    show mfb_smile
    mo "But not the only one here..."
    scene black with dissolve


    scene forest8
    with dissolve
    show mfb_neutral with dissolve
    show cas_right at enter_right with dissolve
    mo "Look at these ruins..."
    hide mfb_neutral
    show mfb_back
    ca "..."
    mo "It feels like home."
    mo "Before they came."
    mo "Before the Gray Gentlemen turned everything to dust."
    ca "..."
    mo "They erased my world."
    mo "I will erase them in return."
    ca "..."
    mo "Don't look at me like that."
    mo "You know I'm right."
    hide mfb_neutral
    show mfb_back 
    # hide cas_right
    with dissolve
    "between the fragments of the past, they found a way that never should have been found..."
    with dissolve

    scene forest9
    with dissolve
    show mmb_back with dissolve
    mo "This looks like a good place to build a fire."
    mo "We could rest here for a while."
    mo "If we leave before dawn, we'll reach the castle in a few hours."
    hide mmb_back 
    show mmb_neutral
    mo "What do you think?"
    mo "Should we rest...or keep moving?"


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
        mo "This is a good place to stop."
        mo "For now."
        ca "..."
        mo "We'll sit beneath the moon."
        mo "The fire will keep the dark at a polite distance."
        mo "I'll read a little more about Clock City."
        mo "About where it all began."
        hide mmb_smile at left
        show mmb_neutral at left
        mo "Somewhere in those pages..."
        mo "There must be a flaw."
        mo "Every machine has one."
        hide mmb_neutral at left
        show mmb_smile at left
        mo "Come on, Casiopeia."
        mo "Gather some wild berries."
        mo "I'll keep watch."
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
        mo "We're close."
        mo "The castle is just ahead."
        hide mfb_neutral
        hide cas_right
        with dissolve
        scene black with fade
        stop music fadeout 1.0


        play movie "images/backgrounds/graygshout.webm"
        $ renpy.pause()   # espera hasta que el video termine
        stop movie
        with dissolve

        scene ruins1
        with dissolve 
        play music "darkambient.mp3" volume 0.1
        show mmb_angry with dissolve
        mo "It's time..."

        scene ruins2
        with dissolve  
        show mmb_neutral with dissolve
        mo "I will tear it apart."
        mo "No mercy for those who devoured my world."
        mo "No mercy for those who fed on our time."

        scene ruins6
        with dissolve
        show mfb_neutral at right with dissolve
        show cas_left at left with dissolve
        mo "I can feel it."
        mo "Like rust in the air."
        ca "..."
        mo "What is it, Casiopeia?"
        ca "   "
        scene black with dissolve
        
        play movie "images/backgrounds/casnox.webm"
        $ renpy.pause()
        stop movie
        with dissolve
        
        scene ruins6
        with dissolve
        show mfb_surprised at right with dissolve
        show cas_left at left with dissolve 
        mo "Those symbols..."
        mo "You've never drawn them before."
        ca "..."
        mo "Are you okay?"
        mo "Was that a warning?"
        mo "Or a memory?"
        ca " ? "
        mo "What kind of premonition is that supposed to be?" 
        ca "..."
        hide mfb_surprised at right
        show mfb_neutral at right
        mo "With that cursed thing nearby..."
        mo "This isn't the time to unravel riddles."
        ca "..."
        mo "We need to move."
        mo "It's close."
        mo "I can feel its shadow pressing against the air."


        scene ruins3
        with dissolve
        show mmb_angry
        mo "SHOW YOURSELF!"
        mo "Stop hiding behind stolen seconds."
        mo "I am done being patient."
        mo "I have already dug your grave."
        hide mmb_angry
        show mmb_back
        pause 1.5
        hide mmb_back
        jump ruins_way
        stop music fadeout 1.0


    label read_story:
        scene forest10
        with dissolve
        show mmb_neutral with dissolve 
        # NVL mode: las líneas se acumulan en pantalla
        
        book "A city built around a tower that never slept."
        book "Every street aligned to the rhythm of a single mechanism."
        book "Every citizen measured by the sound of ticking."
        book "No one remembers who built the first clock."
        book "Only that, one day, time began to fracture."
        book "Shadows started arriving before their owners."
        book "Voices echoed seconds before they were spoken."
        book "And in the deepest chamber of the central tower,"
        book "something began to consume the surplus of time."
        book "They called them the Gray Gentlemen Anomaly."
        book "But the name came much later."
        book "At first, they were only delays."
        book "Only absences."
        book "Only small missing moments..."



        mo "..."
        mo "Casiopeia..."
        mo "It's happen...."
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
        mo "That sound..."
        mo "They're never late."
        mo "Never early."
        mo "Always exactly when something begins to matter."
        ca "..."
        mo "It's time to reclaim what they stole."
        mo "Second by second."
        ca "..."
        hide mmb_angry at left 
        show mmb_neutral at left 
        mo "We'll set an ambush."
        mo "Let them think we are afraid."
        ca "..."
        hide mmb_neutral at left with dissolve
        hide cas_mb_right at right with dissolve
        scene black with fade
        jump river_way


label river_way:
    scene forest11
    with dissolve
    stop music fadeout 1.0
    play music "riversound.mp3" volume 0.35
    show mmb_neutral with dissolve
    mo "The river will wash our scent away."
    mo "They track patterns."
    mo "Not instinct."
    mo "From this direction we can reach the outer ruins..."
    mo "There must be a passage beneath the old foundations."
    mo "Every tower hides something underneath."
    mo "Stay close, Casiopeia."
    hide mmb_neutral 
    show mmb_smile
    mo "And yes..."
    mo "This time you're actually going to fish."
    mo "We'll need the strength."
    hide mmb_smile with dissolve
    scene black with dissolve

    scene river1
    with dissolve
    stop music fadeout 3.0
    play music "riversound.mp3" volume 0.35
    show mmb_neutral at enter_left with dissolve
    show cas_mb_rigth at enter_right with dissolve
    mo "Following the riverbed will hide our scent and swallow our footsteps."
    mo "The cold water confuses their patterns."

    scene river2
    with dissolve
    show mmb_neutral at enter_left with dissolve
    show cas_mb_rigth at enter_right with dissolve
    mo "They don't hunt like beasts."
    mo "They calculate."
    mo "We'll approach from behind."
    scene black with dissolve

    scene river3
    with dissolve
    show mmb_neutral at enter_left with dissolve
    show cas_mb_rigth at enter_right with dissolve
    mo "Casiopeia...do you feel that?"
    mo "The vibration in the air."
    mo "It wasn't like this before."
    ca "..."
    mo "This anomaly is different."
    mo "The arrival blast was louder this time."
    mo "The crater must be wider."
    mo "They're escalating."
    mo "Come on, stay close."
    ca "..."
    scene black with dissolve

    

    scene ruins7
    with dissolve
    stop music fadeout 3.0
    play music "darkambient.mp3" volume 0.1
    show mmb_neutral at enter_left with dissolve
    show cas_mb_rigth at enter_right with dissolve
    mo "Here we go again, Casiopeia."
    mo "These are only forest ruins."
    mo "An old castle swallowed by moss and silence."
    mo "Why would it choose a place like this?"
    ca "..."
    mo "It almost looks like home."
    mo "That's what worries me."
    scene black with dissolve


    scene ruins8
    with dissolve
    show mmb_neutral at right with dissolve
    mo "I wonder what strange object it came to harvest this time."
    ca "..."
    mo "At first, it was random debris."
    mo "Broken tools. Rusted fragments."
    mo "Things no one would ever miss."
    mo "Now they collect them carefully."
    mo "As if they were relics."
    mo "As if each piece mattered."
    mo "Until recently, it wasn't like this."
    mo "Each arrival leaves a crater."
    mo "A circular wound burned into the earth."
    mo "Space folding into itself for something so small."
    "Time leaves traces in its passing."
    "And in its passing, we beg it for mercy."
    "But time does not negotiate."
    scene black with dissolve

    scene ruins9
    with dissolve
    show mmb_neutral at left with dissolve
    show cas_mb_right at right with dissolve
    mo "What do you think about the arrival sound?"
    ca "..."
    mo "It was the strongest I've heard."
    mo "And every time, they grow larger."
    mo "Or stranger."
    ca "..."
    mo "Something is changing."
    mo "They are no longer breaking only time."
    mo "They are breaking direction."
    mo "Breaking sequence."
    mo "Breaking meaning."
    scene black with dissolve



    scene ruins6
    with dissolve
    show mfb_neutral at right with dissolve
    show cas_left at left with dissolve
    mo "Come on Casiopeia..."
    mo "I can smell it from here..."
    ca "..."
    mo "Whats wrong?"
    ca "   "
    scene black with dissolve
    
    play movie "images/backgrounds/casnox.webm"
    $ renpy.pause()
    stop movie
    with dissolve
    
    scene ruins6
    with dissolve
    show mfb_surprised at right with dissolve
    show cas_left at left with dissolve 
    mo "Those symbols..."
    mo "You never trace them before."
    ca "..."
    mo "Are you okay?"
    mo "What was that?"
    ca " ? "
    mo "What kind of premonition is that?" 
    ca "..."
    hide mfb_surprised at right 
    show mfb_neutral at right 
    mo "With that thing this close..."
    mo "This isn't the moment to decipher omens."
    ca "..."
    mo "Move."
    mo "It's close."
    mo "The air is tightening."
    "Hunting the monster together..." 
    "while time tightened around them like a fist"
    "the most dangerous beast of all."
    scene black with dissolve
    

    scene ruins3
    with dissolve
    show mmb_angry
    mo "Stay behind me, Casiopeia."
    mo "I've ended worse than you."
    hide mmb_angry
    show mmb_back
    pause 1.5
    hide mmb_back
    jump ruins_way


label ruins_way:

    play movie "images/backgrounds/ruins4.webm"
    $ renpy.pause()
    stop movie
    with dissolve

    scene ruins3
    with dissolve
    play music "darkambient.mp3" volume 0.1
    show mmb_angry at right with dissolve
    mo "Cover my back Casiopeia"
    show grayg_mb_left at left with dissolve
    play sound "graygtalk1.mp3"
    gr "MOOOOOO-MOOOOOOOO"
    hide mmb_angry at right
    show mmb_surprised at right
    mo "What the hell..."
    mo "That sounded like my name."
    play sound "graygtalk2.mp3"
    gr "WEEEE NEEEEED HEEELLLLLPPPPP"
    mo "Such a violent spatial rupture...for something so small."
    mo "You're not the largest I've faced."
    mo "Not the most grotesque."
    mo "But you are the first that speaks."
    hide mmb_surprised at right
    show mmb_angry at right
    play sound "graygtalk1.mp3"
    gr "DOOON'T WANT FIGGHT..."
    gr "WEE NEEED SAAAVEE UNIVERSEEEE..."
    mo "I DON'T CARE!"
    hide mmb_angry at right
    show mmb_fight at right with dissolve
    play sound "graygtalk2.mp3"
    gr "LEEEETT UUUUSSSS EEEEXXXPLAAAAAIIINNN"
    show grayg_mb_left at exit_left with dissolve
    mo "I see, run..." 
    mo "You wanna make the hunt more interesting..."
    scene black with dissolve
    

    scene ruins5
    show grayg_fb_left at left with dissolve  
    show mfb_fight at right with dissolve
    play sound "graygtalk2.mp3"
    gr "WEEEE NEEEEED THE ARTIFAAAAACTSSS"
    mo "They're not artifacts."
    mo "They're scraps."
    mo "Broken remnants of a world you already consumed."
    play sound "graygtalk1.mp3"
    gr "WEEE JUUUUMP TO FIIIINDD A NEEEWWW GAAAATEE"
    gr "OOOTTHEEERRR REALITY TOOO REEESTAARTT"
    hide mfb_fight at enter_right
    show mfb_surprised_swords at right 
    pause 1.5
    hide mfb_surprised_swords at right
    show mfb_neutral_swords at right
    mo "Another reality?"
    mo "So you destroy one..."
    mo "and escape to the next?"
    play sound "graygtalk2.mp3"
    gr "THIIIISSS RREEEAAALLLIIITTTYYY WAAASSS CLAAAIMMMED"
    gr "FOOOORR SOOOMMMETHIIINGGG FAAAAR MOOOORE POWEEERFFFUUULLLL"
    hide mfb_neutral_swords at right
    show mfb_angry_swords at right
    mo "I don't care."
    mo "You don't get redemption."
    scene black with dissolve
    stop music fadeout 1.0


    play movie "images/backgrounds/momofight.webm"
    $ renpy.pause()
    stop movie
    with dissolve

    scene ruins5
    play music "darkambient.mp3" volume 0.1
    show grayg_hfb_left at left with dissolve
    show mfb_fight at right with dissolve
    play sound "graygtalk1.mp3"
    gr "STOOOOPPP"
    gr "NOOOO TIIIIIMMMEEE LEEFFFTTT"
    gr "ITTT IIISSS COOOMMMIIINNNGGGG"
    mo "Yes."
    mo "Your end is coming."
    play sound "braams1.mp3" volume 2.0
    pause 2.0
    mo "That sound again..."
    mo "It's not from them."
    mo "It's deeper."
    scene black with dissolve

    "And time screamed once more in an attempt to preserve itself."
    scene black with dissolve

    play movie "images/backgrounds/momonox.webm"
    $ renpy.pause()
    stop movie

    scene ruins5
    with dissolve
    show grayg_hfb_left at left with dissolve
    show mfb_surprised_swords at right with dissolve
    play sound "graygtalk2.mp3"
    gr "III SSSSAAAAAIIIDDDDD"
    gr "ITTTT IIIIISSSS COOOMMMIIINNNGGGG"
    mo "What are these symbols?"
    mo "What did you do to my scroll?"
    mo "What did you awaken?"
    hide mfb_surprised_swords at right
    show mfb_fight at right 
    mo "I WILL END YOU."
    scene black 
    with dissolve
    stop music fadeout 1.0


    play movie "images/backgrounds/finalscene.webm"
    $ renpy.pause()
    stop movie

    scene creditscene
    with dissolve
    pause 60.0

    return
