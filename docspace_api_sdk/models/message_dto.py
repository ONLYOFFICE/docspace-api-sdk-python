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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.message_content_dto import MessageContentDto
from docspace_api_sdk.models.role import Role
from typing import Optional, Set
from typing_extensions import Self

class MessageDto(BaseModel):
    """
    The chat message information.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the message.")
    role: Optional[Role] = None
    contents: Optional[List[MessageContentDto]] = Field(default=None, description="The ordered collection of content blocks that make up the message body (text, tool calls, or attachments).")
    created_on: Optional[ApiDateTime] = Field(default=None, alias="createdOn")
    __properties: ClassVar[List[str]] = ["id", "role", "contents", "createdOn"]

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
        """Create an instance of MessageDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contents (list)
        _items = []
        if self.contents:
            for _item_contents in self.contents:
                if _item_contents:
                    _items.append(_item_contents.to_dict())
            _dict['contents'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_on
        if self.created_on:
            _dict['createdOn'] = self.created_on.to_dict()
        # set to None if contents (nullable) is None
        # and model_fields_set contains the field
        if self.contents is None and "contents" in self.model_fields_set:
            _dict['contents'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MessageDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "role": obj.get("role"),
            "contents": [MessageContentDto.from_dict(_item) for _item in obj["contents"]] if obj.get("contents") is not None else None,
            "createdOn": ApiDateTime.from_dict(obj["createdOn"]) if obj.get("createdOn") is not None else None
        })
        return _obj


