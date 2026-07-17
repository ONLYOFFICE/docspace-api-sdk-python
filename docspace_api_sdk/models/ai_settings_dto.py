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
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class AiSettingsDto(BaseModel):
    """
    The AI module settings.
    """ # noqa: E501
    web_search_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether web search is enabled for AI chat sessions.", alias="webSearchEnabled")
    web_search_need_reset: Optional[StrictBool] = Field(default=None, description="Indicates whether the web search API key needs to be reconfigured.", alias="webSearchNeedReset")
    vectorization_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether document vectorization is enabled.", alias="vectorizationEnabled")
    vectorization_need_reset: Optional[StrictBool] = Field(default=None, description="Indicates whether the embedding provider API key needs to be reconfigured.", alias="vectorizationNeedReset")
    ai_ready: Optional[StrictBool] = Field(default=None, description="Indicates whether the AI subsystem is fully configured and operational.", alias="aiReady")
    ai_ready_need_reset: Optional[StrictBool] = Field(default=None, description="Indicates whether the AI provider API key needs to be reconfigured.", alias="aiReadyNeedReset")
    portal_mcp_server_id: Optional[UUID] = Field(default=None, description="The unique identifier of the portal-level MCP server, if configured.", alias="portalMcpServerId")
    embedding_model: Optional[StrictStr] = Field(description="The name of the embedding model used for document vectorization.", alias="embeddingModel")
    model_aliases: Optional[Dict[str, StrictStr]] = Field(description="Mapping of model identifiers to human-readable aliases.", alias="modelAliases")
    knowledge_search_tool_name: Optional[StrictStr] = Field(description="The tool name used by the AI assistant for knowledge base search.", alias="knowledgeSearchToolName")
    web_search_tool_name: Optional[StrictStr] = Field(description="The tool name used by the AI assistant for web search.", alias="webSearchToolName")
    web_crawling_tool_name: Optional[StrictStr] = Field(description="The tool name used by the AI assistant for web page crawling.", alias="webCrawlingToolName")
    generate_docx_tool_name: Optional[StrictStr] = Field(description="The tool name used by the AI to launch docx creation in the editor.", alias="generateDocxToolName")
    generate_form_tool_name: Optional[StrictStr] = Field(description="The tool name used by the AI assistant to launch form creation in the editor.", alias="generateFormToolName")
    generate_presentation_tool_name: Optional[StrictStr] = Field(description="The tool name used by the AI assistant to launch presentation creation in the editor.", alias="generatePresentationToolName")
    system_ai_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the system-level AI provider is enabled.", alias="systemAiEnabled")
    recommended_model_for_forms: Optional[StrictStr] = Field(default=None, description="The identifier of the model recommended for form generation.", alias="recommendedModelForForms")
    __properties: ClassVar[List[str]] = ["webSearchEnabled", "webSearchNeedReset", "vectorizationEnabled", "vectorizationNeedReset", "aiReady", "aiReadyNeedReset", "portalMcpServerId", "embeddingModel", "modelAliases", "knowledgeSearchToolName", "webSearchToolName", "webCrawlingToolName", "generateDocxToolName", "generateFormToolName", "generatePresentationToolName", "systemAiEnabled", "recommendedModelForForms"]

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
        """Create an instance of AiSettingsDto from a JSON string"""
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
        # set to None if portal_mcp_server_id (nullable) is None
        # and model_fields_set contains the field
        if self.portal_mcp_server_id is None and "portal_mcp_server_id" in self.model_fields_set:
            _dict['portalMcpServerId'] = None

        # set to None if embedding_model (nullable) is None
        # and model_fields_set contains the field
        if self.embedding_model is None and "embedding_model" in self.model_fields_set:
            _dict['embeddingModel'] = None

        # set to None if model_aliases (nullable) is None
        # and model_fields_set contains the field
        if self.model_aliases is None and "model_aliases" in self.model_fields_set:
            _dict['modelAliases'] = None

        # set to None if knowledge_search_tool_name (nullable) is None
        # and model_fields_set contains the field
        if self.knowledge_search_tool_name is None and "knowledge_search_tool_name" in self.model_fields_set:
            _dict['knowledgeSearchToolName'] = None

        # set to None if web_search_tool_name (nullable) is None
        # and model_fields_set contains the field
        if self.web_search_tool_name is None and "web_search_tool_name" in self.model_fields_set:
            _dict['webSearchToolName'] = None

        # set to None if web_crawling_tool_name (nullable) is None
        # and model_fields_set contains the field
        if self.web_crawling_tool_name is None and "web_crawling_tool_name" in self.model_fields_set:
            _dict['webCrawlingToolName'] = None

        # set to None if generate_docx_tool_name (nullable) is None
        # and model_fields_set contains the field
        if self.generate_docx_tool_name is None and "generate_docx_tool_name" in self.model_fields_set:
            _dict['generateDocxToolName'] = None

        # set to None if generate_form_tool_name (nullable) is None
        # and model_fields_set contains the field
        if self.generate_form_tool_name is None and "generate_form_tool_name" in self.model_fields_set:
            _dict['generateFormToolName'] = None

        # set to None if generate_presentation_tool_name (nullable) is None
        # and model_fields_set contains the field
        if self.generate_presentation_tool_name is None and "generate_presentation_tool_name" in self.model_fields_set:
            _dict['generatePresentationToolName'] = None

        # set to None if recommended_model_for_forms (nullable) is None
        # and model_fields_set contains the field
        if self.recommended_model_for_forms is None and "recommended_model_for_forms" in self.model_fields_set:
            _dict['recommendedModelForForms'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "webSearchEnabled": obj.get("webSearchEnabled"),
            "webSearchNeedReset": obj.get("webSearchNeedReset"),
            "vectorizationEnabled": obj.get("vectorizationEnabled"),
            "vectorizationNeedReset": obj.get("vectorizationNeedReset"),
            "aiReady": obj.get("aiReady"),
            "aiReadyNeedReset": obj.get("aiReadyNeedReset"),
            "portalMcpServerId": obj.get("portalMcpServerId"),
            "embeddingModel": obj.get("embeddingModel"),
            "modelAliases": obj.get("modelAliases"),
            "knowledgeSearchToolName": obj.get("knowledgeSearchToolName"),
            "webSearchToolName": obj.get("webSearchToolName"),
            "webCrawlingToolName": obj.get("webCrawlingToolName"),
            "generateDocxToolName": obj.get("generateDocxToolName"),
            "generateFormToolName": obj.get("generateFormToolName"),
            "generatePresentationToolName": obj.get("generatePresentationToolName"),
            "systemAiEnabled": obj.get("systemAiEnabled"),
            "recommendedModelForForms": obj.get("recommendedModelForForms")
        })
        return _obj


