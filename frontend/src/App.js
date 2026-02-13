import React, { useState, useEffect } from "react";

const API = "http://localhost:8000/api";

function App() {
  const [file, setFile] = useState(null);
  const [docs, setDocs] = useState([]);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  useEffect(() => {
    fetchDocs();
  }, []);

  const fetchDocs = async () => {
    const res = await fetch(`${API}/documents`);
    const data = await res.json();
    setDocs(data);
  };

  const upload = async () => {
    const form = new FormData();
    form.append("file", file);

    await fetch(`${API}/documents/upload`, {
      method: "POST",
      body: form
    });

    fetchDocs();
  };

  const ask = async () => {
    const res = await fetch(`${API}/chat/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  const deleteDoc = async (id) => {
    await fetch(`${API}/documents/${id}`, {
      method: "DELETE"
    });

    fetchDocs();
  };

  return (
    <div style={{ padding: 40 }}>

      <h1>Phase 2 – Multi File RAG</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={upload}>Upload</button>

      <h3>Documents</h3>

      {Object.entries(docs).map(([id, doc]) => (
        <div key={id}>
          📄 {doc.filename} – {doc.status}
          <button onClick={() => deleteDoc(id)}>Delete</button>
        </div>
      ))}

      <hr />

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={ask}>Ask</button>

      <h3>Answer</h3>

      <p>{answer}</p>

    </div>
  );
}

export default App;
