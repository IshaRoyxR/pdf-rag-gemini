import React, { useState } from "react";

function App() {

  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [mode, setMode] = useState("chat");
  const [provider, setProvider] = useState("gemini");

  const uploadFile = async () => {

    if (!file) {
      alert("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://localhost:8000/api/upload", {
      method: "POST",
      body: formData
    });

    alert("File uploaded successfully!");
  };


  const askQuestion = async () => {

    const res = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question,
        mode,
        provider
      })
    });

    const data = await res.json();

    // convert answer safely to text
    let textAnswer = "";

    if (typeof data.answer === "string") {
      textAnswer = data.answer;
    } 
    else if (data.answer?.text) {
      textAnswer = data.answer.text;
    } 
    else {
      textAnswer = JSON.stringify(data.answer);
    }

    setAnswer(textAnswer);
    setSources(data.sources || []);
  };


  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>

      <h2>📚 Multi File RAG</h2>

      {/* Upload */}
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={uploadFile}>
        Upload
      </button>

      <br /><br />

      {/* Provider */}
      Provider:
      <select
        value={provider}
        onChange={(e) => setProvider(e.target.value)}
      >
        <option value="gemini">Gemini</option>
        <option value="openai">OpenAI</option>
        <option value="ollama">Ollama</option>
      </select>

      <br /><br />

      {/* Mode */}
      Mode:
      <select
        value={mode}
        onChange={(e) => setMode(e.target.value)}
      >
        <option value="chat">Chat</option>
        <option value="qa">Q&A</option>
        <option value="summary">Summary</option>
        <option value="completion">Completion</option>
      </select>

      <br /><br />

      {/* Question */}
      <input
        style={{ width: "400px" }}
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askQuestion}>
        Ask
      </button>

      {/* Answer section (only show when answer exists) */}

      {answer && (
        <>
          <h3>Answer</h3>
          <p>{answer}</p>
        </>
      )}

      {/* Sources section (ONLY if sources exist) */}

      {sources.length > 0 && (
        <>
          <h3>Sources</h3>

          {sources.map((s, i) => (
            <div
              key={i}
              style={{
                marginBottom: 10,
                background: "#f3f3f3",
                padding: 10
              }}
            >
              <b>{s.file}</b> (Page {s.page}) — {s.score}%
              <br />
              <i>{s.excerpt}</i>
            </div>
          ))}
        </>
      )}

    </div>
  );
}

export default App;