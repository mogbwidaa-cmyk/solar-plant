import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import datetime

# --- 1. الثوابت (لا تتغير) ---
st.set_page_config(page_title="منصة مراقبة المصانع والمعدات الميكانيكية", page_icon="☀️", layout="wide")

MY_PHONE = "+966501318054"
LINKEDIN_URL = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
PLATFORM_NAME = "منصة مراقبة المصانع والمعدات الميكانيكية"

# --- 2. التصميم الهندسي (Clean UI) ---
st.markdown("""
    <style>
    .solar-header { background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); padding: 20px; border-radius: 15px; color: white; text-align: right; }
    .metric-box { background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. القائمة الجانبية (الثوابت) ---
with st.sidebar:
    st.markdown(f"### م. مجاهد بشير")
    st.write("🎓 باحث طاقة متجددة")
    st.divider()
    st.markdown(f"📞 التواصل: `{MY_PHONE}`")
    st.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=flat-square&logo=whatsapp&logoColor=white)](https://wa.me/{MY_PHONE.replace('+', '')})")
    st.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)]({LINKEDIN_URL})")

# --- 4. واجهة المحاكاة الرئيسية ---
st.markdown(f"""
    <div class="solar-header">
        <h1>☀️ نظام محاكاة محطة الطاقة الشمسية الذكي</h1>
        <p>تحليل الأداء اللحظي وتوقعات الإنتاج - {PLATFORM_NAME}</p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. مدخلات المحاكاة (Parameters) ---
st.write("### ⚙️ إعدادات المحطة والظروف البيئية")
col_p1, col_p2, col_p3, col_p4 = st.columns(4)

with col_p1:
    capacity = st.number_input("قدرة المحطة (kWp):", value=100)
    panels_count = st.number_input("عدد الألواح:", value=250)
with col_p2:
    irradiance = st.slider("الإشعاع الشمسي (W/m²):", 0, 1200, 800)
    temp = st.slider("درجة الحرارة (C°):", 10, 65, 35)
with col_p3:
    dust_loss = st.slider("نسبة الغبار/الأوساخ (%):", 0, 50, 10)
    tilt_angle = st.slider("زاوية ميل الألواح:", 0, 45, 25)
with col_p4:
    inverter_eff = st.slider("كفاءة العاكس (Inverter) %:", 85, 99, 96)

# --- 6. الحسابات الهندسية (Simulation Logic) ---
# كفاءة اللوح تتناقص بمقدار 0.4% لكل درجة فوق الـ 25 مئوية
temp_loss = max(0, (temp - 25) * 0.004)
system_loss = (dust_loss / 100) + (1 - (inverter_eff / 100))
actual_efficiency = (1 - temp_loss) * (1 - system_loss)
current_output = (capacity * (irradiance / 1000) * actual_efficiency)

# --- 7. عرض النتائج (Live Monitoring Dashboard) ---


st.divider()
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric("الإنتاج اللحظي", f"{current_output:.2f} kW")
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric("كفاءة النظام", f"{actual_efficiency*100:.1f}%")
    st.markdown("</div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric("الطاقة اليومية المتوقعة", f"{current_output * 5.5:.1f} kWh") # فرضية 5.5 ساعات ذروة
    st.markdown("</div>", unsafe_allow_html=True)
with c4:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric("انبعاثات CO2 الموفرة", f"{(current_output * 0.7):.1f} kg")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 8. الرسوم البيانية (Performance Analysis) ---
st.write("### 📊 تحليل منحنى الإنتاج اليومي")

# محاكاة منحنى الإنتاج على مدار 24 ساعة
hours = list(range(24))
power_curve = [max(0, current_output * np.sin(np.pi * (h - 6) / 12)) if 6 <= h <= 18 else 0 for h in hours]

fig = go.Figure()
fig.add_trace(go.Scatter(x=hours, y=power_curve, fill='tozeroy', line_color='#fbbf24', name="Solar Power Output"))
fig.update_layout(
    title="توقع إنتاج الطاقة خلال 24 ساعة (Simulation)",
    xaxis_title="الساعة",
    yaxis_title="القدرة (kW)",
    xaxis=dict(tickmode='linear'),
    template="plotly_white",
    height=400
)
st.plotly_chart(fig, use_container_width=True)

# --- 9. قسم التقرير الفني ---
if st.button("🚀 توليد تقرير أداء المحطة"):
    st.success(f"تم تحليل أداء محطة {capacity} kWp. الحالة الفنية: ممتازة. يتم الآن المزامنة مع منصة مجاهد بشير.")
    st.toast("جاري تصدير البيانات...")

st.sidebar.caption(f"© 2026 {PLATFORM_NAME}")