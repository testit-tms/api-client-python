# PublicTestRunModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_run_id** | **str** |  | 
**test_plan_id** | **str** |  | [optional] 
**test_plan_global_id** | **int** |  | 
**name** | **str** |  | 
**product_name** | **str** |  | [optional] 
**build** | **str** |  | [optional] 
**configurations** | [**List[ConfigurationModel]**](ConfigurationModel.md) |  | 
**auto_tests** | [**List[AutoTestModel]**](AutoTestModel.md) |  | 
**test_points** | [**List[PublicTestPointModel]**](PublicTestPointModel.md) |  | 
**status** | **str** |  | 
**custom_parameters** | **Dict[str, str]** |  | [optional] 
**test_run_description** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.public_test_run_model import PublicTestRunModel

# TODO update the JSON string below
json = "{}"
# create an instance of PublicTestRunModel from a JSON string
public_test_run_model_instance = PublicTestRunModel.from_json(json)
# print the JSON string representation of the object
print PublicTestRunModel.to_json()

# convert the object into a dict
public_test_run_model_dict = public_test_run_model_instance.to_dict()
# create an instance of PublicTestRunModel from a dict
public_test_run_model_from_dict = PublicTestRunModel.from_dict(public_test_run_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


