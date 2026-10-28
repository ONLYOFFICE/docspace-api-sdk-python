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
from docspace_api_sdk.models.ai_tool_annotations import AiToolAnnotations
from typing import Optional, Set
from typing_extensions import Self

class AiMCPItem(BaseModel):
    """
    Descriptor for a tool exposed by an MCP server.
    """ # noqa: E501
    name: StrictStr = Field(description="Tool name as registered on the MCP server (e.g. `web_search`, `insert_text`).", json_schema_extra={"examples": ["docspace_get_folder"]})
    description: StrictStr = Field(description="Human-readable description shown to the AI model and in the tools list UI.", json_schema_extra={"examples": ["Read the contents of a DocSpace folder."]})
    input_schema: Dict[str, Any] = Field(description="JSON Schema describing the tool's input parameters.", alias="inputSchema", json_schema_extra={"examples": [{"type": "object", "properties": {"folderId": {"type": "string"}}, "required": ["folderId"]}]})
    enabled: Optional[StrictBool] = Field(default=None, description="Whether this tool is currently enabled. Disabled tools are hidden from the AI model.", json_schema_extra={"examples": [True]})
    server_type: Optional[StrictStr] = Field(default=None, description="Server type (MCP server name / host tool group id) this tool belongs to — the key the persisted disabled map is stored under. Set by the source that enumerated the tool, so a caller-supplied tool can still be attributed to its group after being flattened into a single list: that is what lets the engine apply the disabled map to `actionArgs.tools` instead of trusting the caller to pre-filter. Wire-serializable, so it survives a remote (server-side) engine.", alias="serverType", json_schema_extra={"examples": ["docspace"]})
    require_approval: Optional[StrictBool] = Field(default=None, description="Whether the consumer must show an approval dialog before this tool runs. Feeds the `autoAllow` flag on a `tool-call-pending` event together with the user's tool permission mode: `false` skips the dialog under the auto mode, the default (under ask only the persisted always-allow list does), `true` and `undefined` defer to that list; allow skips it for every tool. Host tools set it and default to `false`; MCP / custom-server tools leave it unset. Wire-serializable, so it survives a remote (server-side) engine.", alias="requireApproval", json_schema_extra={"examples": [False]})
    annotations: Optional[AiToolAnnotations] = Field(default=None, description="The MCP tool annotations as the server declared them in `tools/list` (kept verbatim on the descriptor; never sent to the model). The approval flow reads two of them under the auto permission mode: `readOnlyHint: true` and `destructiveHint: false` run without the dialog, a destructive or unannotated tool keeps asking — see `resolveAutoAllow`. Wire-serializable.")
    __properties: ClassVar[List[str]] = ["name", "description", "inputSchema", "enabled", "serverType", "requireApproval", "annotations"]

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
        """Create an instance of AiMCPItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiMCPItem from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "inputSchema": obj.get("inputSchema"),
            "enabled": obj.get("enabled"),
            "serverType": obj.get("serverType"),
            "requireApproval": obj.get("requireApproval"),
            "annotations": AiToolAnnotations.from_dict(obj["annotations"]) if obj.get("annotations") is not None else None
        })
        return _obj


