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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.file_share import FileShare
from docspace_api_sdk.models.link_type import LinkType
from typing import Optional, Set
from typing_extensions import Self

class RoomLinkRequest(BaseModel):
    """
    The link of a room to create, change or revoke.
    """ # noqa: E501
    link_id: Optional[UUID] = Field(default=None, description="Which link to change, taken from `GET api/2.0/files/rooms/{id}/links`. Leaving it out creates a link, and an  identifier the room does not know creates a link carrying that identifier.", alias="linkId", json_schema_extra={"examples": ["b3f1c8de-5a64-4d1e-9f27-6c0a8d5b7e41"]})
    access: Optional[FileShare] = Field(default=None, description="What whoever opens the link may do in the room. The value 0 revokes the link instead of changing it, and the  levels a room accepts depend on its kind.")
    expiration_date: Optional[ApiDateTime] = Field(default=None, description="When the link stops working, written with the offset of the portal time zone. A date already past is dropped  silently for an external link and refused for an invitation link, and a date further ahead than the portal  allows is refused as well; leaving it out means the link does not expire.", alias="expirationDate")
    internal: Optional[StrictBool] = Field(default=None, description="Whether the external link works only for people already signed in to the portal. With it off the link opens  the room for anyone who has the address, subject to the password.", json_schema_extra={"examples": [False]})
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The name the link is shown under in the room. An empty value is accepted and the portal names the link itself,  so the answer is what tells the caller the name in use.", json_schema_extra={"examples": ["Read-only access for auditors"]})
    link_type: Optional[LinkType] = Field(default=None, description="Which kind of link to create: an invitation link makes whoever opens it a member of the room, while an  external link opens the room without an account. It is fixed when the link is created and is ignored on later  changes.", alias="linkType")
    password: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The password an external link asks for before it opens the room. An empty value leaves the link open to anyone  who has the address, and the password is never returned when links are listed.", json_schema_extra={"examples": ["S3cret-Phrase"]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Whether people arriving through the link are stopped from downloading and printing what they open. They can  still read the documents in the editor.", alias="denyDownload", json_schema_extra={"examples": [False]})
    max_use_count: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(default=None, description="How many people an invitation link may still let in before it stops working. A value below the number of  people who already used it is refused, and leaving it out puts no ceiling on the link.", alias="maxUseCount", json_schema_extra={"examples": [25]})
    current_use_count: Optional[StrictInt] = Field(default=None, description="How many people have already joined through this invitation link. The value is kept by the portal: it is  reported back when links are listed and anything sent here is ignored.", alias="currentUseCount", json_schema_extra={"examples": [0]})
    __properties: ClassVar[List[str]] = ["linkId", "access", "expirationDate", "internal", "title", "linkType", "password", "denyDownload", "maxUseCount", "currentUseCount"]

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
        """Create an instance of RoomLinkRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of expiration_date
        if self.expiration_date:
            _dict['expirationDate'] = self.expiration_date.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if max_use_count (nullable) is None
        # and model_fields_set contains the field
        if self.max_use_count is None and "max_use_count" in self.model_fields_set:
            _dict['maxUseCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomLinkRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkId": obj.get("linkId"),
            "access": obj.get("access"),
            "expirationDate": ApiDateTime.from_dict(obj["expirationDate"]) if obj.get("expirationDate") is not None else None,
            "internal": obj.get("internal"),
            "title": obj.get("title"),
            "linkType": obj.get("linkType"),
            "password": obj.get("password"),
            "denyDownload": obj.get("denyDownload"),
            "maxUseCount": obj.get("maxUseCount"),
            "currentUseCount": obj.get("currentUseCount")
        })
        return _obj


