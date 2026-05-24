# CHARACTER DEFINITIONS 



define mo = Character(None, kind=bubble, image="mfb_neutral")
define ca = Character(None, kind=bubble, image="cas_right")
define gr = Character(None, kind=bubble, image="grayg_fb")

define book = Character(None, kind=nvl)



# IMAGE DEFINITIONS 
## MOMO
image mfb_neutral = "images/sprites/momo/momo_fb_neutral.webp"
image mfb_smile = "images/sprites/momo/momo_fb_smile.webp"
image mfb_surprised = "images/sprites/momo/momo_fb_surprised.webp"
image mfb_back = "images/sprites/momo/momo_fb_back.webp"
image mfb_fight = "images/sprites/momo/momo_fb_fight.webp"
image mfb_surprised_swords = "images/sprites/momo/momo_fb_surprised_sowrds.webp"
image mfb_angry_swords = "images/sprites/momo/momo_fb_angry_swords.webp"
image mfb_neutral_swords = "images/sprites/momo/momo_fb_neutral_swords.webp"


image mmb_neutral = "images/sprites/momo/momo_mb_neutral.webp"
image mmb_smile = "images/sprites/momo/momo_mb_smile.webp"
image mmb_angry = "images/sprites/momo/momo_mb_angry.webp"
image mmb_surprised = "images/sprites/momo/momo_mb_surprised.webp"
image mmb_back = "images/sprites/momo/momo_mb_back.webp"
image mmb_fight = "images/sprites/momo/momo_mb_fight.webp"

## CASIOPEIA
image cas_right = "images/sprites/casiopeia/cas_right.webp"
image cas_left = "images/sprites/casiopeia/cas_left.webp"
image cas_mb_right = "images/sprites/casiopeia/cas_mb_right.webp"
image cas_mb_left = "images/sprites/casiopeia/cas_mb_left.webp"


## GRAY GENTLEMA ANOMALY
image grayg_fb = "images/sprites/grayg/grayg_fb_left.webp"
image grayg_mb = "images/sprites/grayg/grayg_mb_left.webp"
image grayg_hmb = "images/sprites/grayg/grayg_hmb_left.webp"
image grayg_hfb = "images/sprites/grayg/grayg_hfb_left.webp"




# BACKGROUND DEFINITIONS 

image forest2 = "images/backgrounds/forest2.webp"
image forest3 = "images/backgrounds/forest3.webp"
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
image ruins5 = "images/backgrounds/ruins5.webp"
image ruins6 = "images/backgrounds/ruins6.webp"
image ruins7 = "images/backgrounds/ruins7.webp"
image ruins8 = "images/backgrounds/ruins8.webp"
image ruins9 = "images/backgrounds/ruins9.webp"

image creditscene = "images/backgrounds/creditscene.webp"
# ANIMATIONS DEFINITIONS 

transform enter_left:
    xalign -0.5        # empieza fuera de la pantalla por la izquierda
    linear 1.0 xalign 0.5   # en 1 segundo se mueve al centro

transform enter_right:
    xalign 1.5        # empieza fuera de la pantalla por la derecha
    linear 1.0 xalign 1.5   # en 1 segundo se mueve a la derecha

transform exit_left:
    xalign 0.5        # empieza en el centro
    linear 1.0 xalign -0.5   # en 1 segundo se mueve fuera de la pantalla por la izquierda
