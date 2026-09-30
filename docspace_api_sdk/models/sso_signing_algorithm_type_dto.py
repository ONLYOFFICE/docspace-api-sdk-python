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

class SsoSigningAlgorithmTypeDto(BaseModel):
    """
    The signing algorithms the SSO settings accept.
    """ # noqa: E501
    rsa_sha1: Optional[StrictStr] = Field(default=None, description="The RSA-SHA1 signing algorithm, which the built-in configuration uses. SHA-1 is the weakest of the three  and some identity providers no longer accept it.", alias="rsaSha1", json_schema_extra={"examples": ["http://www.w3.org/2000/09/xmldsig#rsa-sha1"]})
    rsa_sha256: Optional[StrictStr] = Field(default=None, description="The RSA-SHA256 signing algorithm.", alias="rsaSha256", json_schema_extra={"examples": ["http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"]})
    rsa_sha512: Optional[StrictStr] = Field(default=None, description="The RSA-SHA512 signing algorithm.", alias="rsaSha512", json_schema_extra={"examples": ["http://www.w3.org/2001/04/xmldsig-more#rsa-sha512"]})
    __properties: ClassVar[List[str]] = ["rsaSha1", "rsaSha256", "rsaSha512"]

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
        """Create an instance of SsoSigningAlgorithmTypeDto from a JSON string"""
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
            "rsa_sha1",
            "rsa_sha256",
            "rsa_sha512",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if rsa_sha1 (nullable) is None
        # and model_fields_set contains the field
        if self.rsa_sha1 is None and "rsa_sha1" in self.model_fields_set:
            _dict['rsaSha1'] = None

        # set to None if rsa_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.rsa_sha256 is None and "rsa_sha256" in self.model_fields_set:
            _dict['rsaSha256'] = None

        # set to None if rsa_sha512 (nullable) is None
        # and model_fields_set contains the field
        if self.rsa_sha512 is None and "rsa_sha512" in self.model_fields_set:
            _dict['rsaSha512'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SsoSigningAlgorithmTypeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rsaSha1": obj.get("rsaSha1"),
            "rsaSha256": obj.get("rsaSha256"),
            "rsaSha512": obj.get("rsaSha512")
        })
        return _obj


