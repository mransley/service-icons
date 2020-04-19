
import logging, os
from pathlib import Path
from cairosvg import svg2png
from cairocffi import CairoError
from xml.etree.ElementTree import ParseError
from xml.parsers.expat import ExpatError

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("svg_convert")

def find_all_svg_files():
    svg_files = []
    for svg_file in Path("..").glob("**/*.svg"):
        svg_files.append(str(svg_file))
    return svg_files

def get_png_filename(svg_file):
    return svg_file.replace(".svg", ".png")

def does_png_exist(svg_file):
    return os.path.exists(get_png_filename(svg_file))

def convert_svg(svg_file):
    LOGGER.info("Converting %s", svg_file)
    try:
        svg2png(url=svg_file, write_to=get_png_filename(svg_file))
    except Exception:
        LOGGER.exception("Problem processing %s", svg_file) 

def main():
    LOGGER.info("Starting execution")
    svg_files = find_all_svg_files()
    for svg_file in svg_files:
        if not does_png_exist(svg_file):
            convert_svg(svg_file)

LOGGER.info(__name__)
if __name__ == "__main__":
    main()