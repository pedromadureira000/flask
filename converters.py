from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *itens):
        super(RegexConverter, self).__init__(url_map)
        self.regex = itens[0]


class ListConverter(BaseConverter):
    """nome+nome2+nome3"""
    def to_python(self, value):

        return value.split('+')

    def to_url(self, values):
        return '+'.join(
            BaseConverter.to_url(self, item)
            for item in values
        )