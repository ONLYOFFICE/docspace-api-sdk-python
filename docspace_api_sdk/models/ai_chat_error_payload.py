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
from typing import Optional, Set
from typing_extensions import Self

class AiChatErrorPayload(BaseModel):
    """
    Why a round failed or stopped early, as the message status and the stream report it: a stable `code`, a message safe to show the user, and the cause when there is one.
    """ # noqa: E501
    code: StrictStr = Field(description="Stable machine-readable code. One of a canonical set — `auth`, `model_not_found`, `rate_limit`, `timeout`, `network`, `bad_request`, `server`, `not_found`, `insufficient_funds`, `aborted`, `unknown` — or a provider-specific string when the SDK supplies one verbatim.", json_schema_extra={"examples": ["rate_limit"]})
    message: StrictStr = Field(description="Human-readable, end-user-safe message.", json_schema_extra={"examples": ["The provider is rate limiting requests."]})
    cause: Optional[AiChatErrorPayload] = Field(default=None, description="Optional nested cause, normalized through the same helper.")
    __properties: ClassVar[List[str]] = ["code", "message", "cause"]

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
        """Create an instance of AiChatErrorPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cause
        if self.cause:
            _dict['cause'] = self.cause.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiChatErrorPayload from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "message": obj.get("message"),
            "cause": AiChatErrorPayload.from_dict(obj["cause"]) if obj.get("cause") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
AiChatErrorPayload.model_rebuild(raise_errors=False)

