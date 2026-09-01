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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_profile import AiProfile
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from docspace_api_sdk.models.ai_threads_open_or_create_request_entity_meta import AiThreadsOpenOrCreateRequestEntityMeta
from typing import Optional, Set
from typing_extensions import Self

class AiThreadsOpenOrCreateRequest(BaseModel):
    """
    AiThreadsOpenOrCreateRequest
    """ # noqa: E501
    thread_id: Optional[StrictStr] = Field(default=None, alias="threadId")
    profile: AiProfile = Field(description="Profile the title generation runs on.")
    profile_id: StrictStr = Field(alias="profileId")
    first_message: AiThreadMessageLike = Field(description="First user message a fresh thread derives its title from.", alias="firstMessage")
    entity_id: Optional[StrictStr] = Field(default=None, description="Opaque scope token persisted on a freshly created thread.", alias="entityId")
    entity_meta: Optional[AiThreadsOpenOrCreateRequestEntityMeta] = Field(default=None, alias="entityMeta")
    __properties: ClassVar[List[str]] = ["threadId", "profile", "profileId", "firstMessage", "entityId", "entityMeta"]

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
        """Create an instance of AiThreadsOpenOrCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of first_message
        if self.first_message:
            _dict['firstMessage'] = self.first_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity_meta
        if self.entity_meta:
            _dict['entityMeta'] = self.entity_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiThreadsOpenOrCreateRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "threadId": obj.get("threadId"),
            "profile": AiProfile.from_dict(obj["profile"]) if obj.get("profile") is not None else None,
            "profileId": obj.get("profileId"),
            "firstMessage": AiThreadMessageLike.from_dict(obj["firstMessage"]) if obj.get("firstMessage") is not None else None,
            "entityId": obj.get("entityId"),
            "entityMeta": AiThreadsOpenOrCreateRequestEntityMeta.from_dict(obj["entityMeta"]) if obj.get("entityMeta") is not None else None
        })
        return _obj


