import textwrap
from typing import Tuple

from moviepy.editor import (
    AudioFileClip,
    ColorClip,
    CompositeVideoClip,
    TextClip,
    VideoFileClip,
)

WHITE = (255, 255, 255)


class NewsParagraphClip(CompositeVideoClip):
    _background_clip: ColorClip
    _text_clip: TextClip

    text: str
    padding: int
    text_width: int
    background_color: Tuple[int, int, int]

    def __init__(
        self,
        text: str,
        *,
        text_width: int = 50,
        padding: int = 50,
        background_color: Tuple[int, int, int] = WHITE
    ) -> None:
        self.text = text
        self.text_width = text_width
        self.padding = padding
        self.background_color = background_color

        self._text_clip = TextClip(
            "\n".join(textwrap.wrap(self.text, self.text_width)),
            font="Helvetica",
            fontsize=40,
            align="West",
            color="black",
        ).set_position("center")
        self._background_clip = ColorClip(self._background_size, self.background_color)

        CompositeVideoClip.__init__(self, [self._background_clip, self._text_clip])

    @property
    def _background_size(self) -> Tuple[int, int]:
        w, h = self._text_clip.size
        return (w + self.padding, h + self.padding)


audio = AudioFileClip("data/output/speech.wav")

clip = (
    VideoFileClip("data/videos/processed/newsroom.mp4")
    .set_audio(None)
    .set_duration(audio.duration)
    .set_audio(audio)
)

video = CompositeVideoClip(
    [
        clip,
        NewsParagraphClip(
            "In May, the Texas state House voted 121-23 to impeach Attorney General Ken Paxton. He faced accusations of using his influence to benefit a real estate developer named Nate Paul. Paxton was acquitted after a Senate trial, which also dismissed four articles of impeachment. His defense argued the impeachment was politically motivated, targeting him by political opponents, including George P. Bush, who ran against him in 2022. Paxton's lawyer accused the Bush family of manufacturing the allegations.",
        )
        .set_duration(clip.duration)
        .set_position("center"),
    ]
)

video.write_videofile(
    "data/output/output.mp4",
)
