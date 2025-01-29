# TestPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**tester_id** | **str** |  | [optional] 
**iteration_id** | **str** |  | 
**work_item_id** | **str** |  | [optional] 
**configuration_id** | **str** |  | [optional] 
**test_suite_id** | **str** |  | 
**status** | **str** |  | [optional] 
**status_model** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | [optional] 
**last_test_result_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.test_point import TestPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TestPoint from a JSON string
test_point_instance = TestPoint.from_json(json)
# print the JSON string representation of the object
print(TestPoint.to_json())

# convert the object into a dict
test_point_dict = test_point_instance.to_dict()
# create an instance of TestPoint from a dict
test_point_from_dict = TestPoint.from_dict(test_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


