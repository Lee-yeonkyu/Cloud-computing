# function_defi 정의
# 실제 구현 func 동작부분, 기능에 대한 함수를 모아놨음
import boto3

ec2 = boto3.resource("ec2")
ec2client = boto3.client("ec2")
keypairinfo = ec2client.describe_key_pairs()


# 메뉴 기능 구현 부분
def ListInstance():
    print("\n")
    print("ListInstance\n")
    for instance in ec2.instances.all():
        print(
            "[Instance ID] " + instance.instance_id,
            " [Instance Name] " + instance.state.get("Name"),
            " [Instance Type] " + instance.instance_type,
            " [Instance Image ID] " + instance.image_id,
            " [Instance State] " + instance.monitoring.get("State"),
        )


def AvailableZone():
    print("\n")
    print("AvailableZone\n")
    available_region = ec2client.describe_availability_zones()
    RegionArr = available_region.get("AvailabilityZones")
    for ReginInfo in RegionArr:
        print(
            "[id] " + ReginInfo.get("ZoneId"),
            " [region] " + ReginInfo.get("RegionName"),
            " [zone] " + ReginInfo.get("ZoneName"),
        )


def StartInstance():
    print("\n")
    print("StartInstance\n")
    forSelectInstance()
    selectid = str(input("Enter instance id : "))
    result = ec2client.start_instances(
        InstanceIds=[
            selectid,
        ],
    )
    print(result)


def AvailableRegions():
    print("\n")
    print("AvailableRegions\n")
    AvailaleRegionArr = ec2client.describe_regions().get("Regions")
    for RegionInfo in AvailaleRegionArr:
        print(
            "[Region] " + RegionInfo.get("RegionName"),
            " [endpoint] " + RegionInfo.get("Endpoint"),
        )


def StopInstance():
    print("\n")
    print("StopInstance\n")
    forSelectInstance()
    selectid = str(input("Enter instance id : "))
    result = ec2client.stop_instances(
        InstanceIds=[
            selectid,
        ],
    )
    print(result)


def CreateInstance():
    print("\n")
    print("CreateInstance\n")
    print("EC2 인스턴스 생성중..")

    ec2client.run_instances(
        ImageId="ami-0d718c3d715cec4a7",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="aws1",
    )
    print(
        ec2client.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"]
        + "인스턴스 생성 완료"
    )


def RebootInstance():
    print("\n")
    print("RebootInstance\n")
    forSelectInstance()
    selectid = str(input("Enter instance id : "))
    response = ec2client.reboot_instances(
        InstanceIds=[
            selectid,
        ],
    )
    print(response)


def ListImages():
    print("\n")
    print("ListImages\n")
    amiImage = ec2client.describe_images(Owners=["self"])
    for image in amiImage["Images"]:
        print(
            "[ImageID] " + image["ImageId"],
            " [Name] " + image["Name"],
            " [Owner] " + image["OwnerId"],
        )


# 기능함수 보조
# 간단한 인스턴스 및 / 이미지 출력 리스트 함수 구현, 메뉴화면 구성 부분
def forSelectInstance():
    print("----------------------------------------------------------\n")
    print("-------------------인스턴스 리스트------------------------\n")
    for instance in ec2.instances.all():
        print(
            "[Instance ID] " + instance.instance_id,
            " [Instance Name] " + instance.state.get("Name"),
        )
    print("----------------------------------------------------------\n")
    print("----------------------------------------------------------\n")
