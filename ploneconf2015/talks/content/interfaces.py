""" Content interfaces
"""
from zope import schema
from zope.interface import Interface
from plone.supermodel import model


class ITalk(model.Schema):
    """ Talk schema
    """
    target_audience = schema.TextLine(
        title=u"Target audience",
        default=u"",
        required=True
    )

    room = schema.TextLine(
        title=u"Room",
        default=u"",
        required=False
    )


class IAuthor(model.Schema):
    """ Author schema
    """
    email = schema.TextLine(
        title=u"E-mail Address",
        default=u"",
        required=True
    )

    country = schema.TextLine(
        title=u"Country",
        default=u"",
        required=True
    )

    company = schema.TextLine(
        title=u"Company / Organization",
        default=u"",
        required=False
    )

    twitter = schema.TextLine(
        title=u"Twitter",
        default=u"",
        required=False
    )

    irc = schema.TextLine(
        title=u"IRC",
        default=u"",
        required=False
    )