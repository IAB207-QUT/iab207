# Set Up the Hugging Face (HF) Inference Connection

## Before you begin

- **This activity is optional and is not required for assessment.** You can still achieve full marks for deployment by deploying an earlier version of your dynamic website that does not include the AI features.

- **Ensure your application is fully functional when running locally** using the `all-MiniLM-L6-v2` model through the `sentence-transformers` Python library. Troubleshooting deployment issues can be difficult because access to logs is limited and the deployment interface is not particularly user-friendly. Your application must be already working end-to-end on your local machine before attempting deployment.

- **Generate as many embeddings as possible while developing locally.** In particular, create and store all event / description embeddings that will be used for similarity comparisons before deploying. The HF Inference provider incurs usage costs (albeit relatively small), so it is both more efficient and more economical to perform bulk embedding generation locally during development.

## Obtain your HF Token


