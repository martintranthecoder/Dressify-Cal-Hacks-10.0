# Dressify- CalHacks 10.0 2023 Submission:scarf:

Sophia Zheng, Aiden Sallows, Martin Tran, Carol Li

## Inspiration :thought_balloon:
We've all been there: rushing around and running late, with piles of clothes scattered around the room, only to reach the realization that you have absolutely nothing suitable to wear. Dressify's mission is to provide a personalized experience by harnessing AI to curate outfits that truly resonate with your style.

## What it does :dizzy:
Using this app, Dressify creates an AI generated outfit perfect for any user. By analyzing a series of user entries, this program will compare their desired clothing item to a database of 44,000 different clothing. Finding the best match for the given item, this program will create a thoroughly detailed prompt that then connects with together.ai’s API to create an AI image that represents a perfect outfit.  
**Target audience**: Anyone looking for unconventional style inspiration!  

## Tools :hammer_and_pick:
Reflex, together.ai, Python, Figma, Kaggle, Github, VSCode, Jupyter Notebook

## How we built it: :computer:
1) Brainstorm(coming up with project scope, audience), and researching into the data to use  

2) Frontend: prototyping through Figma, connecting mockups with Reflex
3) Backend (Data): Cleaning data (drop NaN values, converting data types, etc), accessing user input and using that information to filter CSV file, and creating a detailed script to generate outfit text
4) Backend (together.ai): input the detailed text to the together.ai model to generate image, implement photos on web app
5) Deployment: connecting frontend and backend with Reflex

## Challenges we ran into :monocle_face:
- Originally, we wanted to use an LLM/Clustering model but did not due to time constraints and a lack of numerical data
- Generating the photos on the web app was time-consuming

## What we learned :bulb:
- Good teamwork and communication go a long way
-  Web development in all forms-frontend, backend, etc
-  Industry knowledge, sponsors provided great insight about their programs

## What's next :arrow_right:
- Implementing more features (creating a wardrobe, individual user accounts, etc)
- Spreading the word, and getting users to experience our project!
