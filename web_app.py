
import streamlit as st
class App:
    def __init__(self):
        self.title = st.sidebar.empty()
        self.notice = st.sidebar.empty()
        self.roomID_input = st.sidebar.empty()
        self.start = st.sidebar.button("start")
        self.userTable = st.sidebar.empty()
        self.userConversation = st.empty()
        self.aiConversation = st.empty()
        st.session_state.connected=True
        self.roomID=0

    def set_title(self, title):
        self.title.title(title)

    def set_notice(self, notice):
        self.notice.success(notice)

    def set_roomID(self, roomID):
        self.roomID=self.roomID_input.number_input("roomID", min_value=0, max_value=100000000, value=roomID)

    def set_user_table(self, data):
        self.userTable.table(data)

    def set_user_conversation(self, uname, text):
        self.userConversation.info(uname + "：" + text)

    def set_ai_conversation(self, data):
        self.aiConversation.success("AI：" + data)

    def set_ai_image(self, data):
        self.aiConversation.image(data)

    def clean_conversation(self):
        self.userConversation.empty()
        self.aiConversation.empty()

    def is_connected(self):
        try:
            if st.session_state.connected:
                return True
            else:
                return False
        except AttributeError:
            return False





