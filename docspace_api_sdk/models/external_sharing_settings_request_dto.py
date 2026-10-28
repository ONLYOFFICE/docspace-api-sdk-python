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

class ExternalSharingSettingsRequestDto(BaseModel):
    """
    The complete external sharing policy of the portal. Every field is written, so an omitted one is stored as  false.
    """ # noqa: E501
    external_share: Optional[StrictBool] = Field(default=None, description="Whether links that open a file or a room without a portal account may be created at all. This is the master  switch of the policy: while it is false the portal keeps the default link type internal, turns sharing on  social networks off, and applies the three restriction fields below.", alias="externalShare", json_schema_extra={"examples": [True]})
    default_share_link_internal: Optional[StrictBool] = Field(default=None, description="The kind of link offered first when a new one is created: true offers a link only accounts of this portal can  open, false one that anyone holding it can open. The portal keeps it at true while external sharing is  switched off.", alias="defaultShareLinkInternal", json_schema_extra={"examples": [False]})
    external_share_apply_to_documents: Optional[StrictBool] = Field(default=None, description="Whether the restriction reaches personal documents: with true, no external link can be created for an entry in  the caller's own documents while external sharing is off. It has no effect while external sharing is allowed.", alias="externalShareApplyToDocuments", json_schema_extra={"examples": [True]})
    external_share_apply_to_rooms: Optional[StrictBool] = Field(default=None, description="Whether the restriction reaches rooms: with true, no external link can be created for a room or its content  while external sharing is off, and a new room cannot be made public. It has no effect while external sharing  is allowed.", alias="externalShareApplyToRooms", json_schema_extra={"examples": [True]})
    block_existing_links_on_restrict: Optional[StrictBool] = Field(default=None, description="What happens to the links that already exist once external sharing is switched off: with true they stop  opening for the sections named above, with false they keep working and only new ones are refused. This is the  field that changes access to data that is already shared.", alias="blockExistingLinksOnRestrict", json_schema_extra={"examples": [True]})
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
        """Create an instance of ExternalSharingSettingsRequestDto from a JSON string"""
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
        """Create an instance of ExternalSharingSettingsRequestDto from a dict"""
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


