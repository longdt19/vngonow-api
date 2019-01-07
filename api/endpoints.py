from api.storage.resources import RESOURCES as STORAGE_RESOURCES
from api.product.resources import RESOURCES as PRODUCT_RESOURCES


ENDPOINTS = {
    **STORAGE_RESOURCES,
    **PRODUCT_RESOURCES
}
