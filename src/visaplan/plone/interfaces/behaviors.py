"""\
visaplan.plone.interfaces: schemas for Dexterity-based content types

The schemas reflect fields which are currently implemented one-by-one
for the Archetypes-based content types of the UNITRACC family of Plone sites.
"""
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from zope.i18nmessageid import MessageFactory


from visaplan.plone.interfaces import _


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


'''
@implementer(IHeightAndWidth)
class HeightAndWidth(object):
    """
    Apply values for the (chosen) height and width
    """
    def __init__(self, context):
        self.context = context

    @property
    def height(self):
        return self.context
'''
       
class ICaptionAndLegend(model.Schema):
    """\
    Caption and Legend
    """
    # do we need a fieldset; what about tabs?
    caption = schema.Text(
        title=_(u'Caption'),
        required=False,
        description=_(u'A short description of the object'
                      # ... e.g. the subject of an image or animation
                      u' which can be displayed below'
                      ))

    legend = schema.Text(
        title=_(u'Legend'),
        required=False,
        description=_(u'Descriptions for marked parts of the object'
                      # (usually an image)
                      u' which can be displayed below'
                      ))


class IExcludeFromSearch(model.Schema):
    """\
    Allows the implementing objects to be excluded from standard search operations
    """
    # in Products.unitracc.content.unitraccanimation: readable/writable with 'Manage portal' 
    excludeFromSearch = schema.Bool(
        title=_(u'Exclude from search'),
        required=True,
        default=False,
        description=_(u'If selected, the object won\'t be found in standard catalog searches'
                      ))


class IHierarchicalBuzzword(model.Schema):
    """\
    A hierarchical buzzword system

    NOTE: this interface might move to another package which implements the vocabulary!
    (and thus completes the behaviour)
    """
    # do we need a fieldset; what about tabs?
    code = schema.ASCIILine(
        title=_(u'Knowledge field'),
        description=_(u'Please select a value from the hierarchical vocabulary'
                      ))


alsoProvides(IHeightAndWidth,       IFormFieldProvider)
alsoProvides(ICaptionAndLegend,     IFormFieldProvider)
alsoProvides(IExcludeFromSearch,    IFormFieldProvider)
alsoProvides(IHierarchicalBuzzword, IFormFieldProvider)
