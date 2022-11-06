# CarGo (Ex-CarShare)

## Inspiration
With the recent volatility of gas prices, and the on-going increase of expenditure for everyone, we found ourselves in a place of wanting a vehicle to drive for longer road trips, barring the month-to-month costs of owning one long-term. 

We realized the best way to tackle this issue without aligning with a private company was to facilitate a way for car owners and short/long-term renters to connect. 
Through this renters would be gaining a car for a specific duration for their desired purpose and the owner would be making money and pay towards their cars monthly payments or insurance for example. 

## What it does
CarGo has two primary features. Users can either choose to rent a car or loan out their car. 
Rentals can be for a few hours or multiple days depending on availability. 
Additional features include a message board where renters can chat with the owners of the car and vice versa as well as a feedback system where renters and owners are rated out of five stars based on how comfortable their experience was. 

## How we built it
We built CarGo from the ground up using **Django, Bootstrap, Figma, Google Cloud Platform, and Heroku**. Following a brainstorming period we realised we wanted to pursue the usage of the highlighted **Map/Location** sub-category while staying within a theme of **Life Convenience**. Afterwards, we began delving deeper into research and drawing from our own experience to highlight any of our own pain points that we would like to see resolved. We realised that in our frustration over the lack of quality, affordable short-term rental vehicles, the best course of action for us would be to facilitate both car owners to lessen some of their monthly costs while enabling individuals to have some the perks of traveling as and when they want.

Our prototype was built from scratch on Figma. We had used this as an opportunity to focus on the UI and the action flow, intentionally choosing to spend time on user design, fonts, layouts, and the user experience as a whole. We were able to do this while simultaneously understanding the core moving parts under the hood.

Our backend was built in Python's Django framework. As we were all relatively familiar with Python, it was the logical choice. We chose to focus on a working backend that would be able to interact with our hosting service as needed, while doing so with the best practices in mind. We were also able to link this with Google's Clout Platform's APIs, using the Google Maps, Location, and Places APIs respectively. 

Furthermore, we also utilised HTML/CSS and JavaScript (Bootstrap) to show the base functionality of the frontend, additionally allowing us to address security concerns and improve the user's protection on their data.

Front-end: JavaScript + HTML/CSS (Bootstrap), Figma
Backend: Django, Google Cloud Platform

## Challenges we ran into
Most of the challenges on our end were due to specific errors within our code. Particularly, while we planned to initially host our Frontend in React, we realised that the multi-page layout of our web app would make it difficult for us to implement and host on our chosen platform as newer users to both JavaScript and React. While we tried debugging this code for hours and consulted many mentors, we decided to regroup, refocus, and compromise on a HTML/CSS and JavaScript based frontend built using the Bootstrap framework to have a Frontend more in line with what we had originally hoped for.

## Accomplishments that we're proud of
We’re extremely proud of the app we were able to design and create. An idea that started yesterday which included intensive hours of coding, research and design made this project worthwhile. Working collaboratively as a team and helping each other out was truly valuable and improved our overall learning and Hackthon experience. Looking back we can all be proud of what we learned and what we were able to create at the end. 


## What's next for CarGo
We hope to initially launch our app in Toronto and the GTA. In order to protect our users and ensure their security we plan on teaming up with local police departments to verify and check for fraudulent or stolen license plates. We’ll also be running the drivers’ license numbers through an open database by the government of Ontario to check for license suspensions. Once these checks are completed CarGo will notify the parties involved. Our hope is to implement CarGo nationwide and one day take it global.
