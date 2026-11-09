# ApiV2TestRunsByAutoTestCasesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**configuration_ids** | **[str]** | Specifies the configuration GUIDs, from which test points are created. You can specify several GUIDs. | 
**option** | [**CreateTestRunAndFillByAutoTestCasesApiModelOption**](CreateTestRunAndFillByAutoTestCasesApiModelOption.md) |  | 
**filter** | [**CreateTestRunAndFillByAutoTestCasesApiModelFilter**](CreateTestRunAndFillByAutoTestCasesApiModelFilter.md) |  | [optional] 
**name** | **str, none_type** | Specifies the name of the test run. | [optional] 
**description** | **str, none_type** | Specifies the test run description. | [optional] 
**launch_source** | **str, none_type** | Specifies the test run launch source. | [optional] 
**tags** | **[str], none_type** | Collection of tags to assign to the test run | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


