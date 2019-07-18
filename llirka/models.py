from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel 
from wagtail.images.blocks import ImageChooserBlock


class LlirkaHomePage(Page):
    body = RichTextField(blank=True)
    body2 = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
        
    ],blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        StreamFieldPanel('body2'),
    ]