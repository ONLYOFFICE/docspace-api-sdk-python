# ChangeHistory
The parameters for changing version history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The file version of the change history. | 
**continue_version** | **bool** | Specifies whether to start a new version or continue revision of the change history. | [optional] 

## Example

```python
from docspace-api-python.models.change_history import ChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeHistory from a JSON string
change_history_instance = ChangeHistory.from_json(json)
# print the JSON string representation of the object
print(ChangeHistory.to_json())

# convert the object into a dict
change_history_dict = change_history_instance.to_dict()
# create an instance of ChangeHistory from a dict
change_history_from_dict = ChangeHistory.from_dict(change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


