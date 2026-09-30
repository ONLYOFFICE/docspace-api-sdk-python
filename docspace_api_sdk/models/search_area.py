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


class SearchArea(str, Enum):
    """
    [Active - Active, Archive - Archive, Any - Any, RecentByLinks - Recent by links, Templates - Template, Knowledge - Knowledge, ResultStorage - Result storage, AiAgents - AiAgents, Forms - Forms, FormTemplates - Form templates]
    """

    """
    allowed enum values
    """
    ACTIVE = 'Active'
    ARCHIVE = 'Archive'
    ANY = 'Any'
    RECENTBYLINKS = 'RecentByLinks'
    TEMPLATES = 'Templates'
    KNOWLEDGE = 'Knowledge'
    RESULTSTORAGE = 'ResultStorage'
    AIAGENTS = 'AiAgents'
    FORMS = 'Forms'
    FORMTEMPLATES = 'FormTemplates'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SearchArea from a JSON string"""
        return cls(json.loads(json_str))

