# Push docker to google cloud registry and artefact registry
1 - Use gcp service account with less privilege principle to set the access only on the gcs bucket created (IAM gcp)

2 - To push to gcp artifact registry you need to create on GCP console a repository named "image"

3 - Grant to this repo a "artifact registry writer"

