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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.continue_chat_body_files_inner import ContinueChatBodyFilesInner
from typing import Optional, Set
from typing_extensions import Self

class StartNewChatBody(BaseModel):
    """
    Parameters for starting a new AI chat session.
    """ # noqa: E501
    message: Optional[StrictStr] = Field(description="The initial user message to send to the AI assistant.")
    context_folder_id: Optional[StrictInt] = Field(default=None, description="The optional collection of file identifiers to attach as context for the AI model.", alias="contextFolderId")
    files: Optional[List[ContinueChatBodyFilesInner]] = Field(default=None, description="The list of attached files.")
    __properties: ClassVar[List[str]] = ["message", "contextFolderId", "files"]

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
        """Create an instance of StartNewChatBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item_files in self.files:
                if _item_files:
                    _items.append(_item_files.to_dict())
            _dict['files'] = _items
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if context_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.context_folder_id is None and "context_folder_id" in self.model_fields_set:
            _dict['contextFolderId'] = None

        # set to None if files (nullable) is None
        # and model_fields_set contains the field
        if self.files is None and "files" in self.model_fields_set:
            _dict['files'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StartNewChatBody from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "contextFolderId": obj.get("contextFolderId"),
            "files": [ContinueChatBodyFilesInner.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None
        })
        return _obj


