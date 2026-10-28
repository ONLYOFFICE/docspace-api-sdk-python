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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from docspace_api_sdk.models.ai_open_ai_chat_completion_chunk import AiOpenAIChatCompletionChunk
from docspace_api_sdk.models.ai_open_ai_stream_error import AiOpenAIStreamError
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

AIOPENAISTREAMCHUNK_ANY_OF_SCHEMAS = ["AiOpenAIChatCompletionChunk", "AiOpenAIStreamError"]

class AiOpenAIStreamChunk(BaseModel):
    """
    A chunk or the terminal error envelope emitted on a failed stream.
    """

    # data type: AiOpenAIChatCompletionChunk
    anyof_schema_1_validator: Optional[AiOpenAIChatCompletionChunk] = None
    # data type: AiOpenAIStreamError
    anyof_schema_2_validator: Optional[AiOpenAIStreamError] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[AiOpenAIChatCompletionChunk, AiOpenAIStreamError]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "AiOpenAIChatCompletionChunk", "AiOpenAIStreamError" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = AiOpenAIStreamChunk.model_construct()
        error_messages = []
        # validate data type: AiOpenAIChatCompletionChunk
        if not isinstance(v, AiOpenAIChatCompletionChunk):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AiOpenAIChatCompletionChunk`")
        else:
            return v

        # validate data type: AiOpenAIStreamError
        if not isinstance(v, AiOpenAIStreamError):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AiOpenAIStreamError`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in AiOpenAIStreamChunk with anyOf schemas: AiOpenAIChatCompletionChunk, AiOpenAIStreamError. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[AiOpenAIChatCompletionChunk] = None
        try:
            instance.actual_instance = AiOpenAIChatCompletionChunk.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[AiOpenAIStreamError] = None
        try:
            instance.actual_instance = AiOpenAIStreamError.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AiOpenAIStreamChunk with anyOf schemas: AiOpenAIChatCompletionChunk, AiOpenAIStreamError. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AiOpenAIChatCompletionChunk, AiOpenAIStreamError]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


