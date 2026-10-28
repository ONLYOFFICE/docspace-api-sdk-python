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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SsoBindingTypeDto(BaseModel):
    """
    The SAML bindings the SSO settings accept.
    """ # noqa: E501
    saml20_http_post: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 HTTP POST binding, which carries the request in a self-submitting form. It is what the  built-in configuration uses and the one to pick when requests are signed, since it has no length limit.", alias="saml20HttpPost", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"]})
    saml20_http_redirect: Optional[StrictStr] = Field(default=None, description="The SAML 2.0 HTTP redirect binding, which carries the request in the query string and is therefore bound  by the length a URL may have.", alias="saml20HttpRedirect", json_schema_extra={"examples": ["urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"]})
    __properties: ClassVar[List[str]] = ["saml20HttpPost", "saml20HttpRedirect"]

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
        """Create an instance of SsoBindingTypeDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "saml20_http_post",
            "saml20_http_redirect",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if saml20_http_post (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_http_post is None and "saml20_http_post" in self.model_fields_set:
            _dict['saml20HttpPost'] = None

        # set to None if saml20_http_redirect (nullable) is None
        # and model_fields_set contains the field
        if self.saml20_http_redirect is None and "saml20_http_redirect" in self.model_fields_set:
            _dict['saml20HttpRedirect'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SsoBindingTypeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "saml20HttpPost": obj.get("saml20HttpPost"),
            "saml20HttpRedirect": obj.get("saml20HttpRedirect")
        })
        return _obj


