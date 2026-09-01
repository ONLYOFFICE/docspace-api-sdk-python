# MigrationStatusWrapper
The successful API response containing the MigrationStatusDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**MigrationStatusDto**](MigrationStatusDto.md) | The MigrationStatusDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.migration_status_wrapper import MigrationStatusWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationStatusWrapper from a JSON string
migration_status_wrapper_instance = MigrationStatusWrapper.from_json(json)
# print the JSON string representation of the object
print(MigrationStatusWrapper.to_json())

# convert the object into a dict
migration_status_wrapper_dict = migration_status_wrapper_instance.to_dict()
# create an instance of MigrationStatusWrapper from a dict
migration_status_wrapper_from_dict = MigrationStatusWrapper.from_dict(migration_status_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


