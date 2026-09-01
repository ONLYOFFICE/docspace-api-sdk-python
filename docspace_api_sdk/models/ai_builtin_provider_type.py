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
import json
from enum import Enum
from typing_extensions import Self


class AiBuiltinProviderType(str, Enum):
    """
    Union of all 17 built-in AI provider type identifiers.  The `external` provider has no built-in transport — it delegates every HTTP request to `PlatformAdapter.externalFetch` and parses the response with the inner provider selected by `Profile.basedOn`.
    """

    """
    allowed enum values
    """
    ANTHROPIC = 'anthropic'
    OLLAMA = 'ollama'
    OPENAI = 'openai'
    OPENAICOMPATIBLE = 'openaicompatible'
    TOGETHER = 'together'
    OPENROUTER = 'openrouter'
    GENAI = 'genai'
    DEEPSEEK = 'deepseek'
    XAI = 'xai'
    LM_MINUS_STUDIO = 'lm-studio'
    MISTRAL = 'mistral'
    GROQ = 'groq'
    ZHIPU = 'zhipu'
    STABILITYAI = 'stabilityai'
    GPT4ALL = 'gpt4all'
    ONLYOFFICE = 'onlyoffice'
    EXTERNAL = 'external'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AiBuiltinProviderType from a JSON string"""
        return cls(json.loads(json_str))

