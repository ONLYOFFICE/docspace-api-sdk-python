#
# (c) Copyright Ascensio System SIA 2026
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.audit_trail_module_mapper_dto import AuditTrailModuleMapperDto
from typing import Optional, Set
from typing_extensions import Self

class AuditTrailProductMapperDto(BaseModel):
    """
    The audit trail actions of one product, grouped by module.
    """ # noqa: E501
    product_type: Optional[StrictStr] = Field(default=None, description="The product this branch of the tree belongs to, as the `productType` filter of this operation spells it and  as `GET api/2.0/security/audit/types` lists it under `productTypes`.", alias="productType", json_schema_extra={"examples": ["Documents"]})
    modules: Optional[List[AuditTrailModuleMapperDto]] = Field(default=None, description="The locations inside the product. It is empty when `moduleType` was passed and this product has no module  of that name, which is why a product can come back with nothing under it.")
    __properties: ClassVar[List[str]] = ["productType", "modules"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AuditTrailProductMapperDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in modules (list)
        _items = []
        if self.modules:
            for _item_modules in self.modules:
                if _item_modules:
                    _items.append(_item_modules.to_dict())
            _dict['modules'] = _items
        # set to None if product_type (nullable) is None
        # and model_fields_set contains the field
        if self.product_type is None and "product_type" in self.model_fields_set:
            _dict['productType'] = None

        # set to None if modules (nullable) is None
        # and model_fields_set contains the field
        if self.modules is None and "modules" in self.model_fields_set:
            _dict['modules'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditTrailProductMapperDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "productType": obj.get("productType"),
            "modules": [AuditTrailModuleMapperDto.from_dict(_item) for _item in obj["modules"]] if obj.get("modules") is not None else None
        })
        return _obj


