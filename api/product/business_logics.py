from api.common.base_logics import BaseLogic
from api.common.base_errors import InvalidRequestParams, PermissionError

from api.storage.models import Image

from .models import Sim

class SimBL(BaseLogic):
    def get_one(self, id=None, slug=None):
        if not id and not slug:
            raise InvalidRequestParams('Must pass atleast code or slug!')

        params = dict(
            deleted=False
        )

        if id:
            params['id'] = id

        else:
            params['slug'] = slug

        product = Sim.objects(**params).first()
        if not product:
            raise InvalidRequestParams('Product not found!')
        product_output = product.output()
        print ('product_output', product_output)

        image_id = product.image_id
        if image_id:
            image = Image.objects(id=image_id).first()
            print ('image', image)
            product_output['image'] = image.url

        return product.output()

    def create(self, name, price, category, image_id, country, owned, day_used):
        product = Sim(name=name,
                      price=price,
                      category=category,
                      image_id=image_id,
                      country=country,
                      owned=owned,
                      day_used=day_used)
        product.create()
        product.save()
        product_output = product.output()

        image_id = product.image_id
        if image_id:
            image = Image.objects(id=image_id).first()
            product_output['image'] = image.url

        return product.output()

sim_bl = SimBL()
