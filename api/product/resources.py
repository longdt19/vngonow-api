from api.common.base_resources import BaseResource

from .forms import *
from .business_logics import sim_bl


class SimResource(BaseResource):
    GET_INPUT_SCHEMA = GetSimDetailForm()
    POST_INPUT_SCHEMA = CreateSimForm()

    def get(self):
        params = self.parse_request_params()
        return sim_bl.get_one(**params)

    def post(self):
        params = self.parse_request_params()
        return sim_bl.create(**params)

RESOURCES = {
    '/sim': {
        'resource': SimResource
    }
}
