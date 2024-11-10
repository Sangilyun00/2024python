import streamlit as st

# 기본 웹앱 설정
st.title('🌟 나의 MBTI 상담소 🌟')
st.subheader('당신의 성격 유형에 대한 깊이 있는 분석을 제공해드립니다. 🧠💡')
st.write("이름과 MBTI 유형을 선택하고, 당신에 대한 맞춤형 코멘트를 확인해보세요! 🎉")

# 사용자 입력
name = st.text_input('이름을 입력해주세요 🖊️')
mbti = st.selectbox('MBTI를 선택해주세요 🔍', 
                    ['ENTJ', 'INTP', 'ENTP', 'INTJ', 
                     'ENFP', 'INFP', 'ENFJ', 'INFJ', 
                     'ESTP', 'ISTP', 'ESTJ', 'ISTJ', 
                     'ESFP', 'ISFP', 'ESFJ', 'ISFJ'])

# MBTI 설명 딕셔너리 생성
mbti_descriptions = {
    'ENTJ': "🔴 ENTJ - 지도자형 🔴\n강한 리더십과 추진력을 지닌 ENTJ는 목표를 향해 냉철하고 논리적인 접근을 선호합니다. 모든 일을 계획하고 실행하는 능력이 탁월하며, 주변 사람들에게 동기 부여를 줍니다. 📈👔",
    'INTP': "🔵 INTP - 논리주의자형 🔵\n호기심 많고 창의적인 사고력을 지닌 INTP는 복잡한 개념을 분석하고 이해하는 것에 큰 즐거움을 느낍니다. 조용하고 독립적인 성향으로, 자유롭게 사고하는 것을 중시합니다. 🤔🧩",
    'ENTP': "🟣 ENTP - 발명가형 🟣\n아이디어가 넘치고 혁신적인 사고를 지닌 ENTP는 자유롭고 도전적인 환경을 좋아합니다. 빠르게 상황을 파악하고, 다양한 관점에서 문제를 해결합니다. 🌍💡",
    'INTJ': "🔶 INTJ - 전략가형 🔶\n명확한 목표와 계획을 세우며, 독창적이고 논리적인 방식으로 해결책을 찾습니다. 깊이 있는 통찰력을 바탕으로 장기적인 관점에서 접근합니다. 📚🕵️‍♂️",
    # 나머지 MBTI 유형에 대한 설명도 추가 가능
}

# '확인!' 버튼 클릭 시 동작
if st.button('확인!') and name and mbti:
    st.success(f"{name}님은 정말 {mbti} 같아보이시네요! 😊")
    st.write(f"**{mbti} 유형에 대한 설명:**\n{mbti_descriptions[mbti]}")
    
    # 이모지와 함께 관련 이미지나 차트 추가
    st.write("당신의 성격에 어울리는 이미지와 더불어 맞춤형 조언도 확인해보세요! 🖼️💡")
    
    if mbti in ['ENTJ', 'INTJ', 'ENTP', 'INTP']:
        st.info("🔍 논리적이고 분석적인 성향이 돋보입니다. 전략적으로 사고하고 문제를 해결하는 능력이 뛰어납니다.")
    elif mbti in ['ENFP', 'INFP', 'ENFJ', 'INFJ']:
        st.info("🌈 감성적이며 창의력이 넘치는 성향입니다. 사람을 이해하고 공감하는 능력이 강합니다.")
    elif mbti in ['ESTP', 'ISTP', 'ESFP', 'ISFP']:
        st.info("🏃‍♂️ 실용적이고 활동적인 성향이 두드러집니다. 현실적이고 즉각적인 행동을 선호합니다.")
    elif mbti in ['ESTJ', 'ISTJ', 'ESFJ', 'ISFJ']:
        st.info("📏 체계적이며 신뢰성 높은 성향입니다. 책임감이 강하고 성실하게 목표를 달성하는 편입니다.")
