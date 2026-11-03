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
from docspace_api_sdk.models.ai_room_skill import AiRoomSkill
from typing import Optional, Set
from typing_extensions import Self

class AiContextRoomRef(BaseModel):
    """
    One Instructions room a round runs with as context: the account and room ID from `GET api/2.0/ai/context/get-context-folders`, plus the skills of the room the round may use.
    """ # noqa: E501
    cloud: StrictStr = Field(description="The account the room belongs to; `docspace` for a room of this portal.", json_schema_extra={"examples": ["docspace"]})
    id: StrictStr = Field(description="The room ID.", json_schema_extra={"examples": ["1234"]})
    skills: Optional[List[AiRoomSkill]] = Field(default=None, description="The skills of the room the round may use, as `GET api/2.0/ai/context/get-room-skills` lists them.", json_schema_extra={"examples": [[]]})
    __properties: ClassVar[List[str]] = ["cloud", "id", "skills"]

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
        """Create an instance of AiContextRoomRef from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in skills (list)
        _items = []
        if self.skills:
            for _item_skills in self.skills:
                if _item_skills:
                    _items.append(_item_skills.to_dict())
            _dict['skills'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiContextRoomRef from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloud": obj.get("cloud"),
            "id": obj.get("id"),
            "skills": [AiRoomSkill.from_dict(_item) for _item in obj["skills"]] if obj.get("skills") is not None else None
        })
        return _obj


