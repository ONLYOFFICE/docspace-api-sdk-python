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

class SsoSpCertificateActionTypeDto(BaseModel):
    """
    What the portal's own key pair may be used for, as the `action` of a service provider certificate.
    """ # noqa: E501
    signing: Optional[StrictStr] = Field(default=None, description="The key pair signs the requests the portal sends and nothing else.", json_schema_extra={"examples": ["signing"]})
    encrypt: Optional[StrictStr] = Field(default=None, description="The key pair encrypts what the portal sends and decrypts what comes back, but signs nothing.", json_schema_extra={"examples": ["encrypt"]})
    signing_and_encrypt: Optional[StrictStr] = Field(default=None, description="The key pair does both, which is what one pair configured on its own has to be set to.", alias="signingAndEncrypt", json_schema_extra={"examples": ["signing and encrypt"]})
    __properties: ClassVar[List[str]] = ["signing", "encrypt", "signingAndEncrypt"]

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
        """Create an instance of SsoSpCertificateActionTypeDto from a JSON string"""
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
            "signing",
            "encrypt",
            "signing_and_encrypt",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if signing (nullable) is None
        # and model_fields_set contains the field
        if self.signing is None and "signing" in self.model_fields_set:
            _dict['signing'] = None

        # set to None if encrypt (nullable) is None
        # and model_fields_set contains the field
        if self.encrypt is None and "encrypt" in self.model_fields_set:
            _dict['encrypt'] = None

        # set to None if signing_and_encrypt (nullable) is None
        # and model_fields_set contains the field
        if self.signing_and_encrypt is None and "signing_and_encrypt" in self.model_fields_set:
            _dict['signingAndEncrypt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SsoSpCertificateActionTypeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "signing": obj.get("signing"),
            "encrypt": obj.get("encrypt"),
            "signingAndEncrypt": obj.get("signingAndEncrypt")
        })
        return _obj


