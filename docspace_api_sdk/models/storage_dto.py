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

class StorageDto(BaseModel):
    """
    One third-party storage provider the portal data can be kept in, with the keys it expects.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(description="The provider's key, which is what `PUT api/2.0/settings/storage` and its CDN and backup counterparts take  as the storage to switch to. The built-in local storage has no entry of its own: a listing in which  nothing is `current` means the data sits locally.", json_schema_extra={"examples": ["s3"]})
    title: Optional[StrictStr] = Field(description="The provider name in the portal language, falling back to `id` when this build ships no wording for it.", json_schema_extra={"examples": ["Amazon AWS S3"]})
    properties: Optional[List[AuthKey]] = Field(default=None, description="The settings the provider expects, each with its key, its localised label and the value the server  currently holds. For the entry marked `current` the values come from the portal's saved storage settings  and for the others from the installation configuration, so a setting nobody has configured comes back with  an empty value rather than being left out.", json_schema_extra={"examples": [[{"name": "acesskey", "value": "AKIAIOSFODNN7EXAMPLE", "title": "Access key"}]]})
    current: StrictBool = Field(description="Whether the portal is using this provider right now. At most one entry of a listing has it set.", json_schema_extra={"examples": [True]})
    is_set: StrictBool = Field(description="Whether the provider's keys are already filled in on the server, so it could be switched to without  sending credentials. It says nothing about whether the credentials still work.", alias="isSet", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["id", "title", "properties", "current", "isSet"]

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
        """Create an instance of StorageDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item_properties in self.properties:
                if _item_properties:
                    _items.append(_item_properties.to_dict())
            _dict['properties'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StorageDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "properties": [AuthKey.from_dict(_item) for _item in obj["properties"]] if obj.get("properties") is not None else None,
            "current": obj.get("current"),
            "isSet": obj.get("isSet")
        })
        return _obj


