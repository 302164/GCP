from google.cloud import pubsub_v1


def hello_pub(event, context):
	"""Triggered by a change to a Cloud Storage bucket.
	Args:
     	event (dict): Event payload.
     	context (google.cloud.functions.Context): Metadata for the event.
	"""
	project_id = "gcp-project2-266914"
	topic_name = "Guixiajiaobaba"
	publisher = pubsub_v1.PublisherClient()
	file = event
	print(f"Processing file: {file['name']}.")
	# The topic_path method creates a fully qualified identifier
	# in the form projects/{project_id}/topics/{topic_name}
	topic_path = publisher.topic_path(project_id, topic_name)
	data = f"Processing file: {file['name']}."
	# Data must be a bytestring
	data = data.encode("utf-8")
	# When you publish a message, the client returns a future.
	future = publisher.publish(topic_path, data=data)
	print(future.result())

