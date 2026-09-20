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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.operation_type import OperationType
from typing import Optional, Set
from typing_extensions import Self

class OperationDto(BaseModel):
    """
    One movement on the portal wallet: what it was for, who caused it, and how much money it moved.
    """ # noqa: E501
    var_date: Optional[ApiDateTime] = Field(default=None, description="When the movement was booked, in the portal time zone - the same zone the `startDate` and `endDate`  filters are read in, so the two do line up here.", alias="date")
    service: Optional[StrictStr] = Field(default=None, description="The wallet service the movement belongs to, by its stable key. It is what the `serviceName` filter  matches on, and it is empty for a movement that belongs to no service, such as a top-up.", json_schema_extra={"examples": ["disk-storage"]})
    description: Optional[StrictStr] = Field(default=None, description="A one-line summary of the movement in the portal language, already composed from the service and the  quantity - meant to be printed as it is rather than parsed.", json_schema_extra={"examples": ["Storage quota increase"]})
    details: Optional[StrictStr] = Field(default=None, description="The longer explanation of the same movement, where the service recorded one. It is empty for a movement  that has nothing to add to `description`.", json_schema_extra={"examples": ["Increased storage from 50GB to 100GB"]})
    service_unit: Optional[StrictStr] = Field(default=None, description="What `quantity` counts for this service, in the portal language. AI consumption is reported in tokens  here rather than in the AI credits the service is sold in.", alias="serviceUnit", json_schema_extra={"examples": ["GB"]})
    quantity: Optional[StrictInt] = Field(default=None, description="How many units the movement covers, in the unit named by `serviceUnit`. It is `0` for a movement that  moves money without consuming a service.", json_schema_extra={"examples": [1]})
    currency: Optional[StrictStr] = Field(default=None, description="The currency `credit` and `debit` are expressed in, as a three-letter ISO 4217 code. It is the accounting  currency of the wallet, which need not be the currency the subscription is priced in.", json_schema_extra={"examples": ["USD"]})
    credit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount that went into the wallet. It is `0` on a movement that only took money out, so the pair of  `credit` and `debit` is what shows which way the money went; the `credit` and `debit` filters of the  operation select the two directions by exactly this.", json_schema_extra={"examples": [99.99]})
    debit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount that was taken out of the wallet, `0` on a movement that put money in.", json_schema_extra={"examples": [99.99]})
    participant_name: Optional[StrictStr] = Field(default=None, description="Who caused the movement, as the billing service records them - an internal name, which is what the  `participantName` filter matches on. Show `participantDisplayName` instead.", alias="participantName", json_schema_extra={"examples": ["john.doe@example.com"]})
    participant_display_name: Optional[StrictStr] = Field(default=None, description="The same person as their portal display name. It falls back to `participantName` when the name belongs to  no portal account, so it is never empty while `participantName` is filled.", alias="participantDisplayName", json_schema_extra={"examples": ["John Doe"]})
    source_type: Optional[StrictStr] = Field(default=None, description="What kind of thing an AI operation was run on - an agent, a file, a folder, a room or a form. It is empty  on any movement that is not an AI charge.", alias="sourceType", json_schema_extra={"examples": ["Agent"]})
    source_title: Optional[StrictStr] = Field(default=None, description="The title that thing had when the operation ran, kept as recorded, so it does not follow a later rename.  Empty under the same conditions as `sourceType`.", alias="sourceTitle", json_schema_extra={"examples": ["My AI Agent"]})
    source_id: Optional[StrictStr] = Field(default=None, description="The identifier of that thing, to look it up in the module it belongs to. Empty under the same conditions  as `sourceType`.", alias="sourceId", json_schema_extra={"examples": ["123"]})
    type: Optional[OperationType] = Field(default=None, description="What kind of movement this is - a payment, a charge, a refund, a correction. It is what the `type` filter  matches on, and `Unknown` covers a movement the billing service reported under a kind this build does not  recognise.")
    __properties: ClassVar[List[str]] = ["date", "service", "description", "details", "serviceUnit", "quantity", "currency", "credit", "debit", "participantName", "participantDisplayName", "sourceType", "sourceTitle", "sourceId", "type"]

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
        """Create an instance of OperationDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_date
        if self.var_date:
            _dict['date'] = self.var_date.to_dict()
        # set to None if service (nullable) is None
        # and model_fields_set contains the field
        if self.service is None and "service" in self.model_fields_set:
            _dict['service'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        # set to None if service_unit (nullable) is None
        # and model_fields_set contains the field
        if self.service_unit is None and "service_unit" in self.model_fields_set:
            _dict['serviceUnit'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if participant_name (nullable) is None
        # and model_fields_set contains the field
        if self.participant_name is None and "participant_name" in self.model_fields_set:
            _dict['participantName'] = None

        # set to None if participant_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.participant_display_name is None and "participant_display_name" in self.model_fields_set:
            _dict['participantDisplayName'] = None

        # set to None if source_type (nullable) is None
        # and model_fields_set contains the field
        if self.source_type is None and "source_type" in self.model_fields_set:
            _dict['sourceType'] = None

        # set to None if source_title (nullable) is None
        # and model_fields_set contains the field
        if self.source_title is None and "source_title" in self.model_fields_set:
            _dict['sourceTitle'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OperationDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": ApiDateTime.from_dict(obj["date"]) if obj.get("date") is not None else None,
            "service": obj.get("service"),
            "description": obj.get("description"),
            "details": obj.get("details"),
            "serviceUnit": obj.get("serviceUnit"),
            "quantity": obj.get("quantity"),
            "currency": obj.get("currency"),
            "credit": obj.get("credit"),
            "debit": obj.get("debit"),
            "participantName": obj.get("participantName"),
            "participantDisplayName": obj.get("participantDisplayName"),
            "sourceType": obj.get("sourceType"),
            "sourceTitle": obj.get("sourceTitle"),
            "sourceId": obj.get("sourceId"),
            "type": obj.get("type")
        })
        return _obj


