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
from docspace_api_sdk.models.action_type import ActionType
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.entry_type import EntryType
from docspace_api_sdk.models.location_type import LocationType
from docspace_api_sdk.models.message_action import MessageAction
from docspace_api_sdk.models.product_type import ProductType
from typing import Optional, Set
from typing_extensions import Self

class AuditEventDto(BaseModel):
    """
    One entry of the portal audit trail: who changed what, from where, and where it belongs in the product.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The ID of the recorded entry. Nothing accepts it as an argument - no operation fetches a single audit event  - so it serves only to tell two otherwise identical entries apart.", json_schema_extra={"examples": [1]})
    var_date: Optional[ApiDateTime] = Field(default=None, description="When the action happened, in the portal time zone. The `from` and `to` filters are read as UTC instants, so  the two do not line up on a portal that is not on UTC.", alias="date")
    user: Optional[StrictStr] = Field(default=None, description="The display name of the user who acted, taken from the account as it stands now rather than as it stood  when the entry was written. A localised placeholder stands in when there is no account to read: a portal  background job, an anonymous guest, or a user who has since been deleted.", json_schema_extra={"examples": ["John Doe"]})
    user_id: Optional[UUID] = Field(default=None, description="The ID of the user who acted, which is what the `userId` filter of this operation matches on. It stays  readable after the account is deleted, which is when `user` falls back to a placeholder.", alias="userId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000001"]})
    action: Optional[StrictStr] = Field(default=None, description="The whole event as a readable sentence in the portal language, with the names of the objects involved  substituted into it. On the two `audit/.../last` operations each substituted value is cut to 50 characters;  the filtered operations substitute them in full. It is empty when the build has no wording for the action.", json_schema_extra={"examples": ["User logged in"]})
    action_id: Optional[MessageAction] = Field(default=None, description="The action itself, as the `action` filter of this operation spells it and as  `GET api/2.0/security/audit/mappers` lists it under `messageAction`. Use this rather than parsing `action`,  which is prose and changes with the portal language.", alias="actionId")
    ip: Optional[StrictStr] = Field(default=None, description="The IP address the request came from, with the port stripped off. It is empty for an action a portal  background job performed, which has no request behind it.", json_schema_extra={"examples": ["192.0.2.1"]})
    country: Optional[StrictStr] = Field(default=None, description="The English name of the country the IP address is located in, empty when the address cannot be located -  the normal outcome for private and loopback addresses.", json_schema_extra={"examples": ["United States"]})
    city: Optional[StrictStr] = Field(default=None, description="The city the IP address is located in, empty under the same conditions as `country`.", json_schema_extra={"examples": ["New York"]})
    browser: Optional[StrictStr] = Field(default=None, description="The browser and its version as parsed from the user agent of the request, empty when the client sent none  that could be parsed or when no request was involved.", json_schema_extra={"examples": ["Chrome 120.0"]})
    platform: Optional[StrictStr] = Field(default=None, description="The operating system as parsed from the same user agent, empty under the same conditions as `browser`.", json_schema_extra={"examples": ["Windows"]})
    page: Optional[StrictStr] = Field(default=None, description="Where in the portal the action was made from: the referrer of the request, or that request's own path when  it carried no referrer. Long values are cut off at 512 characters.", json_schema_extra={"examples": ["/rooms/shared"]})
    action_type: Optional[ActionType] = Field(default=None, description="The kind of change the action stands for, as the `actionType` filter of this operation spells it. It is  derived from `actionId`, not stored per entry, so it is the same on every entry of one action.", alias="actionType")
    product: Optional[ProductType] = Field(default=None, description="The product the action belongs to. It cannot be filtered on here; the tree that groups actions by product  is `GET api/2.0/security/audit/mappers`.")
    location: Optional[LocationType] = Field(default=None, description="The location inside that product, as the `moduleType` filter of this operation spells it. It is also  derived from `actionId` rather than stored per entry.")
    target: Optional[List[StrictStr]] = Field(default=None, description="The objects the action was applied to, as the trail recorded them - a title, an account, an ID - one string  each. It is empty for an action that targets nothing, such as a settings change, and the `target` filter of  this operation matches one of these values in full.", json_schema_extra={"examples": [["item1", "item2"]]})
    entries: Optional[List[EntryType]] = Field(default=None, description="The kinds of object the action applies to, holding at most two entries and none at all for an action that  targets nothing. Only the first of them can be filtered on, through `entryType`.", json_schema_extra={"examples": [["File", "Folder"]]})
    context: Optional[StrictStr] = Field(default=None, description="Where the action took place, spelled out in the portal language rather than as a code: for a Documents  event the room or the root folder it happened in, and for anything else the name of the module. Nothing  filters on it.", json_schema_extra={"examples": ["Security settings updated"]})
    __properties: ClassVar[List[str]] = ["id", "date", "user", "userId", "action", "actionId", "ip", "country", "city", "browser", "platform", "page", "actionType", "product", "location", "target", "entries", "context"]

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
        """Create an instance of AuditEventDto from a JSON string"""
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
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if browser (nullable) is None
        # and model_fields_set contains the field
        if self.browser is None and "browser" in self.model_fields_set:
            _dict['browser'] = None

        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if entries (nullable) is None
        # and model_fields_set contains the field
        if self.entries is None and "entries" in self.model_fields_set:
            _dict['entries'] = None

        # set to None if context (nullable) is None
        # and model_fields_set contains the field
        if self.context is None and "context" in self.model_fields_set:
            _dict['context'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuditEventDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "date": ApiDateTime.from_dict(obj["date"]) if obj.get("date") is not None else None,
            "user": obj.get("user"),
            "userId": obj.get("userId"),
            "action": obj.get("action"),
            "actionId": obj.get("actionId"),
            "ip": obj.get("ip"),
            "country": obj.get("country"),
            "city": obj.get("city"),
            "browser": obj.get("browser"),
            "platform": obj.get("platform"),
            "page": obj.get("page"),
            "actionType": obj.get("actionType"),
            "product": obj.get("product"),
            "location": obj.get("location"),
            "target": obj.get("target"),
            "entries": obj.get("entries"),
            "context": obj.get("context")
        })
        return _obj


