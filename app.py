import streamlit as st
import numpy as np
import re
import tldextract
from urllib.parse import urlparse
import pandas as pd
import pickle

from tensorflow.keras.models import load_model
model = load_model("model.keras")

st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")

with st.sidebar:
    st.title("🧠 About This App")
    st.write("""
    This tool uses a Machine Learning model to detect whether a URL is **phishing** or **legitimate**.
    
    📌 Paste a full URL (starting with http/https)  
    📈 Behind the scenes: Features like dots, domain, path, etc. are analyzed
    """)
    st.markdown("---")
    st.caption("Created by Shreyas R | © 2025")

st.markdown("<h1 style='text-align: center; color: teal;'>🔍 Phishing URL Detection</h1>", unsafe_allow_html=True)

url = st.text_input("🌐 Enter a URL (e.g., https://example.com): 🚨⚠️ Please copy paste the url, don't click it while copying")

def extract_features(url):
    o = urlparse(url)
    ex = tldextract.extract(url)
    pattern_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    pattern_num = r"\d"
    res = re.findall(pattern_ip, url)
    senwords = ['login','username','id','password','admin','account','signin','auth','dashboard','logout','forget-password','change-password','bank']

    def senword(ur):
        coun = 0
        for i in senwords:
            if i in ur:
                coun+=1
        
        return coun

    result = senword(url)

    return pd.DataFrame([{
        'NumDots': url.count('.'),
        'SubdomainLevel': len(ex.subdomain.split('.')),
        'PathLevel': o.path.count('/'),
        'UrlLength': len(url),
        'NumDash': url.count('-'),
        'NumDashInHostname': o.hostname.count('-') if o.hostname else 0,
        'AtSymbol': 1 if url.count('@')>=1 else 0,
        'TildeSymbol': 1 if url.count('~')>=1 else 0,
        'NumUnderscore': url.count('_'),
        'NumPercent': url.count('%'),
        'NumQueryComponents': len(o.query.split('&')) if o.query else 0,
        'NumAmpersand': url.count('&'),
        'NumNumericChars': len(re.findall(pattern_num, url)),
        'NoHttps': 1 if o.scheme == 'http' else 0,
        'IpAddress': 1 if res else 0,
        'HttpsInHostname': int('https' in o.hostname) if o.hostname else 0,
        'HostnameLength': len(o.hostname) if o.hostname else 0,
        'PathLength': len(o.path),
        'QueryLength': len(o.query),
        'DoubleSlashInPath': 1 if o.path.count('//') else 0,
        'NumSensitiveWords': result
    }])

if st.button("🚀 Analyze URL"):
    if url == "":
        st.warning("Please enter a URL before clicking 'Analyze'")
    elif not url.startswith(("http://", "https://")):
        st.error("⚠️ URL must start with http:// or https://")
    else:
        df = extract_features(url)
        prediction = model.predict(df)
        result = round(prediction[0][0]) if isinstance(prediction[0], (list, np.ndarray)) else int(prediction[0])

        st.markdown("---")
        st.subheader("🔐 Prediction Result:")

        if result == 1:
            st.error("🚨 This URL is classified as **Phishing**!")
        else:
            st.success("✅ This URL is classified as **Safe**.")
