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

class RoomTemplateStatusDto(BaseModel):
    """
    The progress of the job that builds a room template out of an existing room.
    """ # noqa: E501
    template_id: StrictInt = Field(description="The template the job is building. It is meaningful once the job has created the template folder, and the  template can be opened with the room operations only after `isCompleted` turns true.", alias="templateId", json_schema_extra={"examples": [123]})
    progress: Union[StrictFloat, StrictInt] = Field(description="How far the job has got. The value climbs while the contents of the room are being copied and reaches its  maximum at the very end, so it is an indication of life rather than a reliable estimate of the time left.", json_schema_extra={"examples": [75.5]})
    error: Optional[StrictStr] = Field(default=None, description="Why the job stopped. It is empty while the job runs and after a successful one; when it is filled the  half-built template has already been removed, so nothing has to be cleaned up by the caller.", json_schema_extra={"examples": ["Template creation failed"]})
    is_completed: StrictBool = Field(description="Whether the job has ended. It is set both after a successful build and after a failure, so `error` is what  tells the two apart, and the record keeps answering with the same values until another job is started.", alias="isCompleted", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["templateId", "progress", "error", "isCompleted"]

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
        """Create an instance of RoomTemplateStatusDto from a JSON string"""
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
        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomTemplateStatusDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "templateId": obj.get("templateId"),
            "progress": obj.get("progress"),
            "error": obj.get("error"),
            "isCompleted": obj.get("isCompleted")
        })
        return _obj


