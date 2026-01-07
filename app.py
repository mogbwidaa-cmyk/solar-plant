import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import requests
from datetime import datetime, timedelta

# --- 1. الثوابت الراسخة (لا تتغير) ---
st.set_page_config(page_title="منصة م. مجاهد | Industry 4.0", page_icon="🚀", layout="wide")

MY_PHONE = "+966501318054"
LINKEDIN_URL = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
PLATFORM_NAME = "منصة مراقبة المصانع والمعدات الميكانيكية"
TELEGRAM_TOKEN = "8050369942:AAEN-n0Qn-kAmu_9k-lqZ9Fe-tsAOSd44OA"
CHAT_ID = "6241195886"

# --- 2. تنسيق الواجهة (CSS) ---
st.markdown(f"""
    <style>
    .main-title {{ background: linear-gradient(90deg, #0f172a 0%, #1e3a8a 100%); padding: 20px; border-radius: 15px; color: white; text-align: right; border-right: 10px solid #fbbf24; }}
    .stMetric {{ background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; }}
    </style>
    <div class="main-title">
        <h1>🚀 {PLATFORM_NAME} (Ver 4.0)</h1>
        <p>نظام التوأم الرقمي والصيانة التنبؤية المدعوم بالذكاء الاصطناعي</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. القائمة الجانبية (الهوية المهنية والثوابت) ---
with st.sidebar:
    st.markdown(f"### 👤 م. مجاهد بشير")
    st.caption("باحث دراسات عليا - طاقة متجددة")
    st.write("---")
    
    # قسم التحكم في الحساسات
    st.header("⚙️ مدخلات الحساسات (IIoT)")
    vib_input = st.slider("مستوى الاهتزاز الحالي (mm/s):", 0.0, 15.0, 4.2)
    
    st.write("---")
    # الثوابت: روابط التواصل
    st.markdown(f"📱 **تواصل مباشر:** `{MY_PHONE}`")
    col_w, col_l = st.columns(2)
    with col_w:
        st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/{MY_PHONE.replace('+', '')})")
    with col_l:
        st.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]({LINKEDIN_URL})")
    
    st.sidebar.caption(f"© 2026 {PLATFORM_NAME}")

# --- 4. قسم التوأم الرقمي للمحطة الشمسية ---
st.header("☀️ التوأم الرقمي (Digital Twin Integration)")


col1, col2 = st.columns([2, 1])

with col1:
    # محاكاة بيانات حية
    times = [(datetime.now() - timedelta(hours=i)).strftime("%H:%00") for i in range(24)][::-1]
    expected = [200 * np.sin(np.pi * i / 12) if 6 <= i <= 18 else 0 for i in range(24)]
    actual = [val * 0.82 for val in expected] # محاكاة فقدان كفاءة بسبب عوامل بيئية
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=times, y=expected, name="المستهدف (Design)", line=dict(dash='dash', color='gray')))
    fig.add_trace(go.Scatter(x=times, y=actual, name="الفعلي (Real-time IIoT)", line=dict(color='#10b981', width=3)))
    fig.update_layout(title="تحليل فجوة الأداء اللحظي", height=350, template="plotly_white", margin=dict(l=0,r=0,t=30,b=0))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### 🤖 تشخيص AI")
    efficiency_gap = 18 
    st.metric("فجوة الأداء", f"{efficiency_gap}%", delta="-3%", delta_color="inverse")
    
    if efficiency_gap > 10:
        st.error(f"⚠️ انحراف أداء مكتشف")
        st.info("💡 السبب: تراكم غبار + انخفاض كفاءة العاكس.")
        if st.button("🚀 تفعيل التنظيف الآلي"):
            msg = f"🤖 تنبيه Industry 4.0:\nتم تفعيل نظام التنظيف التلقائي للمحطة الشمسية.\nالمهندس المسؤول: مجاهد بشير"
            requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
            st.success("تم إرسال أمر التشغيل للروبوتات الميدانية")

# --- 5. قسم الصيانة الاستباقية (Predictive Maintenance) ---
st.divider()
st.header("🛠️ الصيانة التنبؤية الذكية")


# حساب "العمر المتبقي" (RUL) بناءً على المدخلات من السايدبار
remaining_life = max(0, 100 - (vib_input**2))

c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 تحليل حالة الأصول")
    st.metric("العمر الافتراضي المتبقي (RUL)", f"{remaining_life:.1f} يوم")
    st.progress(remaining_life/100)

with c2:
    st.subheader("📝 التقرير الآلي")
    if remaining_life < 30:
        st.warning("🚨 الحالة: حرجة. تم جدولة أمر صيانة تلقائي.")
        if st.button("📤 تصدير تقرير الحالة الفنية"):
            msg = f"🚨 تنبيه صيانة عاجل:\nالمعدة: P-101\nالاهتزاز: {vib_input} mm/s\nالعمر المتبقي: {remaining_life:.1f} يوم\nالمهندس: مجاهد بشير"
            requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
            st.success("تم إرسال التقرير بنجاح")
    else:
        st.success("✅ الحالة: مستقرة. لا توجد إجراءات مطلوبة حالياً.")

st.write("---")
st.markdown(f"<p style='text-align: center;'>{PLATFORM_NAME} - م. مجاهد بشير 2026</p>", unsafe_allow_html=True)
