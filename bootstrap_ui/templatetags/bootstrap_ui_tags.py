from django.template import Library, TemplateSyntaxError
from django.utils.safestring import mark_safe
from dominate import tags
from tag_parser import template_tag
from tag_parser.basetags import BaseNode

register = Library()


@template_tag(register, 'htmltag')
class HtmlTagNode(BaseNode):
    """Implements html tag fundamentals"""
    # Overwrite BaseNode attributes
    allowed_kwargs = ('add_css_classes', 'use_tag',)
    end_tag_name = 'endhtmltag'
    min_args = None

    # Additional constants, overwrite these when inheriting for customisation
    allowed_tags = []
    default_css_classes = []
    default_tag = 'div'

    def render_tag(self, context, safe=True, *tag_args, **tag_kwargs):
        # For thread-safety add all node specific information to a self-scoping dictionary
        if self not in context.render_context:
            scope = {'nodelist': self.nodelist}

            for keyword in tag_kwargs:
                scope[keyword] = tag_kwargs[keyword]

            if 'use_tag' not in scope:
                scope['use_tag'] = self.default_tag
            elif scope['use_tag'] not in self.allowed_tags and self.allowed_tags:
                raise TemplateSyntaxError(
                    '%r tag only allows %r for %r' % (self.tag_name, ', '.join(self.allowed_tags), 'use_tag')
                )

            scope['use_css_classes'] = self.default_css_classes[:]

            if 'add_css_classes' in scope:
                scope['use_css_classes'] += scope['add_css_classes'].split()

            context.render_context[self] = scope

        scope = context.render_context[self]
        htmltag = getattr(tags, scope['use_tag'])()

        if scope['use_css_classes']:
            htmltag.set_attribute('class', ' '.join(scope['use_css_classes']))

        htmltag.add_raw_string(scope['nodelist'].render(context))

        return mark_safe(htmltag) if safe else htmltag


@template_tag(register, 'bootstraptag')
class BootstrapNode(HtmlTagNode):
    """Implements bootstrap component fundamentals"""
    # Overwrite BaseNode attributes
    allowed_kwargs = ('use_tag',)
    end_tag_name = 'endbootstraptag'

    # Overwrite HtmlTagNode attributes
    allowed_tags = []
    default_css_classes = ['bs']
    default_tag = 'div'


@template_tag(register, 'listgroup')
class ListGroupNode(BootstrapNode):
    """Renders a list group"""
    # Overwrite BaseNode attributes
    end_tag_name = 'endlistgroup'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['div', 'ul']
    default_css_classes = ['list-group']
    default_tag = 'ul'


@template_tag(register, 'listgroupitem')
class ListGroupItemNode(BootstrapNode):
    """Renders a list group item"""
    # Overwrite BaseNode attributes
    BootstrapNode.allowed_kwargs += ('link',)
    end_tag_name = 'endlistgroupitem'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['a', 'div', 'li']
    default_css_classes = ['list-group-item']
    default_tag = 'li'

    def render_tag(self, context, *tag_args, **tag_kwargs):
        htmltag = super(ListGroupItemNode, self).render_tag(context, safe=False, *tag_args, **tag_kwargs)
        scope = context.render_context[self]

        if scope['use_tag'] == 'a':
            if 'link' not in scope:
                raise TemplateSyntaxError(
                    '%r requires keyword argument %r when %r is given' % (self.tag_name, 'link', scope['use_tag'])
                )

            htmltag.set_attribute('href', scope['link'])

        return mark_safe(htmltag)


@template_tag(register, 'panel')
class PanelNode(BootstrapNode):
    """Renders a panel"""
    # Overwrite BaseNode attributes
    end_tag_name = 'endpanel'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['div']
    default_css_classes = ['panel', 'panel-default']
    default_tag = 'div'


@template_tag(register, 'panelheading')
class PanelHeadingNode(BootstrapNode):
    """Renders a panel heading"""
    # Overwrite BaseNode attributes
    end_tag_name = 'endpanelheading'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['div']
    default_css_classes = ['panel-heading']
    default_tag = 'div'


@template_tag(register, 'paneltitle')
class PanelTitleNode(BootstrapNode):
    """Renders a panel title"""
    # Overwrite BaseNode attributes
    end_tag_name = 'endpaneltitle'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    default_css_classes = ['panel-title']
    default_tag = 'h3'


@template_tag(register, 'panelbody')
class PanelBodyNode(BootstrapNode):
    """Renders a panel body"""
    # Overwrite BaseNode attributes
    end_tag_name = 'endpanelbody'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['div']
    default_css_classes = ['panel-body']
    default_tag = 'div'


@template_tag(register, 'panelfooter')
class PanelFooterNode(BootstrapNode):
    """Renders a panel footer"""
    # Overwrite BaseNode attributes
    end_tag_name = 'endpanelfooter'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['div']
    default_css_classes = ['panel-footer']
    default_tag = 'div'
