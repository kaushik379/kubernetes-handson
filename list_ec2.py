import boto3

def list_ec2_instances():
    ec2 = boto3.client("ec2")

    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            instance_type = instance["InstanceType"]

            print(f"InstanceId: {instance_id}")
            print(f"State: {state}")
            print(f"Type: {instance_type}")
            print("-" * 40)

if __name__ == "__main__":
    list_ec2_instances() 
