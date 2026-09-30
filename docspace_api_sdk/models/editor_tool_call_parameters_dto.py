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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from docspace_api_sdk.models.generate_docx_tool_call_parameters_dto import GenerateDocxToolCallParametersDto
from docspace_api_sdk.models.generate_form_tool_call_parameters_dto import GenerateFormToolCallParametersDto
from docspace_api_sdk.models.generate_presentation_tool_call_parameters_dto import GeneratePresentationToolCallParametersDto
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

EDITORTOOLCALLPARAMETERSDTO_ONE_OF_SCHEMAS = ["GenerateDocxToolCallParametersDto", "GenerateFormToolCallParametersDto", "GeneratePresentationToolCallParametersDto"]

class EditorToolCallParametersDto(BaseModel):
    """
    The editor tool call parameters.
    """
    # data type: GenerateDocxToolCallParametersDto
    oneof_schema_1_validator: Optional[GenerateDocxToolCallParametersDto] = Field(default=None, description="The generate docx tool call parameters.")
    # data type: GenerateFormToolCallParametersDto
    oneof_schema_2_validator: Optional[GenerateFormToolCallParametersDto] = Field(default=None, description="The generate form tool call parameters.")
    # data type: GeneratePresentationToolCallParametersDto
    oneof_schema_3_validator: Optional[GeneratePresentationToolCallParametersDto] = Field(default=None, description="The generate presentation tool call parameters.")
    actual_instance: Optional[Union[GenerateDocxToolCallParametersDto, GenerateFormToolCallParametersDto, GeneratePresentationToolCallParametersDto]] = None
    one_of_schemas: Set[str] = { "GenerateDocxToolCallParametersDto", "GenerateFormToolCallParametersDto", "GeneratePresentationToolCallParametersDto" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


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
    def actual_instance_must_validate_oneof(cls, v):
        instance = EditorToolCallParametersDto.model_construct()
        error_messages = []
        match = 0
        # validate data type: GenerateDocxToolCallParametersDto
        if not isinstance(v, GenerateDocxToolCallParametersDto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GenerateDocxToolCallParametersDto`")
        else:
            match += 1
        # validate data type: GenerateFormToolCallParametersDto
        if not isinstance(v, GenerateFormToolCallParametersDto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GenerateFormToolCallParametersDto`")
        else:
            match += 1
        # validate data type: GeneratePresentationToolCallParametersDto
        if not isinstance(v, GeneratePresentationToolCallParametersDto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GeneratePresentationToolCallParametersDto`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EditorToolCallParametersDto with oneOf schemas: GenerateDocxToolCallParametersDto, GenerateFormToolCallParametersDto, GeneratePresentationToolCallParametersDto. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EditorToolCallParametersDto with oneOf schemas: GenerateDocxToolCallParametersDto, GenerateFormToolCallParametersDto, GeneratePresentationToolCallParametersDto. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into GenerateDocxToolCallParametersDto
        try:
            instance.actual_instance = GenerateDocxToolCallParametersDto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GenerateFormToolCallParametersDto
        try:
            instance.actual_instance = GenerateFormToolCallParametersDto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GeneratePresentationToolCallParametersDto
        try:
            instance.actual_instance = GeneratePresentationToolCallParametersDto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EditorToolCallParametersDto with oneOf schemas: GenerateDocxToolCallParametersDto, GenerateFormToolCallParametersDto, GeneratePresentationToolCallParametersDto. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EditorToolCallParametersDto with oneOf schemas: GenerateDocxToolCallParametersDto, GenerateFormToolCallParametersDto, GeneratePresentationToolCallParametersDto. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], GenerateDocxToolCallParametersDto, GenerateFormToolCallParametersDto, GeneratePresentationToolCallParametersDto]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


