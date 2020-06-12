import cv2
#Update Frame Does scaling and adds all visual effect
#Pre
#Ret
def updateFrame():
    global currentFrame
    frame = video.getFrame(currentFrame)
    #optImg = frame.getScaledOptImage()
    optImg = frame.getUserOptImage()
    #floImg = frame.getScaledFloImage()
    floImg = frame.getUserFloImage()
    classImg = frame.getClassificationImage()
    finalImg = increasIntens(floImg)

    szX = finalImg.shape[0]
    szY = finalImg.shape[1]

    if showoptImg:
        finalImg = cv2.add(finalImg,optImg)
    if showMaskImg:
        finalImg = cv2.add(finalImg,classImg)
    if showCellID:
        finalImg = cv2.add(frame.getIDImage(),finalImg)
    if showWHI5ActivImg:
        finalImg = cv2.add(finalImg,frame.getWHI5ActivImage())

    cv2.imshow('CellTracker', finalImg)
    return()
