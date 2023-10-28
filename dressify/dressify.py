"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    def onclick(self):
        return rx.redirect("http://google.com")

def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
    
        
        rx.vstack(

            rx.link(
                "Wardrobe",
                href=docs_url,
                color="#FBFBFB",
                font_size="1em",
                font_family="static/Raleway-Light.ttf",
                font_weight=400,
                word_wrap="break-word",
                display="flex",
                justify_content="center",
                align_items="center",
                margin_top="1em",
            ),
            
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
                    width="30%",
                    height="100px",
                    background= "#BCABAE",
                    border_radius="218.50px",
                ),
                rx.box(
                    width="30%",
                    height="100px",
                    background= "#FBFBFB",
                    border_radius="218.50px",
                ),
                rx.box(
                    width="30%",
                    height="100px",
                    background= "#716969",
                    border_radius="218.50px",
                ),
                ),

            rx.link(
                "+ add items",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
            background= "linear-gradient(180deg, #050303 0%, #2D2E2E 100%)",
            background_size= "100%",
        ),
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
