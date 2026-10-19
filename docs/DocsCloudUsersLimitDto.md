# DocsCloudUsersLimitDto
Represents the user limits of a Docs Connect license.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **int** | The maximum number of users who can edit documents. | [optional] 
**view** | **int** | The maximum number of users who can view documents. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_users_limit_dto import DocsCloudUsersLimitDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudUsersLimitDto from a JSON string
docs_cloud_users_limit_dto_instance = DocsCloudUsersLimitDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudUsersLimitDto.to_json())

# convert the object into a dict
docs_cloud_users_limit_dto_dict = docs_cloud_users_limit_dto_instance.to_dict()
# create an instance of DocsCloudUsersLimitDto from a dict
docs_cloud_users_limit_dto_from_dict = DocsCloudUsersLimitDto.from_dict(docs_cloud_users_limit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


