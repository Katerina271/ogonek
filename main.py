checkY = 0
checkX = 0
py = 0
px = 0
preDy = 0
preDx = 0
isSouth = False
isNorth = False
isWest = False
isEast = False
acc_y = 0
acc_x = 0
snakeY: List[number] = []
snakeX: List[number] = []
snakeX.insert_at(0, 2)
snakeY.insert_at(0, 4)
dx = 0
dy = -1

def on_forever():
    global snakeX, snakeY, acc_x, acc_y, dx, dy, isEast, isWest, isNorth, isSouth, preDx, preDy, px, py, score, checkX, checkY
    if len(snakeX) == 20:
        basic.pause(2000)
        snakeX = [2]
        snakeY = [4]
        dx = 0
        dy = -1
    acc_x = input.acceleration(Dimension.X)
    acc_y = input.acceleration(Dimension.Y)
    isEast = acc_x > 256
    isWest = acc_x < -256
    isNorth = acc_y < -256
    isSouth = acc_y > 256
    preDx = dx
    preDy = dy
    if isEast:
        dx = 1
        dy = 0
    elif isNorth:
        dx = 0
        dy = -1
    elif isSouth:
        dx = 0
        dy = 1
    elif isWest:
        dx = -1
        dy = 0
    px = snakeX[len(snakeX) - 1]
    py = snakeY[len(snakeX) - 1]
    if len(snakeX) > 1:
        if px == snakeX[len(snakeX) - 2] and py == snakeY[len(snakeY) - 2]:
            px = snakeX[len(snakeX) - 1] + preDx
            py = snakeY[len(snakeX) - 1] + preDy
        while index <= len(snakeX) - 1:
            checkX = snakeX[index]
            checkY = snakeY[index]
    else:
        if px < 0 or px > 4 or (py < 0 or py > 4):
            game.game_over()
        index2 = 0
        while index2 <= len(snakeX) - 2:
            if px == snakeX[index2] and py == snakeY[index2]:
                game.game_over()
            index2 += 1
        index3 = 0
        while index3 <= len(snakeX) - 2:
            snakeX[index3] = snakeX[index3 + 1]
            snakeY[index3] = snakeY[index3 + 1]
            index3 += 1
        snakeX[len(snakeX) - 1] = px
        snakeY[len(snakeX) - 1] = py
    basic.clear_screen()
    index4 = 0
    while index4 <= len(snakeX) - 1:
        led.plot(snakeX[index4], snakeY[index4])
        index4 += 1
basic.forever(on_forever)
