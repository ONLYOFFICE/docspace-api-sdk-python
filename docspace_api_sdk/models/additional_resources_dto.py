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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AdditionalResourcesDto(BaseModel):
    """
    Which of the ONLYOFFICE help and community entries the interface may offer, installation-wide, in the shape the  reset of these flags returns.
    """ # noqa: E501
    start_docs_enabled: Optional[StrictBool] = Field(default=None, description="Whether the sample documents that ONLYOFFICE ships may be placed in a new user's Documents. Unlike the link  flags below it depends on nothing that has to be configured, so its built-in value is always `true`.", alias="startDocsEnabled", json_schema_extra={"examples": [True]})
    help_center_enabled: Optional[StrictBool] = Field(default=None, description="Whether the interface may offer the Help Center entry. It is `false` both when the entry was switched off  for the installation and when the installation configures no Help Center address at all; the addresses  themselves are not part of this answer and arrive in `externalResources` of `GET api/2.0/settings`.", alias="helpCenterEnabled", json_schema_extra={"examples": [True]})
    feedback_and_support_enabled: Optional[StrictBool] = Field(default=None, description="Whether the interface may offer the Feedback and Support entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="feedbackAndSupportEnabled", json_schema_extra={"examples": [True]})
    user_forum_enabled: Optional[StrictBool] = Field(default=None, description="Whether the interface may offer the user forum entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="userForumEnabled", json_schema_extra={"examples": [True]})
    video_guides_enabled: Optional[StrictBool] = Field(default=None, description="Whether the interface may offer the Video Guides entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="videoGuidesEnabled", json_schema_extra={"examples": [True]})
    license_agreements_enabled: Optional[StrictBool] = Field(default=None, description="Whether the interface may offer the License Agreements entry, `false` for the same two reasons as  `helpCenterEnabled`.", alias="licenseAgreementsEnabled", json_schema_extra={"examples": [True]})
    last_modified: Optional[datetime] = Field(default=None, description="When these flags were last stored. Flags that were never stored report the moment they were read, and the  answer of the reset operation reports `0001-01-01T00:00:00`.", alias="lastModified", json_schema_extra={"examples": ["2026-01-01T10:00:00"]})
    __properties: ClassVar[List[str]] = ["startDocsEnabled", "helpCenterEnabled", "feedbackAndSupportEnabled", "userForumEnabled", "videoGuidesEnabled", "licenseAgreementsEnabled", "lastModified"]

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
        """Create an instance of AdditionalResourcesDto from a JSON string"""
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
        """Create an instance of AdditionalResourcesDto from a dict"""
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
            "lastModified": obj.get("lastModified")
        })
        return _obj


