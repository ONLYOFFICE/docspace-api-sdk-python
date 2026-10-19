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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from docspace_api_sdk.models.run_builder_script_output_request import RunBuilderScriptOutputRequest
from docspace_api_sdk.models.run_builder_script_request_dto_argument import RunBuilderScriptRequestDtoArgument
from typing import Optional, Set
from typing_extensions import Self

class RunBuilderScriptRequestDto(BaseModel):
    """
    The document builder script to run and where to put what it produces.
    """ # noqa: E501
    script: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2097152)]] = Field(description="The document builder script. It names a portal file by its id where the document builder documentation  writes an address - `builder.OpenFile(1234)`; an address written out in the script is refused.", json_schema_extra={"examples": ["builder.OpenFile(\"1234\"); Api.GetDocument().GetElement(0).AddText(Argument.title); builder.SaveFile(\"docx\", \"result.docx\"); builder.SaveFile(\"pdf\", \"result.pdf\"); builder.CloseFile();"]})
    folder_id: Optional[StrictInt] = Field(default=None, description="The id of the folder for the produced files that `outputs` does not list, as reported by a folder listing  such as `GET api/2.0/files/{folderId}`.", alias="folderId", json_schema_extra={"examples": [5678]})
    outputs: Optional[Dict[str, RunBuilderScriptOutputRequest]] = Field(default=None, description="Destinations of the produced files, keyed by the name the script saves each one under - the second argument of  `builder.SaveFile(docx, result.docx)`.", json_schema_extra={"examples": [{"result.docx": {"fileId": 1234}, "result.pdf": {"folderId": 5678, "title": "Quarterly report.pdf"}}]})
    argument: Optional[RunBuilderScriptRequestDtoArgument] = None
    __properties: ClassVar[List[str]] = ["script", "folderId", "outputs", "argument"]

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
        """Create an instance of RunBuilderScriptRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in outputs (dict)
        _field_dict = {}
        if self.outputs:
            for _key_outputs in self.outputs:
                if self.outputs[_key_outputs]:
                    _field_dict[_key_outputs] = self.outputs[_key_outputs].to_dict()
            _dict['outputs'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of argument
        if self.argument:
            _dict['argument'] = self.argument.to_dict()
        # set to None if script (nullable) is None
        # and model_fields_set contains the field
        if self.script is None and "script" in self.model_fields_set:
            _dict['script'] = None

        # set to None if folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.folder_id is None and "folder_id" in self.model_fields_set:
            _dict['folderId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunBuilderScriptRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "script": obj.get("script"),
            "folderId": obj.get("folderId"),
            "outputs": dict(
                (_k, RunBuilderScriptOutputRequest.from_dict(_v))
                for _k, _v in obj["outputs"].items()
            )
            if obj.get("outputs") is not None
            else None,
            "argument": RunBuilderScriptRequestDtoArgument.from_dict(obj["argument"]) if obj.get("argument") is not None else None
        })
        return _obj


