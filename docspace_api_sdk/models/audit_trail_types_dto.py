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
from typing import Optional, Set
from typing_extensions import Self

class AuditTrailTypesDto(BaseModel):
    """
    The vocabularies the audit and login-history filters accept, one array of names per dimension of an event.
    """ # noqa: E501
    actions: Optional[List[StrictStr]] = Field(default=None, description="Every action name the build can record, spelled as the `action` filter of  `GET api/2.0/security/audit/events/filter` and `GET api/2.0/security/audit/login/filter` expects it. It is  the whole vocabulary, not the actions this portal has recorded, and only a handful of the names are the  sign-in actions the login filter accepts.", json_schema_extra={"examples": [["FileCreated"]]})
    action_types: Optional[List[StrictStr]] = Field(default=None, description="The kinds of change an action can stand for, spelled as the `actionType` filter of  `GET api/2.0/security/audit/events/filter` expects it.", alias="actionTypes", json_schema_extra={"examples": [["Create"]]})
    product_types: Optional[List[StrictStr]] = Field(default=None, description="The products an action can belong to, spelled as the `productType` filter of  `GET api/2.0/security/audit/mappers` expects it. The audit trail itself cannot be filtered by product.", alias="productTypes", json_schema_extra={"examples": [["Documents"]]})
    module_types: Optional[List[StrictStr]] = Field(default=None, description="The locations inside those products, spelled as the `moduleType` filter of  `GET api/2.0/security/audit/events/filter` and `GET api/2.0/security/audit/mappers` expects it.", alias="moduleTypes", json_schema_extra={"examples": [["Files"]]})
    entry_types: Optional[List[StrictStr]] = Field(default=None, description="The kinds of object an action can be applied to, spelled as the `entryType` filter of  `GET api/2.0/security/audit/events/filter` expects it.", alias="entryTypes", json_schema_extra={"examples": [["File"]]})
    __properties: ClassVar[List[str]] = ["actions", "actionTypes", "productTypes", "moduleTypes", "entryTypes"]

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
        """Create an instance of AuditTrailTypesDto from a JSON string"""
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
        # set to None if actions (nullable) is None
        # and model_fields_set contains the field
        if self.actions is None and "actions" in self.model_fields_set:
            _dict['actions'] = None

        # set to None if action_types (nullable) is None
        # and model_fields_set contains the field
        if self.action_types is None and "action_types" in self.model_fields_set:
            _dict['actionTypes'] = None

        # set to None if product_types (nullable) is None
        # and model_fields_set contains the field
        if self.product_types is None and "product_types" in self.model_fields_set:
            _dict['productTypes'] = None

        # set to None if module_types (nullable) is None
        # and model_fields_set contains the field
        if self.module_types is None and "module_types" in self.model_fields_set:
            _dict['moduleTypes'] = None

        # set to None if entry_types (nullable) is None
        # and model_fields_set contains the field
        if self.entry_types is None and "entry_types" in self.model_fields_set:
            _dict['entryTypes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditTrailTypesDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": obj.get("actions"),
            "actionTypes": obj.get("actionTypes"),
            "productTypes": obj.get("productTypes"),
            "moduleTypes": obj.get("moduleTypes"),
            "entryTypes": obj.get("entryTypes")
        })
        return _obj


