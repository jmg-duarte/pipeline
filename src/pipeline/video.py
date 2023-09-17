import textwrap

from moviepy.editor import *

audio = AudioFileClip("data/output/speech.wav")

clip = (
    VideoFileClip("data/videos/IMG_2551.mov")
    .set_audio(None)
    .set_duration(audio.duration)
    .set_audio(audio)
)
text_clip = (
    TextClip(
        "\n".join(
            textwrap.wrap(
                "Techtron Inc. saw a remarkable surge of thirty five percent in August twenty twenty, driven by strong demand for its innovative tech products and a successful product launch."
            )
        ),
        font="Helvetica",
        fontsize=20,
        color="black",
        align="West",
    )
    .set_position("center")
    .set_duration(audio.duration)
)


bg_clip = (
    ColorClip((text_clip.size[0] + 50, text_clip.size[1] + 50), color=(255, 255, 255))
    .set_position("center")
    .set_duration(audio.duration)
)
video = CompositeVideoClip([clip, bg_clip, text_clip])


video.write_videofile("data/output/output.mp4")
