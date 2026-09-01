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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class UpcomingPaymentDto(BaseModel):
    """
    The upcoming payment parameters.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The quota ID.", json_schema_extra={"examples": [-11]})
    name: Optional[StrictStr] = Field(default=None, description="The quota name.", json_schema_extra={"examples": ["storage"]})
    title: Optional[StrictStr] = Field(default=None, description="The quota title.", json_schema_extra={"examples": ["Business plan"]})
    unit_of_measure: Optional[StrictStr] = Field(default=None, description="The quota unit of measure.", alias="unitOfMeasure", json_schema_extra={"examples": ["admins"]})
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity that will be charged (the next quantity if set, otherwise the current quantity).", json_schema_extra={"examples": [100]})
    wallet: Optional[StrictBool] = Field(default=None, description="The quota applies to the wallet or not.", json_schema_extra={"examples": [True]})
    due_date: Optional[datetime] = Field(default=None, description="The due date of the upcoming payment in the portal time zone.", alias="dueDate", json_schema_extra={"examples": ["2026-07-08T11:39:43.0000000+03:00"]})
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount that will be charged (unit price multiplied by the quantity).", json_schema_extra={"examples": [14]})
    currency: Optional[StrictStr] = Field(default=None, description="The three-character ISO 4217 currency symbol of the amount.", json_schema_extra={"examples": ["USD"]})
    __properties: ClassVar[List[str]] = ["id", "name", "title", "unitOfMeasure", "quantity", "wallet", "dueDate", "amount", "currency"]

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
        """Create an instance of UpcomingPaymentDto from a JSON string"""
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

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if unit_of_measure (nullable) is None
        # and model_fields_set contains the field
        if self.unit_of_measure is None and "unit_of_measure" in self.model_fields_set:
            _dict['unitOfMeasure'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['dueDate'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpcomingPaymentDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "title": obj.get("title"),
            "unitOfMeasure": obj.get("unitOfMeasure"),
            "quantity": obj.get("quantity"),
            "wallet": obj.get("wallet"),
            "dueDate": obj.get("dueDate"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency")
        })
        return _obj


