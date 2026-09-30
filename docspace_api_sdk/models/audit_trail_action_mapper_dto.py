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

class AuditTrailActionMapperDto(BaseModel):
    """
    One audit trail action, with the kind of change it stands for and the kind of object it applies to.
    """ # noqa: E501
    message_action: Optional[StrictStr] = Field(default=None, description="The action name to send as the `action` filter of `GET api/2.0/security/audit/events/filter`, and the value  that comes back as `actionId` on an event.", alias="messageAction", json_schema_extra={"examples": ["FileCreated"]})
    action_type: Optional[StrictStr] = Field(default=None, description="The kind of change the action makes, accepted by the `actionType` filter of the same operation.", alias="actionType", json_schema_extra={"examples": ["Create"]})
    entity: Optional[StrictStr] = Field(default=None, description="The kind of object the action applies to, accepted by the `entryType` filter. It is `None` for an action  that targets no object, such as a settings change, and an action with a second object type reports only the  first one here.", json_schema_extra={"examples": ["File"]})
    __properties: ClassVar[List[str]] = ["messageAction", "actionType", "entity"]

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
        """Create an instance of AuditTrailActionMapperDto from a JSON string"""
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
        # set to None if message_action (nullable) is None
        # and model_fields_set contains the field
        if self.message_action is None and "message_action" in self.model_fields_set:
            _dict['messageAction'] = None

        # set to None if action_type (nullable) is None
        # and model_fields_set contains the field
        if self.action_type is None and "action_type" in self.model_fields_set:
            _dict['actionType'] = None

        # set to None if entity (nullable) is None
        # and model_fields_set contains the field
        if self.entity is None and "entity" in self.model_fields_set:
            _dict['entity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditTrailActionMapperDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "messageAction": obj.get("messageAction"),
            "actionType": obj.get("actionType"),
            "entity": obj.get("entity")
        })
        return _obj


