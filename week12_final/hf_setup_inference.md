# Set Up the Hugging Face (HF) Inference Connection

## Before you begin

- **This activity is optional and is not required for assessment.** You can still achieve full marks for deployment by deploying an earlier version of your dynamic website that does not include the AI features.

- **Ensure your application is fully functional when running locally** using the `all-MiniLM-L6-v2` model through the `sentence-transformers` Python library. Troubleshooting deployment issues can be difficult because access to logs is limited and the deployment interface is not particularly user-friendly. Your application must be already working end-to-end on your local machine before attempting deployment.

- **Generate as many embeddings as possible while developing locally.** In particular, create and store all event / description embeddings that will be used for similarity comparisons before deploying. The HF Inference provider incurs usage costs (albeit relatively small), so it is both more efficient and more economical to perform bulk embedding generation locally during development.

## Obtain your HF Token

1. **Create a [Hugging Face](https://huggingface.co/) account and add $5 of credit** via the [Billing page](https://huggingface.co/settings/billing). While new accounts may receive a small amount of free credit for initial testing, adding credit is strongly recommended if you plan to complete this activity and essential if you intend to submit the AI-enabled version of your application for assessment. $5 is the minimum amount you can add and this should be more than enough for this activity. Return to the billing page to track your usage quota.
2. **Create an [Access Token]([)](https://huggingface.co/settings/tokens)** by providing a name and selecting the Inference Preset. This will allow applications using the token to make calls to Inference Providers and endpoints. Store the token in a safe place for later use.

## Configure Your Application to Use the Hugging Face Inference Provider

The goal of this section is to replace local embedding generation using the `sentence-transformers` library with remote embedding generation via the Hugging Face Inference provider. The transition requires only a small number of code changes:

1. Install the required dependencies, particularly `huggingface_hub`.
2. Store our HF Access Token as a `.env` file so it can be loaded as an environment variable when the application starts.
3. Update `__init__.py` to create an Inference Client instead of a local `SentenceTransformer` model. You will also need to store your Hugging Face API token securely using environment variables rather than hard-coding it in files that may be committed to GitHub.
4. Update the code that generates embeddings for search queries. The required changes are minimal.
5. Update the code that generates embeddings when new events or items are added. Again, only minor changes are required.

To demonstrate we shall use the travel web application from the tutorial i.e. this [start point](https://download-directory.github.io/?url=https://github.com/IAB207-QUT/iab207/tree/main/week12_final/Task3_4/).

### Step 1: Install the required dependencies

```
pip install numpy dotenv huggingface_hub
```
- *numpy*: required for our cosine similarity function. We did use this previously but didn't install as it was included automatically with sentence-transformers
- *dotenv*: allows our application to load configuration values from a .env file into environment variables when the application starts. This is useful for storing sensitive information, such as API keys, outside of the source code.
- *huggingface_hub*: the official Python library for interacting with Hugging Face services.

### Step 2: Store the HF Access Token in a `.env` file

The file should be located inside the `travel` (package) folder that contains our `__init__.py`. It should contain your HF Access Token as follows:

**contents of `.env`**
```
HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxxxxx
```
To prevent your API token from being accidientally uploaded to GitHub, ensure that the `.env` file is listed in your `.gitignore` file

**contents of `.gitignore` (at a minimum)**
```
.env
```


**Why not simply set the keys directly in the source code?**

It is a bad idea to store secrets in code files that may eventually be
committed to a repository. 

Instead, the secrets can be stored in an .env file which is loaded at runtime
with the values accessed through the operating system environment using
os.getenv().

This .env file is added to .gitignore so that it is never committed to GitHub.

On deployment, you can place the .env file on the server so long as it is
only present in the Code Project Directory (not the Static / Media Web Space
that is served bye the web server). Alternatively, some hosting platforms
have specific secret-management features that can be utilised.

### Step 3: Update `__init__.py` to create an Inference Client instead of a local SentenceTransformer model.
### Step 4: Update `views.py` > `search()` where we generate embeddings for search queries.
### Step 5: Update `destinations.py` > `create` where we generates embeddings for Destination descriptions.
