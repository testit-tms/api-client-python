# NotificationQueryFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[NotificationTypeModel]**](NotificationTypeModel.md) |  | [optional] 
**is_read** | **bool** |  | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.notification_query_filter_model import NotificationQueryFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationQueryFilterModel from a JSON string
notification_query_filter_model_instance = NotificationQueryFilterModel.from_json(json)
# print the JSON string representation of the object
print(NotificationQueryFilterModel.to_json())

# convert the object into a dict
notification_query_filter_model_dict = notification_query_filter_model_instance.to_dict()
# create an instance of NotificationQueryFilterModel from a dict
notification_query_filter_model_from_dict = NotificationQueryFilterModel.from_dict(notification_query_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


