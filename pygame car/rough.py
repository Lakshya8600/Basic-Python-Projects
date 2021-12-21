def background():
    global bgcount
    gamedisplays.blit(side, (-10, 0))
    gamedisplays.blit(side, (640, 0))
    gamedisplays.blit(line, (170, 0))
    gamedisplays.blit(line, (625, 0))

    if bgcount == 0:

        gamedisplays.blit(road,(360,20))
        gamedisplays.blit(road,(360,120))
        gamedisplays.blit(road,(360,230))
        gamedisplays.blit(road,(360,340))
        gamedisplays.blit(road,(360,450))
        gamedisplays.blit(road,(360,560))

        bgcount = 1

    elif bgcount == 1:
        gamedisplays.blit(road, (360, 25))
        gamedisplays.blit(road, (360, 125))
        gamedisplays.blit(road, (360, 235))
        gamedisplays.blit(road, (360, 345))
        gamedisplays.blit(road, (360, 455))
        gamedisplays.blit(road, (360, 565))

        bgcount = 2

    elif bgcount == 2:

        gamedisplays.blit(road, (360, 30))
        gamedisplays.blit(road, (360, 130))
        gamedisplays.blit(road, (360, 240))
        gamedisplays.blit(road, (360, 350))
        gamedisplays.blit(road, (360, 460))
        gamedisplays.blit(road, (360, 570))
        bgcount = 3

    elif bgcount == 3:

        gamedisplays.blit(road, (360, 35))
        gamedisplays.blit(road, (360, 135))
        gamedisplays.blit(road, (360, 245))
        gamedisplays.blit(road, (360, 355))
        gamedisplays.blit(road, (360, 465))
        gamedisplays.blit(road, (360, 575))
        bgcount = 4

    elif bgcount == 4:

        gamedisplays.blit(road, (360, 40))
        gamedisplays.blit(road, (360, 140))
        gamedisplays.blit(road, (360, 250))
        gamedisplays.blit(road, (360, 360))
        gamedisplays.blit(road, (360, 470))
        gamedisplays.blit(road, (360, 580))
        bgcount = 5

    elif bgcount == 5:

        gamedisplays.blit(road, (360, 45))
        gamedisplays.blit(road, (360, 145))
        gamedisplays.blit(road, (360, 255))
        gamedisplays.blit(road, (360, 365))
        gamedisplays.blit(road, (360, 475))
        gamedisplays.blit(road, (360, 585))
        bgcount = 6

    elif bgcount == 6:

        gamedisplays.blit(road, (360, 50))
        gamedisplays.blit(road, (360, 150))
        gamedisplays.blit(road, (360, 260))
        gamedisplays.blit(road, (360, 370))
        gamedisplays.blit(road, (360, 480))
        gamedisplays.blit(road, (360, 590))
        bgcount = 7

    elif bgcount == 7:

        gamedisplays.blit(road, (360, 50))
        gamedisplays.blit(road, (360, 150))
        gamedisplays.blit(road, (360, 260))
        gamedisplays.blit(road, (360, 370))
        gamedisplays.blit(road, (360, 480))
        gamedisplays.blit(road, (360, 590))
        bgcount = 8

    elif bgcount == 8:

        gamedisplays.blit(road, (360, 50))
        gamedisplays.blit(road, (360, 150))
        gamedisplays.blit(road, (360, 260))
        gamedisplays.blit(road, (360, 370))
        gamedisplays.blit(road, (360, 480))
        gamedisplays.blit(road, (360, 590))
        bgcount = 0

        bglist = [[1, 5], [2, 10], [3, 15], [4, 20], [5, 25], [6, 30], [7, 35], [8, 40], [9, 45], [10, 50], [11, 55],
                  [12, 60], [13, 65], [14, 70], [15, 75], [16, 80], [17, 85], [18, 90], [19, 95], [20, 100]]

        for num, y_axis in bglist:
            if bgcount == num:
                gamedisplays.blit(road, (360, 20 + y_axis))
                gamedisplays.blit(road, (360, 120 + y_axis))
                gamedisplays.blit(road, (360, 230 + y_axis))
                gamedisplays.blit(road, (360, 340 + y_axis))
                gamedisplays.blit(road, (360, 450 + y_axis))
                gamedisplays.blit(road, (360, 560 + y_axis))
                bgcount = num + 1
                if y_axis == 100:
                    bgcount = 1