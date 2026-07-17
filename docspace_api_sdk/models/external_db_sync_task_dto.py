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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.distributed_task_status import DistributedTaskStatus
from docspace_api_sdk.models.external_db_sync_form_result_dto import ExternalDbSyncFormResultDto
from typing import Optional, Set
from typing_extensions import Self

class ExternalDbSyncTaskDto(BaseModel):
    """
    The external DB synchronization task parameters.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(description="The task ID.")
    error: Optional[StrictStr] = Field(default=None, description="The error message if the synchronization failed.")
    percentage: StrictInt = Field(description="The progress percentage of the synchronization.")
    is_completed: StrictBool = Field(description="Specifies whether the synchronization is completed or not.", alias="isCompleted")
    status: DistributedTaskStatus
    forms: Optional[List[ExternalDbSyncFormResultDto]] = Field(description="The synchronization results for all original forms in the room.")
    __properties: ClassVar[List[str]] = ["id", "error", "percentage", "isCompleted", "status", "forms"]

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
        """Create an instance of ExternalDbSyncTaskDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in forms (list)
        _items = []
        if self.forms:
            for _item_forms in self.forms:
                if _item_forms:
                    _items.append(_item_forms.to_dict())
            _dict['forms'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if forms (nullable) is None
        # and model_fields_set contains the field
        if self.forms is None and "forms" in self.model_fields_set:
            _dict['forms'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalDbSyncTaskDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "error": obj.get("error"),
            "percentage": obj.get("percentage"),
            "isCompleted": obj.get("isCompleted"),
            "status": obj.get("status"),
            "forms": [ExternalDbSyncFormResultDto.from_dict(_item) for _item in obj["forms"]] if obj.get("forms") is not None else None
        })
        return _obj


