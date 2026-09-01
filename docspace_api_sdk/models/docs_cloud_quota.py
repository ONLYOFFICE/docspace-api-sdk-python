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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.docs_cloud_quota_user import DocsCloudQuotaUser
from typing import Optional, Set
from typing_extensions import Self

class DocsCloudQuota(BaseModel):
    """
    Represents the current user quota of a DocsCloud tenant.
    """ # noqa: E501
    users: Optional[List[DocsCloudQuotaUser]] = Field(default=None, description="The editor users.", json_schema_extra={"examples": [[{"userid": "00000000-0000-0000-0000-000000000000", "expire": "2024-01-15T10:30:00Z"}]]})
    users_view: Optional[List[DocsCloudQuotaUser]] = Field(default=None, description="The viewer users.", alias="usersView", json_schema_extra={"examples": [[{"userid": "00000000-0000-0000-0000-000000000000", "expire": "2024-01-15T10:30:00Z"}]]})
    __properties: ClassVar[List[str]] = ["users", "usersView"]

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
        """Create an instance of DocsCloudQuota from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item_users in self.users:
                if _item_users:
                    _items.append(_item_users.to_dict())
            _dict['users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users_view (list)
        _items = []
        if self.users_view:
            for _item_users_view in self.users_view:
                if _item_users_view:
                    _items.append(_item_users_view.to_dict())
            _dict['usersView'] = _items
        # set to None if users (nullable) is None
        # and model_fields_set contains the field
        if self.users is None and "users" in self.model_fields_set:
            _dict['users'] = None

        # set to None if users_view (nullable) is None
        # and model_fields_set contains the field
        if self.users_view is None and "users_view" in self.model_fields_set:
            _dict['usersView'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocsCloudQuota from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "users": [DocsCloudQuotaUser.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None,
            "usersView": [DocsCloudQuotaUser.from_dict(_item) for _item in obj["usersView"]] if obj.get("usersView") is not None else None
        })
        return _obj


