""" Streamsfield live in here"""

from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    """Title and textand nothing else"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add addicional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"
