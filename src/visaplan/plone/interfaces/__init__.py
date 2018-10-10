"""\
visaplan.plone.interfaces: Purpose

Short description
"""
from plone.supermodel import model
from zope.interface import alsoProvides
from plone.autoform.interfaces import IFormFieldProvider
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('visaplan.plone.interfaces')


class IHeightAndWidth(model.Schema):
    """\
    Given dimensions
    """
    model.fieldset(
        u'dimensions',
        label=_(u"Dimensions"),
        fields=['height',
                'width'
                ])

    # TODO: more flexible defaults, perhaps depending on the datatype
    height = schema.Int(
        title=_(u'Height'),
        default=720,
        required=True,
        description=_(u"The height needed for a reasonable view of the object"))

    width = schema.Int(
        title=_(u'Width'),
        default=1280,
        required=True,
        description=_(u"The width needed for a reasonable view of the object"))


alsoProvides(IHeightAndWidth, IFormFieldProvider)
