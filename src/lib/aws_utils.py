import boto

class AwsUtils(object): 
	def __init__(self, instance):
		c = boto.connect_ec2()
		reservations = c.get_all_instances([instance])
		self.details = reservations[0].instances[0]

	def get_tags(self):
		return self.details.tags
