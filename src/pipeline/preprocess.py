"""Script to preprocess raw videos into a vertical-friendly format."""
import sys

from moviepy.editor import VideoFileClip
from moviepy.video.fx.crop import crop
from skimage.filters import gaussian


# NOTE: using Numba here for the JIT might be interesting
# but again, this is supposed to be run once in a while
def blur(frame):
    return gaussian(frame.astype(float), sigma=6)


def preprocess(input_path: str, output_path: str):
    # Forcefully remove the audio
    clip = VideoFileClip(input_path).set_audio(None)

    # Crop the wide format around the center into a vertical slice,
    # expand to fit the short, blur to cover expansion artifacts
    clip = crop(clip, x1=240, width=608).resize((1080, 1920)).fl_image(blur)

    clip.write_videofile(output_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <INPUT_PATH> <OUTPUT_PATH>")
        sys.exit(1)

    preprocess(sys.argv[1], sys.argv[2])
