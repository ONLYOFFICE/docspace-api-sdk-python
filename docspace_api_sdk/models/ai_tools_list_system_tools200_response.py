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
from typing import Any, ClassVar, Dict, List
from docspace_api_sdk.models.ai_tmcp_item import AiTMCPItem
from typing import Optional, Set
from typing_extensions import Self

class AiToolsListSystemTools200Response(BaseModel):
    """
    AiToolsListSystemTools200Response
    """ # noqa: E501
    groups: Dict[str, List[AiTMCPItem]] = Field(description="Tools by server name, covering both the host-configured system servers and the custom MCP servers registered for this scope.")
    errors: Dict[str, StrictStr] = Field(description="Why a registered custom server could not be reached, keyed by server name. A server that answered is absent from this map.")
    system: List[StrictStr] = Field(description="Names of the host-configured system servers among the keys of `groups`; everything else there was registered as a custom server.")
    __properties: ClassVar[List[str]] = ["groups", "errors", "system"]

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
        """Create an instance of AiToolsListSystemTools200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in groups (dict of array)
        _field_dict_of_array = {}
        if self.groups:
            for _key_groups in self.groups:
                if self.groups[_key_groups] is not None:
                    _field_dict_of_array[_key_groups] = [
                        _item.to_dict() for _item in self.groups[_key_groups]
                    ]
            _dict['groups'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiToolsListSystemTools200Response from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groups": dict(
                (_k,
                        [AiTMCPItem.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("groups", {}).items()
            ),
            "errors": obj.get("errors"),
            "system": obj.get("system")
        })
        return _obj


