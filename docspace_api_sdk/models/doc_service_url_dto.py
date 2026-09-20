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

class DocServiceUrlDto(BaseModel):
    """
    The document service location as this portal has it configured, together with the editor entry points a client  needs in order to open a document.
    """ # noqa: E501
    version: Optional[StrictStr] = Field(description="The editor version the running Document Server reported. It is filled in only when the version was asked for,  and comes back empty otherwise. When the Document Server does not answer, a fallback version is reported  rather than an error, so a value here is no proof that the server is reachable.", json_schema_extra={"examples": ["8.0.1"]})
    doc_service_url_api: Optional[StrictStr] = Field(description="The absolute URL of the editor api script that a client has to load before it can open a document. It is  derived from the public Document Server address unless the deployment overrides it separately.", alias="docServiceUrlApi", json_schema_extra={"examples": ["https://documentserver.example.com/web-apps/apps/api/documents/api.js"]})
    doc_service_url: Optional[StrictStr] = Field(description="The public Document Server address a browser loads the editor from. Empty means no document server is  configured for this portal, and documents cannot be opened for editing or viewing.", alias="docServiceUrl", json_schema_extra={"examples": ["https://documentserver.example.com/"]})
    doc_service_preload_url: Optional[StrictStr] = Field(description="The absolute URL of a page a client may load in advance to warm the editor scripts up. Loading it is optional  and changes nothing on the portal.", alias="docServicePreloadUrl", json_schema_extra={"examples": ["https://documentserver.example.com/web-apps/apps/api/documents/preload.html"]})
    doc_service_url_internal: Optional[StrictStr] = Field(description="The address the portal uses for its own server-to-server calls to the Document Server. When no private-network  address is configured, it repeats the public one.", alias="docServiceUrlInternal", json_schema_extra={"examples": ["http://documentserver-internal.local/"]})
    doc_service_portal_url: Optional[StrictStr] = Field(description="The address the Document Server is told to call this portal back on. Empty means nothing overrides it and the  portal's own resolved address is used.", alias="docServicePortalUrl", json_schema_extra={"examples": ["https://portal.example.com/"]})
    doc_service_signature_header: Optional[StrictStr] = Field(description="The name of the HTTP header that carries the signature on requests between the portal and the Document Server.  The secret itself is not part of the answer, so this only tells a client whether request signing is set up and  under which header.", alias="docServiceSignatureHeader", json_schema_extra={"examples": ["Authorization"]})
    doc_service_ssl_verification: StrictBool = Field(description="Whether the portal validates the TLS certificate of the Document Server. False means any certificate is  accepted, which is expected only in a test deployment.", alias="docServiceSslVerification", json_schema_extra={"examples": [True]})
    is_default: StrictBool = Field(description="Whether every one of these settings is still the one the deployment ships with. False means at least one of  the addresses, the signature settings or SSL verification has been overridden for this portal.", alias="isDefault", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["version", "docServiceUrlApi", "docServiceUrl", "docServicePreloadUrl", "docServiceUrlInternal", "docServicePortalUrl", "docServiceSignatureHeader", "docServiceSslVerification", "isDefault"]

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
        """Create an instance of DocServiceUrlDto from a JSON string"""
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
        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if doc_service_url_api (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_url_api is None and "doc_service_url_api" in self.model_fields_set:
            _dict['docServiceUrlApi'] = None

        # set to None if doc_service_url (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_url is None and "doc_service_url" in self.model_fields_set:
            _dict['docServiceUrl'] = None

        # set to None if doc_service_preload_url (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_preload_url is None and "doc_service_preload_url" in self.model_fields_set:
            _dict['docServicePreloadUrl'] = None

        # set to None if doc_service_url_internal (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_url_internal is None and "doc_service_url_internal" in self.model_fields_set:
            _dict['docServiceUrlInternal'] = None

        # set to None if doc_service_portal_url (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_portal_url is None and "doc_service_portal_url" in self.model_fields_set:
            _dict['docServicePortalUrl'] = None

        # set to None if doc_service_signature_header (nullable) is None
        # and model_fields_set contains the field
        if self.doc_service_signature_header is None and "doc_service_signature_header" in self.model_fields_set:
            _dict['docServiceSignatureHeader'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocServiceUrlDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version": obj.get("version"),
            "docServiceUrlApi": obj.get("docServiceUrlApi"),
            "docServiceUrl": obj.get("docServiceUrl"),
            "docServicePreloadUrl": obj.get("docServicePreloadUrl"),
            "docServiceUrlInternal": obj.get("docServiceUrlInternal"),
            "docServicePortalUrl": obj.get("docServicePortalUrl"),
            "docServiceSignatureHeader": obj.get("docServiceSignatureHeader"),
            "docServiceSslVerification": obj.get("docServiceSslVerification"),
            "isDefault": obj.get("isDefault")
        })
        return _obj


