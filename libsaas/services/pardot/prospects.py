from . import resource

class ProspectsResource(resource.PardotResource):
    path = 'prospect/version/3/do/query'

    def get(self, filters=None):
        """Use this instead of post from PardotResource fore a more explicit
        name.
        """
        return self.post(filters=filters)

class ProspectResource(resource.PardotResource):
    path = 'prospect/version/3/do/update'
