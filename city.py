class City:
    def __init__(self, slug, display_name, state=None):
        self.slug = slug
        self.display_name = display_name
        self.state = state

    def __repr__(self):
        return f'<City slug={self.slug} display_name={self.display_name} state={self.state}>'

