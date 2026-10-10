# Set Up the Hugging Face (HF) Inference Connection

## Before you begin

- **This activity is optional and is not required for assessment.** You can still achieve full marks for deployment by deploying an earlier version of your dynamic website that does not include the AI features.

- **Ensure your application is fully functional when running locally** using the `all-MiniLM-L6-v2` model through the `sentence-transformers` Python library. Troubleshooting deployment issues can be difficult because access to logs is limited and the deployment interface is not particularly user-friendly. Your application must be already working end-to-end on your local machine before attempting deployment.

- **Generate as many embeddings as possible while developing locally.** In particular, create and store all event / description embeddings that will be used for similarity comparisons before deploying. The HF Inference provider incurs usage costs (albeit relatively small), so it is both more efficient and more economical to perform bulk embedding generation locally during development.

## Obtain your HF Token

1. **Create a [Hugging Face](https://huggingface.co/) account and add $5 of credit** via the [Billing page](https://huggingface.co/settings/billing). While new accounts may receive a small amount of free credit for initial testing, adding credit is strongly recommended if you plan to complete this activity and essential if you intend to submit the AI-enabled version of your application for assessment. $5 is the minimum amount you can add and this should be more than enough for this activity. Return to the billing page to track your usage quota.
2. **Create an [Access Token]([)](https://huggingface.co/settings/tokens)** by providing a name and selecting the Inference Preset. This will allow applications using the token to make calls to Inference Providers and endpoints. Store the token in a safe place for later use.

## Configure Your Application to Use the Hugging Face Inference Provider
The goal is to switch from using local embedding generation that uses Sentence Transformers to Hugging Face Inference. This can be achieved with the following steps:
1. Install additional dependencies (in particular huggingface_hub)
2. Update the package constructor (__init__.py) so that our encoder object is now attached to the Hugging Face Inference. We also need to be careful where we store our token as we cannot put it in code that might be committed to GithHub
3. Update the code that creates the embedding for the search query (very minor)
4. Update the code that creates the embedding when a new item is added (very minor)


## Configure Your Application to Use the Hugging Face Inference Provider

The goal of this section is to replace local embedding generation using the `sentence-transformers` library with remote embedding generation via the Hugging Face Inference provider. The transition requires only a small number of code changes:

1. Install the required dependencies, particularly `huggingface_hub`.
2. Update `__init__.py` to create an Inference Client instead of a local `SentenceTransformer` model. You will also need to store your Hugging Face API token securely using environment variables rather than hard-coding it in files that may be committed to GitHub.
3. Update the code that generates embeddings for search queries. The required changes are minimal.
4. Update the code that generates embeddings when new events or items are added. Again, only minor changes are required.

To demonstrate we shall use the travel web application from the tutorial i.e. this [start point](https://download-directory.github.io/?url=https://github.com/IAB207-QUT/iab207/tree/main/week12_final/Task3_4/).
