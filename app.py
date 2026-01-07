import streamlit as st
import numpy as np
import plotly.graph_objects as go
import requests
from datetime import datetime

# --- 1. الثوابت الراسخة (لا تتغير) ---
st.set_page_config(page_title="منصة مراقبة المصانع والمعدات الميكانيكية", page_icon="🛡️", layout="wide")

MY_PHONE = "+966501318054"
LINKEDIN_URL = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
PLATFORM_NAME = "منصة مراقبة المصانع والمعدات الميكانيكية"
TELEGRAM_TOKEN = "8050369942:AAEN-n0Qn-kAmu_9k-lqZ9Fe-tsAOSd44OA"
CHAT_ID = "6241195886"

# --- 2. واجهة Industry 4.0 المتقدمة ---
st.markdown(f"""
    <style>
    .main-box {{ background-color: #f8fafc; padding: 20px; border-radius: 15px; border-right: 10px solid #1e3a8a; }}
    .stButton>button {{ background-color: #1e3a8a; color: white; border-radius: 8px; width: 100%; font-weight: bold; }}
    </style>
    <div class="main-box">
        <h1 style='color: #1e3a8a; text-align: right;'>🛡️ {PLATFORM_NAME}</h1>
        <p style='color: #475569; text-align: right; font-size: 18px;'>النظام السيبراني الموحد لأتمتة الأصول والطاقة المستدامة</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. القائمة الجانبية (الهوية المهنية) ---
with st.sidebar:
    st.markdown(f"### م. مجاهد بشير")
    st.info("🎓 باحث دراسات عليا - طاقة متجددة")
    st.write("---")
    st.markdown(f"📱 تواصل مباشر: `{MY_PHONE}`")
    
    # الثوابت: أزرار التواصل
    c1, c2 = st.columns(2)
    with c1: st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/{MY_PHONE.replace('+', '')})")
    with c2: st.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]({LINKEDIN_URL})")
    
    st.write("---")
    menu = st.radio("انتقل إلى:", ["🚀 التوأم الرقمي (Digital Twin)", "🛠️ الصيانة التنبؤية (AI)", "🤖 وكيل الأتمتة والتوظيف"])

# --- 4. تطبيق مفاهيم Industry 4.0 ---

if menu == "🚀 التوأم الرقمي (Digital Twin)":
    st.subheader("☀️ محاكاة المحطة الشمسية عبر إنترنت الأشياء (IIoT)")
    
    
    col_input, col_chart = st.columns([1, 2])
    with col_input:
        temp = st.slider("درجة الحرارة الميدانية (C°):", 10, 60, 35)
        dust = st.slider("مستوى تراكم الغبار (%):", 0, 100, 20)
        eff = max(0, 22.0 - (temp-25)*0.08 - dust*0.15)
        st.metric("الكفاءة التشغيلية الفعالة", f"{eff:.2f}%")
        
    with col_chart:
        # محاكاة مقارنة الأداء (Target vs Actual)
        x = list(range(24))
        target = [100 * np.sin(np.pi * i / 12) if 6 <= i <= 18 else 0 for i in x]
        actual = [v * (eff/22) for v in target]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=target, name="الإنتاج المستهدف", line=dict(dash='dash', color='gray')))
        fig.add_trace(go.Scatter(x=x, y=actual, name="الإنتاج الفعلي (IIoT)", fill='tozeroy', line_color='#1e3a8a'))
        fig.update_layout(title="مقارنة الأداء اللحظي للمحطة", height=300)
        st.plotly_chart(fig, use_container_width=True)

elif menu == "🛠️ الصيانة التنبؤية (AI)":
    st.subheader("🛠️ تحليل الأصول المستند إلى الذكاء الاصطناعي")
    
    vib = st.slider("Vibration (mm/s RMS):", 0.0, 15.0, 3.2)
    # خوارزمية Industry 4.0 للتنبؤ بالعمر المتبقي (RUL)
    rul = max(0, 100 - (vib**2))
    st.write(f"### العمر الافتراضي المتبقي للمعدة: **{rul:.1f} يوم**")
    st.progress(rul/100)
    
    if st.button("📤 إرسال تقرير حالة الأصل"):
        status = "آمن" if vib < 3 else "حرج"
        msg = f"🛡️ {PLATFORM_NAME}\nالمعدة: P-101\nالاهتزاز: {vib}\nالعمر المتبقي: {rul:.1f} يوم\nالحالة: {status}"
        requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
        st.success("تم إرسال البيانات للسيرفر المركزي")

elif menu == "🤖 وكيل الأتمتة والتوظيف":
    st.subheader("🤖 وكيل الأتمتة الاستراتيجي (AI Agent)")
    st.markdown("""
    هذا الوكيل يعمل بتقنية Industry 4.0 لربط المهارات الهندسية بمتطلبات السوق:
    - **أتمتة التقديم:** التقديم الذكي على الفرص التي تطابق بحثك العلمي (Bio-Gas).
    - **تحليل الفجوة:** تنبيهك بالمهارات المطلوبة في مشاريع الهيدروجين والطاقة المتجددة غداً.
    """)
    if st.button("🚀 تفعيل الوكيل الذكي الآن"):
        st.balloons()
        st.info("تم تفعيل الروبوت، سيتم موافاتك بالنتائج عبر تليجرام.")

st.sidebar.caption(f"تطوير م. مجاهد بشير © 2026 | {MY_PHONE}")
