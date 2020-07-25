<h1 align="center">
    <img alt="Logo" src="https://github.com/BrianRuizy/favours/blob/master/favours/static/assets/favours_light.png" width="100"> </br>
    Favours
</h1>

## Installation

Prerequisites for installation django web-application include Python 3.7+, and pip.

1. Fork and clone repo to local system

```bash
git clone https://github.com/<your-username>/favours.git
```

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