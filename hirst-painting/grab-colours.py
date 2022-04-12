import colorgram

colors = colorgram.extract('image.jpg', 36)


extracted_rgbs = []
# for i in range(len(colors)):
#     current_color = colors[i]
#     rgb = current_color.rgb
#     red = rgb.r
#     blue = rgb.b
#     green = rgb.g
#     extracted_rgbs.append((red, green, blue))

for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    extracted_rgbs.append((r, g, b))
print(extracted_rgbs)
