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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.provider_type import ProviderType
from typing import Optional, Set
from typing_extensions import Self

class AiProviderDto(BaseModel):
    """
    AI provider details.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="AI provider identifier.")
    title: Optional[StrictStr] = Field(description="AI provider display title.")
    type: Optional[ProviderType] = None
    url: Optional[StrictStr] = Field(default=None, description="API endpoint URL for the AI provider.")
    created_on: ApiDateTime = Field(alias="createdOn")
    modified_on: ApiDateTime = Field(alias="modifiedOn")
    need_reset: Optional[StrictBool] = Field(default=None, description="Indicates whether the provider's API key needs to be reset.", alias="needReset")
    is_default: Optional[StrictBool] = Field(default=None, description="Indicates whether this provider is the default provider for the tenant.", alias="isDefault")
    __properties: ClassVar[List[str]] = ["id", "title", "type", "url", "createdOn", "modifiedOn", "needReset", "isDefault"]

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
        """Create an instance of AiProviderDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_on
        if self.created_on:
            _dict['createdOn'] = self.created_on.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_on
        if self.modified_on:
            _dict['modifiedOn'] = self.modified_on.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiProviderDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "createdOn": ApiDateTime.from_dict(obj["createdOn"]) if obj.get("createdOn") is not None else None,
            "modifiedOn": ApiDateTime.from_dict(obj["modifiedOn"]) if obj.get("modifiedOn") is not None else None,
            "needReset": obj.get("needReset"),
            "isDefault": obj.get("isDefault")
        })
        return _obj


