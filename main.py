import json
import boto3
import uuid
import re

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    if event['path'] == "/customers":
        if event['httpMethod'] == "POST":
            guid = str(uuid.uuid4())
            payload = json.loads(event['body'])
            response = client.put_item(
                                TableName='iot-customers',
                                Item={'id':{'S':guid},'Name':{'S':payload['Name']},'Email':{'S':payload['Email']},'Phone':{'S':payload['Phone']},'Address':{'S':payload['Address']}}
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 201,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({
                        "Customer_ID": guid,
                        "Name": payload['Name'],
                        "Email": payload['Email'],
                        "Phone": payload['Phone'],
                        "Address": payload['Address']
                    })
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "GET":
            response = client.scan(TableName="iot-customers")
            customers = response['Items']
            customer_list = {}
            for i in range(len(customers)):
                customer_list[customers[i]['id']['S']]={"Name":customers[i]['Name']['S'],"Email":customers[i]['Email']['S'],"Phone":customers[i]['Phone']['S'],"Address":customers[i]['Address']['S']}
            if len(customers)>0: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps(customer_list)
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }

    if event['path'] == "/mechanics":
        if event['httpMethod'] == "POST":
            guid = str(uuid.uuid4())
            payload = json.loads(event['body'])
            response = client.put_item(
                                TableName='iot-mechanics',
                                Item={'id':{'S':guid},'Name':{'S':payload['Name']},'Email':{'S':payload['Email']},'Phone':{'S':payload['Phone']}, 'Experience':{'S':payload['Experience']},'Address':{'S':payload['Address']}}
            )
            response = 200
            if response == 200: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 201,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({
                        "Mechanic_ID": guid,
                        "Name": payload['Name'],
                        "Email": payload['Email'],
                        "Phone": payload['Phone'],
                        "Address": payload['Address'],
                        "Experience": payload['Experience']
                    })
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }  
        if event['httpMethod'] == "GET":
            response = client.scan(TableName="iot-mechanics")
            mechanics = response['Items']
            mechanics_list = {}
            for i in range(len(mechanics)):
                mechanics_list[mechanics[i]['id']['S']]={"Name":mechanics[i]['Name']['S'],"Email":mechanics[i]['Email']['S'],"Phone":mechanics[i]['Phone']['S'],"Address":mechanics[i]['Address']['S'],"Experience":mechanics[i]['Experience']['S']}
            if len(mechanics)>0: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps(mechanics_list)
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
    
    if event['path'] == "/services":
        if event['httpMethod'] == "POST":
            guid = str(uuid.uuid4())
            payload = json.loads(event['body'])
            response = client.put_item(
                                TableName='iot-services',
                                Item={'id':{'S':guid},'Type':{'S':payload['Type']},'Price':{'S':payload['Price']},'DurationInMinutes':{'S':payload['DurationInMinutes']}}
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 201,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({
                        "Service_ID": guid,
                        "Type": payload['Type'],
                        "Price": payload['Price'],
                        "DurationInMinutes": payload['DurationInMinutes']
                    })
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "GET":
            response = client.scan(TableName="iot-services")
            services = response['Items']
            services_list = {}
            for i in range(len(services)):
                services_list[services[i]['id']['S']]={"Type":services[i]['Type']['S'],"Price":services[i]['Price']['S'],"DurationInMinutes":services[i]['DurationInMinutes']['S']}
            if 1: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps(services_list)
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }



    if re.search("^/services/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",event['path']):
        guid = event['path'].split("/services/")[1]
        if event['httpMethod'] == "PUT":
            payload = json.loads(event['body'])
            response = client.put_item(
                                TableName='iot-services',
                                Item={'id':{'S':guid},'Type':{'S':payload['Type']},'Price':{'S':payload['Price']},'DurationInMinutes':{'S':payload['DurationInMinutes']}}
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({
                        "Service_ID": guid,
                        "Type": payload['Type'],
                        "Price": payload['Price'],
                        "DurationInMinutes": payload['DurationInMinutes']
                    })
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "GET":
            response = client.get_item(TableName='iot-services',Key={"id":{'S':guid}})
            services = response['Item']
            services_list = {}
            services_list[services['id']['S']]={"Type":services['Type']['S'],"Price":services['Price']['S'],"DurationInMinutes":services['DurationInMinutes']['S']}
            if 1: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps(services_list)
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "DELETE":
            response = client.delete_item(TableName='iot-services',Key={"id":{'S':guid}})
            if response['ResponseMetadata']['RequestId']: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 204,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Deleted"})
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }



    if re.search("^/customers/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",event['path']):
        guid = event['path'].split("/customers/")[1]
        if event['httpMethod'] == "PUT":
            payload = json.loads(event['body'])
            response = client.put_item(
                                TableName='iot-customers',
                                Item={'id':{'S':guid},'Name':{'S':payload['Name']},'Email':{'S':payload['Email']},'Phone':{'S':payload['Phone']},'Address':{'S':payload['Address']}}
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({
                        "Customer_ID": guid,
                        "Name": payload['Name'],
                        "Email": payload['Email'],
                        "Phone": payload['Phone'],
                        "Address": payload['Address']
                    })
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "GET":
            response = client.get_item(TableName='iot-customers',Key={"id":{'S':guid}})
            customers = response['Item']
            customers_list = {}
            customers_list[customers['id']['S']]={"Name":customers['Name']['S'],"Email":customers['Email']['S'],"Phone":customers['Phone']['S'],"Address":customers['Address']['S']}
            if 1: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps(customers_list)
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "DELETE":
            response = client.delete_item(TableName='iot-customers',Key={"id":{'S':guid}})
            if response['ResponseMetadata']['RequestId']: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 204,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Deleted"})
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }



    if re.search("^/mechanics/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",event['path']):
        guid = event['path'].split("/mechanics/")[1]
        if event['httpMethod'] == "PUT":
            payload = json.loads(event['body'])
            response = client.put_item(
                                TableName='iot-mechanics',
                                Item={'id':{'S':guid},'Name':{'S':payload['Name']},'Email':{'S':payload['Email']},'Phone':{'S':payload['Phone']}, 'Experience':{'S':payload['Experience']},'Address':{'S':payload['Address']}}
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({
                        "Mechanic_ID": guid,
                        "Name": payload['Name'],
                        "Email": payload['Email'],
                        "Phone": payload['Phone'],
                        "Address": payload['Address'],
                        "Experience": payload['Experience']
                    })
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "GET":
            response = client.get_item(TableName='iot-mechanics',Key={"id":{'S':guid}})
            mechanics = response['Item']
            mechanics_list = {}
            mechanics_list[mechanics['id']['S']]={"Name":mechanics['Name']['S'],"Email":mechanics['Email']['S'],"Phone":mechanics['Phone']['S'],"Address":mechanics['Address']['S'],"Experience":mechanics['Experience']['S']}
            if 1: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps(mechanics_list)
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }
        if event['httpMethod'] == "DELETE":
            response = client.delete_item(TableName='iot-mechanics',Key={"id":{'S':guid}})
            if response['ResponseMetadata']['RequestId']: 
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 204,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Deleted"})
                }
            else:
                return {
                    "isBase64Encoded": "false",
                    "statusCode": 500,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps({"message":"Server Error"})
                }

    return{
         "isBase64Encoded": "false",
                    "statusCode": 200,
                    "headers": { "Content-Type ": "application/json"},
                    "body": json.dumps(event)
    } 
         
