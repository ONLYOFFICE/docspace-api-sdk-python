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
from docspace_api_sdk.models.api_date_time import ApiDateTime
from typing import Optional, Set
from typing_extensions import Self

class MetadataValueDto(BaseModel):
    """
    The value of a metadata field on an entry. Exactly one of the value properties is set, the one matching the field type:  `stringValue` for a string field, `numberValue` for a number field, `dateValue` for a date field,  `optionIds` for a single or multiple choice field.
    """ # noqa: E501
    string_value: Optional[StrictStr] = Field(default=None, description="The string value.", alias="stringValue", json_schema_extra={"examples": ["ACME Corp"]})
    number_value: Optional[StrictInt] = Field(default=None, description="The number value.", alias="numberValue", json_schema_extra={"examples": [150000]})
    date_value: Optional[ApiDateTime] = Field(default=None, description="The date value.", alias="dateValue")
    option_ids: Optional[List[UUID]] = Field(default=None, description="The selected choice option IDs.", alias="optionIds", json_schema_extra={"examples": [["4f1e2d3c-5b6a-4788-99aa-0c1d2e3f4a55"]]})
    __properties: ClassVar[List[str]] = ["stringValue", "numberValue", "dateValue", "optionIds"]

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
        """Create an instance of MetadataValueDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of date_value
        if self.date_value:
            _dict['dateValue'] = self.date_value.to_dict()
        # set to None if string_value (nullable) is None
        # and model_fields_set contains the field
        if self.string_value is None and "string_value" in self.model_fields_set:
            _dict['stringValue'] = None

        # set to None if number_value (nullable) is None
        # and model_fields_set contains the field
        if self.number_value is None and "number_value" in self.model_fields_set:
            _dict['numberValue'] = None

        # set to None if option_ids (nullable) is None
        # and model_fields_set contains the field
        if self.option_ids is None and "option_ids" in self.model_fields_set:
            _dict['optionIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetadataValueDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "stringValue": obj.get("stringValue"),
            "numberValue": obj.get("numberValue"),
            "dateValue": ApiDateTime.from_dict(obj["dateValue"]) if obj.get("dateValue") is not None else None,
            "optionIds": obj.get("optionIds")
        })
        return _obj


