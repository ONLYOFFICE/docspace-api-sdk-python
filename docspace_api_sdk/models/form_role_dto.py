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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.employee_full_dto import EmployeeFullDto
from docspace_api_sdk.models.form_filling_status import FormFillingStatus
from typing import Optional, Set
from typing_extensions import Self

class FormRoleDto(BaseModel):
    """
    One role of a PDF form, with the state the turn of that role is in.
    """ # noqa: E501
    role_name: Optional[StrictStr] = Field(description="The name the role was given when the form was laid out, unique within that form. It is the value that names  the role in the calls which change or stop the filling.", alias="roleName", json_schema_extra={"examples": ["Approver"]})
    role_color: Optional[StrictStr] = Field(default=None, description="The colour a client paints the role with, as a hexadecimal RGB value; empty when the role mapping assigned  none.", alias="roleColor", json_schema_extra={"examples": ["#FF5733"]})
    user: Optional[EmployeeFullDto] = Field(default=None, description="The account the role was assigned to, which is the person expected to fill this part of the form.")
    sequence: StrictInt = Field(description="The turn this role takes: the roles come back ordered by this number, roles sharing a number are filled in  parallel, and a role with a higher number waits until every lower one has been submitted.", json_schema_extra={"examples": [1]})
    submitted: StrictBool = Field(description="Reports whether this role has already handed in its part. The lowest sequence number that still holds an  unsubmitted role is the turn the form as a whole is waiting on.", json_schema_extra={"examples": [False]})
    stoped_by: Optional[EmployeeFullDto] = Field(default=None, description="The account that interrupted the filling. It is filled in on the one role the filling was stopped at and stays  empty on every other role, and on all of them while the filling runs normally.", alias="stopedBy")
    history: Optional[Dict[str, datetime]] = Field(default=None, description="When the role passed through the stages of its turn, keyed by stage: 0 is the moment the form was opened for  it, 1 the moment it was submitted and 2 the moment the filling was stopped at it. The times are given in the  time zone of the portal, and only the stages that have actually happened are present, so an empty object means  the role has not been opened yet.", json_schema_extra={"examples": [{"0": "2025-01-15T10:30:00"}]})
    role_status: Optional[FormFillingStatus] = Field(default=None, description="Where the role stands in the queue: roles of earlier turns are reported as complete, roles of later turns as a  draft, and the role whose turn it is as either yours to fill or in progress, depending on whether that person  has already opened the form. The role the filling was stopped at is reported as stopped whatever its turn.", alias="roleStatus")
    __properties: ClassVar[List[str]] = ["roleName", "roleColor", "user", "sequence", "submitted", "stopedBy", "history", "roleStatus"]

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
        """Create an instance of FormRoleDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stoped_by
        if self.stoped_by:
            _dict['stopedBy'] = self.stoped_by.to_dict()
        # set to None if role_name (nullable) is None
        # and model_fields_set contains the field
        if self.role_name is None and "role_name" in self.model_fields_set:
            _dict['roleName'] = None

        # set to None if role_color (nullable) is None
        # and model_fields_set contains the field
        if self.role_color is None and "role_color" in self.model_fields_set:
            _dict['roleColor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FormRoleDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "roleName": obj.get("roleName"),
            "roleColor": obj.get("roleColor"),
            "user": EmployeeFullDto.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "sequence": obj.get("sequence"),
            "submitted": obj.get("submitted"),
            "stopedBy": EmployeeFullDto.from_dict(obj["stopedBy"]) if obj.get("stopedBy") is not None else None,
            "history": obj.get("history"),
            "roleStatus": obj.get("roleStatus")
        })
        return _obj


