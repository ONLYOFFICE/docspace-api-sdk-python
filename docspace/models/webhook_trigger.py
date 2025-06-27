# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WebhookTrigger(int, Enum):
    """
    [0 - *, 1 - user.created, 2 - user.invited, 4 - user.updated, 8 - user.deleted, 16 - group.created, 32 - group.updated, 64 - group.deleted, 128 - file.created, 256 - file.uploaded, 512 - file.updated, 1024 - file.trashed, 2048 - file.deleted, 4096 - file.restored, 8192 - file.copied, 16384 - file.moved, 32768 - folder.created, 65536 - folder.updated, 131072 - folder.trashed, 262144 - folder.deleted, 524288 - folder.restored, 1048576 - folder.copied, 2097152 - folder.moved, 4194304 - room.created, 8388608 - room.updated, 16777216 - room.archived, 33554432 - room.deleted, 67108864 - room.restored, 134217728 - room.copied]
    """

    """
    allowed enum values
    """
    All = 0
    UserCreated = 1
    UserInvited = 2
    UserUpdated = 4
    UserDeleted = 8
    GroupCreated = 16
    GroupUpdated = 32
    GroupDeleted = 64
    FileCreated = 128
    FileUploaded = 256
    FileUpdated = 512
    FileTrashed = 1024
    FileDeleted = 2048
    FileRestored = 4096
    FileCopied = 8192
    FileMoved = 16384
    FolderCreated = 32768
    FolderUpdated = 65536
    FolderTrashed = 131072
    FolderDeleted = 262144
    FolderRestored = 524288
    FolderCopied = 1048576
    FolderMoved = 2097152
    RoomCreated = 4194304
    RoomUpdated = 8388608
    RoomArchived = 16777216
    RoomDeleted = 33554432
    RoomRestored = 67108864
    RoomCopied = 134217728

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebhookTrigger from a JSON string"""
        return cls(json.loads(json_str))


