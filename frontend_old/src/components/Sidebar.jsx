import { useEffect, useState } from "react";

export default function Sidebar() {
  const [conversations, setConversations] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/conversations")
      .then((res) => res.json())
      .then(setConversations);
  }, []);

  const createNew = async () => {
    await fetch("http://localhost:8000/api/conversations", {
      method: "POST",
    });
    window.location.reload();
  };

  return (
    <div
      style={{
        width: 260,
        background: "#111",
        color: "#fff",
        padding: 10,
      }}
    >
      <button onClick={createNew}>+ New Chat</button>

      <div style={{ marginTop: 20 }}>
        {conversations.map((c) => (
          <div key={c.id} style={{ padding: "6px 0" }}>
            {c.id.slice(0, 8)}
          </div>
        ))}
      </div>
    </div>
  );
}