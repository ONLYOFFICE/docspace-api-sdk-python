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

class SsoNameIdFormatTypeDto(BaseModel):
    """
    The SAML name ID formats the SSO settings accept.
    """ # noqa: E501
    saml11_unspecified: Optional[StrictStr] = Field(default=None, description="The SAML 1.1 unspecified name ID format.", alias="saml11Unspecified", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"]})
    saml11_email_address: Optional[StrictStr] = Field(default=None, description="The SAML 1.1 email address name ID format.", alias="saml11EmailAddress", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"]})
    saml20_entity: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 entity name ID format.", alias="saml20Entity", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:nameid-format:entity"]})
    saml20_transient: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 transient name ID format, whose identifier differs from one session to the next. It is what  the built-in configuration uses.", alias="saml20Transient", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:nameid-format:transient"]})
    saml20_persistent: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 persistent name ID format, whose identifier stays the same for one person across sessions.", alias="saml20Persistent", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:nameid-format:persistent"]})
    saml20_encrypted: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 encrypted name ID format.", alias="saml20Encrypted", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:nameid-format:encrypted"]})
    saml20_unspecified: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 unspecified name ID format.", alias="saml20Unspecified", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:nameid-format:unspecified"]})
    saml11_x509_subject_name: Optional[StrictStr] = Field(default=None, description="The SAML 1.1 X.509 subject name name ID format.", alias="saml11X509SubjectName", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName"]})
    saml11_windows_domain_qualified_name: Optional[StrictStr] = Field(default=None, description="The SAML 1.1 Windows domain qualified name name ID format.", alias="saml11WindowsDomainQualifiedName", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName"]})
    saml20_kerberos: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 Kerberos name ID format.", alias="saml20Kerberos", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos"]})
    __properties: ClassVar[List[str]] = ["saml11Unspecified", "saml11EmailAddress", "saml20Entity", "saml20Transient", "saml20Persistent", "saml20Encrypted", "saml20Unspecified", "saml11X509SubjectName", "saml11WindowsDomainQualifiedName", "saml20Kerberos"]

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
        """Create an instance of SsoNameIdFormatTypeDto from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "saml11_unspecified",
            "saml11_email_address",
            "saml20_entity",
            "saml20_transient",
            "saml20_persistent",
            "saml20_encrypted",
            "saml20_unspecified",
            "saml11_x509_subject_name",
            "saml11_windows_domain_qualified_name",
            "saml20_kerberos",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if saml11_unspecified (nullable) is None
        # and model_fields_set contains the field
        if self.saml11_unspecified is None and "saml11_unspecified" in self.model_fields_set:
            _dict['saml11Unspecified'] = None

        # set to None if saml11_email_address (nullable) is None
        # and model_fields_set contains the field
        if self.saml11_email_address is None and "saml11_email_address" in self.model_fields_set:
            _dict['saml11EmailAddress'] = None

        # set to None if saml20_entity (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_entity is None and "saml20_entity" in self.model_fields_set:
            _dict['saml20Entity'] = None

        # set to None if saml20_transient (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_transient is None and "saml20_transient" in self.model_fields_set:
            _dict['saml20Transient'] = None

        # set to None if saml20_persistent (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_persistent is None and "saml20_persistent" in self.model_fields_set:
            _dict['saml20Persistent'] = None

        # set to None if saml20_encrypted (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_encrypted is None and "saml20_encrypted" in self.model_fields_set:
            _dict['saml20Encrypted'] = None

        # set to None if saml20_unspecified (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_unspecified is None and "saml20_unspecified" in self.model_fields_set:
            _dict['saml20Unspecified'] = None

        # set to None if saml11_x509_subject_name (nullable) is None
        # and model_fields_set contains the field
        if self.saml11_x509_subject_name is None and "saml11_x509_subject_name" in self.model_fields_set:
            _dict['saml11X509SubjectName'] = None

        # set to None if saml11_windows_domain_qualified_name (nullable) is None
        # and model_fields_set contains the field
        if self.saml11_windows_domain_qualified_name is None and "saml11_windows_domain_qualified_name" in self.model_fields_set:
            _dict['saml11WindowsDomainQualifiedName'] = None

        # set to None if saml20_kerberos (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_kerberos is None and "saml20_kerberos" in self.model_fields_set:
            _dict['saml20Kerberos'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SsoNameIdFormatTypeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "saml11Unspecified": obj.get("saml11Unspecified"),
            "saml11EmailAddress": obj.get("saml11EmailAddress"),
            "saml20Entity": obj.get("saml20Entity"),
            "saml20Transient": obj.get("saml20Transient"),
            "saml20Persistent": obj.get("saml20Persistent"),
            "saml20Encrypted": obj.get("saml20Encrypted"),
            "saml20Unspecified": obj.get("saml20Unspecified"),
            "saml11X509SubjectName": obj.get("saml11X509SubjectName"),
            "saml11WindowsDomainQualifiedName": obj.get("saml11WindowsDomainQualifiedName"),
            "saml20Kerberos": obj.get("saml20Kerberos")
        })
        return _obj


