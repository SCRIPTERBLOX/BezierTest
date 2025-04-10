import pygame

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

pygame.draw.circle(screen, (255, 0, 0), point1, 10)
pygame.draw.circle(screen, (255, 0, 0), point2, 10)
pygame.draw.circle(screen, (0, 255, 0), point3, 10)

currentlySelectedPoint = 0
currentlyHoldingAPoint = False

sizeSlider = 1

while running:
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

            pygame.draw.circle(screen, (255, 0, 0), point1, 10)
            pygame.draw.circle(screen, (255, 0, 0), point2, 10)
            pygame.draw.circle(screen, (0, 255, 0), point3, 10)
        else:
            #options
            if 50-10 <= pygame.mouse.get_pos()[1] <= 50+10:
                if 600+25 <= pygame.mouse.get_pos()[0] <= 800-25:
                    #get the position in between
                    rightCorner = 800-25+10
                    leftCorner = 600+25
                    size = rightCorner-leftCorner
                    relativePosition = pygame.mouse.get_pos()[0] - leftCorner
                    sizeSlider = relativePosition / size * 99 + 1
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

            pygame.draw.circle(screen, (255, 0, 0), point1, 10)
            pygame.draw.circle(screen, (255, 0, 0), point2, 10)
            pygame.draw.circle(screen, (0, 255, 0), point3, 10)
    else:
        currentlyHoldingAPoint = False


    """pygame.draw.line(screen, (255, 255, 255), point1, point3, 2)
    pygame.draw.line(screen, (255, 255, 255), point2, point3, 2)

    pygame.draw.circle(screen, (0, 255, 0), drawingPoint1, 10)
    pygame.draw.circle(screen, (0, 255, 0), drawingPoint2, 10)"""

    pygame.draw.rect(screen, (100, 100, 100), (600, 0, 200, 600))
    pygame.draw.rect(screen, (255, 255, 255), (600-5, 0, 10, 600))

    pygame.draw.circle(screen, (255, 255, 255), (600+25, 50), 10)
    pygame.draw.circle(screen, (255, 255, 255), (800-25, 50), 10)
    pygame.draw.rect(screen, (255, 255, 255), (600+25, 50-10, (800-25)-(600+25), 20))
    leftPos = 600+25-10
    rightPos = 800-25+10
    pygame.draw.circle(screen, (255, 0, 0), (leftPos, 50), 2)
    pygame.draw.circle(screen, (255, 0, 0), (rightPos, 50), 2)
    pygame.draw.circle(screen, (255, 255, 255), (600 + 25 + ((rightPos-leftPos) / 100 * sizeSlider), 50), 20)

    while repetitions < 400:
        drawingPoint1[0] += (point3[0] - originalPoint1[0]) / 400
        drawingPoint1[1] += (point3[1] - originalPoint1[1]) / 400

        drawingPoint2[0] += -(point3[0] - originalPoint2[0]) / 400
        drawingPoint2[1] += -(point3[1] - originalPoint2[1]) / 400
        repetitions += 1

        # draw a circle so far between the two points as respect is to 300
        # so that the circle is closer to point2 when repetitions is close to 300
        percentage = repetitions / 400
        distance = ((drawingPoint1[0] - drawingPoint2[0]) ** 2 + (drawingPoint1[1] - drawingPoint2[1]) ** 2) ** 0.5
        howFarIn = distance/100 * percentage
        #get the position of the line of the two points respecting the howFarIn
        x = drawingPoint1[0] + (drawingPoint2[0] - drawingPoint1[0]) * percentage
        y = drawingPoint1[1] + (drawingPoint2[1] - drawingPoint1[1]) * percentage
        pygame.draw.circle(screen, (255, 255, 255), (x, y), sizeSlider/1)
    else:
        repetitions = 0

    pygame.display.flip()
    pygame.time.delay(20)