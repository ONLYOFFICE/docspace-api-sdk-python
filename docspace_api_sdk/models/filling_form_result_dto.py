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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.employee_full_dto import EmployeeFullDto
from docspace_api_sdk.models.file_dto import FileDto
from typing import Optional, Set
from typing_extensions import Self

class FillingFormResultDto(BaseModel):
    """
    The outcome of one completed form-filling session, as the person who has just filled the form sees it.
    """ # noqa: E501
    form_number: StrictInt = Field(description="The number this copy was given among the copies made of the same form, counting up from 1. It is the number  the results of the form are ordered by and the one the title of the copy carries.", alias="formNumber", json_schema_extra={"examples": [1]})
    completed_form: Optional[FileDto] = Field(default=None, description="The filled copy that the session produced, as an ordinary file: it can be read and downloaded with the file  operations of this API.", alias="completedForm")
    original_form: Optional[FileDto] = Field(default=None, description="The form the copy was made from, so that a client can offer filling it once more.", alias="originalForm")
    manager: Optional[EmployeeFullDto] = Field(default=None, description="The account that owns the original form, reported with its email address, so that the person who has just  filled the form knows who receives it and whom to ask about it.")
    room_id: StrictInt = Field(description="The room the form was filled in. It comes back as 0 when the session was reached through a link shared for  that single form rather than for its room, in which case there is no room the caller could be sent to.", alias="roomId", json_schema_extra={"examples": [123]})
    is_room_member: Optional[StrictBool] = Field(default=None, description="Tells whether the calling account may open that room: true for a member of the room and for a portal  administrator, in which case a client can offer going to the room; false for the anonymous caller who filled  the form through a link and can only be shown the copy itself.", alias="isRoomMember", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["formNumber", "completedForm", "originalForm", "manager", "roomId", "isRoomMember"]

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
        """Create an instance of FillingFormResultDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of completed_form
        if self.completed_form:
            _dict['completedForm'] = self.completed_form.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_form
        if self.original_form:
            _dict['originalForm'] = self.original_form.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manager
        if self.manager:
            _dict['manager'] = self.manager.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FillingFormResultDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "formNumber": obj.get("formNumber"),
            "completedForm": FileDto.from_dict(obj["completedForm"]) if obj.get("completedForm") is not None else None,
            "originalForm": FileDto.from_dict(obj["originalForm"]) if obj.get("originalForm") is not None else None,
            "manager": EmployeeFullDto.from_dict(obj["manager"]) if obj.get("manager") is not None else None,
            "roomId": obj.get("roomId"),
            "isRoomMember": obj.get("isRoomMember")
        })
        return _obj


