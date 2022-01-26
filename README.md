# Deploy API containerized in docker image on GCP using github actions
In this example I'll show you how to deploy an API on google cloud container registry (GCR) and artifact registry (AR).
Note that the artifact registry is just and upgraded version of GCR. So, in real life example you select only one registry solution between AR ang GCR. 


## Push docker image to GCR
1 - Create a GCP project 
2 - Enable billing on your project
3 - Enable Container Registry API
4 - Create a service account and download the json key file.
5 - Plaste the content of the service account json file on github secret named SERVICE_ACCOUNT_KEY 
6 - Make a push the run github actions workflows
7 - Use gcp service account with less privilege principle : Grant to the service account only access on the gcs bucket created on "cloud storage" IAM role. 
Required role is "Storage Admin" so that gcr can update bucket contents. 
PS : see "github/workflows/gcp.yml" to understand github actions workflow. 


## Push docker image to artifact registry
1 - You need to create on GCP console a repository named "images" as i choosed this names as repo name in my yaml file
2 - Grant to this repo a "artifact registry writer"
3 - commit and push


### Note that i created a tag at every push on the master branch. This tag name can be also seen in GCR and AR. 

Do no hesitate your any question :)  


