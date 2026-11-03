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
from typing import Any, ClassVar, Dict, List
from docspace_api_sdk.models.ai_profile import AiProfile
from typing import Optional, Set
from typing_extensions import Self

class AiAssignmentsExpanded(BaseModel):
    """
    The bindings with `expand=profile`: the bound profiles themselves, plus how many profiles the portal has, so a chat can start on this one read.
    """ # noqa: E501
    assignments: Dict[str, AiProfile] = Field(description="The bound profiles keyed by action type, as `GET api/2.0/ai/profiles/list` describes them. A binding whose profile no longer exists is left out.")
    profiles_total: StrictInt = Field(description="How many profiles the portal has.", alias="profilesTotal")
    chat_profiles_total: StrictInt = Field(description="How many of those profiles can chat; a profile without declared capabilities counts as one that can.", alias="chatProfilesTotal")
    __properties: ClassVar[List[str]] = ["assignments", "profilesTotal", "chatProfilesTotal"]

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
        """Create an instance of AiAssignmentsExpanded from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in assignments (dict)
        _field_dict = {}
        if self.assignments:
            for _key_assignments in self.assignments:
                if self.assignments[_key_assignments]:
                    _field_dict[_key_assignments] = self.assignments[_key_assignments].to_dict()
            _dict['assignments'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiAssignmentsExpanded from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignments": dict(
                (_k, AiProfile.from_dict(_v))
                for _k, _v in obj["assignments"].items()
            )
            if obj.get("assignments") is not None
            else None,
            "profilesTotal": obj.get("profilesTotal"),
            "chatProfilesTotal": obj.get("chatProfilesTotal")
        })
        return _obj


