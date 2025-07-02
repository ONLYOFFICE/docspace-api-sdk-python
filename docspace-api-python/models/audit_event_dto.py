# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace-api-python.models.action_type import ActionType
from docspace-api-python.models.api_date_time import ApiDateTime
from docspace-api-python.models.entry_type import EntryType
from docspace-api-python.models.message_action import MessageAction
from docspace-api-python.models.module_type import ModuleType
from docspace-api-python.models.product_type import ProductType
from typing import Optional, Set
from typing_extensions import Self

class AuditEventDto(BaseModel):
    """
    The audit event parameters.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The audit event ID.")
    var_date: Optional[ApiDateTime] = Field(default=None, alias="date")
    user: Optional[StrictStr] = Field(default=None, description="The name of the user who triggered the audit event.")
    user_id: Optional[StrictStr] = Field(default=None, description="The ID of the user who triggered the audit event.", alias="userId")
    action: Optional[StrictStr] = Field(default=None, description="The audit event action.")
    action_id: Optional[MessageAction] = Field(default=None, alias="actionId")
    ip: Optional[StrictStr] = Field(default=None, description="The audit event IP.")
    country: Optional[StrictStr] = Field(default=None, description="The audit event country.")
    city: Optional[StrictStr] = Field(default=None, description="The audit event city.")
    browser: Optional[StrictStr] = Field(default=None, description="The audit event browser.")
    platform: Optional[StrictStr] = Field(default=None, description="The audit event platform.")
    page: Optional[StrictStr] = Field(default=None, description="The audit event page.")
    action_type: Optional[ActionType] = Field(default=None, alias="actionType")
    product: Optional[ProductType] = None
    module: Optional[ModuleType] = None
    target: Optional[List[StrictStr]] = Field(default=None, description="The list of target objects affected by the audit event (e.g., document ID, user account).")
    entries: Optional[List[EntryType]] = Field(default=None, description="The list of audit entry types (e.g., Folder, User, File).")
    context: Optional[StrictStr] = Field(default=None, description="The audit event context.")
    __properties: ClassVar[List[str]] = ["id", "date", "user", "userId", "action", "actionId", "ip", "country", "city", "browser", "platform", "page", "actionType", "product", "module", "target", "entries", "context"]

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
            "module": obj.get("module"),
            "target": obj.get("target"),
            "entries": obj.get("entries"),
            "context": obj.get("context")
        })
        return _obj


