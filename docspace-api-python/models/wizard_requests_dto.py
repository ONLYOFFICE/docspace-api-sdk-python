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

class WizardRequestsDto(BaseModel):
    """
    The request parameters for initial configuration of the setup wizard.
    """ # noqa: E501
    email: Optional[StrictStr] = Field(description="The user's email address for authentication and communication.")
    password_hash: Optional[StrictStr] = Field(description="The hashed representation of the user's password.", alias="passwordHash")
    lng: Optional[StrictStr] = Field(default=None, description="The user's preferred interface language code.")
    time_zone: Optional[StrictStr] = Field(default=None, description="The user's time zone identifier.", alias="timeZone")
    ami_id: Optional[StrictStr] = Field(default=None, description="The Amazon Machine Image (AMI) identifier.", alias="amiId")
    subscribe_from_site: Optional[StrictBool] = Field(default=None, description="Specifies whether the user opted in for site communications.", alias="subscribeFromSite")
    __properties: ClassVar[List[str]] = ["email", "passwordHash", "lng", "timeZone", "amiId", "subscribeFromSite"]

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
        """Create an instance of WizardRequestsDto from a JSON string"""
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
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if password_hash (nullable) is None
        # and model_fields_set contains the field
        if self.password_hash is None and "password_hash" in self.model_fields_set:
            _dict['passwordHash'] = None

        # set to None if lng (nullable) is None
        # and model_fields_set contains the field
        if self.lng is None and "lng" in self.model_fields_set:
            _dict['lng'] = None

        # set to None if time_zone (nullable) is None
        # and model_fields_set contains the field
        if self.time_zone is None and "time_zone" in self.model_fields_set:
            _dict['timeZone'] = None

        # set to None if ami_id (nullable) is None
        # and model_fields_set contains the field
        if self.ami_id is None and "ami_id" in self.model_fields_set:
            _dict['amiId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WizardRequestsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "passwordHash": obj.get("passwordHash"),
            "lng": obj.get("lng"),
            "timeZone": obj.get("timeZone"),
            "amiId": obj.get("amiId"),
            "subscribeFromSite": obj.get("subscribeFromSite")
        })
        return _obj


