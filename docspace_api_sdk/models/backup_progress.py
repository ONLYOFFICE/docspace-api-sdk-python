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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.backup_progress_enum import BackupProgressEnum
from docspace_api_sdk.models.distributed_task_status import DistributedTaskStatus
from typing import Optional, Set
from typing_extensions import Self

class BackupProgress(BaseModel):
    """
    The state of one backup or restoring job.
    """ # noqa: E501
    is_completed: Optional[StrictBool] = Field(default=None, description="Specifies whether the job has stopped running. This is the field to poll: true means the job will not  change any more, whether it succeeded, failed or was cancelled, and `status` tells which of the three  it is.", alias="isCompleted", json_schema_extra={"examples": [False]})
    progress: Optional[StrictInt] = Field(default=None, description="The share of the job that is already done, from 0 to 100. A job that has only been queued reports 0,  because the work starts when a separate worker service picks it up.", json_schema_extra={"examples": [50]})
    error: Optional[StrictStr] = Field(default=None, description="The message of the error that stopped the job. It is an empty string, not null, while the job runs  and after a job that succeeded, so the sign of a failure is a non-empty value - and this is the only  place where the reason is reported.", json_schema_extra={"examples": ["An error occurred during processing"]})
    warning: Optional[StrictStr] = Field(default=None, description="A message about a job that stopped without failing: it names the entry inside the archive that lists  the files which could not be read, when a backup finished without some of them, and it says so when  the job was cancelled. It is an empty string otherwise, and it is only ever filled in for a backup  job - a cancelled restoring job leaves it empty.", json_schema_extra={"examples": ["Some files were not included in the backup. For more details, please check storage/missing_info"]})
    link: Optional[StrictStr] = Field(default=None, description="The link to download the stored archive. It is an empty string until the archive has been uploaded,  and it is only ever filled in for a backup job, never for a restoring one.", json_schema_extra={"examples": ["https://example.com/products/files/httphandlers/filehandler.ashx?action=download&fileid=1234"]})
    tenant_id: Optional[StrictInt] = Field(default=None, description="The ID of the portal the job belongs to, or -1 for a job that covers the whole server.", alias="tenantId", json_schema_extra={"examples": [1]})
    backup_progress_enum: Optional[BackupProgressEnum] = Field(default=None, description="Whether this is a backup or a restoring job, reported as a number rather than as a name.", alias="backupProgressEnum")
    status: Optional[DistributedTaskStatus] = Field(default=None, description="The state of the job: `Created` while it waits for a worker to pick it up, `Running` while it works,  `Completed` once it has finished on its own, `Canceled` after it was cancelled, and `Failted` when it  stopped on an error, in which case `error` carries the reason. Reported as a number rather than as a  name.")
    task_id: Optional[StrictStr] = Field(default=None, description="The ID of the job. It is the handle to poll this operation with, and for a backup job it also becomes  the `id` of the record in `GET api/2.0/backup/getbackuphistory`.", alias="taskId", json_schema_extra={"examples": ["11111111-1111-1111-1111-111111111111"]})
    __properties: ClassVar[List[str]] = ["isCompleted", "progress", "error", "warning", "link", "tenantId", "backupProgressEnum", "status", "taskId"]

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
        """Create an instance of BackupProgress from a JSON string"""
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
        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if warning (nullable) is None
        # and model_fields_set contains the field
        if self.warning is None and "warning" in self.model_fields_set:
            _dict['warning'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if task_id (nullable) is None
        # and model_fields_set contains the field
        if self.task_id is None and "task_id" in self.model_fields_set:
            _dict['taskId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackupProgress from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isCompleted": obj.get("isCompleted"),
            "progress": obj.get("progress"),
            "error": obj.get("error"),
            "warning": obj.get("warning"),
            "link": obj.get("link"),
            "tenantId": obj.get("tenantId"),
            "backupProgressEnum": obj.get("backupProgressEnum"),
            "status": obj.get("status"),
            "taskId": obj.get("taskId")
        })
        return _obj


