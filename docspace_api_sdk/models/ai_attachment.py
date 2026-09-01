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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.ai_attachment_form_keys_inner import AiAttachmentFormKeysInner
from typing import Optional, Set
from typing_extensions import Self

class AiAttachment(BaseModel):
    """
    Persistent record for a single attachment (file or image) referenced from a user message. Files carry extracted text in `content`; images carry base64 data in `base64`. Metadata (`title`, `path`, `type`) is always present for display purposes regardless of whether the heavy payload is loaded.
    """ # noqa: E501
    id: StrictStr = Field(description="Storage-assigned UUID.")
    kind: StrictStr = Field(description="file | image.")
    source: Optional[StrictStr] = Field(default=None, description="Origin of the attachment. `user` — uploaded by the user in the composer (the default when unset, for backward compatibility). `tool` — produced by a tool call (e.g. `generate_image`). Lets the integrator's adapter route or apply policies (separate bucket, quotas, TTL, CDN) per source.")
    title: StrictStr = Field(description="Display label (filename or user-visible title).")
    content: Optional[StrictStr] = Field(default=None, description="Extracted text for files.")
    var_base64: Optional[StrictStr] = Field(default=None, description="Base64 data URL for images.", alias="base64")
    path: Optional[StrictStr] = Field(default=None, description="Original host file path (for files).")
    type: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="ONLYOFFICE file type code (for files).")
    message_id: Optional[StrictStr] = Field(default=None, description="Owning message id once linked. Unset while the attachment is a draft.", alias="messageId")
    thread_id: Optional[StrictStr] = Field(default=None, description="Owning thread id once linked. Unset while the attachment is a draft.", alias="threadId")
    entity_id: Optional[StrictStr] = Field(default=None, description="Opaque scope token (entity / room) the attachment was created in. Drafts carry it so an entity switch keeps in-flight composer state isolated; once linked to a message the field is redundant with the thread's own entity binding.", alias="entityId")
    created_at: Union[StrictFloat, StrictInt] = Field(description="Storage-assigned creation timestamp.", alias="createdAt")
    can_analyze: Optional[StrictBool] = Field(default=None, description="Whether the attached form can be analyzed.", alias="canAnalyze")
    form_keys: Optional[List[AiAttachmentFormKeysInner]] = Field(default=None, description="Keys of the fields inside the form. `key` is the field identifier, `text` its human-readable label.", alias="formKeys")
    __properties: ClassVar[List[str]] = ["id", "kind", "source", "title", "content", "base64", "path", "type", "messageId", "threadId", "entityId", "createdAt", "canAnalyze", "formKeys"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['file', 'image']):
            raise ValueError("must be one of enum values ('file', 'image')")
        return value

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['user', 'tool']):
            raise ValueError("must be one of enum values ('user', 'tool')")
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
        """Create an instance of AiAttachment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in form_keys (list)
        _items = []
        if self.form_keys:
            for _item_form_keys in self.form_keys:
                if _item_form_keys:
                    _items.append(_item_form_keys.to_dict())
            _dict['formKeys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiAttachment from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "kind": obj.get("kind"),
            "source": obj.get("source"),
            "title": obj.get("title"),
            "content": obj.get("content"),
            "base64": obj.get("base64"),
            "path": obj.get("path"),
            "type": obj.get("type"),
            "messageId": obj.get("messageId"),
            "threadId": obj.get("threadId"),
            "entityId": obj.get("entityId"),
            "createdAt": obj.get("createdAt"),
            "canAnalyze": obj.get("canAnalyze"),
            "formKeys": [AiAttachmentFormKeysInner.from_dict(_item) for _item in obj["formKeys"]] if obj.get("formKeys") is not None else None
        })
        return _obj


