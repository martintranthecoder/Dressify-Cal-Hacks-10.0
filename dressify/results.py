from rxconfig import config
from .wardrobe import imageList

import reflex as rx

def results() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.button(
                "HOME",
                on_click=rx.redirect("/"),
               size = "md",
               color= "#BCABAE",   
            ),

            rx.text(
                    "Results",
                    color= "#FBFBFB",
                    font_family="static/Raleway-Light.ttf",
                    font_size= "2em",
                    font_style= "normal",
                    font_weight= "400",
                    line_height= "normal",
                    position = "relative",
                    
            ),
            rx.text(
                    "Please wait patiently! The A.I. is hard at work making your cyuuuute outfit!\n Please refresh in 10 seconds",
                    color= "#FBFBFB",
                    font_family="static/Raleway-Light.ttf",
                    font_size= "1.0em",
                    font_style= "normal",
                    font_weight= "400",
                    line_height= "normal",
                    position = "relative",
                    
                ),
            rx.responsive_grid(
                rx.image(src="http://localhost:3000/result0.png", width="auto", height="auto"),
                rx.image(src="http://localhost:3000/result1.png", width="auto", height="auto"),
                rx.image(src="http://localhost:3000/result2.png", width="auto", height="auto"),
                columns=[3],
                spacing="10",
                margin ="auto",
            ),
            
            rx.button(
                "BACK TO SELECTIONS",
                on_click=rx.redirect("/selections"),
               size = "md",
               color= "#BCABAE",
                    
            ),                
            display ="flex",
            justify_content="center",
            align_items="center",
            height="100vh",
        
        ),
        background ="linear-gradient(180deg, #050303 0%, #2D2E2E 100%)",
    )