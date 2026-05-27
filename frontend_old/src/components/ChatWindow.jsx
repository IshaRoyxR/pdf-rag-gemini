import { useState } from "react";

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [file, setFile] = useState(null);

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://localhost:8000/api/upload", {
      method: "POST",
      body: formData,
    });

    alert("PDF uploaded!");
  };

  const sendMessage = async () => {
    if (!input) return;

    const userMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    const res = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: input }),
    });

    const data = await res.json();

    const aiMsg = { role: "ai", text: data.answer };
    setMessages((prev) => [...prev, aiMsg]);

    setInput("");
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Chat</h2>

      {/* Upload */}
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadFile}>Upload PDF</button>

      {/* Chat */}
      <div style={{ marginTop: 20 }}>
        {messages.map((m, i) => (
          <div
            key={i}
            style={{
              textAlign: m.role === "user" ? "right" : "left",
              margin: "10px 0",
            }}
          >
            <span
              style={{
                background: m.role === "user" ? "#007bff" : "#eee",
                color: m.role === "user" ? "white" : "black",
                padding: "8px 12px",
                borderRadius: 8,
                display: "inline-block",
              }}
            >
              {m.text}
            </span>
          </div>
        ))}
      </div>

      {/* Input */}
      <div style={{ marginTop: 20 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask something..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}