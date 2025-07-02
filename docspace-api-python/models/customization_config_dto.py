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
from docspace-api-python.models.anonymous_config_dto import AnonymousConfigDto
from docspace-api-python.models.customer_config_dto import CustomerConfigDto
from docspace-api-python.models.feedback_config import FeedbackConfig
from docspace-api-python.models.goback_config import GobackConfig
from docspace-api-python.models.logo_config_dto import LogoConfigDto
from docspace-api-python.models.start_filling_form import StartFillingForm
from docspace-api-python.models.submit_form import SubmitForm
from typing import Optional, Set
from typing_extensions import Self

class CustomizationConfigDto(BaseModel):
    """
    The customization config parameters.
    """ # noqa: E501
    about: Optional[StrictBool] = Field(default=None, description="Specifies if the customization is about.")
    customer: Optional[CustomerConfigDto] = None
    anonymous: Optional[AnonymousConfigDto] = None
    feedback: Optional[FeedbackConfig] = None
    forcesave: Optional[StrictBool] = Field(default=None, description="Specifies if the customization should be force saved.")
    goback: Optional[GobackConfig] = None
    logo: Optional[LogoConfigDto] = None
    mention_share: Optional[StrictBool] = Field(default=None, description="Specifies if the share should be mentioned.", alias="mentionShare")
    review_display: Optional[StrictStr] = Field(default=None, description="The review display of the customization.", alias="reviewDisplay")
    submit_form: Optional[SubmitForm] = Field(default=None, alias="submitForm")
    start_filling_form: Optional[StartFillingForm] = Field(default=None, alias="startFillingForm")
    __properties: ClassVar[List[str]] = ["about", "customer", "anonymous", "feedback", "forcesave", "goback", "logo", "mentionShare", "reviewDisplay", "submitForm", "startFillingForm"]

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
        """Create an instance of CustomizationConfigDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anonymous
        if self.anonymous:
            _dict['anonymous'] = self.anonymous.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feedback
        if self.feedback:
            _dict['feedback'] = self.feedback.to_dict()
        # override the default output from pydantic by calling `to_dict()` of goback
        if self.goback:
            _dict['goback'] = self.goback.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of submit_form
        if self.submit_form:
            _dict['submitForm'] = self.submit_form.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_filling_form
        if self.start_filling_form:
            _dict['startFillingForm'] = self.start_filling_form.to_dict()
        # set to None if forcesave (nullable) is None
        # and model_fields_set contains the field
        if self.forcesave is None and "forcesave" in self.model_fields_set:
            _dict['forcesave'] = None

        # set to None if review_display (nullable) is None
        # and model_fields_set contains the field
        if self.review_display is None and "review_display" in self.model_fields_set:
            _dict['reviewDisplay'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomizationConfigDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "about": obj.get("about"),
            "customer": CustomerConfigDto.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "anonymous": AnonymousConfigDto.from_dict(obj["anonymous"]) if obj.get("anonymous") is not None else None,
            "feedback": FeedbackConfig.from_dict(obj["feedback"]) if obj.get("feedback") is not None else None,
            "forcesave": obj.get("forcesave"),
            "goback": GobackConfig.from_dict(obj["goback"]) if obj.get("goback") is not None else None,
            "logo": LogoConfigDto.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "mentionShare": obj.get("mentionShare"),
            "reviewDisplay": obj.get("reviewDisplay"),
            "submitForm": SubmitForm.from_dict(obj["submitForm"]) if obj.get("submitForm") is not None else None,
            "startFillingForm": StartFillingForm.from_dict(obj["startFillingForm"]) if obj.get("startFillingForm") is not None else None
        })
        return _obj


