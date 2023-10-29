"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from .state import State
from .selections import selections
from .wardrobe import wardrobe
from .results import results

def index() -> rx.Component:
    return rx.center(
        rx.vstack(

            rx.link(
                "Wardrobe",
                color="#FBFBFB",
                font_size="1em",
                font_family="static/Raleway-Light.ttf",
                font_weight=400,
                word_wrap="break-word",
                display="flex",
                justify_content="center",
                align_items="center",
                margin_top="1em",
                on_click=rx.redirect("/wardrobe"),
            ),
            rx.responsive_grid(
                rx.hstack(
                    rx.image(
                    src="box 1.png",
                    width= "30%",
                    margin_top= "3em",
                    ),
                rx.image(
                    src="box2.png",
                    width= "30%",
                    ),
                rx.image(
                    src="box3.png",
                    width= "30%",
                    margin_top= "3em",
                    ),
                ),
                padding_left= "8%" 
            ),
            rx.text(
                "Dressify",
                color="#FBFBFB",
                font_size="2em",
                font_family="static/Raleway-Light.ttf",
                font_weight=400,
                word_wrap="break-word"
            ),

            rx.button(
                "START",
                on_click= State.onclick
            ),

            rx.text(
                "GETTING STARTED",
                width= "100%",
                height= "100%",
                color= "#FBFBFB", 
                font_size="1em", 
                font_family="static/Raleway-Light.ttf",
                font_weight= 400,
                word_wrap="break-word",
                display="flex",
                justify_content="center",
                align_items="center",
            ),
            
            rx.hstack(
                rx.box(
                    rx.image(
                        src="icon1.png",  
                        width="100%",
                        height="100px", 
                        object_fit="cover", 
                    ),
                    rx.text(
                        "browse wardrobe",  
                        color="#FBFBFB",  
                        font_size="0.5em",
                        font_family="static/Raleway-Light.ttf", 
                        font_weight=400,  
                        word_wrap="break-word",
                        text_align="center",
                    ),
                    
                    width="100%",
                    height="100px",
                    background= "#BCABAE",
                    border_radius="218.50px",
                ),

                rx.box(
                    rx.image(
                        src="icon2.png",  
                        width="100%",
                        height="100px", 
                        object_fit="cover", 
                    ),
                    rx.text(
                        "filter your selection",  
                        color="#FBFBFB",  
                        font_size="0.5em",
                        font_family="static/Raleway-Light.ttf", 
                        font_weight=400,  
                        word_wrap="break-word",
                        text_align="center",
                    ),
                    width="100%",
                    height="100px",
                    background= "#FBFBFB",
                    border_radius="218.50px",
                    margin_right= "2rem",
                ),

                rx.box(
                    rx.image(
                        src="icon3.png",  
                        width="100%",
                        height="100px", 
                        object_fit="cover", 
                    ),
                    rx.text(
                        "generate your outfit",  
                        color="#FBFBFB",  
                        font_size="0.5em",
                        font_family="static/Raleway-Light.ttf", 
                        font_weight=400,  
                        word_wrap="break-word",
                        text_align="center",
                    ),
                    width="100%",
                    height="100px",
                    background= "#716969",
                    border_radius="218.50px",
                ),
                spacing="2em",
                padding_bottom= "30%",
            ),
            spacing="4em",
            font_size="2em",
            padding_top="10%",
            height= "100vh",
            padding_bottom= "30%",
        ),
        background_color= "linear-gradient(180deg, #050303 0%, #2D2E2E 100%)",
        height= "100%"
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(selections)
app.add_page(wardrobe)
app.add_page(results)
app.compile()
