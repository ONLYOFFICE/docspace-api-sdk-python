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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class MetadataFilterConditionRequest(BaseModel):
    """
    One metadata filter condition as the clients send it: an element of the metadataFilters JSON of the listings and of  the body of the search endpoints. All conditions are combined with AND.
    """ # noqa: E501
    field_id: Optional[StrictInt] = Field(default=None, description="The ID of the template field the condition is on. A custom field is addressed by ASC.Files.Core.MetadataFilterConditionRequest.Name instead.", alias="fieldId", json_schema_extra={"examples": [1]})
    name: Optional[StrictStr] = Field(default=None, description="The name of a custom field, for the conditions on the custom fields, which have no identifier outside. Either the  field ID or the name is given; the name is matched without regard to case.", json_schema_extra={"examples": ["Client"]})
    op: Optional[StrictStr] = Field(default=None, description="The operator, one of ASC.Files.Core.MetadataFilterOperators: eq or contains for a string field, eq, range,  gt, gte, lt or lte for a number field, range, gt, gte, lt or lte for a date field, in for a  choice field. Optional: an omitted operator is read as eq for a string, as range for a date, as in for a  choice, and for a number as eq when a value is given or as range when a bound is. A present one has to belong  to the field type and to the arguments: eq takes a value, range takes bounds.", json_schema_extra={"examples": ["eq"]})
    value: Optional[StrictStr] = Field(default=None, description="The value of a single-valued condition: the whole or a part of a string field, the exact value of a number field,  or the bound of a gt, gte, lt or lte condition on a number or a date field. A JSON number is accepted as  well as a string. A number is a whole number of at most 2^53-1 in magnitude, the limit of a stored number value.  A date given without a time (2026-06-30) names the whole day (UTC).", json_schema_extra={"examples": ["ACME"]})
    var_from: Optional[StrictStr] = Field(default=None, description="The inclusive lower bound of a range. A number is a whole number of at most 2^53-1 in magnitude, the limit of a  stored number value. A date given without a time (2026-06-01) is the start of that day (UTC).", alias="from", json_schema_extra={"examples": ["2026-01-01"]})
    to: Optional[StrictStr] = Field(default=None, description="The inclusive upper bound of a range. A number is a whole number of at most 2^53-1 in magnitude, the limit of a  stored number value. A date given without a time (2026-06-30) covers the whole day (UTC); a value with a time  is an instant and is taken as is.", json_schema_extra={"examples": ["2026-06-30"]})
    option_ids: Optional[List[UUID]] = Field(default=None, description="The options any of which the choice field must hold.", alias="optionIds", json_schema_extra={"examples": [["4f1e2d3c-5b6a-4788-99aa-0c1d2e3f4a55"]]})
    __properties: ClassVar[List[str]] = ["fieldId", "name", "op", "value", "from", "to", "optionIds"]

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
        """Create an instance of MetadataFilterConditionRequest from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if op (nullable) is None
        # and model_fields_set contains the field
        if self.op is None and "op" in self.model_fields_set:
            _dict['op'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if var_from (nullable) is None
        # and model_fields_set contains the field
        if self.var_from is None and "var_from" in self.model_fields_set:
            _dict['from'] = None

        # set to None if to (nullable) is None
        # and model_fields_set contains the field
        if self.to is None and "to" in self.model_fields_set:
            _dict['to'] = None

        # set to None if option_ids (nullable) is None
        # and model_fields_set contains the field
        if self.option_ids is None and "option_ids" in self.model_fields_set:
            _dict['optionIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetadataFilterConditionRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fieldId": obj.get("fieldId"),
            "name": obj.get("name"),
            "op": obj.get("op"),
            "value": obj.get("value"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "optionIds": obj.get("optionIds")
        })
        return _obj


