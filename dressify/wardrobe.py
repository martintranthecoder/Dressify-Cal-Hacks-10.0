from rxconfig import config

import reflex as rx


def wardrobe() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                    "Wardrobe",
                    color= "#FBFBFB",
                    font_family="static/Raleway-Light.ttf",
                    font_size= "6.25rem",
                    font_style= "normal",
                    font_weight= "400",
                    line_height= "normal",
                    bottom= "200px",
                    position = "relative",
                    
                    
                        
            ),
            
            rx.responsive_grid(
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                rx.box(height="5em", width="5em", bg="#BCABAE"),
                columns=[3],
                spacing="4",
                margin ="auto",
            ),
            
            rx.button(
                "Generate",
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