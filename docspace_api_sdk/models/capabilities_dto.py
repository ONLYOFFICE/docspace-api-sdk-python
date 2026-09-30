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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CapabilitiesDto(BaseModel):
    """
    The sign-in methods this portal offers, as a login client needs them before anyone has signed in.
    """ # noqa: E501
    ldap_enabled: StrictBool = Field(description="Whether members may sign in with their directory credentials. It is `false` both when LDAP sign-in is  switched off and when the pricing plan or the installation does not include it, and also when the settings  could not be read at all - a `false` here means the method is not offered, never that it is unknown.", alias="ldapEnabled", json_schema_extra={"examples": [False]})
    ldap_domain: Optional[StrictStr] = Field(default=None, description="The directory domain members authenticate against, to be shown next to the login field. It is empty  whenever `ldapEnabled` is `false`, and also while the portal has not completed a directory synchronisation.", alias="ldapDomain", json_schema_extra={"examples": ["example.com"]})
    providers: Optional[List[StrictStr]] = Field(description="The keys of the external identity providers to offer, ordered for the country the caller's IP address  resolves to and reduced to those this installation has credentials for. Pass one of them as `provider` to  `POST api/2.0/authentication`. An empty list means external sign-in is not on offer.", json_schema_extra={"examples": [["google", "facebook", "microsoft"]]})
    sso_label: Optional[StrictStr] = Field(description="The caption for the single sign-on button in the portal language, empty whenever `ssoUrl` is.", alias="ssoLabel", json_schema_extra={"examples": ["Enterprise SSO"]})
    oauth_enabled: StrictBool = Field(description="Whether external identity providers may be used on this portal at all. While it is `false`, `providers` is  empty because the list is not even assembled.", alias="oauthEnabled", json_schema_extra={"examples": [True]})
    sso_url: Optional[StrictStr] = Field(description="The address to send the browser to for SAML single sign-on. It is empty when single sign-on is not on  offer, which is the one thing to test - there is no separate flag for it.", alias="ssoUrl", json_schema_extra={"examples": ["https://sso.example.com/login"]})
    identity_server_enabled: StrictBool = Field(description="Whether the installation exposes its built-in identity server, which is what the portal's own OAuth  applications authenticate against. It concerns third-party applications signing in to the portal, not  portal members signing in to an external provider - that is `providers`.", alias="identityServerEnabled", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["ldapEnabled", "ldapDomain", "providers", "ssoLabel", "oauthEnabled", "ssoUrl", "identityServerEnabled"]

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
        """Create an instance of CapabilitiesDto from a JSON string"""
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
        # set to None if ldap_domain (nullable) is None
        # and model_fields_set contains the field
        if self.ldap_domain is None and "ldap_domain" in self.model_fields_set:
            _dict['ldapDomain'] = None

        # set to None if providers (nullable) is None
        # and model_fields_set contains the field
        if self.providers is None and "providers" in self.model_fields_set:
            _dict['providers'] = None

        # set to None if sso_label (nullable) is None
        # and model_fields_set contains the field
        if self.sso_label is None and "sso_label" in self.model_fields_set:
            _dict['ssoLabel'] = None

        # set to None if sso_url (nullable) is None
        # and model_fields_set contains the field
        if self.sso_url is None and "sso_url" in self.model_fields_set:
            _dict['ssoUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CapabilitiesDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ldapEnabled": obj.get("ldapEnabled"),
            "ldapDomain": obj.get("ldapDomain"),
            "providers": obj.get("providers"),
            "ssoLabel": obj.get("ssoLabel"),
            "oauthEnabled": obj.get("oauthEnabled"),
            "ssoUrl": obj.get("ssoUrl"),
            "identityServerEnabled": obj.get("identityServerEnabled")
        })
        return _obj


