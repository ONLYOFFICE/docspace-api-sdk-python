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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace-api-python.models.current_license_info import CurrentLicenseInfo
from typing import Optional, Set
from typing_extensions import Self

class PaymentSettingsDto(BaseModel):
    """
    The payment settings parameters.
    """ # noqa: E501
    sales_email: Optional[StrictStr] = Field(default=None, description="The email address for sales inquiries and support.", alias="salesEmail")
    feedback_and_support_url: Optional[StrictStr] = Field(default=None, description="The URL for accessing the feedback and support resources.", alias="feedbackAndSupportUrl")
    buy_url: Optional[StrictStr] = Field(default=None, description="The URL for purchasing or upgrading the product.", alias="buyUrl")
    standalone: Optional[StrictBool] = Field(default=None, description="Indicates whether the system is running in standalone mode.")
    current_license: Optional[CurrentLicenseInfo] = Field(default=None, alias="currentLicense")
    max: Optional[StrictInt] = Field(default=None, description="The maximum quota quantity.")
    __properties: ClassVar[List[str]] = ["salesEmail", "feedbackAndSupportUrl", "buyUrl", "standalone", "currentLicense", "max"]

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
        """Create an instance of PaymentSettingsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of current_license
        if self.current_license:
            _dict['currentLicense'] = self.current_license.to_dict()
        # set to None if sales_email (nullable) is None
        # and model_fields_set contains the field
        if self.sales_email is None and "sales_email" in self.model_fields_set:
            _dict['salesEmail'] = None

        # set to None if feedback_and_support_url (nullable) is None
        # and model_fields_set contains the field
        if self.feedback_and_support_url is None and "feedback_and_support_url" in self.model_fields_set:
            _dict['feedbackAndSupportUrl'] = None

        # set to None if buy_url (nullable) is None
        # and model_fields_set contains the field
        if self.buy_url is None and "buy_url" in self.model_fields_set:
            _dict['buyUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "salesEmail": obj.get("salesEmail"),
            "feedbackAndSupportUrl": obj.get("feedbackAndSupportUrl"),
            "buyUrl": obj.get("buyUrl"),
            "standalone": obj.get("standalone"),
            "currentLicense": CurrentLicenseInfo.from_dict(obj["currentLicense"]) if obj.get("currentLicense") is not None else None,
            "max": obj.get("max")
        })
        return _obj


