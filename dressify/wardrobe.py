from rxconfig import config
from dressify.state import State
from typing import List
import PIL

import reflex as rx
## when you submit the form, take the submission and send to api, then get url and pass the url into here
# 
import together
import base64


import pandas as pd
all_clothes = pd.read_csv('clothes_reflex.csv')

import random

stored = 0
new_list = []
imageList = []

class WardrobeState(State):
    
    image_urls: list[str] = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1280px-Image_created_with_a_mobile_phone.png", "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg", "https://cdn.pixabay.com/photo/2013/10/02/23/03/mountains-190055_1280.jpg", "https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_1280.jpg"
    ]# whenever you add in selection
    # put in a new image_url

    def handle_form(self, form_data): # what is form_data
        #print(form_data)
        # Generate the image based on form_data.
        # Get a url.
        stored = 0
        print(form_data)
        outfitList = []

        h = ["gender", "primaryattribute", "secondaryattribute", "itemtype", "color", "season"]
        for x in h:
            new_list.append(form_data[x])

                
        #generates a topwear item list for outfit if it doesnt have top already or if it is dress
        if((form_data["secondaryattribute"] != "topwear") & (form_data["secondaryattribute"] != "dress")):
            current_clothes = all_clothes[(all_clothes["gender"].str.lower() == form_data["gender"]) &
                                      (all_clothes["subCategory"].str.lower() == "topwear") &
                                      (all_clothes["baseColour"].str.lower() == form_data["color"]) & 
                                      (all_clothes["season"].str.lower() == form_data["season"])]
            
            #choose one topwear item
            randIndex = random.randrange(0,len(current_clothes)-1)
            #stores topwear item in first index
            temp = list(current_clothes.iloc[randIndex])[2:8]
            
            # for att in temp:
            #     att = att.str.lower()
            
            temp = [x.lower() for x in temp]

            outfitList.append(temp)
            #cleanedList = [x for x in outfitList if str(x) != 'nan']
            #print(outfitList)
            #is still dict
        else:
            outfitList.append(new_list)
            stored = 1
            #print(cleanedList)

        #generates a bottomwear item list for outfit if it is not bot already and is not dress
        if((form_data["secondaryattribute"] != "bottomwear") & (form_data["secondaryattribute"] != "dress")):
            current_clothes = all_clothes[(all_clothes["gender"].str.lower() == form_data["gender"]) &
                                       (all_clothes["subCategory"].str.lower() == "bottomwear") &
                                      (all_clothes["baseColour"].str.lower() == form_data["color"]) & 
                                      (all_clothes["season"].str.lower() == form_data["season"])]
            
            #choose one item
            if(len(current_clothes != 0)):
                randIndex = random.randrange(0,len(current_clothes)-1)
                temp = list(current_clothes.iloc[randIndex])[2:8]
            
            # for att in temp:
            #     att = att.str.lower()
            
                temp = [x.lower() for x in temp]

                outfitList.append(temp)

        else:
            #works
            if (form_data["secondaryattribute"] != "dress"):
                outfitList.append(new_list)
                stored = 1

                h = ["gender", "primaryattribute", "secondaryattribute", "itemtype", "color", "season"]
        
                for x in h:
                    new_list.append(form_data[x])
            #print(cleanedList)

        #generates a shoes item list for outfit
        if(form_data["secondaryattribute"] != "shoes"):
            current_clothes = all_clothes[(all_clothes["gender"].str.lower() == form_data["gender"]) &
                                       (all_clothes["subCategory"].str.lower() == "shoes") &
                                      (all_clothes["baseColour"].str.lower() == form_data["color"]) & 
                                      (all_clothes["season"].str.lower() == form_data["season"])]
            
            #choose one item
            randIndex = random.randrange(0,len(current_clothes)-1)
            #stores item
            temp = list(current_clothes.iloc[randIndex])[2:8]
            
            # for att in temp:
            #     att = att.str.lower()
            
            temp = [x.lower() for x in temp]

            outfitList.append(temp)

        else:

            outfitList.append(new_list)
            stored = 1

        if (stored == 0):
            outfitList.append(new_list)
            stored = 1
  
        print(outfitList)
        
        outfitGender = form_data["gender"]
        print(outfitGender)
        outfitItems = []
        for x in outfitList:
                outfitItems.append(x[4] + " " + x[3])
        
        aiPrompt = "The image features a full body photo taken of a "
        if(outfitGender == "men"):
            aiPrompt += "man"
        elif (outfitGender == "women"):
            aiPrompt += "woman"
        else:
            aiPrompt += "unisex individual"

        aiPrompt += " wearing "
        for x in outfitItems:
            aiPrompt += x
            aiPrompt += ", "

        aiPrompt += "The person appears to be posing for a photo, smiling confidently."
        #===============================================

        together.api_key = "f341f8bd5ed902431354a08964e3be83394ce1ebbf5fb99d2ac6abe8366acd92"
        print(aiPrompt)
        # generate image 
        response = together.Image.create(prompt=aiPrompt,model= "SG161222/Realistic_Vision_V3.0_VAE",steps= 20, results = 3, seed = 42, height=1024, width=1024)
        
        image = response["output"]["choices"][0]
        with open("assets/result0.png", "wb") as f:
            f.write(base64.b64decode(image["image_base64"]))
        
        image = response["output"]["choices"][1]
        with open("assets/result1.png", "wb") as f:
            f.write(base64.b64decode(image["image_base64"]))

        image = response["output"]["choices"][2]
        with open("assets/result2.png", "wb") as f:
            f.write(base64.b64decode(image["image_base64"]))
        
        # image = response["output"]["choices"][3]
        # with open("assets/resultPhotos/result3.png", "wb") as f:
        #     f.write(base64.b64decode(image["image_base64"]))
        
        # image = response["output"]["choices"][4]
        # with open("assets/resultPhotos/result4.png", "wb") as f:
        #     f.write(base64.b64decode(image["image_base64"]))
        
        # image = response["output"]["choices"][5]
        # with open("assets/resultPhotos/result5.png", "wb") as f:
        #     f.write(base64.b64decode(image["image_base64"]))
        # image = response["output"]["choices"][6]
        # with open("result6.png", "wb") as f:
        #     f.write(base64.b64decode(image["image_base64"]))

        # image = response["output"]["choices"][7]
        # with open("result7.png", "wb") as f:
        #     f.write(base64.b64decode(image["image_base64"]))     

        # image = response["output"]["choices"][8]
        # with open("result8.png", "wb") as f:
        #     f.write(base64.b64decode(image["image_base64"]))

    def add_image(self, url):
        self.image_urls.append(url)

        

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