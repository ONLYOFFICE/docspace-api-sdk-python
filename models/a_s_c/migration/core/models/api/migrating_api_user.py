from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .migrating_api_files import MigratingApiFiles

@dataclass
class MigratingApiUser(Parsable):
    # The displayName property
    display_name: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The firstName property
    first_name: Optional[str] = None
    # The key property
    key: Optional[str] = None
    # The lastName property
    last_name: Optional[str] = None
    # The migratingFiles property
    migrating_files: Optional[MigratingApiFiles] = None
    # The shouldImport property
    should_import: Optional[bool] = None
    # [0 - All, 1 - Room admin, 2 - Guest, 3 - DocSpace admin, 4 - User]
    user_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MigratingApiUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MigratingApiUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MigratingApiUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .migrating_api_files import MigratingApiFiles

        from .migrating_api_files import MigratingApiFiles

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "migratingFiles": lambda n : setattr(self, 'migrating_files', n.get_object_value(MigratingApiFiles)),
            "shouldImport": lambda n : setattr(self, 'should_import', n.get_bool_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_int_value()),
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
        from .migrating_api_files import MigratingApiFiles

        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("key", self.key)
        writer.write_str_value("lastName", self.last_name)
        writer.write_object_value("migratingFiles", self.migrating_files)
        writer.write_bool_value("shouldImport", self.should_import)
        writer.write_int_value("userType", self.user_type)
    

