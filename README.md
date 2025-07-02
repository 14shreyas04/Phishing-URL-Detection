🧠 URL Detection Using Machine Learning

This project is a lightweight web application built using Streamlit that uses a trained machine learning model to classify whether a given URL is malicious or safe.

## 🚀 Deployment (Planned)

## ⚠️ Deployment Status: Delayed

Although the project is fully functional in a local environment, deployment to Streamlit Cloud is currently on hold due to compatibility issues between:

- The TensorFlow/Keras versions used to train and save the model locally, and
- The Python and TensorFlow versions supported by Streamlit Cloud.

Specifically, the `.h5` or `.keras` model format saved using newer TensorFlow/Keras versions throws deserialization errors when loaded in the Streamlit deployment environment.

To resolve this, the model will either be:
- Re-saved using an older TensorFlow version to match Streamlit Cloud, or
- The hosted environment will be configured to support newer versions (when available).

The deployment will be finalized once this version mismatch is resolved.

📌 Features
✅ User-friendly web interface built with Streamlit

✅ Takes user input (URL)

✅ Classifies the URL as malicious or benign

✅ Model saved using Pickle

✅ Easy to deploy locally or on Streamlit Cloud

🧰 Tech Stack

  ->Python 🐍

  ->Streamlit

  ->tensorflow

  ->Pickle (for model serialization)

📁 Project Structure
Phishing-URL-Detection/

├── app.py                 # Streamlit UI code

├── model.pkl              # Pickled trained model

├── requirements.txt       # Dependencies

├── README.md              # You're reading this!

🚀 How to Run Locally
Clone the repository: 

git clone https://github.com/14shreyas04/Phishing-URL-Detection.git

cd Phishing-URL-Detection

Install dependencies: pip install -r requirements.txt

Run the app: streamlit run app.py

🌐 Deployment (Optional)

You can deploy this app easily using Streamlit Cloud.

Just upload this repo to GitHub and connect it on Streamlit Cloud!

🧠 Model Info 

Trained using: Artificial Neural Network

Features used: [http/https, ipaddress, subdomain, url_length etc....]

Accuracy: 92.36% on testing data

AUC:  97.99% on testing data

f1:  92.66% on testing data

Recall:  93.57% on testing data

Precision:  91.76% on testing data

🙌 Author
Shreyas R.

Feel free to connect or suggest improvements!
