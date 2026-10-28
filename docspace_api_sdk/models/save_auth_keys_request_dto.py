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
from docspace_api_sdk.models.auth_key_request import AuthKeyRequest
from typing import Optional, Set
from typing_extensions import Self

class SaveAuthKeysRequestDto(BaseModel):
    """
    The keys to store for one third-party authorization or storage provider.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The internal key of the provider, such as `google` or `box`. Take it from the `name` of  `GET api/2.0/settings/authservice`.", json_schema_extra={"examples": ["google"]})
    title: Optional[StrictStr] = Field(default=None, description="Accepted for compatibility with earlier clients and not read: the server keeps its own value.", json_schema_extra={"examples": ["Google"]})
    description: Optional[StrictStr] = Field(default=None, description="Accepted for compatibility with earlier clients and not read: the server keeps its own value.", json_schema_extra={"examples": ["Lets users sign in with a Google account."]})
    instruction: Optional[StrictStr] = Field(default=None, description="Accepted for compatibility with earlier clients and not read: the server keeps its own value.", json_schema_extra={"examples": ["Create a project in the Google Cloud console and copy its OAuth client ID and secret."]})
    can_set: Optional[StrictBool] = Field(default=None, description="Accepted for compatibility with earlier clients and not read: the server keeps its own value.", alias="canSet", json_schema_extra={"examples": [True]})
    paid: Optional[StrictBool] = Field(default=None, description="Accepted for compatibility with earlier clients and not read: the server keeps its own value.", json_schema_extra={"examples": [False]})
    props: Optional[List[AuthKeyRequest]] = Field(default=None, description="The keys of the provider with their new values, by the key names `GET api/2.0/settings/authservice` lists in  `props`.", json_schema_extra={"examples": [[{"name": "googleClientId", "value": "1234567890-abc.apps.googleusercontent.com"}]]})
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
        """Create an instance of SaveAuthKeysRequestDto from a JSON string"""
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
        """Create an instance of SaveAuthKeysRequestDto from a dict"""
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
            "props": [AuthKeyRequest.from_dict(_item) for _item in obj["props"]] if obj.get("props") is not None else None
        })
        return _obj


