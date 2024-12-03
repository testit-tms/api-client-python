# TestPointPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tester_id** | **str** |  | [optional] 
**iteration_id** | **str** |  | 
**work_item_id** | **str** |  | [optional] 
**configuration_id** | **str** |  | [optional] 
**test_suite_id** | **str** |  | 
**status** | **str** |  | [optional] 
**status_model** | [**TestStatusModel**](TestStatusModel.md) |  | 
**last_test_result_id** | **str** |  | [optional] 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.test_point_put_model import TestPointPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointPutModel from a JSON string
test_point_put_model_instance = TestPointPutModel.from_json(json)
# print the JSON string representation of the object
print(TestPointPutModel.to_json())

# convert the object into a dict
test_point_put_model_dict = test_point_put_model_instance.to_dict()
# create an instance of TestPointPutModel from a dict
test_point_put_model_from_dict = TestPointPutModel.from_dict(test_point_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


