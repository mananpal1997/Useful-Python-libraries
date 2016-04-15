from PIL import Image

#fixes text in image (CAPTCHA - SOLVER)
def ocr():
    threshold = 200
    mask = "letters.bmp"
    alphabet = "0123456789abcdef"
    im = 'C:/Python34/work_of_every_library/PIL/test.jpg' #path of image
    img = Image.open(im)
    img = img.convert("RGB")
    box = (8, 8, 58, 18)
    img = img.crop(box)
    pix_data = img.load()

    # open the mask
    letters = Image.open(mask)
    le_data = letters.load()

    def test_letter(img, letter):
        A = img.load()
        B = letter.load()
        mx = 1000000
        max_x = 0
        x = 0
        for x in range(img.size[0] - letter.size[0]):
            dist_sum = 0
            for i in range(letter.size[0]):
                for j in range(letter.size[1]):
                    dist_sum = dist_sum + abs(A[x + i, j][0] - B[i, j][0])
            if (dist_sum < mx):
                mx = dist_sum
                max_x = x
        return mx, max_x

    # Clean the background, if color is not white, then set to black.
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if (pix_data[x, y][0] > threshold) \
                    and (pix_data[x, y][1] > threshold) \
                    and (pix_data[x, y][2] > threshold):

                pix_data[x, y] = (255, 255, 255, 255)
            else:
                pix_data[x, y] = (0, 0, 0, 255)

    counter = 0
    old_x = -1

    letter_list = []

    for x in range(letters.size[0]):
        black = True
        for y in range(letters.size[1]):
            if le_data[x, y][0] != 0:
                black = False
                break
        if black:
            if True:
                box = (old_x + 1, 0, x, 10)
                letter = letters.crop(box)
                t = test_letter(img, letter)
                letter_list.append((t[0], alphabet[counter], t[1]))
            old_x = x
            counter += 1

    box = (old_x + 1, 0, 140, 10)
    letter = letters.crop(box)
    t = test_letter(img, letter)
    letter_list.append((t[0], alphabet[counter], t[1]))

    t = sorted(letter_list)
    t = t[0:5]  # 5-letter captcha

    final = sorted(t, key=lambda e: e[2])
    answer = ""
    for l in final:
        answer = answer + l[1]
    return answer

print(ocr())
