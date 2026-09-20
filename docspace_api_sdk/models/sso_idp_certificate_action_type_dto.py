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

class SsoIdpCertificateActionTypeDto(BaseModel):
    """
    What the identity provider's certificate may be used for, as the `action` of an identity provider certificate.
    """ # noqa: E501
    verification: Optional[StrictStr] = Field(default=None, description="The certificate verifies the signatures on what the provider sends, and nothing else - the counterpart of  the service provider's signing action.", json_schema_extra={"examples": ["verification"]})
    decrypt: Optional[StrictStr] = Field(default=None, description="The certificate is used to decrypt what the provider sends, but verifies no signature.", json_schema_extra={"examples": ["decrypt"]})
    verification_and_decrypt: Optional[StrictStr] = Field(default=None, description="The certificate does both, which is what a single provider certificate has to be set to.", alias="verificationAndDecrypt", json_schema_extra={"examples": ["verification and decrypt"]})
    __properties: ClassVar[List[str]] = ["verification", "decrypt", "verificationAndDecrypt"]

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
        """Create an instance of SsoIdpCertificateActionTypeDto from a JSON string"""
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
            "verification",
            "decrypt",
            "verification_and_decrypt",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if verification (nullable) is None
        # and model_fields_set contains the field
        if self.verification is None and "verification" in self.model_fields_set:
            _dict['verification'] = None

        # set to None if decrypt (nullable) is None
        # and model_fields_set contains the field
        if self.decrypt is None and "decrypt" in self.model_fields_set:
            _dict['decrypt'] = None

        # set to None if verification_and_decrypt (nullable) is None
        # and model_fields_set contains the field
        if self.verification_and_decrypt is None and "verification_and_decrypt" in self.model_fields_set:
            _dict['verificationAndDecrypt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SsoIdpCertificateActionTypeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "verification": obj.get("verification"),
            "decrypt": obj.get("decrypt"),
            "verificationAndDecrypt": obj.get("verificationAndDecrypt")
        })
        return _obj


