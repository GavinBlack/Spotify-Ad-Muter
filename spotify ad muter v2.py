import pyautogui

def checkIfPopupAdIsOnScreen():
    """
    popup ads on the screen will block the volume button sometimes and prevent the ad from being
    muted, click the exit button on the popup ad to fix this
    """
    exitButton = pyautogui.locateOnScreen('pics/popupAdExitButton.png', confidence=0.95)
    if exitButton is not None:
        pyautogui.moveTo(exitButton)
        pyautogui.click(exitButton)

def muteThatAd(adLengths, volumeButtons):
    onScreen = False
    length = None
    whichVolumePic = None

    #check if an ad is on the screen based on the total ad length (shown in pics)
    for adPic in adLengths:
        length = pyautogui.locateOnScreen(f'pics/{adPic}', confidence=0.95)
        if length is not None: #if found an ad
            onScreen = True
            break

    checkIfPopupAdIsOnScreen()

    if not onScreen: #if searched through all of the pics and still haven't found it, repeat the loop
        return
    
    #we have detected an ad and need to figure out which volume button is currently on the screen
    for volumePic in volumeButtons:
        volume = pyautogui.locateOnScreen(f'pics/{volumePic}', confidence=0.95)
        if volume is not None: #we found which volume button is on the screen
            whichVolumePic = volume #assign whichVolumePic to what the volume pic was found
            break

    pyautogui.moveTo(whichVolumePic)
    pyautogui.click(whichVolumePic)

    numOfAdPics = len(adLengths)
    length = None
    ct = 0
    while ct < numOfAdPics: #loop through all the pics and see if one of them is on the screen
        length = pyautogui.locateOnScreen(f'pics/{adLengths[ct]}', confidence=0.95)
        ct += 1
        if length is not None: #ad is still on the screen and restart the loop
            ct = 0
            length = None
            continue

    checkIfPopupAdIsOnScreen()

    #once the ad is off of the screen, unmute the sound
    volumeButton = pyautogui.locateOnScreen(f'pics/{volumeButtons[0]}', confidence=0.95)
    pyautogui.moveTo(volumeButton)
    pyautogui.click(volumeButton)

def main():
    adLengths = ['adLength1.png', 'adLength2.png', 'adLength3.png', 'adLength4.png', 'adLength5.png', 'adLength6.png']
    volumeButtons = ['volumeMuted.png', 'volumeButton1.png', 'volumeButton2.png', 'volumeButton3.png']
    
    while True:
        muteThatAd(adLengths, volumeButtons)

main()
