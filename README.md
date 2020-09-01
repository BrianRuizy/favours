<h1 align="center">
    <img alt="Logo" src="https://media.giphy.com/media/Vh2ac0wlNuC7nz2b2N/giphy.gif" width="">
</h1>

[![Gitter chat](https://img.shields.io/badge/Chat-Gitter-FC0063.svg?label=Chat&logo=gitter)](https://gitter.im/favours-io/community#)
[![MIT License](https://camo.githubusercontent.com/a307f74a14e41e762300323414ddef81f3d53ae2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f736f757263657265722d696f2f736f757263657265722d6170702e7376673f636f6c6f72423d666630303030)](https://github.com/favours-io/favours/blob/master/LICENSE)

## About

A local marketplace where users post small-jobs (favours) in exchange for cash; currently in **beta**. Favours-io plays out in the domain of collaborative consumption. Need a favour? Or want to make some quick cash committing to a favour? The application aims at bringing local communities together by leveraging local connections you have through existing social networks. Open-source and free.

## Getting Started

### Prerequisites

- Python 3.7+
- Pip (package manager)

### Installing

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

4. Add new **.env** file, at project level. 

    Set DEBUG=True in dev. stage, and USE_S3=False to use local static files (.css, .js).
    Else, you will require AWS IAM credentials

    ```env
    DEBUG=<True or False>
    SECRET_KEY=<place-secret-key>
    AWS_STORAGE_BUCKET_NAME=favours-bucket
    USE_S3=False
    ```

5. Ready to go! Now run Django

    Note: running the Django server without the *--settings=...dev* arg will use static files from S3 bucket

    ```bash
    python manage.py runserver --settings=favours.settings.dev
    ```

## How it Works

### Components

This back-end codebase is found on on a [Linode](https://www.linode.com/) Linux server with SSH and firewalls (UFW) enabled. Running an Apache http server from Django's WSGI, and serving our static files on [AWS S3](https://aws.amazon.com/s3/). Kudos to [LetsEncrypt](https://letsencrypt.org/) for free SSL!

The goal is to then use Django's built-in REST API to be consumed by Flutter for native mobile application.

## Discussion

Discuss Favours-io in the open [Gitter chat](https://gitter.im/favours-io/community). Propose new ideas, or disuss any already existing features. All constructive conversation is welcomed!

## License
@ [MIT License](https://github.com/favours-io/favours/blob/master/LICENSE)