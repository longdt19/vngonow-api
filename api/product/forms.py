from api.common.base_forms import (ValidationError, BaseCreateForm, BaseListForm,
                                  BaseReadForm, BaseUpdateForm, IdField,
                                  fields, STRING_LENGTH_VALIDATORS, BaseForm)


class BaseCreateProductForm(BaseForm):
    name = fields.String(validate=STRING_LENGTH_VALIDATORS['LONG'])
    price = fields.Integer(required=True)
    category = fields.String(validate=STRING_LENGTH_VALIDATORS['LONG'])
    image_id = IdField(required=True)
    country = fields.String(validate=STRING_LENGTH_VALIDATORS['LONG'])


class CreateSimForm(BaseCreateProductForm):
    owned = fields.String(validate=STRING_LENGTH_VALIDATORS['LONG'])
    day_used = fields.Integer(required=True)


class GetSimDetailForm(BaseForm):
    slug = fields.String(validate=STRING_LENGTH_VALIDATORS['LONG'])
    id = IdField()
