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


# --- ទំព័ររៀបចំតួអង្គ និងផ្លង់ (Character Setup) ---
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

# កំណត់ទម្រង់ទំព័រឱ្យពេញអេក្រង់
st.set_page_config(
    page_title="MysticVideo AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ផ្ទៀងផ្ទាត់ State សម្រាប់ដូរទំព័រ
if 'page' not in st.session_state:
    st.session_state.page = 'home'
# --- ផ្ទាំងទី ១: ទំព័រដើម (Home Page) ---
if st.session_state.page == 'home':
    st.markdown("""
        <style>
        .stApp {
            background-color: #3b5976;
        }
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 42px; margin-bottom: 30px;'>MysticVideo AI</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎬 បង្កើត Video", use_container_width=True):
            st.session_state.page = 'create_video'
            st.rerun()
        
        if st.button("👤 រៀបចំគណនីផ្ទាល់ខ្លួន", use_container_width=True):
            pass
            
        if st.button("⚙️ កំណត់", use_container_width=True):
            pass

# --- ផ្ទាំងទី ២: မျက်နှာပြင်បង្កើត Video (Create Video Page - ផ្ទៃខ្មៅ 100%) ---
elif st.session_state.page == 'create_video':
    st.markdown("""
        <style>
        .stApp {
            background-color: #000000;
        }
        header {visibility: hidden;}
        
        /* រចនាប័ទ្មប្រអប់មូលធំនៅបាតក្រោមដូចរូបទី 15 */
        .bottom-chat-box {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 90%;
            max-width: 650px;
            background-color: #161616;
            padding: 14px 16px;
            border-radius: 24px;
            border: 1px solid #2a2a2a;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.8);
            z-index: 999;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        
        .chat-input-field {
            width: 100%;
            background: transparent;
            border: none;
            color: #ffffff;
            font-size: 15px;
            outline: none;
        }
        
        .chat-input-field::placeholder {
            color: #777777;
        }
        
        .chat-bottom-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .left-tools {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .plus-btn {
            background-color: #222222;
            color: #ffffff;
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .meta-pill {
            background-color: #222222;
            color: #cccccc;
            padding: 5px 12px;
            border-radius: 12px;
            font-size: 12px;
        }
        
        .send-btn {
            background-color: #ffffff;
            color: #000000;
            border: none;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            font-size: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # ប៊ូតុងថយក្រោយមកទំព័រដើមវិញ
    if st.button("← ត្រឡប់ក្រោយ"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # រូបផ្កា pixel និងអត្ថបទកណ្តាលអេក្រង់ (ដូចរូបទី 15)
    st.markdown("""
        <div style="text-align: center; color: white;">
            <div style="font-size: 45px; margin-bottom: 15px; line-height: 1;">✿</div>
            <h2 style="font-weight: 400; font-size: 24px; color: #ffffff; margin: 0;">Start creating or drop<br>media</h2>
        </div>
    """, unsafe_allow_html=True)

    # ប្រើប្រាស់ HTML Form ផ្ទាល់ដើម្បីឱ្យធាតុទាំងអស់ស្ថិតនៅក្នុងប្រអប់តែមួយយ៉ាងល្អឥតខ្ចោះ
    st.markdown("""
        <div class="bottom-chat-box">
            <input type="text" class="chat-input-field" placeholder="What do you want to create?">
            <div class="chat-bottom-row">
                <div class="left-tools">
                    <button class="plus-btn">+</button>
                    <div class="meta-pill">Video • 720p • 8s 📱 x2</div>
                </div>
                <button class="send-btn">→</button>
            </div>
        </div>
    """, unsafe_allow_html=True)
