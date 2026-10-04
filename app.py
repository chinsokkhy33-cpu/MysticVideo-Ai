import streamlit as st

# កំណត់ទម្រង់ទំព័រ
st.set_page_config(page_title="MysticVideo AI", layout="wide")

# កូដ CSS រចនាពណ៌ផ្ទៃខាងក្រោយ និងប៊ូតុងទូទៅ
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2b5876;
    }
    h1 {
        color: #ffffff !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
    }
    .stButton>button {
        background-color: #4a7a96;
        color: white;
        border-radius: 8px;
        border: 1px solid #6a9ab6;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #5a8aa6;
        color: white;
        border-color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# គ្រប់គ្រងទំព័រ (Page Navigation State)
if "page" not in st.session_state:
  st.session_state.page = "home"

# មុខងារប្តូរទំព័រ
def set_page(page_name):
  st.session_state.page = page_name

# --- ទំព័រដើម (Home Screen) ---
if st.session_state.page == "home":
  st.markdown("<h1>MysticVideo AI</h1>", unsafe_allow_html=True)
  st.markdown("<br><br>", unsafe_allow_html=True)

  col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

  with col2:
    if st.button("🎬 បង្កើត Video", use_container_width=True, key="btn_create"):
      set_page("create_video")
      st.rerun()

  with col3:
    if st.button("👤 រៀបចំតួអង្គនឹងផ្លង់", use_container_width=True, key="btn_character"):
      set_page("character_setup")
      st.rerun()

  with col4:
    if st.button("⚙️ កំណត់", use_container_width=True, key="btn_settings"):
      set_page("settings")
      st.rerun()

# --- ទំព័ររៀបចំតួអង្គ និងផ្លង់ (Character Setup) ---
elif st.session_state.page == "character_setup":
  # ផ្នែកខាងលើ៖ ប៊ូតុងត្រឡប់ក្រោយ និងចំណងជើង
  col_h1, col_h2 = st.columns([1, 3])
  with col_h1:
    if st.button("< ត្រឡប់ក្រោយ"):
      set_page("home")
      st.rerun()
  with col_h2:
    st.markdown(
        "<p style='color: #ffffff; font-size: 16px; font-weight: 500;"
        " padding-top: 8px;'>រៀបចំតួអង្គ និងផ្លង់</p>",
        unsafe_allow_html=True,
    )

  # រក្សាទុកទិន្នន័យមេឌៀក្នុង session_state
  if "uploaded_media" not in st.session_state:
    st.session_state.uploaded_media = None

  # ផ្នែកកណ្តាល៖ បង្ហាញរូបភាព/វីដេអូ ឬសញ្ញាផ្កា
  if st.session_state.uploaded_media is not None:
    st.markdown(
        """
      <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-top: 20px;">
          <div style="font-size: 16px; color: #4CAF50; font-weight: 500; margin-bottom: 10px;">✓ បានជ្រើសរើសមេឌៀរួចរាល់</div>
      </div>
    """,
        unsafe_allow_html=True,
    )
    if st.session_state.uploaded_media.type.startswith("image"):
      st.image(st.session_state.uploaded_media, width=250)
    else:
      st.video(st.session_state.uploaded_media)
  else:
    st.markdown(
        """
      <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-top: 40px;">
          <div style="font-size: 40px; margin-bottom: 10px; color: #a0b2c6;">❀</div>
          <div style="font-size: 18px; color: #ffffff; font-weight: 500;">ចាប់ផ្តើមបង្កើត ឬទម្លាក់មេឌៀទីនេះ</div>
      </div>
    """,
        unsafe_allow_html=True,
    )

  # រៀបចំប្រអប់ខាងក្រោមតាមរចនាប័ទ្ម Flow App
  st.write("")
  st.write("")

  with st.container():
    st.markdown(
        """
        <style>
            div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
                background-color: #121212;
                border: 1px solid #2a2a2a;
                border-radius: 20px;
                padding: 15px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='color: #888888; font-size: 14px; margin-bottom: 5px;'>តើអ្នកចង់បង្កើតអ្វីដែរ?</p>",
        unsafe_allow_html=True,
    )

    # ជួរសម្រាប់ប៊ូតុងសញ្ញា + និងប៊ូតុងផ្សេងៗ
    col_b1, col_b2, col_b3 = st.columns([1, 4, 1])

    with col_b1:
      uploaded_file = st.file_uploader(
          "+", type=["png", "jpg", "jpeg", "mp4"], label_visibility="collapsed"
      )
      if uploaded_file is not None:
        st.session_state.uploaded_media = uploaded_file
        st.rerun()

    with col_b2:
      st.markdown(
          "<div style='text-align: center; color: #cccccc; font-size: 12px;"
          " padding-top: 8px;'>វីដេអូ • 720p • 8វិនាទី 📱 x2</div>",
          unsafe_allow_html=True,
      )

    with col_b3:
      if st.button("→", key="send_btn"):
        st.toast("កំពុងបញ្ជូន...")