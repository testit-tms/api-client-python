# NotificationModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_date** | **datetime** |  | [optional] 
**is_read** | **bool** |  | 
**entity_id** | **str** |  | 
**notification_type** | [**NotificationTypeModel**](NotificationTypeModel.md) |  | 
**project_global_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**test_plan_global_id** | **int** |  | 
**test_plan_name** | **str** |  | 
**workitem_global_id** | **int** |  | [optional] 
**comment** | **str** |  | 
**work_item_name** | **str** |  | 
**attribute_name** | **str** |  | [optional] 
**created_by_id** | **str** |  | 

## Example

```python
from testit_api_client.models.notification_model import NotificationModel

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationModel from a JSON string
notification_model_instance = NotificationModel.from_json(json)
# print the JSON string representation of the object
print NotificationModel.to_json()

# convert the object into a dict
notification_model_dict = notification_model_instance.to_dict()
# create an instance of NotificationModel from a dict
notification_model_from_dict = NotificationModel.from_dict(notification_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


