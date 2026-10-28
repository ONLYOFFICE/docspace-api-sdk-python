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
from typing import Optional, Set
from typing_extensions import Self

class SsoEncryptAlgorithmTypeDto(BaseModel):
    """
    The encryption algorithms the SSO settings accept.
    """ # noqa: E501
    aes128: Optional[StrictStr] = Field(default=None, description="The AES-128-CBC encryption algorithm, which the built-in configuration uses.", json_schema_extra={"examples": ["http://www.w3.org/2001/04/xmlenc#aes128-cbc"]})
    aes256: Optional[StrictStr] = Field(default=None, description="The AES-256-CBC encryption algorithm, the strongest of the three.", json_schema_extra={"examples": ["http://www.w3.org/2001/04/xmlenc#aes256-cbc"]})
    tri_dec: Optional[StrictStr] = Field(default=None, description="The Triple DES CBC encryption algorithm, kept for identity providers that support nothing newer.", alias="triDec", json_schema_extra={"examples": ["http://www.w3.org/2001/04/xmlenc#tripledes-cbc"]})
    __properties: ClassVar[List[str]] = ["aes128", "aes256", "triDec"]

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
        """Create an instance of SsoEncryptAlgorithmTypeDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "aes128",
            "aes256",
            "tri_dec",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if aes128 (nullable) is None
        # and model_fields_set contains the field
        if self.aes128 is None and "aes128" in self.model_fields_set:
            _dict['aes128'] = None

        # set to None if aes256 (nullable) is None
        # and model_fields_set contains the field
        if self.aes256 is None and "aes256" in self.model_fields_set:
            _dict['aes256'] = None

        # set to None if tri_dec (nullable) is None
        # and model_fields_set contains the field
        if self.tri_dec is None and "tri_dec" in self.model_fields_set:
            _dict['triDec'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SsoEncryptAlgorithmTypeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aes128": obj.get("aes128"),
            "aes256": obj.get("aes256"),
            "triDec": obj.get("triDec")
        })
        return _obj


