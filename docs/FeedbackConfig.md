# FeedbackConfig
The settings for the \"Feedback & Support\" menu button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The absolute URL to the website address which will be opened when clicking the \&quot;Feedback &amp; Support\&quot; menu button. | [optional] 
**visible** | **bool** | Shows or hides the \&quot;Feedback &amp; Support\&quot; menu button. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.feedback_config import FeedbackConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackConfig from a JSON string
feedback_config_instance = FeedbackConfig.from_json(json)
# print the JSON string representation of the object
print(FeedbackConfig.to_json())

# convert the object into a dict
feedback_config_dict = feedback_config_instance.to_dict()
# create an instance of FeedbackConfig from a dict
feedback_config_from_dict = FeedbackConfig.from_dict(feedback_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


