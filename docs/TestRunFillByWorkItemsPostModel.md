# TestRunFillByWorkItemsPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_ids** | **[str]** | Specifies the configuration GUIDs, from which test points are created. You can specify several GUIDs. | 
**work_item_ids** | **[str]** | Specifies the work item GUIDs, from which test points are created. You can specify several GUIDs. | 
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**test_plan_id** | **str** | Specifies the GUID of the test plan, within which the test run will be created. | 
**name** | **str, none_type** | Specifies the name of the test run. | [optional] 
**description** | **str, none_type** | Specifies the test run description. | [optional] 
**launch_source** | **str, none_type** | Specifies the test run launch source. | [optional] 
**attachments** | [**[AttachmentPutModel], none_type**](AttachmentPutModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**[LinkPostModel], none_type**](LinkPostModel.md) | Collection of links to relate to the test run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


