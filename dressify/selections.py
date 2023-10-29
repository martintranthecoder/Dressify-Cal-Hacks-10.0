"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from typing import List

from .wardrobe import WardrobeState


gender: List[str] = ["women", "men", "unisex"]
primaryattribute: List[str] = ["apparel", "accessories", "footwear"]
secondaryattribute: List[str] = ["topwear", "bottomwear", "shoes", "jewelry", "eyewear", "dress", "accessories"]
itemtype: List[str] = ["shirts", "jeans", "track pants", "casual shoes", "tops", "sweatshirts", "formal shoes", "bracelet", "flats", "waistcoat", "sports shoes", "shorts", "heels", "saree", "sunglasses", "scarves", "dresses", "skirts", "blazers", "ring", "caps", "trousers", "earrings", "camisoles", "tunics", "jackets", "necklace and chains", "sweaters"]
color: List[str] = ["navy blue", "blue", "black", "grey", "green", "purple", "white", "beige", "brown", "bronze", "teal", "copper", "pink", "off white", "maroon", "red", "khaki", "orange", "coffee brown", "yellow", "charcoal", "gold", "steel", "tan", "multi", "magenta", "lavender", "sea green", "cream", "peach", "olive", "skin", "burgundy", "grey melange", "rust", "rose", "lime green", "mauve", "turquoise", "metallic", "mustard", "taupe", "nude", "mushroom", "fluorescence"]
season: List[str] = ["fall", "summer", "winter", "spring"]

def selections() -> rx.Component:
    
    return rx.center(

        rx.vstack(

            rx.button(
                "HOME",
                on_click=rx.redirect("/"),
               size = "md",
               color= "#BCABAE",   
            ),

            rx.text(
                "Selections",
                color="#FBFBFB",
                font_size="2em",
                font_family="static/Raleway-Light.ttf",
                font_weight=400,
                word_wrap="break-word"
            ),

            rx.text(
            "Let's Start by Filtering Your Selection!",
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
            rx.form(
                rx.select(
                    gender, id="gender", placeholder="Select a gender.", size="lg"
                ),
                rx.select(
                    primaryattribute, id="primaryattribute", placeholder="Select a primary attribute.", size="lg"
                ),
                rx.select(
                    secondaryattribute, id="secondaryattribute", placeholder="Select a secondary attribute.", size="lg"
                ),
                rx.select(
                    itemtype, id = "itemtype", placeholder="Select an item type.", size="lg"
                ),
                rx.select(
                    color, id = "color", placeholder="Select a color.", size="lg"
                ),
                rx.select(
                    season, id = "season", placeholder="Select a season.", size="lg"
                ),
                
                rx.button("GENERATE", type_="submit",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                on_click=rx.redirect("/results"),
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
                ),
                on_submit= WardrobeState.handle_form,
            ),
            text_align= "center",
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
            height= "100vh",
            padding_bottom= "10%",
        ),
    background ="linear-gradient(180deg, #050303 0%, #2D2E2E 100%)",
    height= "100%"
    )
