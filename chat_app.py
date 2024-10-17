import openai
import streamlit as st
import requests

# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# Streamlit 웹 페이지 구성
st.title("Chat with GPT-4o-mini")

# 사용자 입력 받기
user_input = st.text_input("You: ", "Hello!")

# 버튼을 클릭하면 응답 생성
if st.button("Send"):
    if user_input:
        try:
            # OpenAPI를 통해 GPT-4o-mini 모델에 요청
            response = openai.Completion.create(
                engine="gpt-4o-mini",  # GPT-4o-mini 모델 이름에 맞게 수정
                prompt=user_input,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7
            )
            
            # 모델의 응답 가져오기
            model_response = response.choices[0].text.strip()
            
            # 응답 출력
            st.text_area("GPT-4o-mini: ", model_response, height=150)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message to start the conversation.")