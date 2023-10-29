from rxconfig import config
from dressify.state import State
from typing import List


import reflex as rx
## when you submit the form, take the submission and send to api, then get url and pass the url into here
# 


class WardrobeState(State):
    
    image_urls: list[str] = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1280px-Image_created_with_a_mobile_phone.png", "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg", "https://cdn.pixabay.com/photo/2013/10/02/23/03/mountains-190055_1280.jpg", "https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_1280.jpg"
    ]# whenever you add in selection
    # put in a new image_url

    def handle_form(self, form_data): # what is form_data
        print(form_data)
        # Generate the image based on form_data.
        # Get a url.
        self.add_image(url)
        

    def add_image(self, url):
        self.image_urls.append(url)

def wardrobe() -> rx.Component:
    return rx.center(
        rx.vstack(

            rx.button(
                "HOME",
                on_click=rx.redirect("/"),
               size = "md",
               color= "#BCABAE",   
            ),

            rx.text(
                    "Wardrobe",
                    color= "#FBFBFB",
                    font_family="static/Raleway-Light.ttf",
                    font_size= "2em",
                    font_style= "normal",
                    font_weight= "400",
                    line_height= "normal",
                    bottom= "120px",
                    position= "relative",
                    padding_top= "0%",
            ),
            
            rx.responsive_grid(
                rx.foreach(
                    WardrobeState.image_urls,
                    lambda url:rx.text(rx.image(
                        src=url,
    
                    ))
                ),
                columns=[3],
                spacing="10",
                margin ="auto",
            ),

            rx.stack(
                rx.button("ADD MORE",
                on_click=rx.redirect("/selections"),
               size = "md",
               color= "#BCABAE",
               border= "10%",),
                rx.button("GENERATE",
                on_click=rx.redirect("/results"),
               size = "md",
               color= "#BCABAE"),
                direction="column",
            ),
            
            display ="flex",
            justify_content="center",
            align_items="center",
            height="100vh",
        ),
         background ="linear-gradient(180deg, #050303 0%, #2D2E2E 100%)",
    )