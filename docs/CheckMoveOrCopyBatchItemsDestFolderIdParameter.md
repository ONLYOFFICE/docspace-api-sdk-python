# CheckMoveOrCopyBatchItemsDestFolderIdParameter
The folder the items go to, by id — a number for a folder stored in the portal itself, a string for a folder  on a connected third-party account. Take it from a folder listing such as `GET api/2.0/files/@root`; the  caller has to be allowed to create items in it, and the id of a room addresses the root of that room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.check_move_or_copy_batch_items_dest_folder_id_parameter import CheckMoveOrCopyBatchItemsDestFolderIdParameter

# TODO update the JSON string below
json = "{}"
# create an instance of CheckMoveOrCopyBatchItemsDestFolderIdParameter from a JSON string
check_move_or_copy_batch_items_dest_folder_id_parameter_instance = CheckMoveOrCopyBatchItemsDestFolderIdParameter.from_json(json)
# print the JSON string representation of the object
print(CheckMoveOrCopyBatchItemsDestFolderIdParameter.to_json())

# convert the object into a dict
check_move_or_copy_batch_items_dest_folder_id_parameter_dict = check_move_or_copy_batch_items_dest_folder_id_parameter_instance.to_dict()
# create an instance of CheckMoveOrCopyBatchItemsDestFolderIdParameter from a dict
check_move_or_copy_batch_items_dest_folder_id_parameter_from_dict = CheckMoveOrCopyBatchItemsDestFolderIdParameter.from_dict(check_move_or_copy_batch_items_dest_folder_id_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


