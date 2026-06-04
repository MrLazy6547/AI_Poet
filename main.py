#from dotenv import load_dotenv 
#load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

subject = "AI"
result = chat_model.invoke(subject + "에 대한 시를 써줘.")
print(result.content)

import streamlit as st
from openai import RateLimitError

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 생성"):
    try:
        result = chat_model.invoke(subject + "에 대한 시를 써줘.")
        st.write(result.content)

    except RateLimitError:
        st.error("OpenAI API 사용량 또는 결제 한도가 부족합니다. Billing/Usage를 확인해주세요.")