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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.ai_builtin_provider_type import AiBuiltinProviderType
from docspace_api_sdk.models.ai_provider_type import AiProviderType
from typing import Optional, Set
from typing_extensions import Self

class AiProfile(BaseModel):
    """
    Complete AI provider + model configuration saved by the user. Profiles are the primary way users save and reuse provider configurations.
    """ # noqa: E501
    id: StrictStr = Field(description="Unique profile identifier (UUID).")
    name: StrictStr = Field(description="User-defined profile display name.")
    provider_type: AiProviderType = Field(description="Provider type for this profile. Use `external` to delegate all HTTP transport to `PlatformAdapter.externalFetch` while reusing an existing provider's response parser — see `Profile.basedOn` for the format selector.", alias="providerType")
    based_on: Optional[AiBuiltinProviderType] = Field(default=None, description="Selects the response-format parser used by the `external` provider. Ignored for any other `providerType`.  Supported values are `openai`, `anthropic`, `mistral` and `openrouter`. Remaining values (`genai`, `stabilityai`, …) are accepted by the type but not yet implemented; passing one raises an error at request time.", alias="basedOn")
    base_url: StrictStr = Field(description="Base URL of the provider API.", alias="baseUrl")
    key: Optional[StrictStr] = Field(default=None, description="API key or token. Optional for local providers.")
    headers: Optional[Dict[str, StrictStr]] = Field(default=None, description="Extra HTTP headers sent with every request to this provider. Merged into the SDK client's default headers; an explicit `Authorization` here wins over the one derived from `key`. Honoured by the OpenAI-family providers.")
    model_id: StrictStr = Field(description="Selected model ID within this provider.", alias="modelId")
    reasoning: Optional[StrictBool] = Field(default=None, description="Whether extended thinking is enabled for this profile's model.")
    capabilities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Bitmask of capabilities supported by the selected model.")
    can_use_tool: Optional[StrictBool] = Field(default=None, description="Result of the live tool-capability probe performed at create time and on changes to `modelId` / `providerType` / `baseUrl`. `undefined` means the probe has never run for this profile (legacy record).", alias="canUseTool")
    use_responses_api: Optional[StrictBool] = Field(default=None, description="Result of the live Responses-API probe (parallel to `canUseTool`). `true` means the model speaks `/v1/responses` and the OpenAI provider must route through `client.responses.create` — required for gpt-5+ reasoning models that reject `reasoning_effort` together with `tools` on `/v1/chat/completions`. Probed at create time and whenever `modelId` / `providerType` / `baseUrl` change. `undefined` means the probe never ran (legacy record) — readers treat that as `false`.", alias="useResponsesApi")
    is_cloud_provider: Optional[StrictBool] = Field(default=None, description="Whether this profile uses a cloud-hosted provider (e.g. ONLYOFFICE DocSpace).", alias="isCloudProvider")
    use_proxy: Optional[StrictBool] = Field(default=None, description="Route every provider request through the host's `fetchProxy` instead of the global `fetch`. Useful when the host runs the widget in a sandbox without direct network access (CORS, custom auth, etc.). Has no effect when the `PlatformAdapter.fetchProxy` is not configured.", alias="useProxy")
    created_at: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Creation timestamp (ms since epoch). Used to sort the AI models list newest-first.", alias="createdAt")
    __properties: ClassVar[List[str]] = ["id", "name", "providerType", "basedOn", "baseUrl", "key", "headers", "modelId", "reasoning", "capabilities", "canUseTool", "useResponsesApi", "isCloudProvider", "useProxy", "createdAt"]

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
        """Create an instance of AiProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of provider_type
        if self.provider_type:
            _dict['providerType'] = self.provider_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiProfile from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "providerType": AiProviderType.from_dict(obj["providerType"]) if obj.get("providerType") is not None else None,
            "basedOn": obj.get("basedOn"),
            "baseUrl": obj.get("baseUrl"),
            "key": obj.get("key"),
            "headers": obj.get("headers"),
            "modelId": obj.get("modelId"),
            "reasoning": obj.get("reasoning"),
            "capabilities": obj.get("capabilities"),
            "canUseTool": obj.get("canUseTool"),
            "useResponsesApi": obj.get("useResponsesApi"),
            "isCloudProvider": obj.get("isCloudProvider"),
            "useProxy": obj.get("useProxy"),
            "createdAt": obj.get("createdAt")
        })
        return _obj


