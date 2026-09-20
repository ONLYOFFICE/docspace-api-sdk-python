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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UpdateClientRequest(BaseModel):
    """
    Client update request containing modified client details
    """ # noqa: E501
    name: Annotated[str, Field(min_length=3, strict=True, max_length=256)] = Field(description="The display name shown to the user on the consent screen. It has to be between 3 and 256 characters long.", json_schema_extra={"examples": ["Updated Client"]})
    description: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The free-text description shown next to the name on the consent screen, at most 255 characters.", json_schema_extra={"examples": ["Updated description of the client"]})
    logo: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The client logo as a data URI carrying base64 image data, shown on the consent screen. Only png, jpeg, jpg and svg+xml are accepted.", json_schema_extra={"examples": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="]})
    scopes: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="The permissions the client may ask for, named as they appear in the tenant scope catalogue - for example files:read, rooms:write or openid. A client cannot request a scope that is not listed here.")
    allow_pkce: Optional[StrictBool] = Field(default=None, description="Whether the client may use PKCE. Turning it on lets the client authenticate with the none method and prove itself with a code verifier instead of sending a secret, which is what a client that cannot keep a secret needs.", json_schema_extra={"examples": [True]})
    allowed_origins: Annotated[List[StrictStr], Field(min_length=1, max_length=12)] = Field(description="The web origins allowed to call the portal on behalf of this client, used for the CORS check. The set holds between 1 and 12 addresses.")
    redirect_uris: Annotated[List[StrictStr], Field(min_length=1, max_length=12)] = Field(description="The URIs an authorization code may be delivered to. An authorization request naming any other URI is refused, and the set holds between 1 and 12 addresses.")
    is_public: Optional[StrictBool] = Field(default=None, description="Whether the client is offered to third-party tenants rather than only to the tenant that registers it.", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["name", "description", "logo", "scopes", "allow_pkce", "allowed_origins", "redirect_uris", "is_public"]

    @field_validator('logo')
    def logo_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^data:image\/(?:png|jpeg|jpg|svg\+xml);base64,.*.{1,}", value):
            raise ValueError(r"must validate the regular expression /^data:image\/(?:png|jpeg|jpg|svg\+xml);base64,.*.{1,}/")
        return value

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
        """Create an instance of UpdateClientRequest from a JSON string"""
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
        """Create an instance of UpdateClientRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "logo": obj.get("logo"),
            "scopes": obj.get("scopes"),
            "allow_pkce": obj.get("allow_pkce"),
            "allowed_origins": obj.get("allowed_origins"),
            "redirect_uris": obj.get("redirect_uris"),
            "is_public": obj.get("is_public")
        })
        return _obj


