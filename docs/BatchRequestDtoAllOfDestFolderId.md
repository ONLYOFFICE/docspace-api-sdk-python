# BatchRequestDtoAllOfDestFolderId
The folder the items go to, by id — a number for a folder stored in the portal itself, a string for a folder  on a connected third-party account. Take it from a folder listing such as `GET api/2.0/files/@root`; the  caller has to be allowed to create items in it, and the id of a room addresses the root of that room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.batch_request_dto_all_of_dest_folder_id import BatchRequestDtoAllOfDestFolderId

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRequestDtoAllOfDestFolderId from a JSON string
batch_request_dto_all_of_dest_folder_id_instance = BatchRequestDtoAllOfDestFolderId.from_json(json)
# print the JSON string representation of the object
print(BatchRequestDtoAllOfDestFolderId.to_json())

# convert the object into a dict
batch_request_dto_all_of_dest_folder_id_dict = batch_request_dto_all_of_dest_folder_id_instance.to_dict()
# create an instance of BatchRequestDtoAllOfDestFolderId from a dict
batch_request_dto_all_of_dest_folder_id_from_dict = BatchRequestDtoAllOfDestFolderId.from_dict(batch_request_dto_all_of_dest_folder_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


