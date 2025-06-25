🧠 URL Detection Using Machine Learning

This project is a lightweight web application built using Streamlit that uses a trained machine learning model to classify whether a given URL is malicious or safe.

📌 Features
✅ User-friendly web interface built with Streamlit

✅ Takes user input (URL)

✅ Classifies the URL as malicious or benign

✅ Model saved using Pickle

✅ Easy to deploy locally or on Streamlit Cloud

🧰 Tech Stack
Python 🐍

Streamlit

tensorflow

Pickle (for model serialization)

📁 Project Structure
URL-Detection-ML/
│
├── app.py                 # Streamlit UI code
├── model.pkl              # Pickled trained model
├── requirements.txt       # Dependencies
├── README.md              # You're reading this!

🚀 How to Run Locally
Clone the repository: git clone https://github.com/14shreyas04/Phishing-URL-Detection.git
                      cd url-detection-ml

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
