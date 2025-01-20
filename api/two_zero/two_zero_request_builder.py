from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .accounts.accounts_request_builder import AccountsRequestBuilder
    from .authentication.authentication_request_builder import AuthenticationRequestBuilder
    from .backup.backup_request_builder import BackupRequestBuilder
    from .capabilities.capabilities_request_builder import CapabilitiesRequestBuilder
    from .files.files_request_builder import FilesRequestBuilder
    from .group.group_request_builder import GroupRequestBuilder
    from .migration.migration_request_builder import MigrationRequestBuilder
    from .modules.modules_request_builder import ModulesRequestBuilder
    from .people.people_request_builder import PeopleRequestBuilder
    from .portal.portal_request_builder import PortalRequestBuilder
    from .security.security_request_builder import SecurityRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .smtpsettings.smtpsettings_request_builder import SmtpsettingsRequestBuilder

class TwoZeroRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TwoZeroRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0", path_parameters)
    
    @property
    def accounts(self) -> AccountsRequestBuilder:
        """
        The accounts property
        """
        from .accounts.accounts_request_builder import AccountsRequestBuilder

        return AccountsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication(self) -> AuthenticationRequestBuilder:
        """
        The authentication property
        """
        from .authentication.authentication_request_builder import AuthenticationRequestBuilder

        return AuthenticationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def backup(self) -> BackupRequestBuilder:
        """
        The backup property
        """
        from .backup.backup_request_builder import BackupRequestBuilder

        return BackupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def capabilities(self) -> CapabilitiesRequestBuilder:
        """
        The capabilities property
        """
        from .capabilities.capabilities_request_builder import CapabilitiesRequestBuilder

        return CapabilitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files(self) -> FilesRequestBuilder:
        """
        The files property
        """
        from .files.files_request_builder import FilesRequestBuilder

        return FilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> GroupRequestBuilder:
        """
        The group property
        """
        from .group.group_request_builder import GroupRequestBuilder

        return GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def migration(self) -> MigrationRequestBuilder:
        """
        The migration property
        """
        from .migration.migration_request_builder import MigrationRequestBuilder

        return MigrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def modules(self) -> ModulesRequestBuilder:
        """
        The modules property
        """
        from .modules.modules_request_builder import ModulesRequestBuilder

        return ModulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def people(self) -> PeopleRequestBuilder:
        """
        The people property
        """
        from .people.people_request_builder import PeopleRequestBuilder

        return PeopleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def portal(self) -> PortalRequestBuilder:
        """
        The portal property
        """
        from .portal.portal_request_builder import PortalRequestBuilder

        return PortalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security(self) -> SecurityRequestBuilder:
        """
        The security property
        """
        from .security.security_request_builder import SecurityRequestBuilder

        return SecurityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def smtpsettings(self) -> SmtpsettingsRequestBuilder:
        """
        The smtpsettings property
        """
        from .smtpsettings.smtpsettings_request_builder import SmtpsettingsRequestBuilder

        return SmtpsettingsRequestBuilder(self.request_adapter, self.path_parameters)
    

