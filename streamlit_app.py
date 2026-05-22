import streamlit as st

# 페이지 제목 설정
st.title("🚚 배송비 안내 및 결제 시스템")
st.write("정기 회원 여부와 주문 금액을 입력해주세요.")

# 1. 사용자 입력 부분
member = st.radio("정기 회원입니까?", ('예 (y)', '아니오 (n)'))
total_order = st.number_input("주문 금액은 얼마입니까? (원)", min_value=0, step=1000)

# 2. 로직 처리 부분
shipping_fee = 0

if member == '예 (y)':
    st.success("✨ 정기회원으로 배송비가 면제됩니다.")
    shipping_fee = 0
else:
    st.info("ℹ️ 배송비 3,000원이 부과됩니다.")
    shipping_fee = 3000

# 최종 금액 계산
final_price = total_order + shipping_fee

# 3. 결과 출력 부분
st.divider() # 구분선
st.subheader(f"💰 최종 결제 금액: {final_price:,}원")