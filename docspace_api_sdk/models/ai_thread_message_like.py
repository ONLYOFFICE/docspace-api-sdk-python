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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_thread_message_like_content import AiThreadMessageLikeContent
from docspace_api_sdk.models.ai_thread_message_like_status import AiThreadMessageLikeStatus
from typing import Optional, Set
from typing_extensions import Self

class AiThreadMessageLike(BaseModel):
    """
    AiThreadMessageLike
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Storage-assigned message id (absent on inbound drafts).")
    role: StrictStr = Field(description="Message author role.")
    content: AiThreadMessageLikeContent
    created_at: Optional[StrictStr] = Field(default=None, description="Creation timestamp, ISO-8601 on the wire.", alias="createdAt")
    status: Optional[AiThreadMessageLikeStatus] = None
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Arbitrary per-message metadata.")
    attachments: Optional[List[Dict[str, Any]]] = Field(default=None, description="Attachments linked to the message.")
    __properties: ClassVar[List[str]] = ["id", "role", "content", "createdAt", "status", "metadata", "attachments"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['user', 'assistant', 'system']):
            raise ValueError("must be one of enum values ('user', 'assistant', 'system')")
        return value

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
        """Create an instance of AiThreadMessageLike from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiThreadMessageLike from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "role": obj.get("role"),
            "content": AiThreadMessageLikeContent.from_dict(obj["content"]) if obj.get("content") is not None else None,
            "createdAt": obj.get("createdAt"),
            "status": AiThreadMessageLikeStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "metadata": obj.get("metadata"),
            "attachments": obj.get("attachments")
        })
        return _obj


