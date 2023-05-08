from office365.runtime.odata.url_builder import ODataUrlBuilder
from office365.runtime.queries.client_query import ClientQuery


class FunctionQuery(ClientQuery):
    """"Service operation query"""

    def __init__(self, binding_type,
                 method_name=None,
                 method_params=None,
                 return_type=None):
        """
        Function query

        :type method_params: list or dict or office365.runtime.client_value.ClientValue or None
        :type method_name: str or None
        """
        super(FunctionQuery, self).__init__(binding_type.context,
                                            binding_type,
                                            None,
                                            None,
                                            return_type)
        self._method_name = method_name
        self._method_params = method_params

    @property
    def url(self):
        orig_url = super(FunctionQuery, self).url
        return "/".join([orig_url, ODataUrlBuilder.build(self._method_name, self._method_params)])

    @property
    def method_name(self):
        return self._method_name
