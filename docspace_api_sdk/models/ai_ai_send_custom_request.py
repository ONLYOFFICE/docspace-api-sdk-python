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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_ai_action_args import AiAiActionArgs
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from typing import Optional, Set
from typing_extensions import Self

class AiAiSendCustomRequest(BaseModel):
    """
    AiAiSendCustomRequest
    """ # noqa: E501
    is_stream: StrictBool = Field(description="Stream the reply (ndjson) when true, else return a single message.", alias="isStream")
    system_prompt: StrictStr = Field(description="Caller-supplied system prompt for this one-turn call.", alias="systemPrompt")
    user_message: AiThreadMessageLike = Field(alias="userMessage")
    action_args: Optional[AiAiActionArgs] = Field(default=None, description="Per-request engine options: extra tools, reasoning, prompt override.", alias="actionArgs")
    __properties: ClassVar[List[str]] = ["isStream", "systemPrompt", "userMessage", "actionArgs"]

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
        """Create an instance of AiAiSendCustomRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_message
        if self.user_message:
            _dict['userMessage'] = self.user_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of action_args
        if self.action_args:
            _dict['actionArgs'] = self.action_args.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiAiSendCustomRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isStream": obj.get("isStream"),
            "systemPrompt": obj.get("systemPrompt"),
            "userMessage": AiThreadMessageLike.from_dict(obj["userMessage"]) if obj.get("userMessage") is not None else None,
            "actionArgs": AiAiActionArgs.from_dict(obj["actionArgs"]) if obj.get("actionArgs") is not None else None
        })
        return _obj


