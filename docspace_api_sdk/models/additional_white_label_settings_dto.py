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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class AdditionalWhiteLabelSettingsDto(BaseModel):
    """
    Which of the ONLYOFFICE help and community entries the interface may offer, installation-wide.
    """ # noqa: E501
    start_docs_enabled: StrictBool = Field(description="Whether the sample documents that ONLYOFFICE ships may be placed in a new user's Documents. Unlike the link  flags below it depends on nothing that has to be configured, so its built-in value is always `true`.", alias="startDocsEnabled", json_schema_extra={"examples": [True]})
    help_center_enabled: StrictBool = Field(description="Whether the interface may offer the Help Center entry. It is `false` both when the entry was switched off  for the installation and when the installation configures no Help Center address at all; the addresses  themselves are not part of this answer and arrive in `externalResources` of `GET api/2.0/settings`.", alias="helpCenterEnabled", json_schema_extra={"examples": [True]})
    feedback_and_support_enabled: StrictBool = Field(description="Whether the interface may offer the Feedback and Support entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="feedbackAndSupportEnabled", json_schema_extra={"examples": [True]})
    user_forum_enabled: StrictBool = Field(description="Whether the interface may offer the user forum entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="userForumEnabled", json_schema_extra={"examples": [True]})
    video_guides_enabled: StrictBool = Field(description="Whether the interface may offer the Video Guides entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="videoGuidesEnabled", json_schema_extra={"examples": [True]})
    license_agreements_enabled: StrictBool = Field(description="Whether the interface may offer the License Agreements entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="licenseAgreementsEnabled", json_schema_extra={"examples": [True]})
    is_default: StrictBool = Field(description="Whether all six flags still hold the values the installation starts out with. It turns `false` as soon as  one of them is saved differently and `true` again after `DELETE api/2.0/settings/rebranding/additional`.  Because a link flag starts out off when no address is configured for it, `true` does not mean every entry  is on.", alias="isDefault", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["startDocsEnabled", "helpCenterEnabled", "feedbackAndSupportEnabled", "userForumEnabled", "videoGuidesEnabled", "licenseAgreementsEnabled", "isDefault"]

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
        """Create an instance of AdditionalWhiteLabelSettingsDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdditionalWhiteLabelSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startDocsEnabled": obj.get("startDocsEnabled"),
            "helpCenterEnabled": obj.get("helpCenterEnabled"),
            "feedbackAndSupportEnabled": obj.get("feedbackAndSupportEnabled"),
            "userForumEnabled": obj.get("userForumEnabled"),
            "videoGuidesEnabled": obj.get("videoGuidesEnabled"),
            "licenseAgreementsEnabled": obj.get("licenseAgreementsEnabled"),
            "isDefault": obj.get("isDefault")
        })
        return _obj


