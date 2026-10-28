# FeedbackConfigDto
The settings for the Feedback & Support menu button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The absolute URL to the website address which will be opened when clicking the Feedback & Support menu button. | [optional] 
**visible** | **bool** | Whether the support button is shown. The portal always asks for it to be shown. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.feedback_config_dto import FeedbackConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackConfigDto from a JSON string
feedback_config_dto_instance = FeedbackConfigDto.from_json(json)
# print the JSON string representation of the object
print(FeedbackConfigDto.to_json())

# convert the object into a dict
feedback_config_dto_dict = feedback_config_dto_instance.to_dict()
# create an instance of FeedbackConfigDto from a dict
feedback_config_dto_from_dict = FeedbackConfigDto.from_dict(feedback_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


