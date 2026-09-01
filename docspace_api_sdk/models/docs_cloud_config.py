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
from typing_extensions import Annotated
from docspace_api_sdk.models.docs_cloud_ip_filter_config import DocsCloudIpFilterConfig
from docspace_api_sdk.models.docs_cloud_security_config import DocsCloudSecurityConfig
from docspace_api_sdk.models.docs_cloud_server_config import DocsCloudServerConfig
from docspace_api_sdk.models.docs_cloud_wopi_config import DocsCloudWopiConfig
from typing import Optional, Set
from typing_extensions import Self

class DocsCloudConfig(BaseModel):
    """
    Represents the configuration of a DocsCloud tenant.
    """ # noqa: E501
    tenant_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The tenant name.", alias="tenantName", json_schema_extra={"examples": ["My Portal"]})
    security: Optional[DocsCloudSecurityConfig] = Field(default=None, description="The security configuration.")
    server: Optional[DocsCloudServerConfig] = Field(default=None, description="The server configuration.")
    wopi: Optional[DocsCloudWopiConfig] = Field(default=None, description="The WOPI configuration.")
    ip_filter: Optional[DocsCloudIpFilterConfig] = Field(default=None, description="The IP filter configuration.", alias="ipFilter")
    __properties: ClassVar[List[str]] = ["tenantName", "security", "server", "wopi", "ipFilter"]

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
        """Create an instance of DocsCloudConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server
        if self.server:
            _dict['server'] = self.server.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wopi
        if self.wopi:
            _dict['wopi'] = self.wopi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ip_filter
        if self.ip_filter:
            _dict['ipFilter'] = self.ip_filter.to_dict()
        # set to None if tenant_name (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_name is None and "tenant_name" in self.model_fields_set:
            _dict['tenantName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocsCloudConfig from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantName": obj.get("tenantName"),
            "security": DocsCloudSecurityConfig.from_dict(obj["security"]) if obj.get("security") is not None else None,
            "server": DocsCloudServerConfig.from_dict(obj["server"]) if obj.get("server") is not None else None,
            "wopi": DocsCloudWopiConfig.from_dict(obj["wopi"]) if obj.get("wopi") is not None else None,
            "ipFilter": DocsCloudIpFilterConfig.from_dict(obj["ipFilter"]) if obj.get("ipFilter") is not None else None
        })
        return _obj


