# streamlit 및 pytrends 라이브러리 임포트
import streamlit as st
from pytrends.request import TrendReq

# pytrends 연결 설정
pytrends = TrendReq(hl='ko-KR', tz=360)

# 구글 트렌드에서 현재 인기 검색어 상위 10개 가져오기
def get_trending_searches():
    trending_searches_df = pytrends.trending_searches(pn='south_korea')
    return trending_searches_df.head(10)

# Streamlit 앱 구성
def main():
    st.title("Google Trends: Top 10 Trending Searches")
    
    # 검색어 추출
    trending_searches = get_trending_searches()
    
    # 상위 10개의 검색어 출력
    st.subheader("Top 10 Trending Searches in the U.S.")
    st.write(trending_searches)

if __name__ == "__main__":
    main()
