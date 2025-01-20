from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .migrating_api_group import MigratingApiGroup
    from .migrating_api_user import MigratingApiUser

@dataclass
class MigrationApiInfo(Parsable):
    # The errors property
    errors: Optional[List[str]] = None
    # The existUsers property
    exist_users: Optional[List[MigratingApiUser]] = None
    # The failedArchives property
    failed_archives: Optional[List[str]] = None
    # The failedUsers property
    failed_users: Optional[int] = None
    # The files property
    files: Optional[List[str]] = None
    # The groups property
    groups: Optional[List[MigratingApiGroup]] = None
    # The importCommonFiles property
    import_common_files: Optional[bool] = None
    # The importGroups property
    import_groups: Optional[bool] = None
    # The importPersonalFiles property
    import_personal_files: Optional[bool] = None
    # The importProjectFiles property
    import_project_files: Optional[bool] = None
    # The importSharedFiles property
    import_shared_files: Optional[bool] = None
    # The importSharedFolders property
    import_shared_folders: Optional[bool] = None
    # The migratorName property
    migrator_name: Optional[str] = None
    # The operation property
    operation: Optional[str] = None
    # The successedUsers property
    successed_users: Optional[int] = None
    # The users property
    users: Optional[List[MigratingApiUser]] = None
    # The withoutEmailUsers property
    without_email_users: Optional[List[MigratingApiUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MigrationApiInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MigrationApiInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MigrationApiInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .migrating_api_group import MigratingApiGroup
        from .migrating_api_user import MigratingApiUser

        from .migrating_api_group import MigratingApiGroup
        from .migrating_api_user import MigratingApiUser

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_primitive_values(str)),
            "existUsers": lambda n : setattr(self, 'exist_users', n.get_collection_of_object_values(MigratingApiUser)),
            "failedArchives": lambda n : setattr(self, 'failed_archives', n.get_collection_of_primitive_values(str)),
            "failedUsers": lambda n : setattr(self, 'failed_users', n.get_int_value()),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_primitive_values(str)),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(MigratingApiGroup)),
            "importCommonFiles": lambda n : setattr(self, 'import_common_files', n.get_bool_value()),
            "importGroups": lambda n : setattr(self, 'import_groups', n.get_bool_value()),
            "importPersonalFiles": lambda n : setattr(self, 'import_personal_files', n.get_bool_value()),
            "importProjectFiles": lambda n : setattr(self, 'import_project_files', n.get_bool_value()),
            "importSharedFiles": lambda n : setattr(self, 'import_shared_files', n.get_bool_value()),
            "importSharedFolders": lambda n : setattr(self, 'import_shared_folders', n.get_bool_value()),
            "migratorName": lambda n : setattr(self, 'migrator_name', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_str_value()),
            "successedUsers": lambda n : setattr(self, 'successed_users', n.get_int_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(MigratingApiUser)),
            "withoutEmailUsers": lambda n : setattr(self, 'without_email_users', n.get_collection_of_object_values(MigratingApiUser)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .migrating_api_group import MigratingApiGroup
        from .migrating_api_user import MigratingApiUser

        writer.write_collection_of_primitive_values("errors", self.errors)
        writer.write_collection_of_object_values("existUsers", self.exist_users)
        writer.write_collection_of_primitive_values("failedArchives", self.failed_archives)
        writer.write_int_value("failedUsers", self.failed_users)
        writer.write_collection_of_primitive_values("files", self.files)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_bool_value("importCommonFiles", self.import_common_files)
        writer.write_bool_value("importGroups", self.import_groups)
        writer.write_bool_value("importPersonalFiles", self.import_personal_files)
        writer.write_bool_value("importProjectFiles", self.import_project_files)
        writer.write_bool_value("importSharedFiles", self.import_shared_files)
        writer.write_bool_value("importSharedFolders", self.import_shared_folders)
        writer.write_str_value("migratorName", self.migrator_name)
        writer.write_str_value("operation", self.operation)
        writer.write_int_value("successedUsers", self.successed_users)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_collection_of_object_values("withoutEmailUsers", self.without_email_users)
    

