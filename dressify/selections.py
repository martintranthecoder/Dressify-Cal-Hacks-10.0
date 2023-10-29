"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
from typing import List

from .state import State


gender: List[str] = ["women", "men", "unisex"]
primaryattribute: List[str] = ["apparel", "accessories", "footwear"]
secondaryattribute: List[str] = ["topwear", "bottomwear", "shoes", "jewelry", "eyewear", "dress", "accessories"]
itemtype: List[str] = ["shirts", "jeans", "track pants", "casual shoes", "tops", "sweatshirts", "formal shoes", "bracelet", "flats", "waistcoat", "sports shoes", "shorts", "heels", "saree", "sunglasses", "scarves", "dresses", "skirts", "blazers", "ring", "caps", "trousers", "earrings", "camisoles", "tunics", "jackets", "necklace and chains", "sweaters"]
color: List[str] = ["navy blue", "blue", "black", "grey", "green", "purple", "white", "beige", "brown", "bronze", "teal", "copper", "pink", "off white", "maroon", "red", "khaki", "orange", "coffee brown", "yellow", "charcoal", "gold", "steel", "tan", "multi", "magenta", "lavender", "sea green", "cream", "peach", "olive", "skin", "burgundy", "grey melange", "rust", "rose", "lime green", "mauve", "turquoise", "metallic", "mustard", "taupe", "nude", "mushroom", "fluorescence"]
season: List[str] = ["fall", "summer", "winter", "spring"]

def selections() -> rx.Component:
    
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),

        rx.vstack(
            rx.text(
                "Selections",
                color="#FBFBFB",
                font_size="2em",
                font_family="static/Raleway-Light.ttf",
                font_weight=400,
                word_wrap="break-word"
            ),

            rx.text(
            "Make Your Selections",
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
            rx.select(
                gender, placeholder="Select an example.", size="lg"
            ),
            rx.select(
                primaryattribute, placeholder="Select an example.", size="lg"
            ),
            rx.select(
                secondaryattribute, placeholder="Select an example.", size="lg"
            ),
            rx.select(
                itemtype, placeholder="Select an example.", size="lg"
            ),
            rx.select(
                color, placeholder="Select an example.", size="lg"
            ),
            rx.select(
                season, placeholder="Select an example.", size="lg"
            ),
            
            rx.link(
                "+ add items",
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
