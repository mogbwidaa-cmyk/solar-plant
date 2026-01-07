import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import requests
from datetime import datetime, timedelta

# --- الثوابت (لا تتغير) ---
MY_PHONE = "+966501318054"
PLATFORM_NAME = "منصة مراقبة المصانع والمعدات الميكانيكية"

# --- محاكاة Industry 4.0 (البيانات الضخمة) ---
def get_sensor_stream():
    """محاكاة تدفق بيانات من حساسات حقيقية IIoT"""
    return np.random.normal(3.5, 0.2, 24) # 24 قراءة خلال اليوم

# --- الواجهة ---
st.title(f"🚀 {PLATFORM_NAME} (Ver 4.0)")

# قسم التوأم الرقمي للمحطة الشمسية
st.header("☀️ التوأم الرقمي للمحطة الشمسية (Digital Twin)")


col1, col2 = st.columns([2, 1])

with col1:
    # رسم بياني حي يوضح الفرق بين "الإنتاج المتوقع" و "الإنتاج الفعلي"
    times = [(datetime.now() - timedelta(hours=i)).strftime("%H:%00") for i in range(24)][::-1]
    expected = [200 * np.sin(np.pi * i / 12) if 6 <= i <= 18 else 0 for i in range(24)]
    actual = [val * 0.85 for val in expected] # محاكاة خسائر حقيقية (غبار/حرارة)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=times, y=expected, name="الإنتاج المستهدف (Target)", line=dict(dash='dash', color='gray')))
    fig.add_trace(go.Scatter(x=times, y=actual, name="الإنتاج الفعلي (IIoT Stream)", line=dict(color='#10b981', width=3)))
    fig.update_layout(title="مقارنة الأداء اللحظي عبر إنترنت الأشياء", height=400, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### 🤖 تشخيص الذكاء الاصطناعي")
    efficiency_gap = 15 # فجوة الأداء
    if efficiency_gap > 10:
        st.error(f"⚠️ انحراف في الأداء بنسبة {efficiency_gap}%")
        st.info("💡 التشخيص التلقائي: تراكم غبار كثيف + ارتفاع حرارة الخلايا.")
        if st.button("تفعيل نظام التنظيف الآلي"):
            st.success("تم إرسال أمر التشغيل لروبوتات التنظيف.")

# قسم الصيانة الاستباقية (Predictive Maintenance)
st.divider()
st.header("🛠️ الصيانة التنبؤية (AI-Predict)")


# حساب "العمر المتبقي" للمحمل (Bearing) بناءً على الاهتزاز
vib_input = st.sidebar.slider("مستوى الاهتزاز الحالي (mm/s):", 0.0, 15.0, 4.2)
remaining_life = max(0, 100 - (vib_input**2))

c1, c2 = st.columns(2)
c1.metric("العمر الافتراضي المتبقي للأصل", f"{remaining_life:.1f} يوم")
c2.progress(remaining_life/100)

if remaining_life < 30:
    st.warning("⚠️ تم اكتشاف نمط اهتزاز غير طبيعي. الروبوت قام بجدولة أمر صيانة تلقائي.")

# --- التواصل (الثوابت) ---
st.sidebar.divider()
st.sidebar.markdown(f"👤 **مطور النظام:** م. مجاهد بشير")
st.sidebar.markdown(f"📞 `{MY_PHONE}`")
