<h1 align="center">
    <img alt="Logo" src="https://media.giphy.com/media/Vh2ac0wlNuC7nz2b2N/giphy.gif" width="">
</h1>

## About
a scalable local marketplace where users post small-jobs (favours) in exchange for cash; currently in beta.
Hosted on AWS, with Docker, and using Django ORM with built-in REST API which is then consumed by Flutter for native mobile application.
## Installation

Prerequisites for installation of django web-application include Python 3.5+, and pip (package manager).

1. Fork and clone repo to local system

2. Create local virtual environment inside project directory, and activate.

```bash
python -m venv env

source env/bin/activate  # Linux/Mac
env/Scripts/activate  # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run development Django server

```bash
python manage.py runserver --settings=favours.settings.dev
```

## Deployment

Deployment is currently manual and tentative, will change whenever CI/CD is employed. Prerequisites include Docker desktop, AWS IAM credentials.

1. Using Docker CLI we will need to tag our image with our username and then push it to Dockerhub. [Reference](https://stackabuse.com/deploying-django-applications-to-aws-ec2-with-docker/).

```bash
docker login
docker tag favours <DOCKERHUB_USERNAME>/favours
docker push <DOCKERHUB_USERNAME>/favours
```

2. Connect to the AWS EC2 Linux instance using given [SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html), then pull and run the Docker container.

```bash
ssh -i /path/my-key-pair.pem my-instance-user-name@my-instance-IPv6-address
```

```bash
 docker run -d -p 8000:8000 <DOCKERHUB_USERNAME>/favours
 ```
