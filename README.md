# Nikubenki
#### This project is used for automating the prededures of refreshing the car list in game Destiny's child.
### How to use it
1. Install python
2. Install the needed modules:requests
3. Attach your android device to your computer
4. Enable debug mode of your android device
5. Go to the car list page
5. Adjust the parameters in the script, such as the coordinate of the touch point as the coordinate of the refresh button and screenshot point are different in different devices
5. You must also create your own slack project
6. Run the script: python car_watcher.py
### How does this work
1. Use adb shell to simulate tapping of the refresh button
2. Use adb shell to generate screenshot of the device
3. Check a pixel of the screenshot, we use the point of the character "B" in word "Boss"
4. If the pixel is white, as the "B" in "Boss" is drawn in white, push a notification to slack
### What can go from here
1. Use tap swipe to write scripts to do the daily quests without doing by yourself
2. Auto use slide skill when you are farming
3. Analyse the screenshot to get a list of firends who are active, especially at farming. In fact lv 100 players are less willing to farm, so they almost produce no cars. This kind of friend are USELESS.
