# UserConfig
The account the editors attribute the changes of this session to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The account the changes are recorded under. Two sessions carrying the same value are taken by the editors for  the same person. | [optional] 
**name** | **str** | The name shown next to the changes and in the list of participants. | [optional] 
**image** | **str** | An absolute address of the avatar shown for this participant. | [optional] 
**roles** | **List[str]** | The filling roles this participant holds in the form being filled out. It is set only for a form in a virtual  data room, where the role decides which fields open for them. | [optional] 
**customer_id** | **str** | Identifies the paying customer this participant belongs to, on deployments where the editors are licensed per  customer. | [optional] 

## Example

```python
from docspace_api_sdk.models.user_config import UserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UserConfig from a JSON string
user_config_instance = UserConfig.from_json(json)
# print the JSON string representation of the object
print(UserConfig.to_json())

# convert the object into a dict
user_config_dict = user_config_instance.to_dict()
# create an instance of UserConfig from a dict
user_config_from_dict = UserConfig.from_dict(user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


