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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ClientResponse(BaseModel):
    """
    The whole stored record of an OAuth2 client, including the secret and every address the client is allowed to use.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The display name shown to the user on the consent screen, between 3 and 256 characters.", json_schema_extra={"examples": ["Example Name"]})
    description: Optional[StrictStr] = Field(default=None, description="The free-text description shown next to the name on the consent screen, at most 255 characters.", json_schema_extra={"examples": ["Example Description"]})
    tenant: Optional[StrictInt] = Field(default=None, description="The identifier of the portal the client belongs to. A client is visible only inside its own tenant, apart from the unauthenticated public info read.", json_schema_extra={"examples": [1]})
    scopes: Optional[List[StrictStr]] = Field(default=None, description="The permissions the client may ask for, named as they appear in the tenant scope catalogue - for example files:read, rooms:write or openid. A client cannot request a scope that is not listed here.")
    enabled: Optional[StrictBool] = Field(default=None, description="Whether the client may currently obtain tokens. A disabled client keeps its registration and the tokens already issued to it, but new authorization requests for it are refused.", json_schema_extra={"examples": [True]})
    client_id: Optional[StrictStr] = Field(default=None, description="The generated identifier of the client, sent as client_id in every OAuth2 request. It is assigned when the client is registered and never changes afterwards.", json_schema_extra={"examples": ["6c7cf17b-1bd3-47d5-94c6-be2d3570e168"]})
    client_secret: Optional[StrictStr] = Field(default=None, description="The client secret, which the client presents at the token endpoint when it authenticates with client_secret_post. It is omitted from the response rather than sent as null when the client has none.", json_schema_extra={"examples": ["6c7cf17b-1bd3-47d5-94c6-be2d3570e168"]})
    website_url: Optional[StrictStr] = Field(default=None, description="The URL of the client home page, offered to the user before they consent.", json_schema_extra={"examples": ["http://example.com"]})
    terms_url: Optional[StrictStr] = Field(default=None, description="The URL of the client terms of service, linked from the consent screen.", json_schema_extra={"examples": ["http://example.com"]})
    policy_url: Optional[StrictStr] = Field(default=None, description="The URL of the client privacy policy, linked from the consent screen.", json_schema_extra={"examples": ["http://example.com"]})
    logo: Optional[StrictStr] = Field(default=None, description="The client logo as a data URI carrying base64 image data, shown on the consent screen. Only png, jpeg, jpg and svg+xml are accepted, the whole string may not exceed 2000000 characters and the decoded image may not exceed 256000 bytes.", json_schema_extra={"examples": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="]})
    authentication_methods: Optional[List[StrictStr]] = Field(default=None, description="How the client authenticates itself at the token endpoint: client_secret_post for a confidential client that sends its secret, none for a public client that proves itself with PKCE instead.")
    redirect_uris: Optional[List[StrictStr]] = Field(default=None, description="The URIs an authorization code may be delivered to. An authorization request naming any other URI is refused, and the set holds between 1 and 12 addresses.")
    allowed_origins: Optional[List[StrictStr]] = Field(default=None, description="The web origins allowed to call the portal on behalf of this client, used for the CORS check. The set holds between 1 and 12 addresses.")
    logout_redirect_uris: Optional[List[StrictStr]] = Field(default=None, description="The URIs the user may be sent back to once they have logged out.")
    created_on: Optional[datetime] = Field(default=None, description="When the client was registered, as an ISO-8601 timestamp with a zone offset.", json_schema_extra={"examples": ["2024-04-04T12:00:00Z"]})
    created_by: Optional[StrictStr] = Field(default=None, description="The identifier of the user who registered the client. A plain user may read and change only the clients where this is their own identifier.", json_schema_extra={"examples": ["6c7cf17b-1bd3-47d5-94c6-be2d3570e168"]})
    modified_on: Optional[datetime] = Field(default=None, description="When the client was last changed, as an ISO-8601 timestamp with a zone offset.", json_schema_extra={"examples": ["2024-04-04T12:00:00Z"]})
    modified_by: Optional[StrictStr] = Field(default=None, description="The identifier of the user who last changed the client.", json_schema_extra={"examples": ["6c7cf17b-1bd3-47d5-94c6-be2d3570e168"]})
    is_public: Optional[StrictBool] = Field(default=None, description="Whether the client is offered to third-party tenants rather than only to the tenant that registered it.", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["name", "description", "tenant", "scopes", "enabled", "client_id", "client_secret", "website_url", "terms_url", "policy_url", "logo", "authentication_methods", "redirect_uris", "allowed_origins", "logout_redirect_uris", "created_on", "created_by", "modified_on", "modified_by", "is_public"]

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
        """Create an instance of ClientResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientResponse from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "tenant": obj.get("tenant"),
            "scopes": obj.get("scopes"),
            "enabled": obj.get("enabled"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "website_url": obj.get("website_url"),
            "terms_url": obj.get("terms_url"),
            "policy_url": obj.get("policy_url"),
            "logo": obj.get("logo"),
            "authentication_methods": obj.get("authentication_methods"),
            "redirect_uris": obj.get("redirect_uris"),
            "allowed_origins": obj.get("allowed_origins"),
            "logout_redirect_uris": obj.get("logout_redirect_uris"),
            "created_on": obj.get("created_on"),
            "created_by": obj.get("created_by"),
            "modified_on": obj.get("modified_on"),
            "modified_by": obj.get("modified_by"),
            "is_public": obj.get("is_public")
        })
        return _obj


