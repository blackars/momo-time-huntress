# CHARACTER DEFINITIONS 



define mo = Character(None, kind=bubble, image="mfb_neutral")
define ca = Character(None, kind=bubble, image="grayg_idle")
define book = Character(None, kind=nvl)



# IMAGE DEFINITIONS 
## MOOMO
image mfb_neutral = "images/sprites/momo/momo_fb_neutral.png"
image mfb_smile = "images/sprites/momo/momo_fb_smile.png"
image mfb_angry = "images/sprites/momo/momo_fb_angry.png"
image mfb_surprised = "images/sprites/momo/momo_fb_surprised.png"
image mfb_back = "images/sprites/momo/momo_fb_back.png"
## CASIOPEIA
image cas_neutral = "images/sprites/casiopeia/cas_neutral.png"
image cas_right = "images/sprites/casiopeia/cas_right.png"
image cas_left = "images/sprites/casiopeia/cas_left.png"



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
image ruins3 = "images/backgrounds/ruins3.webm"


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