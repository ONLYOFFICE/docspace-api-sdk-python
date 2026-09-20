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
from typing_extensions import Annotated
from docspace_api_sdk.models.duplicate_request_dto_all_of_file_ids import DuplicateRequestDtoAllOfFileIds
from docspace_api_sdk.models.file_share_params import FileShareParams
from typing import Optional, Set
from typing_extensions import Self

class SecurityInfoRequestDto(BaseModel):
    """
    The entries whose sharing rights are being changed, and the rights to apply to them.
    """ # noqa: E501
    folder_ids: Optional[List[DuplicateRequestDtoAllOfFileIds]] = Field(default=None, description="The folders and rooms whose rights are being changed, identified as a listing operation returns them - a  number on the portal, a string on a connected third-party account.", alias="folderIds", json_schema_extra={"examples": [[1, 2, 3]]})
    file_ids: Optional[List[DuplicateRequestDtoAllOfFileIds]] = Field(default=None, description="The files whose rights are being changed, identified as a listing operation returns them - a number on the  portal, a string on a connected third-party account.", alias="fileIds", json_schema_extra={"examples": [[7, 8]]})
    share: Optional[List[FileShareParams]] = Field(default=None, description="One record per account or group whose rights are being set, each naming the subject and the level it gets on  all of the listed entries; a level of `None` takes the access away. An empty collection makes the call change  nothing.", json_schema_extra={"examples": [[{"access": 2, "shareTo": "9924256a-739c-462b-af15-e652a3b1b6eb"}]]})
    notify: Optional[StrictBool] = Field(default=None, description="Set to true to have every account named in `share` emailed about the access it just received; false changes  the rights without telling anyone.", json_schema_extra={"examples": [True]})
    sharing_message: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The text put into that email, ignored while `notify` is false. Markup is stripped before sending, so only the  plain text of the value survives.", alias="sharingMessage", json_schema_extra={"examples": ["You have been granted access to the file"]})
    __properties: ClassVar[List[str]] = ["folderIds", "fileIds", "share", "notify", "sharingMessage"]

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
        """Create an instance of SecurityInfoRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in folder_ids (list)
        _items = []
        if self.folder_ids:
            for _item_folder_ids in self.folder_ids:
                if _item_folder_ids:
                    _items.append(_item_folder_ids.to_dict())
            _dict['folderIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in file_ids (list)
        _items = []
        if self.file_ids:
            for _item_file_ids in self.file_ids:
                if _item_file_ids:
                    _items.append(_item_file_ids.to_dict())
            _dict['fileIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in share (list)
        _items = []
        if self.share:
            for _item_share in self.share:
                if _item_share:
                    _items.append(_item_share.to_dict())
            _dict['share'] = _items
        # set to None if folder_ids (nullable) is None
        # and model_fields_set contains the field
        if self.folder_ids is None and "folder_ids" in self.model_fields_set:
            _dict['folderIds'] = None

        # set to None if file_ids (nullable) is None
        # and model_fields_set contains the field
        if self.file_ids is None and "file_ids" in self.model_fields_set:
            _dict['fileIds'] = None

        # set to None if share (nullable) is None
        # and model_fields_set contains the field
        if self.share is None and "share" in self.model_fields_set:
            _dict['share'] = None

        # set to None if sharing_message (nullable) is None
        # and model_fields_set contains the field
        if self.sharing_message is None and "sharing_message" in self.model_fields_set:
            _dict['sharingMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecurityInfoRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "folderIds": [DuplicateRequestDtoAllOfFileIds.from_dict(_item) for _item in obj["folderIds"]] if obj.get("folderIds") is not None else None,
            "fileIds": [DuplicateRequestDtoAllOfFileIds.from_dict(_item) for _item in obj["fileIds"]] if obj.get("fileIds") is not None else None,
            "share": [FileShareParams.from_dict(_item) for _item in obj["share"]] if obj.get("share") is not None else None,
            "notify": obj.get("notify"),
            "sharingMessage": obj.get("sharingMessage")
        })
        return _obj


