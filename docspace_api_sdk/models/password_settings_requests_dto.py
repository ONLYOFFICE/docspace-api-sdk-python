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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PasswordSettingsRequestsDto(BaseModel):
    """
    The four values that make up the portal password policy, replaced together.
    """ # noqa: E501
    min_length: StrictInt = Field(description="The shortest password the portal will accept. It has to sit between the floor the installation is configured  with, 8 characters unless it was changed, and the ceiling of 30; a value outside that is refused with 400.", alias="minLength", json_schema_extra={"examples": [8]})
    upper_case: Optional[StrictBool] = Field(default=None, description="Whether a password must contain at least one uppercase letter. There is no partial update on this body, so  leaving the flag out stores it as `false` and drops the requirement.", alias="upperCase", json_schema_extra={"examples": [True]})
    digits: Optional[StrictBool] = Field(default=None, description="Whether a password must contain at least one digit. Leaving the flag out stores it as `false` and drops the  requirement.", json_schema_extra={"examples": [True]})
    spec_symbols: Optional[StrictBool] = Field(default=None, description="Whether a password must contain at least one special symbol. Leaving the flag out stores it as `false` and  drops the requirement.", alias="specSymbols", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["minLength", "upperCase", "digits", "specSymbols"]

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
        """Create an instance of PasswordSettingsRequestsDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PasswordSettingsRequestsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minLength": obj.get("minLength"),
            "upperCase": obj.get("upperCase"),
            "digits": obj.get("digits"),
            "specSymbols": obj.get("specSymbols")
        })
        return _obj


