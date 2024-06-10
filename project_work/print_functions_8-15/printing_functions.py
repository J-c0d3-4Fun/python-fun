def make_car(manufacturer, model, **options):
    """Allows you to create your own car from scratch"""
    options['manufacturer'] = manufacturer
    options['model'] = model
    return options

