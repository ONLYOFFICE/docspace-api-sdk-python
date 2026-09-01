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
from docspace_api_sdk.models.files_statistics_folder import FilesStatisticsFolder
from typing import Optional, Set
from typing_extensions import Self

class FilesStatisticsResultDto(BaseModel):
    """
    The file statistics result parameters.
    """ # noqa: E501
    my_documents_used_space: Optional[FilesStatisticsFolder] = Field(default=None, description="The used space of files in the \\My Documents\\ section.", alias="myDocumentsUsedSpace")
    trash_used_space: Optional[FilesStatisticsFolder] = Field(default=None, description="The used space of files in the \\Trash\\ section.", alias="trashUsedSpace")
    archive_used_space: Optional[FilesStatisticsFolder] = Field(default=None, description="The used space of files in the \\Archive\\ section.", alias="archiveUsedSpace")
    rooms_used_space: Optional[FilesStatisticsFolder] = Field(default=None, description="The used space of files in the \\Rooms\\ section.", alias="roomsUsedSpace")
    ai_agents_used_space: Optional[FilesStatisticsFolder] = Field(default=None, description="The used space of files in the \\AI agents\\ section.", alias="aiAgentsUsedSpace")
    forms_used_space: Optional[FilesStatisticsFolder] = Field(default=None, description="The used space of files in the \\Forms\\ section.", alias="formsUsedSpace")
    __properties: ClassVar[List[str]] = ["myDocumentsUsedSpace", "trashUsedSpace", "archiveUsedSpace", "roomsUsedSpace", "aiAgentsUsedSpace", "formsUsedSpace"]

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
        """Create an instance of FilesStatisticsResultDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of my_documents_used_space
        if self.my_documents_used_space:
            _dict['myDocumentsUsedSpace'] = self.my_documents_used_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trash_used_space
        if self.trash_used_space:
            _dict['trashUsedSpace'] = self.trash_used_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of archive_used_space
        if self.archive_used_space:
            _dict['archiveUsedSpace'] = self.archive_used_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rooms_used_space
        if self.rooms_used_space:
            _dict['roomsUsedSpace'] = self.rooms_used_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ai_agents_used_space
        if self.ai_agents_used_space:
            _dict['aiAgentsUsedSpace'] = self.ai_agents_used_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forms_used_space
        if self.forms_used_space:
            _dict['formsUsedSpace'] = self.forms_used_space.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FilesStatisticsResultDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "myDocumentsUsedSpace": FilesStatisticsFolder.from_dict(obj["myDocumentsUsedSpace"]) if obj.get("myDocumentsUsedSpace") is not None else None,
            "trashUsedSpace": FilesStatisticsFolder.from_dict(obj["trashUsedSpace"]) if obj.get("trashUsedSpace") is not None else None,
            "archiveUsedSpace": FilesStatisticsFolder.from_dict(obj["archiveUsedSpace"]) if obj.get("archiveUsedSpace") is not None else None,
            "roomsUsedSpace": FilesStatisticsFolder.from_dict(obj["roomsUsedSpace"]) if obj.get("roomsUsedSpace") is not None else None,
            "aiAgentsUsedSpace": FilesStatisticsFolder.from_dict(obj["aiAgentsUsedSpace"]) if obj.get("aiAgentsUsedSpace") is not None else None,
            "formsUsedSpace": FilesStatisticsFolder.from_dict(obj["formsUsedSpace"]) if obj.get("formsUsedSpace") is not None else None
        })
        return _obj


