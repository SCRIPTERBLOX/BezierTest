import pygame

import math

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

running = True

originalPoint1 = (100, 100)
originalPoint2 = (300, 100)
originalPoint3 = (150, 50)

point1 = (100, 100)
point2 = (300, 100)
point3 = (150, 50)

drawingPoint1 = [point1[0], point1[1]]
drawingPoint2 = [point3[0], point3[1]]

repetitions = 0

sizeSlider = 1
maxSteps = 400; maxMaxSteps = 800
enabledFeatures = [
    False, # Bezier third points
    False, # Bezier first points
    False, # Bezier second points
    False # Bezier construction lines
]

feature1Debounce = 0
feature2Debounce = 0
feature3Debounce = 0
feature4Debounce = 0

if enabledFeatures[1]:
    pygame.draw.circle(screen, (255, 0, 0), point1, 10)
if enabledFeatures[2]:
    pygame.draw.circle(screen, (255, 0, 0), point2, 10)
if enabledFeatures[0]:
    pygame.draw.circle(screen, (0, 255, 0), point3, 10)

currentlySelectedPoint = 0
currentlyHoldingAPoint = False

while running:
    if feature1Debounce > 0:
        feature1Debounce += 1
        if feature1Debounce >= 20:
            feature1Debounce = 0
    if feature2Debounce > 0:
        feature2Debounce += 1
        if feature2Debounce >= 20:
            feature2Debounce = 0
    if feature3Debounce > 0:
        feature3Debounce += 1
        if feature3Debounce >= 20:
            feature3Debounce = 0
    if feature4Debounce > 0:
        feature4Debounce += 1
        if feature4Debounce >= 20:
            feature4Debounce = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] < 600:
            point3 = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
            repetitions = 0

            drawingPoint1 = [point1[0], point1[1]]
            drawingPoint2 = [point3[0], point3[1]]

            if enabledFeatures[1]:
                pygame.draw.circle(screen, (255, 0, 0), point1, 10)
            if enabledFeatures[2]:
                pygame.draw.circle(screen, (255, 0, 0), point2, 10)
            if enabledFeatures[0]:
                pygame.draw.circle(screen, (0, 255, 0), point3, 10)
        else:
            #options
            # size slider
            if 50-10 <= pygame.mouse.get_pos()[1] <= 50+10:
                if 600+25 <= pygame.mouse.get_pos()[0] <= 800-25:
                    #get the position in between
                    rightCorner = 800-25+10
                    leftCorner = 600+25
                    size = rightCorner-leftCorner
                    relativePosition = pygame.mouse.get_pos()[0] - leftCorner
                    sizeSlider = relativePosition / size * 99 + 1

                    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
                    repetitions = 0
                    drawingPoint1 = [point1[0], point1[1]]
                    drawingPoint2 = [point3[0], point3[1]]

                    if enabledFeatures[1]:
                        pygame.draw.circle(screen, (255, 0, 0), point1, 10)
                    if enabledFeatures[2]:
                        pygame.draw.circle(screen, (255, 0, 0), point2, 10)
                    if enabledFeatures[0]:
                        pygame.draw.circle(screen, (0, 255, 0), point3, 10)

            # steps slider
            if 100-10 <= pygame.mouse.get_pos()[1] <= 100+10:
                if 600+25 <= pygame.mouse.get_pos()[0] <= 800-25:
                    #get the position in between
                    rightCorner = 800-25+10
                    leftCorner = 600+25
                    size = rightCorner-leftCorner
                    relativePosition = pygame.mouse.get_pos()[0] - leftCorner
                    maxSteps = relativePosition / size * (maxMaxSteps-1) + 1

                    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
                    repetitions = 0
                    drawingPoint1 = [point1[0], point1[1]]
                    drawingPoint2 = [point3[0], point3[1]]

                    if enabledFeatures[1]:
                        pygame.draw.circle(screen, (255, 0, 0), point1, 10)
                    if enabledFeatures[2]:
                        pygame.draw.circle(screen, (255, 0, 0), point2, 10)
                    if enabledFeatures[0]:
                        pygame.draw.circle(screen, (0, 255, 0), point3, 10)

            # features
            # third point
            if 600 + 25 + 10 <= pygame.mouse.get_pos()[0] <= 600 + 25 + 10 + round(((800 - 25) - (600 + 25))/2)-5:
                if 150 - 10 + 10 <= pygame.mouse.get_pos()[1] <= 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)-5:
                    if not feature1Debounce:
                        enabledFeatures[0] = not enabledFeatures[0]
                        feature1Debounce = 1
                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
                        repetitions = 0
                        drawingPoint1 = [point1[0], point1[1]]
                        drawingPoint2 = [point3[0], point3[1]]

                        if enabledFeatures[1]:
                            pygame.draw.circle(screen, (255, 0, 0), point1, 10)
                        if enabledFeatures[2]:
                            pygame.draw.circle(screen, (255, 0, 0), point2, 10)
                        if enabledFeatures[0]:
                            pygame.draw.circle(screen, (0, 255, 0), point3, 10)
            # first point
            if 600 + 25 + 10 + round(((800 - 25) - (600 + 25))/2)+10 <= pygame.mouse.get_pos()[0] <= 600 + 25 + 10 + round(((800 - 25) - (600 + 25))/2)-5 + round(((800 - 25) - (600 + 25))/2)-5:
                if 150 - 10 + 10 <= pygame.mouse.get_pos()[1] <= 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)-5:
                    if not feature2Debounce:
                        enabledFeatures[1] = not enabledFeatures[1]
                        feature2Debounce = 1
                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
                        repetitions = 0
                        drawingPoint1 = [point1[0], point1[1]]
                        drawingPoint2 = [point3[0], point3[1]]

                        if enabledFeatures[1]:
                            pygame.draw.circle(screen, (255, 0, 0), point1, 10)
                        if enabledFeatures[2]:
                            pygame.draw.circle(screen, (255, 0, 0), point2, 10)
                        if enabledFeatures[0]:
                            pygame.draw.circle(screen, (0, 255, 0), point3, 10)

            # second point
            if 600 + 25 <= pygame.mouse.get_pos()[0] <= 600 + 25 + round(((800 - 25) - (600 + 25))/2)-5:
                if 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)+10 <= pygame.mouse.get_pos()[1] <= 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)-5 + round(((800 - 25) - (600 + 25))/2)-5:
                    if not feature3Debounce:
                        enabledFeatures[2] = not enabledFeatures[2]
                        feature3Debounce = 1
                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
                        repetitions = 0
                        drawingPoint1 = [point1[0], point1[1]]
                        drawingPoint2 = [point3[0], point3[1]]

                        if enabledFeatures[1]:
                            pygame.draw.circle(screen, (255, 0, 0), point1, 10)
                        if enabledFeatures[2]:
                            pygame.draw.circle(screen, (255, 0, 0), point2, 10)
                        if enabledFeatures[0]:
                            pygame.draw.circle(screen, (0, 255, 0), point3, 10)

            # construction lines
            if 600 + 25 + round(((800 - 25) - (600 + 25))/2)+10 <= pygame.mouse.get_pos()[0] <= 600 + 25 + round(((800 - 25) - (600 + 25))/2)-5 + round(((800 - 25) - (600 + 25))/2)-5:
                if 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)+10 <= pygame.mouse.get_pos()[1] <= 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)-5 + round(((800 - 25) - (600 + 25))/2)-5:
                    if not feature4Debounce:
                        enabledFeatures[3] = not enabledFeatures[3]
                        feature4Debounce = 1
                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
                        repetitions = 0
                        drawingPoint1 = [point1[0], point1[1]]
                        drawingPoint2 = [point3[0], point3[1]]

                        if enabledFeatures[1]:
                            pygame.draw.circle(screen, (255, 0, 0), point1, 10)
                        if enabledFeatures[2]:
                            pygame.draw.circle(screen, (255, 0, 0), point2, 10)
                        if enabledFeatures[0]:
                            pygame.draw.circle(screen, (0, 255, 0), point3, 10)
    elif pygame.mouse.get_pressed()[2]:
        if pygame.mouse.get_pos()[0] < 600:
            if not currentlyHoldingAPoint:
                currentlyHoldingAPoint = True
                currentlySelectedPoint = 0 if currentlySelectedPoint == 1 else 1

            if currentlySelectedPoint == 0:
                point1 = pygame.mouse.get_pos()
                originalPoint1 = point1
            else:
                point2 = pygame.mouse.get_pos()
                originalPoint2 = point2

            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))

            if enabledFeatures[1]:
                pygame.draw.circle(screen, (255, 0, 0), point1, 10)
            if enabledFeatures[2]:
                pygame.draw.circle(screen, (255, 0, 0), point2, 10)
            if enabledFeatures[0]:
                pygame.draw.circle(screen, (0, 255, 0), point3, 10)
            repetitions = 0
            drawingPoint1 = [point1[0], point1[1]]
            drawingPoint2 = [point3[0], point3[1]]
    else:
        currentlyHoldingAPoint = False


    """pygame.draw.line(screen, (255, 255, 255), point1, point3, 2)
    pygame.draw.line(screen, (255, 255, 255), point2, point3, 2)

    pygame.draw.circle(screen, (0, 255, 0), drawingPoint1, 10)
    pygame.draw.circle(screen, (0, 255, 0), drawingPoint2, 10)"""

    # settings bg
    pygame.draw.rect(screen, (100, 100, 100), (600, 0, 200, 600))
    pygame.draw.rect(screen, (255, 255, 255), (600-5, 0, 10, 600))

    #size slider
    pygame.draw.circle(screen, (255, 255, 255), (600+25, 50), 10)
    pygame.draw.circle(screen, (255, 255, 255), (800-25, 50), 10)
    pygame.draw.rect(screen, (255, 255, 255), (600+25, 50-10, (800-25)-(600+25), 20))
    leftPos = 600+25-10
    rightPos = 800-25+10
    pygame.draw.circle(screen, (255, 255, 255), (600 + 25 + ((rightPos-leftPos) / 100 * sizeSlider), 50), 20)

    # steps slider
    pygame.draw.circle(screen, (255, 255, 255), (600 + 25, 100), 10)
    pygame.draw.circle(screen, (255, 255, 255), (800 - 25, 100), 10)
    pygame.draw.rect(screen, (255, 255, 255), (600 + 25, 100 - 10, (800 - 25) - (600 + 25), 20))
    pygame.draw.circle(screen, (255, 255, 255), (600 + 25 + ((rightPos - leftPos) / maxMaxSteps * maxSteps), 100), 20)

    # features
    # third point
    pygame.draw.rect(screen, (255, 255, 255), (600 + 25, 150 - 10, round(((800 - 25) - (600 + 25))/2)-5, round(((800 - 25) - (600 + 25))/2)-5))

    if enabledFeatures[0]:
        pygame.draw.rect(screen, (0, 255, 0), (600 + 25 + 10, 150 - 10 + 10, round(((800 - 25) - (600 + 25))/2)-5 - 20, round(((800 - 25) - (600 + 25))/2)-5 - 20))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (600 + 25 + 10, 150 - 10 + 10, round(((800 - 25) - (600 + 25)) / 2) - 5 - 20, round(((800 - 25) - (600 + 25)) / 2) - 5 - 20))

    # first point
    pygame.draw.rect(screen, (255, 255, 255), (600 + 25 + round(((800 - 25) - (600 + 25))/2)+10, 150 - 10, round(((800 - 25) - (600 + 25))/2)-5, round(((800 - 25) - (600 + 25))/2)-5))

    if enabledFeatures[1]:
        pygame.draw.rect(screen, (0, 255, 0), (600 + 25 + 10 + round(((800 - 25) - (600 + 25))/2)+10, 150 - 10 + 10, round(((800 - 25) - (600 + 25))/2)-5 - 20, round(((800 - 25) - (600 + 25))/2)-5 - 20))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (600 + 25 + 10 + round(((800 - 25) - (600 + 25)) / 2) + 10, 150 - 10 + 10, round(((800 - 25) - (600 + 25)) / 2) - 5 - 20,  round(((800 - 25) - (600 + 25)) / 2) - 5 - 20))

    # second point
    pygame.draw.rect(screen, (255, 255, 255), (600 + 25, 150 - 10 + round(((800 - 25) - (600 + 25))/2)+10, round(((800 - 25) - (600 + 25))/2)-5, round(((800 - 25) - (600 + 25))/2)-5))

    if enabledFeatures[2]:
        pygame.draw.rect(screen, (0, 255, 0), (600 + 25 + 10, 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)+10, round(((800 - 25) - (600 + 25))/2)-5 - 20, round(((800 - 25) - (600 + 25))/2)-5 - 20))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (600 + 25 + 10, 150 - 10 + 10 + round(((800 - 25) - (600 + 25)) / 2) + 10, round(((800 - 25) - (600 + 25)) / 2) - 5 - 20, round(((800 - 25) - (600 + 25)) / 2) - 5 - 20))

    # construction lines
    pygame.draw.rect(screen, (255, 255, 255), (600 + 25 + round(((800 - 25) - (600 + 25))/2)+10, 150 - 10 + round(((800 - 25) - (600 + 25))/2)+10, round(((800 - 25) - (600 + 25))/2)-5, round(((800 - 25) - (600 + 25))/2)-5))

    if enabledFeatures[3]:
        pygame.draw.rect(screen, (0, 255, 0), (600 + 25 + 10 + round(((800 - 25) - (600 + 25))/2)+10, 150 - 10 + 10 + round(((800 - 25) - (600 + 25))/2)+10, round(((800 - 25) - (600 + 25))/2)-5 - 20, round(((800 - 25) - (600 + 25))/2)-5 - 20))
    else:
        pygame.draw.rect(screen, (255, 0, 0), (600 + 25 + 10 + round(((800 - 25) - (600 + 25)) / 2) + 10, 150 - 10 + 10 + round(((800 - 25) - (600 + 25)) / 2) + 10, round(((800 - 25) - (600 + 25)) / 2) - 5 - 20, round(((800 - 25) - (600 + 25)) / 2) - 5 - 20))

    while repetitions < maxSteps:
        drawingPoint1[0] += (point3[0] - originalPoint1[0]) / maxSteps
        drawingPoint1[1] += (point3[1] - originalPoint1[1]) / maxSteps

        drawingPoint2[0] += -(point3[0] - originalPoint2[0]) / maxSteps
        drawingPoint2[1] += -(point3[1] - originalPoint2[1]) / maxSteps

        if enabledFeatures[3]: pygame.draw.line(screen, (255, 255, 255), drawingPoint1, drawingPoint2, 2)

        repetitions += 1

        # draw a circle so far between the two points as respect is to 300
        # so that the circle is closer to point2 when repetitions is close to 300
        percentage = repetitions / maxSteps
        distance = ((drawingPoint1[0] - drawingPoint2[0]) ** 2 + (drawingPoint1[1] - drawingPoint2[1]) ** 2) ** 0.5
        howFarIn = distance/100 * percentage
        #get the position of the line of the two points respecting the howFarIn
        x = drawingPoint1[0] + (drawingPoint2[0] - drawingPoint1[0]) * percentage
        y = drawingPoint1[1] + (drawingPoint2[1] - drawingPoint1[1]) * percentage
        pygame.draw.circle(screen, (255, 255, 255), (x, y), math.ceil(sizeSlider/15))
    """else:
        repetitions = 0""" # this part made some whacky things happen

    pygame.display.flip()
    pygame.time.delay(20)