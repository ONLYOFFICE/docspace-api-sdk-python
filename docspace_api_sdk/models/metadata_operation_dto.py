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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MetadataOperationDto(BaseModel):
    """
    The cascade metadata assignment operation status.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The operation ID.", json_schema_extra={"examples": ["a1f4c9b2-3d8e-4f77-9b16-2c5de8f0a913"]})
    progress: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The operation progress percentage.", json_schema_extra={"examples": [100]})
    is_completed: Optional[StrictBool] = Field(default=None, description="Specifies if the operation is completed.", alias="isCompleted", json_schema_extra={"examples": [True]})
    error: Optional[StrictStr] = Field(default=None, description="The operation error message.", json_schema_extra={"examples": ["Folder not found."]})
    template_ids: Optional[List[StrictInt]] = Field(default=None, description="The IDs of the metadata templates the operation propagates to the subtree. Empty when there is no operation to  report, so the answer describes nothing in progress.", alias="templateIds", json_schema_extra={"examples": [[3]]})
    __properties: ClassVar[List[str]] = ["id", "progress", "isCompleted", "error", "templateIds"]

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
        """Create an instance of MetadataOperationDto from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if template_ids (nullable) is None
        # and model_fields_set contains the field
        if self.template_ids is None and "template_ids" in self.model_fields_set:
            _dict['templateIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetadataOperationDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "progress": obj.get("progress"),
            "isCompleted": obj.get("isCompleted"),
            "error": obj.get("error"),
            "templateIds": obj.get("templateIds")
        })
        return _obj


