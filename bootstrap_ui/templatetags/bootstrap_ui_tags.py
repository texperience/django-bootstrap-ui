from django.conf import settings
from django.template import Library, TemplateSyntaxError
from django.utils.safestring import mark_safe
from dominate import tags
from tag_parser import template_tag
from tag_parser.basetags import BaseNode

register = Library()


@register.assignment_tag(takes_context=True)
def get_value_from_session_or_cookie(context, key):
    request = context['request']

    try:
        # First check for key in session
        # If no session is available this throws an AttributeError, if the key is not available in an existing session
        # this throws a KeyError
        return request.session[key]
    except (AttributeError, KeyError):
        try:
            # Second check for key in cookies
            return request.COOKIES[key]
        except KeyError:
            # Third fallback to settings or return default value
            return getattr(settings, key, '')


@template_tag(register, 'htmltag')
class HtmlTagNode(BaseNode):
    """Implements html tag fundamentals"""
    # Overwrite BaseNode attributes
    allowed_kwargs = ('add_css_classes', 'use_tag',)
    end_tag_name = 'endhtmltag'
    min_args = None

    # Additional constants, overwrite these when inheriting for customisation
    allowed_tags = [tag.__name__ for tag in tags.html_tag.__subclasses__()]
    default_css_classes = []
    default_tag = 'div'

    def render_tag(self, context, safe=True, *tag_args, **tag_kwargs):
        # For thread-safety add all node specific information to a self-scoping dictionary
        scope = {'nodelist': self.nodelist}

        # Preserve all kwargs
        for keyword in tag_kwargs:
            scope[keyword] = tag_kwargs[keyword]

        # Decide to use either given tag or default
        if 'use_tag' not in scope:
            scope['use_tag'] = self.default_tag

        # Check if given tag is allowed
        if scope['use_tag'] not in self.allowed_tags and self.allowed_tags:
            raise TemplateSyntaxError(
                '%r tag only allows %r for %r' % (self.tag_name, ', '.join(self.allowed_tags), 'use_tag')
            )

        # Collect css classes to apply
        scope['use_css_classes'] = self.default_css_classes[:]

        if 'add_css_classes' in scope:
            scope['use_css_classes'] += scope['add_css_classes'].split()

        # Add scope to context identified by self
        context.render_context[self] = scope

        # Instantiate a html tag from the given tag
        htmltag = getattr(tags, scope['use_tag'])()

        # Apply css classes
        if scope['use_css_classes']:
            htmltag.set_attribute('class', ' '.join(scope['use_css_classes']))

        # Render inner html content
        htmltag.add_raw_string(scope['nodelist'].render(context))

        return mark_safe(htmltag.render()) if safe else htmltag


@template_tag(register, 'bootstraptag')
class BootstrapNode(HtmlTagNode):
    """Implements bootstrap component fundamentals"""
    # Overwrite BaseNode attributes
    allowed_kwargs = ('use_tag',)
    end_tag_name = 'endbootstraptag'

    # Overwrite HtmlTagNode attributes
    allowed_tags = [
        'a',
        'div',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'ul', 'li',
    ]
    default_css_classes = ['bs']
    default_tag = 'div'


@template_tag(register, 'column')
class ColumnNode(BootstrapNode):
    """Renders a column"""
    # Overwrite BaseNode attributes
    allowed_kwargs = (
        'xs', 'sm', 'md', 'lg',
        'xs_offset', 'sm_offset', 'md_offset', 'lg_offset',
        'xs_push', 'sm_push', 'md_push', 'lg_push',
        'xs_pull', 'sm_pull', 'md_pull', 'lg_pull',
    )
    end_tag_name = 'endcolumn'

    # Overwrite HtmlTagNode attributes
    default_css_classes = ['col-xs-12']
    default_tag = 'div'

    def render_tag(self, context, *tag_args, **tag_kwargs):
        htmltag = super(BootstrapNode, self).render_tag(context, safe=False, *tag_args, **tag_kwargs)
        scope = context.render_context[self]

        # Apply column grid classes
        apply_grid_classes = list(set(scope) & set(self.allowed_kwargs))

        if apply_grid_classes:
            htmltag.set_attribute(
                'class',
                ' '.join(
                    'col-'
                    + grid_class.replace('_', '-')
                    + '-'
                    + (scope[grid_class] or '12') for grid_class in apply_grid_classes
                )
            )

        return mark_safe(htmltag.render())


@template_tag(register, 'row')
class RowNode(BootstrapNode):
    """Renders a row"""
    # Overwrite BaseNode attributes
    allowed_kwargs = ()
    end_tag_name = 'endrow'

    # Overwrite HtmlTagNode attributes
    default_css_classes = ['row']
    default_tag = 'div'


@template_tag(register, 'container')
class ContainerNode(BootstrapNode):
    """Renders a container"""
    # Overwrite BaseNode attributes
    allowed_kwargs = ('type',)
    end_tag_name = 'endcontainer'

    # Overwrite HtmlTagNode attributes
    default_css_classes = ['container']
    default_tag = 'div'

    def render_tag(self, context, *tag_args, **tag_kwargs):
        htmltag = super(ContainerNode, self).render_tag(context, safe=False, *tag_args, **tag_kwargs)
        scope = context.render_context[self]

        if 'type' in scope:
            if scope['type'] != 'fluid':
                raise TemplateSyntaxError(
                    '%r tag only allows %r for %r' % (self.tag_name, 'fluid', 'type')
                )

            htmltag.set_attribute('class', 'container-fluid')

        return mark_safe(htmltag.render())


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
    BootstrapNode.allowed_kwargs += ('add_css_classes', 'link',)
    end_tag_name = 'endlistgroupitem'

    # Overwrite HtmlTagNode attributes
    allowed_tags = ['a', 'button', 'div', 'li']
    default_css_classes = ['list-group-item']
    default_tag = 'li'

    def render_tag(self, context, *tag_args, **tag_kwargs):
        htmltag = super(ListGroupItemNode, self).render_tag(context, safe=False, *tag_args, **tag_kwargs)
        scope = context.render_context[self]

        if scope['use_tag'] == 'a':
            if 'link' not in scope or not scope['link']:
                raise TemplateSyntaxError(
                    '%r requires keyword argument %r when %r is given' % (self.tag_name, 'link', scope['use_tag'])
                )

            htmltag.set_attribute('href', scope['link'])

        if scope['use_tag'] == 'button':
            htmltag.set_attribute('type', 'button')

        return mark_safe(htmltag.render())


@template_tag(register, 'panel')
class PanelNode(BootstrapNode):
    """Renders a panel"""
    # Overwrite BaseNode attributes
    BootstrapNode.allowed_kwargs += ('add_css_classes',)
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
