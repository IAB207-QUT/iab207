# Deploy on PythonAnywhere using the Hugging Face (HF) Inference Connection

## Before you begin

- **This activity is optional and is not required for assessment.** You can still achieve full marks for deployment by deploying an earlier version of your dynamic website that does not include the AI features.
- **Deploy a non AI version of the site first**. Follow the instructions available on Canvas and deploy a dynamic website that does not include the AI features. This initial step will allow to build knowledge incrementally.
- **Ensure that your application is fully functional when running locally using the HF Inference Connection ([see here](https://github.com/IAB207-QUT/iab207/blob/main/week12_final/hf_setup_inference.md))**. Troubleshooting during deployment can be difficult because access to logs is limited and the deployment interface is not particularly user-friendly. Verify that all functionality (including AI functionality with HF Inference Connection) works correctly before attempting deployment.

---

## Create a PythonAnywhere account and upload your files

- **Create your account**. Hopefully you followed the advice to initially install a non AI version of your dynamic website so you already have a [PythonAnywhere](https://www.pythonanywhere.com/) account. If not then you should create one.

- **Perhaps don't use pip freeze**. You may be tempted to use pip freeze to generate a requirements.txt file, but it records all packages installed in the current environment, including any unrelated dependencies that you installed during experimentation. For PythonAnywhere, it is often cleaner to create a fresh virtual environment and install only the packages your application actually requires using `pip`. For example, packages such as `sentence-transformers` (if you forgot to uninstall it) have very large dependencies (often exceeding 1 GB once models are downloaded).

There are two ways of uploading your files:
1. In a terminal (console) in PythonAnywhere you can use `git clone` to create a copy of your whole repository.
2. You can upload the files as a zip file using PythonAnywhere > files > upload. You can easily obtain a zip of any public folder on GitHub using [download-directory.github.io](https://download-directory.github.io/). In this example we will use the following [zip file](https://download-directory.github.io/?url=https://github.com/IAB207-QUT/iab207/tree/main/week12_final/Task3_4_with_hf/).


## Configure the site to use our HF Token

Inside the package folder (e.g. travel for this example) we must create a `.env` file containing our HF Token. This can be achieved by navigating to the correct place and using the terminal text editor nano using the command `nano .env`.

Contents of `.env` should be
```
HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxxxxx
```

After writing the contents you can exit nano using `ctrl + x` and saving. Take note of the folder structure using the terminal command `pwd` (print working directory) as you will need it for the next step. For my example the folder structure was `home/jasonqut/travel-project/travel/` which means the exact location of the `.env` file is `home/jasonqut/travel-project/travel/nano`. Record this exact location.

**Important:** Now update the `` in `__init__.py` with this *explicit path* to the .env file e.g. `load_dotenv()` becomes `load_dotenv("/home/jasonqut/travel-project/travel/.env")` in my case.






