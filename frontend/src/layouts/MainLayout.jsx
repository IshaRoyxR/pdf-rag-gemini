import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";

export default function MainLayout() {
  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <Sidebar />
      <ChatWindow />
    </div>
  );
}