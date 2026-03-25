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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class AddMcpServerRequestBody(BaseModel):
    """
    Parameters for creating a new custom MCP server.
    """ # noqa: E501
    name: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(description="Unique display name for the server. Only letters, numbers, underscores, and hyphens are allowed. Maximum 128 characters.")
    description: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(description="Human-readable description of the server's purpose and capabilities. Maximum 255 characters.")
    endpoint: Optional[StrictStr] = Field(description="Base URL of the MCP server endpoint. Must be a valid, reachable URL. The system will verify connectivity during registration.")
    headers: Optional[Dict[str, StrictStr]] = Field(default=None, description="Optional HTTP headers to include with every request to the MCP server (e.g., authentication tokens or API keys).")
    icon: Optional[StrictStr] = Field(default=None, description="Optional Base64-encoded icon image for the server. Used as the visual identifier in the UI.")
    __properties: ClassVar[List[str]] = ["name", "description", "endpoint", "headers", "icon"]

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
        """Create an instance of AddMcpServerRequestBody from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint is None and "endpoint" in self.model_fields_set:
            _dict['endpoint'] = None

        # set to None if headers (nullable) is None
        # and model_fields_set contains the field
        if self.headers is None and "headers" in self.model_fields_set:
            _dict['headers'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddMcpServerRequestBody from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "endpoint": obj.get("endpoint"),
            "headers": obj.get("headers"),
            "icon": obj.get("icon")
        })
        return _obj


