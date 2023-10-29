from rxconfig import config

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
                    bottom= "120px",
                    position = "relative",
                        
            ),
            
            rx.responsive_grid(
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
                rx.box(height="10em", width="10em", bg="#BCABAE"),
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