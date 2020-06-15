# ThingsBoard Python REST API client


The ThingsBoard REST API Client helps you interact with [ThingsBoard REST API](https://thingsboard.io/docs/reference/rest-api/) from your Python script.  
With [Python Rest Client](https://thingsboard.io/docs/reference/python-rest-client/) you can programmatically create assets, devices, customers, users and other entities and their relations in ThingsBoard.

The recommended method for installing the Rest Client is a pip.  

*The Python version of the REST API client is under developing. If you have discovered any bug, please write us using email or by opening the issue.*


##### Installation 

In order to install the ThingsBoard REST client, you should use the following command:

```bash
pip3 install tb-rest-client
``` 


##### Examples 

You can find the examples of the usage in the "examples" folder or on the [our website](https://thingsboard.io/docs/reference/python-rest-client/).


**Note:** There are 2 REST clients for ThingsBoard, they are depend on version of the ThingsBoard, you use.  

 - If you use the ThingsBoard Community Edition (ThingsBoard CE) - please use the following command to import the REST client into your script:  
   `from tb_rest_client.rest_client_ce import *`  
   The REST client class has name "RestClientCE".  
   
 - If you use the ThingsBoard Professional Edition (ThingsBoard PE) - please use the following command to import the REST client into your script:  
   `from tb_rest_client.rest_client_pe import *`  
   The REST client class has name "RestClientPE".  

If you use the wrong version of the REST client, it could work unexpectedly.


## Support

 - [Community chat](https://gitter.im/thingsboard/chat)
 - [Q&A forum](https://groups.google.com/forum/#!forum/thingsboard)
 - [Stackoverflow](http://stackoverflow.com/questions/tagged/thingsboard)
 
**Don't forget to star the repository to show your ❤️ and support.**


## Licenses

This project is released under [Apache 2.0 License](./LICENSE).
