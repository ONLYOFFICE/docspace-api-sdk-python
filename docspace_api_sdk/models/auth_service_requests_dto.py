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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.auth_key import AuthKey
from typing import Optional, Set
from typing_extensions import Self

class AuthServiceRequestsDto(BaseModel):
    """
    One third-party authorization or storage provider and the keys the portal connects to it with.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The provider being configured, by its internal key such as `google` or `box`. Take it from the `name` of  `GET api/2.0/settings/authservice`; it is the only field that selects the provider, and a key this  installation does not know is refused the same way a provider that forbids changes is.", json_schema_extra={"examples": ["google"]})
    title: Optional[StrictStr] = Field(default=None, description="The provider name as it is shown in the interface. It is filled in by the portal when the providers are  listed and is ignored when keys are saved.", json_schema_extra={"examples": ["Google"]})
    description: Optional[StrictStr] = Field(default=None, description="A sentence about what connecting the provider gives the portal, shown next to it in the interface. It is  filled in by the portal and ignored when keys are saved.", json_schema_extra={"examples": ["Google OAuth authentication"]})
    instruction: Optional[StrictStr] = Field(default=None, description="The steps an administrator has to take on the provider side to obtain the keys, shown in the interface. It is  filled in by the portal and ignored when keys are saved.", json_schema_extra={"examples": ["Configure your Google OAuth credentials"]})
    can_set: Optional[StrictBool] = Field(default=None, description="Whether this provider accepts keys through the API at all. A provider whose keys are fixed by the  installation reports `false`, and saving keys for it is refused; the field is reported by the portal and  ignored on the way in.", alias="canSet", json_schema_extra={"examples": [True]})
    paid: Optional[StrictBool] = Field(default=None, description="Whether the provider is a paid option. A paid one can only be connected while the portal plan includes  third-party storage or the installation is licensed as self-hosted; the field is reported by the portal and  ignored on the way in.", json_schema_extra={"examples": [False]})
    props: Optional[List[AuthKey]] = Field(default=None, description="The credentials the portal authenticates to the provider with, as the name and value pairs the provider  defines. Send the whole set the provider expects: leaving every value empty disconnects it, and a set that  fails the provider validation is cleared rather than stored half-applied. The listing operation reports the  values last saved, and a provider that forbids changes reports none at all.", json_schema_extra={"examples": [[{"name": "key", "value": "value"}]]})
    __properties: ClassVar[List[str]] = ["name", "title", "description", "instruction", "canSet", "paid", "props"]

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
        """Create an instance of AuthServiceRequestsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in props (list)
        _items = []
        if self.props:
            for _item_props in self.props:
                if _item_props:
                    _items.append(_item_props.to_dict())
            _dict['props'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if instruction (nullable) is None
        # and model_fields_set contains the field
        if self.instruction is None and "instruction" in self.model_fields_set:
            _dict['instruction'] = None

        # set to None if props (nullable) is None
        # and model_fields_set contains the field
        if self.props is None and "props" in self.model_fields_set:
            _dict['props'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthServiceRequestsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "instruction": obj.get("instruction"),
            "canSet": obj.get("canSet"),
            "paid": obj.get("paid"),
            "props": [AuthKey.from_dict(_item) for _item in obj["props"]] if obj.get("props") is not None else None
        })
        return _obj


