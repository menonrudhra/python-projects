import colorgram

painting_colors = colorgram.extract('painting.jpeg', 30)
color_palette = []

for painting_color in painting_colors:
    r = painting_color.rgb.r
    g = painting_color.rgb.g
    b = painting_color.rgb.b
    color = (r, g, b)
    color_palette.append(color)