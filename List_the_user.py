import boto3

client_var = boto3.client('iam',aws_access_key_id="AKIAYTCSR333HP7F24FM",aws_secret_access_key="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")



response = client_var.list_users()

print(response['Users'])
for i in response['Path']:
                for j in i['UserName']:
                        print(j)
                        