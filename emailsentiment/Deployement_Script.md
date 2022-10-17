Script for creating and deploying a docker image on github

1. Create a personal access token on github
    export CR_PAT = "access token" (to add it to the environment)
    echo $CR_PAT | docker login ghcr.io -u "username" --password-stdin (to add the permissions)

2. Go to the directory which contains your dockerfile
    docker image build -t ghcr.io/"username"/"image-name":latest .

3. docker push ghcr.io/shail-1812/emailsentiment:latest (package pushed to github). In order to download the package from github you can make the package public. 

4. To run the email sentiment package run the following command
	docker run -p 5002:5002 -d ghcr.io/shail-1812/emailsentiment
