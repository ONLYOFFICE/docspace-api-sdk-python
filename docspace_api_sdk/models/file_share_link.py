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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.link_type import LinkType
from typing import Optional, Set
from typing_extensions import Self

class FileShareLink(BaseModel):
    """
    A sharing link of a file, a folder or a room, with everything set on it.
    """ # noqa: E501
    id: Optional[UUID] = Field(default=None, description="The identifier of the link, the one to send back as `linkId` to change or delete it.", json_schema_extra={"examples": ["9a2c1b3e-6d47-4f10-9b52-ac7d3e5f0812"]})
    title: Optional[StrictStr] = Field(default=None, description="The name the link is listed under, which its author is free to choose and to leave empty.", json_schema_extra={"examples": ["Shared document"]})
    share_link: Optional[StrictStr] = Field(default=None, description="The shortened address to hand out. Opening it is what turns the link into access; the address stays the same  while the link exists.", alias="shareLink", json_schema_extra={"examples": ["https://portal.example.com/s/a1b2c3d4"]})
    expiration_date: Optional[ApiDateTime] = Field(default=None, description="The moment the link stops working, written with the offset of the portal time zone. Null when the link was  left without an end.", alias="expirationDate")
    link_type: Optional[LinkType] = Field(default=None, description="Which of the two jobs the link does: letting somebody into the room as a member, or handing out the entry  itself. The counters of uses are filled in for the first kind only.", alias="linkType")
    password: Optional[StrictStr] = Field(default=None, description="The password a visitor has to send before the link resolves, readable only by those who may manage the link.  Empty when the link asks for none.", json_schema_extra={"examples": ["S3cretPhrase"]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Whether visitors coming through this link may only read the entry in the editor and not download or print it.", alias="denyDownload", json_schema_extra={"examples": [False]})
    is_expired: Optional[StrictBool] = Field(default=None, description="Whether the moment in `expirationDate` has already passed, which leaves the link in place but refuses  everybody who opens it.", alias="isExpired", json_schema_extra={"examples": [False]})
    primary: Optional[StrictBool] = Field(default=None, description="Whether this is the one link the entry always keeps: a public or a form-filling room is given it at creation,  and deleting it there only makes a new one.", json_schema_extra={"examples": [True]})
    internal: Optional[StrictBool] = Field(default=None, description="Whether the visitor has to sign in to the portal before the link resolves, as opposed to it being open to  anybody who has the address.", json_schema_extra={"examples": [False]})
    request_token: Optional[StrictStr] = Field(default=None, description="The key that stands for this link in the calls that resolve it, such as `GET api/2.0/files/share/{key}`. It is  filled in for links that hand out the entry, and empty for the ones that invite into a room.", alias="requestToken", json_schema_extra={"examples": ["gg9J4mBW7pW9Wk0HqQoQ9L2mS1x6bK8vTnQ0aZ3"]})
    max_use_count: Optional[StrictInt] = Field(default=None, description="How many accounts may still join the room through this invitation link in total. Null on a link that hands out  the entry, where nothing is counted.", alias="maxUseCount", json_schema_extra={"examples": [10]})
    current_use_count: Optional[StrictInt] = Field(default=None, description="How many accounts have already joined through this invitation link. Once it reaches `maxUseCount` the link  stops letting anybody else in. Null on a link that hands out the entry.", alias="currentUseCount", json_schema_extra={"examples": [5]})
    __properties: ClassVar[List[str]] = ["id", "title", "shareLink", "expirationDate", "linkType", "password", "denyDownload", "isExpired", "primary", "internal", "requestToken", "maxUseCount", "currentUseCount"]

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
        """Create an instance of FileShareLink from a JSON string"""
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

        # set to None if share_link (nullable) is None
        # and model_fields_set contains the field
        if self.share_link is None and "share_link" in self.model_fields_set:
            _dict['shareLink'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if deny_download (nullable) is None
        # and model_fields_set contains the field
        if self.deny_download is None and "deny_download" in self.model_fields_set:
            _dict['denyDownload'] = None

        # set to None if is_expired (nullable) is None
        # and model_fields_set contains the field
        if self.is_expired is None and "is_expired" in self.model_fields_set:
            _dict['isExpired'] = None

        # set to None if internal (nullable) is None
        # and model_fields_set contains the field
        if self.internal is None and "internal" in self.model_fields_set:
            _dict['internal'] = None

        # set to None if request_token (nullable) is None
        # and model_fields_set contains the field
        if self.request_token is None and "request_token" in self.model_fields_set:
            _dict['requestToken'] = None

        # set to None if max_use_count (nullable) is None
        # and model_fields_set contains the field
        if self.max_use_count is None and "max_use_count" in self.model_fields_set:
            _dict['maxUseCount'] = None

        # set to None if current_use_count (nullable) is None
        # and model_fields_set contains the field
        if self.current_use_count is None and "current_use_count" in self.model_fields_set:
            _dict['currentUseCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileShareLink from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "shareLink": obj.get("shareLink"),
            "expirationDate": ApiDateTime.from_dict(obj["expirationDate"]) if obj.get("expirationDate") is not None else None,
            "linkType": obj.get("linkType"),
            "password": obj.get("password"),
            "denyDownload": obj.get("denyDownload"),
            "isExpired": obj.get("isExpired"),
            "primary": obj.get("primary"),
            "internal": obj.get("internal"),
            "requestToken": obj.get("requestToken"),
            "maxUseCount": obj.get("maxUseCount"),
            "currentUseCount": obj.get("currentUseCount")
        })
        return _obj


