for entry in st.session_state.chat_history:
    st.markdown(
        f"""
        <div class='chat-container'>
            <div class='user-message'>
                <img src="{USER_ICON}" style="width:18px; vertical-align:middle; margin-right:6px;">
                {entry['user']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    bot_class = "bot-message-positive" if "✅" in entry["bot"] else "bot-message-negative"

    st.markdown(
        f"""
        <div class='chat-container'>
            <div class='{bot_class}'>
                <img src="{BOT_ICON}" style="width:18px; vertical-align:middle; margin-right:6px;">
                {entry['bot']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
