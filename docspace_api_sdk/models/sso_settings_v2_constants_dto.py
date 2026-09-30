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
from docspace_api_sdk.models.sso_binding_type_dto import SsoBindingTypeDto
from docspace_api_sdk.models.sso_encrypt_algorithm_type_dto import SsoEncryptAlgorithmTypeDto
from docspace_api_sdk.models.sso_idp_certificate_action_type_dto import SsoIdpCertificateActionTypeDto
from docspace_api_sdk.models.sso_name_id_format_type_dto import SsoNameIdFormatTypeDto
from docspace_api_sdk.models.sso_signing_algorithm_type_dto import SsoSigningAlgorithmTypeDto
from docspace_api_sdk.models.sso_sp_certificate_action_type_dto import SsoSpCertificateActionTypeDto
from typing import Optional, Set
from typing_extensions import Self

class SsoSettingsV2ConstantsDto(BaseModel):
    """
    The SSO settings constants: every value the settings accept, by name.
    """ # noqa: E501
    sso_name_id_format_type: Optional[SsoNameIdFormatTypeDto] = Field(default=None, description="The values the `nameIdFormat` of the identity provider settings accepts. The built-in configuration uses  the SAML 2.0 transient format.", alias="ssoNameIdFormatType")
    sso_binding_type: Optional[SsoBindingTypeDto] = Field(default=None, description="The values the `ssoBinding` and `sloBinding` of the identity provider settings accept - how the portal  sends its sign-in and sign-out requests. The built-in configuration uses HTTP POST for both.", alias="ssoBindingType")
    sso_signing_algorithm_type: Optional[SsoSigningAlgorithmTypeDto] = Field(default=None, description="The values the `signingAlgorithm` of the service provider certificate and the `verifyAlgorithm` of the  identity provider certificate accept. The built-in configuration uses RSA-SHA1 for both.", alias="ssoSigningAlgorithmType")
    sso_encrypt_algorithm_type: Optional[SsoEncryptAlgorithmTypeDto] = Field(default=None, description="The values the `encryptAlgorithm` and `decryptAlgorithm` of the certificate settings accept. The built-in  configuration uses AES-128 everywhere.", alias="ssoEncryptAlgorithmType")
    sso_sp_certificate_action_type: Optional[SsoSpCertificateActionTypeDto] = Field(default=None, description="The values the `action` of a service provider certificate accepts, which is what the portal's own key  pair may be used for.", alias="ssoSpCertificateActionType")
    sso_idp_certificate_action_type: Optional[SsoIdpCertificateActionTypeDto] = Field(default=None, description="The values the `action` of an identity provider certificate accepts, which is what the provider's  certificate may be used for - the mirror image of the service provider actions.", alias="ssoIdpCertificateActionType")
    __properties: ClassVar[List[str]] = ["ssoNameIdFormatType", "ssoBindingType", "ssoSigningAlgorithmType", "ssoEncryptAlgorithmType", "ssoSpCertificateActionType", "ssoIdpCertificateActionType"]

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
        """Create an instance of SsoSettingsV2ConstantsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sso_name_id_format_type
        if self.sso_name_id_format_type:
            _dict['ssoNameIdFormatType'] = self.sso_name_id_format_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sso_binding_type
        if self.sso_binding_type:
            _dict['ssoBindingType'] = self.sso_binding_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sso_signing_algorithm_type
        if self.sso_signing_algorithm_type:
            _dict['ssoSigningAlgorithmType'] = self.sso_signing_algorithm_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sso_encrypt_algorithm_type
        if self.sso_encrypt_algorithm_type:
            _dict['ssoEncryptAlgorithmType'] = self.sso_encrypt_algorithm_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sso_sp_certificate_action_type
        if self.sso_sp_certificate_action_type:
            _dict['ssoSpCertificateActionType'] = self.sso_sp_certificate_action_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sso_idp_certificate_action_type
        if self.sso_idp_certificate_action_type:
            _dict['ssoIdpCertificateActionType'] = self.sso_idp_certificate_action_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SsoSettingsV2ConstantsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ssoNameIdFormatType": SsoNameIdFormatTypeDto.from_dict(obj["ssoNameIdFormatType"]) if obj.get("ssoNameIdFormatType") is not None else None,
            "ssoBindingType": SsoBindingTypeDto.from_dict(obj["ssoBindingType"]) if obj.get("ssoBindingType") is not None else None,
            "ssoSigningAlgorithmType": SsoSigningAlgorithmTypeDto.from_dict(obj["ssoSigningAlgorithmType"]) if obj.get("ssoSigningAlgorithmType") is not None else None,
            "ssoEncryptAlgorithmType": SsoEncryptAlgorithmTypeDto.from_dict(obj["ssoEncryptAlgorithmType"]) if obj.get("ssoEncryptAlgorithmType") is not None else None,
            "ssoSpCertificateActionType": SsoSpCertificateActionTypeDto.from_dict(obj["ssoSpCertificateActionType"]) if obj.get("ssoSpCertificateActionType") is not None else None,
            "ssoIdpCertificateActionType": SsoIdpCertificateActionTypeDto.from_dict(obj["ssoIdpCertificateActionType"]) if obj.get("ssoIdpCertificateActionType") is not None else None
        })
        return _obj


