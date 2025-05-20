import streamlit as st

# MBTI별 성격 특징 및 이미지
mbti_descriptions = {
    "INTJ": {
        "description": "INTJ는 논리적이고 계획적인 성격으로, 혁신적인 아이디어를 제시하고 독립적으로 문제를 해결하는 데 능숙합니다.",
        "image": "https://via.placeholder.com/150?text=INTJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ENTP",
        "incompatible": "ESFP"
    },
    "INTP": {
        "description": "INTP는 창의적이고 분석적인 사고를 통해 새로운 이론과 아이디어를 탐구하는 것을 좋아합니다.",
        "image": "https://via.placeholder.com/150?text=INTP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ENTJ",
        "incompatible": "ESFJ"
    },
    "ENTJ": {
        "description": "ENTJ는 리더십이 뛰어나며 목표 지향적이고 효율적인 전략을 세워 문제를 해결하는 능력이 탁월합니다.",
        "image": "https://via.placeholder.com/150?text=ENTJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INTJ",
        "incompatible": "ISFP"
    },
    "ENTP": {
        "description": "ENTP는 창의적이고 유연한 사고를 가진 문제 해결자입니다. 대화를 통해 아이디어를 발전시키는 것을 좋아합니다.",
        "image": "https://via.placeholder.com/150?text=ENTP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INTJ",
        "incompatible": "ISFJ"
    },
    "INFJ": {
        "description": "INFJ는 깊은 통찰력과 공감 능력을 지닌 사람들로, 자신의 가치와 목표를 위해 헌신적으로 노력합니다.",
        "image": "https://via.placeholder.com/150?text=INFJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ENFP",
        "incompatible": "ESTP"
    },
    "INFP": {
        "description": "INFP는 이상적이고, 깊은 감정을 가진 사람들로, 자신의 가치관을 중시하며 예술적이고 창의적인 면이 강합니다.",
        "image": "https://via.placeholder.com/150?text=INFP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ENFJ",
        "incompatible": "ESTJ"
    },
    "ENFJ": {
        "description": "ENFJ는 타인을 이끄는 능력이 뛰어나며, 공감 능력이 매우 높고 사람들의 성장과 발전을 도울 수 있습니다.",
        "image": "https://via.placeholder.com/150?text=ENFJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INFJ",
        "incompatible": "ISTP"
    },
    "ENFP": {
        "description": "ENFP는 창의적이고 열정적인 성격을 가진 사람들로, 새로운 아이디어와 가능성에 끊임없이 탐구합니다.",
        "image": "https://via.placeholder.com/150?text=ENFP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INFJ",
        "incompatible": "ISTJ"
    },
    "ISFJ": {
        "description": "ISFJ는 따뜻하고 신뢰할 수 있는 사람들로, 실용적이고 세심하게 주변 사람들을 돌보는 경향이 있습니다.",
        "image": "https://via.placeholder.com/150?text=ISFJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ESFP",
        "incompatible": "ENTP"
    },
    "ISFP": {
        "description": "ISFP는 자유롭고 창의적인 성격을 가진 사람들로, 예술적이고 감성적인 면이 강합니다.",
        "image": "https://via.placeholder.com/150?text=ISFP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ESFJ",
        "incompatible": "ENTJ"
    },
    "ESFJ": {
        "description": "ESFJ는 사람들을 돌보며, 조직적인 일처리를 잘 하고 타인과의 관계에서 만족을 느끼는 성격입니다.",
        "image": "https://via.placeholder.com/150?text=ESFJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ISFJ",
        "incompatible": "INTP"
    },
    "ESFP": {
        "description": "ESFP는 외향적이고, 감각적이며, 사람들과 함께 하는 것을 좋아하는 즐거운 성격을 가지고 있습니다.",
        "image": "https://via.placeholder.com/150?text=ESFP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ISFJ",
        "incompatible": "INTJ"
    },
    "ISTJ": {
        "description": "ISTJ는 실용적이고 조직적인 성격을 가진 사람들로, 책임감을 가지고 일을 정확히 처리하는 데 능숙합니다.",
        "image": "https://via.placeholder.com/150?text=ISTJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ESTJ",
        "incompatible": "ENFP"
    },
    "ISTP": {
        "description": "ISTP는 독립적이고, 실용적인 성격을 가진 사람들로, 기술적인 문제 해결에 뛰어납니다.",
        "image": "https://via.placeholder.com/150?text=ISTP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ESTP",
        "incompatible": "ENFJ"
    },
    "ESTJ": {
        "description": "ESTJ는 실용적이고 체계적인 성격을 가진 사람들로, 규칙과 질서를 중시하고 효율성을 추구합니다.",
        "image": "https://via.placeholder.com/150?text=ESTJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ISTJ",
        "incompatible": "INFP"
    },
    "ESTP": {
        "description": "ESTP는 외향적이고 실용적인 문제 해결 능력이 뛰어난 사람들로, 모험을 즐기고 즉각적인 결과를 중시합니다.",
        "image": "https://via.placeholder.com/150?text=ESTP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ISTP",
        "incompatible": "INFJ"
    }
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
        st.write(f"{compatible}는 {mbti_type}와 비슷한 사고방식을 가지고 있어, 협력이나 대화에서 긍정적인 시너지를 낼 수 있습니다.")
        
        # 이미지 출력 (잘 어울리는 유형)
        compatible_image_url = mbti_descriptions[compatible]["image"]
        st.image(compatible_image_url, caption=f"{compatible} 유형", use_column_width=True)
        
        # 가장 안 어울리는 MBTI
        incompatible = mbti_descriptions[mbti_type]["incompatible"]
        st.subheader(f"{incompatible}와는 잘 어울리지 않습니다.")
        st.write(f"{incompatible}는 {mbti_type}와 매우 다른 성격을 가지고 있어서 충돌이 발생할 수 있습니다.")
        
        # 이미지 출력 (안 어울리는 유형)
        incompatible_image_url = mbti_descriptions[incompatible]["image"]
        st.image(incompatible_image_url, caption=f"{incompatible} 유형", use_column_width=True)

if __name__ == "__main__":
    main()

import streamlit as st

# MBTI별 성격 특징 및 이미지
mbti_descriptions = {
    "INTJ": {
        "description": "INTJ는 독립적이고 계획적인 성격을 가진 사람들로, 미래에 대한 비전과 전략을 세우는 데 능숙합니다. 혁신적이고 논리적인 사고를 통해 문제를 해결하려 합니다.",
        "image": "https://via.placeholder.com/150?text=INTJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ENTP",
        "incompatible": "ESFP",
        "compatibility_reason": "ENTP는 INTJ의 혁신적인 사고와 아이디어를 받아들이고 발전시킬 수 있는 능력을 가집니다. 둘은 서로의 비전을 현실화하려고 협력할 수 있습니다.",
        "incompatibility_reason": "ESFP는 감각적이고 즉흥적인 성격을 가지고 있어, 계획적이고 논리적인 INTJ와 충돌이 일어날 수 있습니다. ESFP는 INTJ의 깊은 사고를 이해하기 어려울 수 있습니다."
    },
    "INTP": {
        "description": "INTP는 논리적이고 분석적인 성격을 가진 사람들로, 이론을 탐구하고 문제를 해결하는 데 집중합니다. 독립적으로 사고하고 자유롭게 아이디어를 펼칩니다.",
        "image": "https://via.placeholder.com/150?text=INTP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "ENTJ",
        "incompatible": "ESFJ",
        "compatibility_reason": "ENTJ는 목표 지향적이고 조직적인 성향을 가지며, INTP의 아이디어를 실현하는 데 협력할 수 있습니다. 이들은 서로 다른 능력을 결합하여 뛰어난 결과를 낼 수 있습니다.",
        "incompatibility_reason": "ESFJ는 감정적이고 외향적인 성향을 가지며, INTP의 논리적이고 분석적인 접근을 다루는 데 어려움을 겪을 수 있습니다. 서로의 대화 방식이 충돌할 수 있습니다."
    },
    "ENTJ": {
        "description": "ENTJ는 강력한 리더십을 가지고 있으며, 목표 지향적이고 전략적인 성격을 지닌 사람들입니다. 효율적인 해결책을 제시하고, 문제를 조직적으로 해결합니다.",
        "image": "https://via.placeholder.com/150?text=ENTJ",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INTJ",
        "incompatible": "ISFP",
        "compatibility_reason": "INTJ는 ENTJ와 비슷한 논리적이고 전략적인 사고를 공유합니다. 이들은 함께 미래를 계획하고 전략적으로 문제를 해결할 수 있습니다.",
        "incompatibility_reason": "ISFP는 감성적이고 즉흥적인 성격으로, ENTJ의 목표 지향적이고 조직적인 접근과 충돌할 수 있습니다. ISFP는 ENTJ의 강력한 리더십을 부담스러워할 수 있습니다."
    },
    "ENTP": {
        "description": "ENTP는 창의적이고 아이디어 중심의 사고를 하는 사람들로, 변화를 두려워하지 않으며 새로운 아이디어를 탐구하는 것을 좋아합니다. 대화를 통해 문제를 해결하고 혁신적인 해결책을 제시합니다.",
        "image": "https://via.placeholder.com/150?text=ENTP",  # 실제 이미지 URL로 바꾸세요.
        "compatible": "INTJ",
        "incompatible": "ISFJ",
        "compatibility_reason": "INTJ와 ENTP는 창의적인 사고를 통해 서로의 아이디어를 발전시키고, 논리적으로 접근하는 성향이 잘 맞습니다. 함께 혁신적인 결과를 도출할 수 있습니다.",
        "incompatibility_reason":_
