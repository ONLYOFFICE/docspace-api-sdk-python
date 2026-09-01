# DocsCloudUsersLimit
Represents the user limits of a DocsCloud license.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | **int** | The maximum number of users who can edit documents. | [optional] 
**view** | **int** | The maximum number of users who can view documents. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_users_limit import DocsCloudUsersLimit

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudUsersLimit from a JSON string
docs_cloud_users_limit_instance = DocsCloudUsersLimit.from_json(json)
# print the JSON string representation of the object
print(DocsCloudUsersLimit.to_json())

# convert the object into a dict
docs_cloud_users_limit_dict = docs_cloud_users_limit_instance.to_dict()
# create an instance of DocsCloudUsersLimit from a dict
docs_cloud_users_limit_from_dict = DocsCloudUsersLimit.from_dict(docs_cloud_users_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


