import boto3
import sys
from datetime import datetime, timedelta
#import boto3.ec2.cloudwatch
# https://codeandunicorns.com/get-weekly-cpu-usage-function-aws-python-lambda/
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html


def ec2_instances():

	ec2 = boto3.resource('ec2')
	  
	for instance in ec2.instances.all():
	     print(
	         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
	         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
	         )
	     )
         
        return ec2.instances.all()



def get_cpu_util(instanceID,startTime,endTime):
 
        client = boto3.client('cloudwatch')
        response = client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': instanceID
                },
            ],
             
            StartTime=startTime,
            EndTime=endTime,
            Period=86400,
            Statistics=[
                'Average',
            ],
            Unit='Percent'
        )
        print("response ",response)
      
        for k, v in response.items():
            if k == 'Datapoints':
                for y in v:
                    return "{0:.2f}".format(y['Average'])


instances = ec2_instances()


print("start time = 2020-03-04 18:06:59.258943")
print(datetime.now())

endTime=datetime.now()
endTime="2020-03-05 00:30:59.258943"
startTime="2020-03-04 18:06:59.258943"


table=[]
for instance in instances:
    tmpDict={}
    tmpDict['cpu']=get_cpu_util(instance.id,startTime,endTime)

    print("instant_id average % cpu  = ",tmpDict)
    if tmpDict:
        print(instance.tags)
        for tags in instance.tags:
            print("tags ",tags)
            try:
                if tags['Key'] == 'Name':
                  print(tags['Value'])
                  print(type(tmpDict))
                  tmpDict['Name']=tags['Value']
                  break
            except KeyError: pass
        else:
            print("Name not found")

    table.append(tmpDict)

print("######################")
print(table)
