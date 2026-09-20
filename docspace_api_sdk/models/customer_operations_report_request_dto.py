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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.operation_order_type import OperationOrderType
from docspace_api_sdk.models.operation_status import OperationStatus
from docspace_api_sdk.models.operation_type import OperationType
from typing import Optional, Set
from typing_extensions import Self

class CustomerOperationsReportRequestDto(BaseModel):
    """
    The filters that select which wallet movements are reported: the services, the period, the participant, the  direction and the outcome of the movement, and the ordering.
    """ # noqa: E501
    service_name: Optional[List[StrictStr]] = Field(default=None, description="The wallet services whose movements are kept, named the way the billing catalogue names them - `backup`,  `ai-tools`, `ai-search`, `disk-storage`, `docscloud`. Take the values from the `serviceName` field of  `GET api/2.0/portal/payment/walletservices`; the match ignores case, a name this installation does not sell  fails the call with 404, and an omitted list keeps every service. A bare string is accepted in place of an  array for backward compatibility.", alias="serviceName", json_schema_extra={"examples": ["[backup]"]})
    start_date: Optional[datetime] = Field(default=None, description="The beginning of the reported period, inclusive. Read in the portal time zone rather than in UTC, so a  movement at the edge of the period falls where the portal sees it; defaults to the portal creation date.", alias="startDate", json_schema_extra={"examples": ["2024-01-01T00:00:00Z"]})
    end_date: Optional[datetime] = Field(default=None, description="The end of the reported period, inclusive. Read in the portal time zone rather than in UTC, and defaults to  the moment the call is made.", alias="endDate", json_schema_extra={"examples": ["2024-01-31T23:59:59Z"]})
    participant_name: Optional[StrictStr] = Field(default=None, description="The participant whose movements are kept - the account the accounting service records as the cause of a  movement. A movement caused by a portal user carries that user ID here, and one caused by the portal itself  carries the customer name; surrounding whitespace is trimmed, and an omitted value keeps every participant.", alias="participantName", json_schema_extra={"examples": ["My Own Corporation"]})
    credit: Optional[StrictBool] = Field(default=None, description="Whether movements that add money to the wallet - top-ups, refunds and corrections in the portal's favour -  are kept. Both directions are reported when neither this nor `debit` is given.", json_schema_extra={"examples": [True]})
    debit: Optional[StrictBool] = Field(default=None, description="Whether movements that take money out of the wallet - the charges of the wallet services - are kept. Both  directions are reported when neither this nor `credit` is given.", json_schema_extra={"examples": [False]})
    type: Optional[OperationType] = Field(default=None, description="The kind of movement to keep, which says what caused the money to move rather than how it ended. Every kind  is reported when it is omitted.")
    status: Optional[OperationStatus] = Field(default=None, description="The outcome to keep. A movement that is still being settled is reported as pending and may change later,  while the other outcomes are final; every outcome is reported when this is omitted.")
    order_by: Optional[StrictStr] = Field(default=None, description="The name of the field the movements are sorted by, spelled as the accounting service names it, such as  `StartDate` or `ServiceName`. Surrounding whitespace is trimmed, and the accounting service applies its own  ordering when this is omitted.", alias="orderBy", json_schema_extra={"examples": ["StartDate"]})
    order_type: Optional[OperationOrderType] = Field(default=None, description="The direction the field named in `orderBy` is sorted in. Newest or largest first is what the accounting  service does by default, so leaving this out sorts the same way as asking for descending explicitly.", alias="orderType")
    __properties: ClassVar[List[str]] = ["serviceName", "startDate", "endDate", "participantName", "credit", "debit", "type", "status", "orderBy", "orderType"]

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
        """Create an instance of CustomerOperationsReportRequestDto from a JSON string"""
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
        # set to None if service_name (nullable) is None
        # and model_fields_set contains the field
        if self.service_name is None and "service_name" in self.model_fields_set:
            _dict['serviceName'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['startDate'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['endDate'] = None

        # set to None if participant_name (nullable) is None
        # and model_fields_set contains the field
        if self.participant_name is None and "participant_name" in self.model_fields_set:
            _dict['participantName'] = None

        # set to None if credit (nullable) is None
        # and model_fields_set contains the field
        if self.credit is None and "credit" in self.model_fields_set:
            _dict['credit'] = None

        # set to None if debit (nullable) is None
        # and model_fields_set contains the field
        if self.debit is None and "debit" in self.model_fields_set:
            _dict['debit'] = None

        # set to None if order_by (nullable) is None
        # and model_fields_set contains the field
        if self.order_by is None and "order_by" in self.model_fields_set:
            _dict['orderBy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerOperationsReportRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serviceName": obj.get("serviceName"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "participantName": obj.get("participantName"),
            "credit": obj.get("credit"),
            "debit": obj.get("debit"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "orderBy": obj.get("orderBy"),
            "orderType": obj.get("orderType")
        })
        return _obj


