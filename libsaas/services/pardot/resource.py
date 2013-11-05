from libsaas import http, parsers
from libsaas.services import base

class PardotResource(base.RESTResource):

    def get_params(self, format, filters):
        params = {}
        params.update(filters)
        # Default response format for Pardot is XML. We need to manually pass
        # the format we want.
        params.update({'format': format})

        return params

    @base.apimethod
    def post(self, format='json', filters=None):
        """ Since in Pardot API documentation is recommended that all request
        should be POST request we will use this method to retrieve, create, and
        update objects.
        """
        if not filters:
            filters = {}
        params = self.get_params(format, filters)
        request = http.Request('POST', self.get_url(), params)

        return request, parsers.parse_json

    @base.apimethod
    def update(self, id, data, format='json'):
        """ Add id={id} to URL and make a request to update the object. """
        params = self.get_params(format, data)
        params.update({'id':id})

        return http.Request('POST', self.get_url(), params), parsers.parse_json
