import streamlit as st
from PIL import Image

# MBTI별 성격 특징 및 이미지
mbti_descriptions = {
    "INTJ": {
        "description": "INTJ는 논리적이고 계획적인 성격으로, 혁신적인 아이디어를 제시하고 독립적으로 문제를 해결하는 데 능숙합니다.",
        "image": "https://example.com/intj_image.jpg",  # 이 부분은 실제 이미지 URL로 바꿔주세요.
        "compatible": "ENTP",
        "incompatible": "ISFP"
    },
    "INTP": {
        "description": "INTP는 창의적이고 분석적인 사고를 통해 새로운 이론과 아이디어를 탐구하는 것을 좋아합니다.",
        "image": "https://example.com/intp_image.jpg",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ENTJ",
        "incompatible": "ESFJ"
    },
    "ENTJ": {
        "description": "ENTJ는 리더십이 뛰어나며 목표 지향적이고 효율적인 전략을 세워 문제를 해결하는 능력이 탁월합니다.",
        "image": "https://example.com/entj_image.jpg",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INTJ",
        "incompatible": "ISFP"
    },
    "ENTP": {
        "description": "ENTP는 창의적이고 유연한 사고를 가진 문제 해결자입니다. 대화를 통해 아이디어를 발전시키는 것을 좋아합니다.",
        "image": "https://example.com/entp_image.jpg",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INTJ",
        "incompatible": "ISFJ"
    },
    # 나머지 MBTI들도 추가해주세요
}

# Streamlit 앱
def main():
    st.title("MBTI 성격 유형과 가장 잘 어울리는 사람과 안 어울리는 사람 찾기")
    
    # MBTI 입력 받기
    mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요", list(mbti_descriptions.keys()))
    
    # 선택된 MBTI에 대한 정보 출력
    if mbti_type:
        st.subheader(f"{mbti_type} 유형 설명:")
        st.write(mbti_descriptions[mbti_type]["description"])
        
        # 이미지 출력
        image_url = mbti_descriptions[mbti_type]["image"]
        st.image(image_url, caption=f"{mbti_type} 유형", use_column_width=True)
        
        # 가장 잘 어울리는 MBTI
        compatible = mbti_descriptions[mbti_type]["compatible"]
        st.subheader(f"{compatible}와 잘 어울립니다!")
        st.write(f"{compatible}는 {mbti_type}와 비슷한 사고방식을 가지고 있어, 협력이나 대화에서 긍정적인 시너지를 낼 수 있습니다. 이들은 서로의 아이디어를 공유하고 도전하는 것을 좋아하며, 효율적인 결과를 창출할 수 있습니다.")
        
        # 이미지 출력 (잘 어울리는 유형)
        compatible_image_url = mbti_descriptions[compatible]["image"]
        st.image(compatible_image_url, caption=f"{compatible} 유형", use_column_width=True)
        
        # 가장 안 어울리는 MBTI
        incompatible = mbti_descriptions[mbti_type]["incompatible"]
        st.subheader(f"{incompatible}와는 잘 어울리지 않습니다.")
        st.write(f"{incompatible}는 {mbti_type}와 매우 다른 성격을 가지고 있어서 충돌이 발생할 수 있습니다. 서로의 가치관이나 일 처리 방식이 다르기 때문에, 협업에 어려움을 겪을 수 있습니다.")
        
        # 이미지 출력 (안 어울리는 유형)
        incompatible_image_url = mbti_descriptions[incompatible]["image"]
        st.image(incompatible_image_url, caption=f"{incompatible} 유형", use_column_width=True)

if __name__ == "__main__":
    main()
