# Deploy on PythonAnywhere using the Hugging Face (HF) Inference Connection

## Before you begin

- **This activity is optional and is not required for assessment.** You can still achieve full marks for deployment by deploying an earlier version of your dynamic website that does not include the AI features.
- **Deploy a non AI version of the site first**. Follow the instructions available on Canvas and deploy a dynamic website that does not include the AI features. This initial step will allow to build knowledge incrementally.
- **Ensure that your application is fully functional when running locally using the HF Inference Connection ([see here](https://github.com/IAB207-QUT/iab207/blob/main/week12_final/hf_setup_inference.md))**. Troubleshooting during deployment can be difficult because access to logs is limited and the deployment interface is not particularly user-friendly. Verify that all functionality (including AI functionality with HF Inference Connection) works correctly before attempting deployment.

## Create a PythonAnywhere account and upload your files

- **Create your account**. Hopefully you followed the advice to initially install a non AI version of your dynamic website so you already have a [PythonAnywhere](https://www.pythonanywhere.com/) account. If not then you should create one.

- **Perhaps don't use pip freeze**. You may be tempted to use pip freeze to generate a requirements.txt file, but it records all packages installed in the current environment, including any unrelated dependencies that you installed during experimentation. For PythonAnywhere, it is often cleaner to create a fresh virtual environment and install only the packages your application actually requires using `pip`. For example, packages such as `sentence-transformers` (if you forgot to uninstall it) have very large dependencies (often exceeding 1 GB once models are downloaded).

There are two ways of uploading your files:
1. In a terminal (console) in PythonAnywhere you can use `git clone` to create a copy of your whole repository.
2. You can upload the files as a zip file using PythonAnywhere > files > upload. You can easily obtain a zip of any public folder on GitHub using [download-directory.github.io](https://download-directory.github.io/). In this example we will use the following [zip file](https://download-directory.github.io/?url=https://github.com/IAB207-QUT/iab207/tree/main/week12_final/Task3_4_with_hf/). Create a project folder and upload your zip file to it before using the `unzip filename` command to unzip.


## Configure the site to use the HF Token

Inside the package folder (e.g. travel for this example) we must create a `.env` file containing our HF Token. This can be achieved by navigating to the correct place and using the terminal text editor nano using the command `nano .env`.

Contents of `.env` should be
```
HF_API_KEY=hf_xxxxx_use_your_key_xxxxx
```

After writing the contents you can exit nano using `ctrl + x` and saving. Take note of the folder structure using the terminal command `pwd` (print working directory) as you will need it for the next step. For my example the folder structure was `home/jasonqut/travel-project/travel/` which means the exact location of the `.env` file is `home/jasonqut/travel-project/travel/nano`. Record this exact location.

**Important:** Now update the `load_dotenv()` in `__init__.py` to use an *explicit path* to the `.env` file. `load_dotenv()` becomes `load_dotenv("/home/jasonqut/travel-project/travel/.env")` (in my case).

## Create a Virtual Environment and install your requirements

Using the PythonAnywhere console, use the command `mkvirtualenv venv --python=/usr/bin/python3.13` to create a python Virtual Environment. In this case we called the virtual environment `venv` so it will be stored in `/home/<username>/.virtualenvs/venv/` or `/home/jasonqut/.virtualenvs/venv/` in my case. You need to remember the location for a later step, so perhaps navigate to ``/home/<username>/.virtualenvs/` and take a look that it is present before writing down the path for use later.

Note how your console prompt now begins with `> (venv)`. This is because the Virtual Environment was enabled automatically after installation so that you can begin installing your requirements

Next, install your requirements using pip
```
pip install flask werkzeug flask-wtf bootstrap-flask flask-sqlalchemy flask-login email-validator flask-bcrypt numpy dotenv huggingface_hub
```
You can now create your web application instance on PythonAnywhere

## Create Web App instance using PythonAnywhere dashboard

On PythonAnywhere homepage dashboard select Web Tab. Add a new web app with options:
- Flask
- Python 3.13
- Quickstart new Flask project: provide the path to the `main.py` file (in my case `/home/jasonqut/project-travel/main.py`). This is the entry point for the web application.

We now must adjust the settings of our Web App
1. Update WSGI configuration file: See section called "Code:" and click on the 3rd link down and replace the bottom line with the following code:
```
# import flask app but need to call it "application" for WSGI to work
from travel import create_app
application = create_app()
```
Don't forget to save
2. Tell the Web App to use our Virtual Environment: Return to the Web Tab and see section called "Virtualenv:" and set the path to Virtual Environment point at the one that you created. For me the path was `/home/jasonqut/.virtualenvs/venv/`.
3. Reload and test site using Green button at the top of the page and then click on the link at the top to test your site including semantic search and creating new items.









