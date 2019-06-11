from django import template

register_filter = template.Library()


@template.filter(name = "cut")
def cut(val,args):
    return val.replace(args,'')

# register_filter.filter('cut',cut)  ## using decorator instead
