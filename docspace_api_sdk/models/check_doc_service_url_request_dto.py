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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CheckDocServiceUrlRequestDto(BaseModel):
    """
    The ONLYOFFICE Docs connection settings to store and verify.
    """ # noqa: E501
    doc_service_url: Optional[StrictStr] = Field(description="The public address of the Document Server, the one a browser loads the editor from. An empty value drops the  portal's own setting, so the address configured for the deployment takes over again. A value with no scheme is  stored with `http://` prepended, and an absolute address may not carry a query string.", alias="docServiceUrl", json_schema_extra={"examples": ["https://documentserver.example.com"]})
    doc_service_url_internal: Optional[StrictStr] = Field(default=None, description="The address the portal itself uses for its server-to-server calls to the Document Server, for deployments  where that traffic stays inside the private network. Left empty, those calls go to the public address instead.", alias="docServiceUrlInternal", json_schema_extra={"examples": ["https://documentserver-internal.example.com"]})
    doc_service_url_portal: Optional[StrictStr] = Field(default=None, description="The address of this portal as the Document Server has to call it back on in order to fetch and save a  document. Set it when the Document Server cannot resolve the portal by its public name; left empty, the  portal's own resolved address is used.", alias="docServiceUrlPortal", json_schema_extra={"examples": ["https://portal.example.com"]})
    doc_service_signature_secret: Optional[StrictStr] = Field(default=None, description="The shared secret that requests between the portal and the Document Server are signed with; it has to be the  same value the Document Server itself is configured with, otherwise the verification of the new settings  fails. It is write-only: the document service location is reported without it.", alias="docServiceSignatureSecret", json_schema_extra={"examples": ["secret-key-123"]})
    doc_service_signature_header: Optional[StrictStr] = Field(default=None, description="The name of the HTTP header the signature travels in, which has to match the header the Document Server  expects. A secret without a header is not a usable pair and is rejected.", alias="docServiceSignatureHeader", json_schema_extra={"examples": ["Authorization"]})
    doc_service_ssl_verification: Optional[StrictBool] = Field(default=None, description="Whether the portal validates the TLS certificate of the Document Server. With verification on, a self-signed  certificate breaks the connection; with it off, any certificate is accepted, which is meant for test  deployments only. Omitting the field turns verification on.", alias="docServiceSslVerification", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["docServiceUrl", "docServiceUrlInternal", "docServiceUrlPortal", "docServiceSignatureSecret", "docServiceSignatureHeader", "docServiceSslVerification"]

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
        """Create an instance of CheckDocServiceUrlRequestDto from a JSON string"""
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
        # set to None if doc_service_url (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_url is None and "doc_service_url" in self.model_fields_set:
            _dict['docServiceUrl'] = None

        # set to None if doc_service_url_internal (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_url_internal is None and "doc_service_url_internal" in self.model_fields_set:
            _dict['docServiceUrlInternal'] = None

        # set to None if doc_service_url_portal (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_url_portal is None and "doc_service_url_portal" in self.model_fields_set:
            _dict['docServiceUrlPortal'] = None

        # set to None if doc_service_signature_secret (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_signature_secret is None and "doc_service_signature_secret" in self.model_fields_set:
            _dict['docServiceSignatureSecret'] = None

        # set to None if doc_service_signature_header (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_signature_header is None and "doc_service_signature_header" in self.model_fields_set:
            _dict['docServiceSignatureHeader'] = None

        # set to None if doc_service_ssl_verification (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_ssl_verification is None and "doc_service_ssl_verification" in self.model_fields_set:
            _dict['docServiceSslVerification'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CheckDocServiceUrlRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "docServiceUrl": obj.get("docServiceUrl"),
            "docServiceUrlInternal": obj.get("docServiceUrlInternal"),
            "docServiceUrlPortal": obj.get("docServiceUrlPortal"),
            "docServiceSignatureSecret": obj.get("docServiceSignatureSecret"),
            "docServiceSignatureHeader": obj.get("docServiceSignatureHeader"),
            "docServiceSslVerification": obj.get("docServiceSslVerification")
        })
        return _obj


