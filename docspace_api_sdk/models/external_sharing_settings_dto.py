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
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ExternalSharingSettingsDto(BaseModel):
    """
    The Access Control external sharing settings.
    """ # noqa: E501
    external_share: Optional[StrictBool] = Field(default=None, description="Specifies whether external (public) link creation is allowed.", alias="externalShare")
    default_share_link_internal: Optional[StrictBool] = Field(default=None, description="Specifies the default sharing link type: true = DocSpace users only, false = Anyone with the link.", alias="defaultShareLinkInternal")
    external_share_apply_to_documents: Optional[StrictBool] = Field(default=None, description="When external sharing is restricted, specifies whether the restriction applies to the My Documents section.", alias="externalShareApplyToDocuments")
    external_share_apply_to_rooms: Optional[StrictBool] = Field(default=None, description="When external sharing is restricted, specifies whether the restriction applies to the Rooms section.", alias="externalShareApplyToRooms")
    block_existing_links_on_restrict: Optional[StrictBool] = Field(default=None, description="When external sharing is restricted, specifies whether existing public links are blocked immediately.", alias="blockExistingLinksOnRestrict")
    __properties: ClassVar[List[str]] = ["externalShare", "defaultShareLinkInternal", "externalShareApplyToDocuments", "externalShareApplyToRooms", "blockExistingLinksOnRestrict"]

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
        """Create an instance of ExternalSharingSettingsDto from a JSON string"""
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
        """Create an instance of ExternalSharingSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "externalShare": obj.get("externalShare"),
            "defaultShareLinkInternal": obj.get("defaultShareLinkInternal"),
            "externalShareApplyToDocuments": obj.get("externalShareApplyToDocuments"),
            "externalShareApplyToRooms": obj.get("externalShareApplyToRooms"),
            "blockExistingLinksOnRestrict": obj.get("blockExistingLinksOnRestrict")
        })
        return _obj


