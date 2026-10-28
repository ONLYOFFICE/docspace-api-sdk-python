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

class CompanyWhiteLabelSettingsDto(BaseModel):
    """
    The vendor details the About page and the notification letters print, shared by the whole installation.
    """ # noqa: E501
    company_name: Optional[StrictStr] = Field(description="The vendor name the About page shows and the letters sign off with. Until details are saved it holds  whatever the installation ships as its built-in vendor, and it is empty on an installation that ships none.", alias="companyName", json_schema_extra={"examples": ["My Own Corporation"]})
    site: Optional[StrictStr] = Field(description="The address the vendor name links to, as an absolute URL with its scheme. Empty under the same conditions  as `companyName`.", json_schema_extra={"examples": ["https://www.example.com"]})
    email: Optional[StrictStr] = Field(description="The mailbox the About page offers for reaching the vendor. It is not the portal's own support address, and  it is empty under the same conditions as `companyName`.", json_schema_extra={"examples": ["contact@example.com"]})
    address: Optional[StrictStr] = Field(description="The postal address of the vendor as one free-form line, in the shape it was saved in - no structure is  imposed on it.", json_schema_extra={"examples": ["123 Business St, New York, NY 10001"]})
    phone: Optional[StrictStr] = Field(description="The telephone number of the vendor in the shape it was saved in, with no dialling format enforced.", json_schema_extra={"examples": ["+1-800-555-0123"]})
    is_licensor: StrictBool = Field(description="Whether these details are those of the licensor of the product itself rather than of a reseller. Saving  through `POST api/2.0/settings/rebranding/company` always clears it, so only details that came with the  installation can report `true`.", alias="isLicensor", json_schema_extra={"examples": [False]})
    hide_about: StrictBool = Field(description="Whether the About page is hidden from the interface. A plan that does not include branding cannot switch it  on: the value is stored as `false` in that case, so it can come back different from what was saved.", alias="hideAbout", json_schema_extra={"examples": [False]})
    is_default: StrictBool = Field(description="Whether every field above still matches the installation's built-in vendor details. It turns `false` as  soon as one of them is saved differently and `true` again after  `DELETE api/2.0/settings/rebranding/company`.", alias="isDefault", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["companyName", "site", "email", "address", "phone", "isLicensor", "hideAbout", "isDefault"]

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
        """Create an instance of CompanyWhiteLabelSettingsDto from a JSON string"""
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
        # set to None if company_name (nullable) is None
        # and model_fields_set contains the field
        if self.company_name is None and "company_name" in self.model_fields_set:
            _dict['companyName'] = None

        # set to None if site (nullable) is None
        # and model_fields_set contains the field
        if self.site is None and "site" in self.model_fields_set:
            _dict['site'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CompanyWhiteLabelSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "companyName": obj.get("companyName"),
            "site": obj.get("site"),
            "email": obj.get("email"),
            "address": obj.get("address"),
            "phone": obj.get("phone"),
            "isLicensor": obj.get("isLicensor"),
            "hideAbout": obj.get("hideAbout"),
            "isDefault": obj.get("isDefault")
        })
        return _obj


