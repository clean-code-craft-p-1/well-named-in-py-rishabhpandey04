from constants import MAJOR_COLORS, MINOR_COLORS

def format_color_coding():
    formatted_string = ""
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            formatted_string += f"{i * len(MINOR_COLORS) + j + 1}: {major} - {minor}\n"
    return formatted_string