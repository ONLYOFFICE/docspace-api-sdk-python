# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



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
    The document service URL parameters.
    """ # noqa: E501
    version: Optional[StrictStr] = Field(description="The version of the document service.")
    doc_service_url_api: Optional[StrictStr] = Field(description="The document service URL API.", alias="docServiceUrlApi")
    doc_service_url: Optional[StrictStr] = Field(description="The document service URL.", alias="docServiceUrl")
    doc_service_url_internal: Optional[StrictStr] = Field(description="The internal document service URL.", alias="docServiceUrlInternal")
    doc_service_portal_url: Optional[StrictStr] = Field(description="The document service portal URL.", alias="docServicePortalUrl")
    doc_service_signature_header: Optional[StrictStr] = Field(default=None, description="The document service signature header.", alias="docServiceSignatureHeader")
    doc_service_ssl_verification: Optional[StrictBool] = Field(default=None, description="Specifies if the document service SSL verification is enabled.", alias="docServiceSslVerification")
    is_default: StrictBool = Field(description="Specifies if the document service is default.", alias="isDefault")
    __properties: ClassVar[List[str]] = ["version", "docServiceUrlApi", "docServiceUrl", "docServiceUrlInternal", "docServicePortalUrl", "docServiceSignatureHeader", "docServiceSslVerification", "isDefault"]

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
            "docServiceUrlInternal": obj.get("docServiceUrlInternal"),
            "docServicePortalUrl": obj.get("docServicePortalUrl"),
            "docServiceSignatureHeader": obj.get("docServiceSignatureHeader"),
            "docServiceSslVerification": obj.get("docServiceSslVerification"),
            "isDefault": obj.get("isDefault")
        })
        return _obj


