# LoginEventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**user** | **str** | User | [optional] 
**user_id** | **str** | User ID | [optional] 
**login** | **str** | Login | [optional] 
**action** | **str** | Action | [optional] 
**action_id** | [**MessageAction**](MessageAction.md) |  | [optional] 
**ip** | **str** | IP | [optional] 
**country** | **str** | Country | [optional] 
**city** | **str** | City | [optional] 
**browser** | **str** | Browser | [optional] 
**platform** | **str** | Platform | [optional] 
**page** | **str** | Page | [optional] 

## Example

```python
from docspace.models.login_event_dto import LoginEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginEventDto from a JSON string
login_event_dto_instance = LoginEventDto.from_json(json)
# print the JSON string representation of the object
print(LoginEventDto.to_json())

# convert the object into a dict
login_event_dto_dict = login_event_dto_instance.to_dict()
# create an instance of LoginEventDto from a dict
login_event_dto_from_dict = LoginEventDto.from_dict(login_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


