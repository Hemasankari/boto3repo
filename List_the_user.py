import boto3

client_var = boto3.client('iam',aws_access_key_id="AKIASTPYRH4UKPVZGJKW",aws_secret_access_key="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")



response = client_var.list_users()

print(response['Users'])
for i in response['Path']:
                for j in i['UserName']:
                        print(j)
                        
