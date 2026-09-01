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
from docspace_api_sdk.models.docs_cloud_license_info import DocsCloudLicenseInfo
from docspace_api_sdk.models.docs_cloud_server_info import DocsCloudServerInfo
from docspace_api_sdk.models.docs_cloud_stats import DocsCloudStats
from docspace_api_sdk.models.docs_cloud_users_limit import DocsCloudUsersLimit
from typing import Optional, Set
from typing_extensions import Self

class DocsCloudTenantInfo(BaseModel):
    """
    Represents the license and server information of a DocsCloud tenant, with usage statistics for the current period.
    """ # noqa: E501
    license: Optional[DocsCloudLicenseInfo] = Field(default=None, description="The license information.")
    server: Optional[DocsCloudServerInfo] = Field(default=None, description="The DocsCloud server information.")
    users_limit: Optional[DocsCloudUsersLimit] = Field(default=None, description="The user limits of the license.", alias="usersLimit")
    stats: Optional[DocsCloudStats] = Field(default=None, description="The usage statistics for the current period.")
    __properties: ClassVar[List[str]] = ["license", "server", "usersLimit", "stats"]

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
        """Create an instance of DocsCloudTenantInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of license
        if self.license:
            _dict['license'] = self.license.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['server'] = self.server.to_dict()
        # override the default output from pydantic by calling `to_dict()` of users_limit
        if self.users_limit:
            _dict['usersLimit'] = self.users_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocsCloudTenantInfo from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "license": DocsCloudLicenseInfo.from_dict(obj["license"]) if obj.get("license") is not None else None,
            "server": DocsCloudServerInfo.from_dict(obj["server"]) if obj.get("server") is not None else None,
            "usersLimit": DocsCloudUsersLimit.from_dict(obj["usersLimit"]) if obj.get("usersLimit") is not None else None,
            "stats": DocsCloudStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None
        })
        return _obj


