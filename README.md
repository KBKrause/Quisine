# Quisine

This was an Android application built for finding recipes for ingredients that you have in your house. The idea behind the app is to reduce the amount of food wasted in your fridge. The way it works is: users enter in ingredients that they have left in their fridge, and the app recommends potential recipies you can make with the leftover ingredients.

The recipe generation works on the premise of web-scraping. BeautifulSoup was used to find recipies from free online resources and store them in a Firebase database. The Android app then would query the app for potential recipies.

Future work includes a feature that allows users to take images of their refridgerator, instead of typing in ingredients.
