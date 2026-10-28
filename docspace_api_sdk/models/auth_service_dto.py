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
from docspace_api_sdk.models.auth_key_dto import AuthKeyDto
from typing import Optional, Set
from typing_extensions import Self

class AuthServiceDto(BaseModel):
    """
    One third-party authorization or storage provider and the keys the portal connects to it with.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The internal key of the provider, such as `google` or `box`. It is the `name` that  `POST api/2.0/settings/authservice` takes to select the provider.", json_schema_extra={"examples": ["google"]})
    title: Optional[StrictStr] = Field(default=None, description="The provider name as it is shown in the interface.", json_schema_extra={"examples": ["Google"]})
    description: Optional[StrictStr] = Field(default=None, description="A sentence about what connecting the provider gives the portal, shown next to it in the interface.", json_schema_extra={"examples": ["Google OAuth authentication"]})
    instruction: Optional[StrictStr] = Field(default=None, description="The steps an administrator has to take on the provider side to obtain the keys, shown in the interface.", json_schema_extra={"examples": ["Configure your Google OAuth credentials"]})
    can_set: Optional[StrictBool] = Field(default=None, description="Whether this provider accepts keys through the API at all. A provider whose keys are fixed by the  installation reports `false`, and saving keys for it is refused.", alias="canSet", json_schema_extra={"examples": [True]})
    paid: Optional[StrictBool] = Field(default=None, description="Whether the provider is a paid option. A paid one can only be connected while the portal plan includes  third-party storage or the installation is licensed as self-hosted.", json_schema_extra={"examples": [False]})
    props: Optional[List[AuthKeyDto]] = Field(default=None, description="The keys the provider defines, with the values last saved and how the settings form shows each of them.  It is `null` for a provider that forbids changes (`canSet` is `false`): its keys are not read at all.", json_schema_extra={"examples": [[{"name": "googleClientId", "value": "1234567890-abc.apps.googleusercontent.com", "title": "Client ID", "type": "text"}]]})
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
        """Create an instance of AuthServiceDto from a JSON string"""
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
        """Create an instance of AuthServiceDto from a dict"""
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
            "props": [AuthKeyDto.from_dict(_item) for _item in obj["props"]] if obj.get("props") is not None else None
        })
        return _obj


