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

class CheckDocServiceUrlRequestDto(BaseModel):
    """
    The request parameters for checking the document service location.
    """ # noqa: E501
    doc_service_url: Optional[StrictStr] = Field(default=None, description="The ONLYOFFICE Docs URL address.", alias="docServiceUrl")
    doc_service_url_internal: Optional[StrictStr] = Field(default=None, description="The ONLYOFFICE Docs URL address in the local private network.", alias="docServiceUrlInternal")
    doc_service_url_portal: Optional[StrictStr] = Field(default=None, description="The ONLYOFFICE Docs URL address.", alias="docServiceUrlPortal")
    doc_service_signature_secret: Optional[StrictStr] = Field(default=None, description="The signature secret of the ONLYOFFICE Docs.", alias="docServiceSignatureSecret")
    doc_service_signature_header: Optional[StrictStr] = Field(default=None, description="The signature header of the ONLYOFFICE Docs.", alias="docServiceSignatureHeader")
    doc_service_ssl_verification: Optional[StrictBool] = Field(default=None, description="Specifies if the SSL verification of the ONLYOFFICE Docs is enabled or not.", alias="docServiceSslVerification")
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


