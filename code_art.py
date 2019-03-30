from PIL import Image, ImageDraw
import random

# Sierpinski from Circles


def draw_circles(x, y, r, img_draw):
    img_draw.ellipse((x-r, y-r, x+r, y+r))
    if r < 1:
        return
    else:
        draw_circles(x-r, y, r/2, img_draw)
        draw_circles(x+r, y, r/2, img_draw)
        draw_circles(x, y-r, r/2, img_draw)
        draw_circles(x, y+r, r/2, img_draw)


def sierpinski_from_circles():
    square_size = 1000
    size = (square_size, square_size)
    buffer_factor = 1.1
    size_plus_buffer = (int(size[0]*buffer_factor), int(size[1]*buffer_factor))
    img = Image.new('RGB', size_plus_buffer, color='black')
    draw = ImageDraw.Draw(img)

    initial_x = size_plus_buffer[0] / 2
    initial_y = size_plus_buffer[1] / 2
    initial_r = min(size) / 4

    draw_circles(initial_x, initial_y, initial_r, draw)

    return img


doodle = sierpinski_from_circles()
# doodle.save('doodle' + str(random.randint(0, 100000000)) + '.png')
doodle.show()
# sierpinski_from_circles().save('sierpinski from circles.png')


# Print10

def print10():
    square_size = 1000
    size = (square_size, square_size)
    buffer_factor = 1.1
    size_plus_buffer = (int(size[0] * buffer_factor), int(size[1] * buffer_factor))
    buffer_size = ((size_plus_buffer[0]-size[0])/2, (size_plus_buffer[1]-size[1])/2)
    img = Image.new('RGB', size_plus_buffer, color='black')
    draw = ImageDraw.Draw(img)

    line_size = square_size/100
    x = 0
    y = 0
    while y < size[1]:
        real_x = x+buffer_size[0]
        real_y = y+buffer_size[1]
        if random.random() < 0.5:
            draw.line((real_x, real_y, real_x+line_size, real_y+line_size))
        else:
            draw.line((real_x, real_y+line_size, real_x+line_size, real_y))
        x += line_size
        if x >= size[0]:
            x = 0
            y += line_size
    return img


# doodle = print10()
# doodle.save('print10 doodle' + str(random.randint(0, 100000000)) + '.png')
# doodle.show()
