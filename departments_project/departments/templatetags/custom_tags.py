from django import template

register = template.Library()


@register.filter(name='add_class')
def add_classes(value, args):
    classes = value.field.widget.attrs.get('class', '')

    classes = classes.split(' ')
    new_classes = args.split(' ')

    for c in new_classes:
        if c not in classes:
            classes.append(c)

    # classes += [c for c in new_classes if c not in classes]
    # classes += new_classes
    # classes = set(classes)

    # One way
    # value.field.widget.attrs['class'] = ' '.join(classes)
    # return value

    # Second way
    return value.as_widget(attrs={'class': ' '.join(classes)})


@register.simple_tag
def mute(*args):
    try:
        city, country = args[0].split(', ')
    except:
        city = args[0]

    return city
