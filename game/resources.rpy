# CHARACTER DEFINITIONS 



define mo = Character(None, kind=bubble, image="mfb_neutral")
define ca = Character(None, kind=bubble, image="cas_right")
define gr = Character(None, kind=bubble, image="grayg_idle")

define book = Character(None, kind=nvl)



# IMAGE DEFINITIONS 
## MOMO
image mfb_neutral = "images/sprites/momo/momo_fb_neutral.png"
image mfb_smile = "images/sprites/momo/momo_fb_smile.png"
image mfb_angry = "images/sprites/momo/momo_fb_angry.png"
image mfb_surprised = "images/sprites/momo/momo_fb_surprised.png"
image mfb_back = "images/sprites/momo/momo_fb_back.png"
image mfb_fight = "images/sprites/momo/momo_fb_fight.png"
image mfb_surprised_swords = "images/sprites/momo/momo_fb_surprised_sowrds.png"
image mfb_angry_swords = "images/sprites/momo/momo_fb_angry_swords.png"
image mfb_smile_swords = "images/sprites/momo/momo_fb_smile_swords.png"
image mfb_neutral_swords = "images/sprites/momo/momo_fb_neutral_swords.png"


image mmb_neutral = "images/sprites/momo/momo_mb_neutral.png"
image mmb_smile = "images/sprites/momo/momo_mb_smile.png"
image mmb_angry = "images/sprites/momo/momo_mb_angry.png"
image mmb_surprised = "images/sprites/momo/momo_mb_surprised.png"
image mmb_back = "images/sprites/momo/momo_mb_back.png"
image mmb_fight = "images/sprites/momo/momo_mb_fight.png"

## CASIOPEIA
image cas_right = "images/sprites/casiopeia/cas_right.png"
image cas_left = "images/sprites/casiopeia/cas_left.png"
image cas_mb_right = "images/sprites/casiopeia/cas_mb_right.png"
image cas_mb_left = "images/sprites/casiopeia/cas_mb_left.png"


## GRAY GENTLEMA ANOMALY
image grayg_fb = "images/sprites/grayg/grayg_fb.png"
image grayg_fb_left = "images/sprites/grayg/grayg_fb_left.png"
image grayg_fb_right = "images/sprites/grayg/grayg_fb_right.png"
# image grayg_idle = "images/sprites/grayg/grayg_idle.png"
image grayg_mb = "images/sprites/grayg/grayg_mb.png"
image grayg_mb_left = "images/sprites/grayg/grayg_mb_left.png"
image grayg_mb_right = "images/sprites/grayg/grayg_mb_right.png"



# BACKGROUND DEFINITIONS 

image forest1 = "images/backgrounds/forest1.webm"
image forest2 = "images/backgrounds/forest2.webp"
image forest3 = "images/backgrounds/forest3.webp"
image forest4 = "images/backgrounds/forest4.webm"
image forest5 = "images/backgrounds/forest5.webp"
image forest6 = "images/backgrounds/forest6.webp"
image forest7 = "images/backgrounds/forest7.webp"
image forest8 = "images/backgrounds/forest8.webp"
image forest9 = "images/backgrounds/forest9.webp"
image forest10 = "images/backgrounds/forest10.webp"
image forest11 = "images/backgrounds/forest11.webp"
image river1 = "images/backgrounds/river1.webp"
image river2 = "images/backgrounds/river2.webp"
image river3 = "images/backgrounds/river3.webp"
image ruins1 = "images/backgrounds/ruins1.webp"
image ruins2 = "images/backgrounds/ruins2.webp"
image ruins3 = "images/backgrounds/ruins3.webp"
image ruins4 = "images/backgrounds/ruins4.webm"
image ruins5 = "images/backgrounds/ruins5.webp"
image ruins6 = "images/backgrounds/ruins6.webp"
image ruins7 = "images/backgrounds/ruins7.webp"
image ruins8 = "images/backgrounds/ruins8.webp"
image ruins9 = "images/backgrounds/ruins9.webp"

image momonox = "images/backgrounds/momonox.webm"
image graygshout = "images/backgrounds/graygshout.webm"
image casnox = "images/backgrounds/casnox.webm"
image finalscene = "images/backgrounds/finalscene.webm"
image creditscene = "images/backgrounds/creditscene.webp"



### MUSIC AND SOUND DEFINITIONS


define graygtalk1 = "audio/graygtalk1.mp3"
define graygtalk2 = "audio/graygtalk2.mp3"
define darkambient1 = "audio/music dark ambient 1.mp3"
define darkambient2 = "audio/music dark ambient 2.mp3"
define braams1 = "audio/braams1.mp3"
define braams2 = "audio/braams2.mp3"
define braams3 = "audio/braams3.mp3"

define forest1 = "audio/music forest 1.mp3"
define forest2 = "audio/music forest 2.mp3"
define forest3 = "audio/music forest 3.mp3"
define forest4 = "audio/music forest 4.mp3"
define forest5 = "audio/music forest 2.mp3"
define river1 = "audio/music river 1.mp3"
define river2 = "audio/music river 2.mp3"
define darkambient1 = "audio/music dark ambient 1.mp3"
define darkambient2 = "audio/music dark ambient 2.mp3"
define forestambient1 = "audio/forestambient1.mp3"








# ANIMATIONS DEFINITIONS 

transform move_center_to_left:
    xalign 0.5         # empieza en el centro
    linear 1.0 xalign 0.0   # en 1 segundo se mueve a la izquierda

transform move_center_to_right:
    xalign 0.5         # empieza en el centro
    linear 1.0 xalign 1.0   # en 1 segundo se mueve a la derecha    

transform move_left_to_center:
    xalign 0.0         # empieza en el centro
    linear 1.0 xalign 0.5   # en 1 segundo se mueve a la izquierda    

transform move_right_to_center:
    xalign 1.0         # empieza en el centro
    linear 1.0 xalign 0.5   # en 1 segundo se mueve a la derecha    

transform enter_left:
    xalign -0.5        # empieza fuera de la pantalla por la izquierda
    linear 1.0 xalign 0.5   # en 1 segundo se mueve al centro

transform enter_right:
    xalign 1.5        # empieza fuera de la pantalla por la derecha
    linear 1.0 xalign 1.5   # en 1 segundo se mueve a la derecha

transform exit_left:
    xalign 0.5        # empieza en el centro
    linear 1.0 xalign -0.5   # en 1 segundo se mueve fuera de la pantalla por la izquierda

transform exit_right:
    xalign 0.5        # empieza en el centro
    linear 1.0 xalign 1.5   # en 1 segundo se mueve fuera de la pantalla por la derecha



transform bubble_follow(char_xalign):
    xalign char_xalign
    yalign 0.0

# FIRE SCENE INTERACTIVE