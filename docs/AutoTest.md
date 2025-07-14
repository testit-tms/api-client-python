# AutoTest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | External ID of the autotest | 
**links** | [**List[Link]**](Link.md) | Collection of the autotest links | [optional] 
**project_id** | **str** | Unique ID of the autotest project | 
**name** | **str** | Name of the autotest | 
**namespace** | **str** | Name of the autotest namespace | [optional] 
**classname** | **str** | Name of the autotest class | [optional] 
**steps** | [**List[AutoTestStep]**](AutoTestStep.md) | Collection of the autotest steps | [optional] 
**setup** | [**List[AutoTestStep]**](AutoTestStep.md) | Collection of the autotest setup steps | [optional] 
**teardown** | [**List[AutoTestStep]**](AutoTestStep.md) | Collection of the autotest teardown steps | [optional] 
**title** | **str** | Name of the autotest in autotest&#39;s card | [optional] 
**description** | **str** | Description of the autotest in autotest&#39;s card | [optional] 
**labels** | [**List[Label]**](Label.md) | Collection of the autotest labels | [optional] 
**is_flaky** | **bool** | Indicates if the autotest is marked as flaky | [optional] 
**external_key** | **str** | External key of the autotest | [optional] 
**global_id** | **int** | Global ID of the autotest | 
**is_deleted** | **bool** | Indicates if the autotest is deleted | 
**must_be_approved** | **bool** | Indicates if the autotest has unapproved changes from linked work items | 
**id** | **str** | Unique ID of the autotest | 
**created_date** | **datetime** | Creation date of the autotest | 
**modified_date** | **datetime** | Last modification date of the project | [optional] 
**created_by_id** | **str** | Unique ID of the project creator | 
**modified_by_id** | **str** | Unique ID of the project last editor | [optional] 
**last_test_run_id** | **str** | Unique ID of the autotest last test run | [optional] 
**last_test_run_name** | **str** | Name of the autotest last test run | [optional] 
**last_test_result_id** | **str** | Unique ID of the autotest last test result | [optional] 
**last_test_result_configuration** | [**ConfigurationShort**](ConfigurationShort.md) | Configuration of the autotest last test result | [optional] 
**last_test_result_outcome** | **str** | Outcome of the autotest last test result | [optional] 
**stability_percentage** | **int** | Stability percentage of the autotest | [optional] 

## Example

```python
from testit_api_client.models.auto_test import AutoTest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTest from a JSON string
auto_test_instance = AutoTest.from_json(json)
# print the JSON string representation of the object
print AutoTest.to_json()

# convert the object into a dict
auto_test_dict = auto_test_instance.to_dict()
# create an instance of AutoTest from a dict
auto_test_from_dict = AutoTest.from_dict(auto_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


