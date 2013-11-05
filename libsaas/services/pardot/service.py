from libsaas.services import base

from .authorization import AuthorizationResource
from .prospects import ProspectsResource, ProspectResource

class Pardot(base.Resource):

    def __init__ (self, api_key_or_email, user_key, password=None):
        self.api_root = 'https://pi.pardot.com/api'

        self.user_key = user_key

        if password is None:
            self.api_key = api_key_or_email
            self.add_filter(self.add_api_key_authorization)
        else:
            self.email = api_key_or_email
            self.password = password
            self.add_filter(self.add_basic_authorization)

    def add_basic_authorization(self, request):
        """Pardot uses for basic authorization email, password and user_key. """
        request.params.update({'email': self.email,
                               'password': self.password,
                               'user_key': self.user_key}
                             )

    def add_api_key_authorization(self, request):
        """Pardot uses for basic authorization email, password and user_key. """
        request.params.update({'api_key': self.api_key,
                               'user_key': self.user_key}
                             )

    def get_url(self):
        return self.api_root

    @base.resource(AuthorizationResource)
    def authorization(self):
        return AuthorizationResource(self)

    @base.resource(ProspectsResource)
    def prospects(self):
        return ProspectsResource(self)

    @base.resource(ProspectResource)
    def prospect(self):
        """ For updating a prospect Pardot needs explictly id={id} in params
        which is not provied if adding prospect id to constructor.
        """
        return ProspectResource(self)
