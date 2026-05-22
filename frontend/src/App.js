import React, { useState, useRef, useEffect } from "react";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  // ✅ Auto scroll
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage = { role: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const res = await fetch("https://interview-trainer-agent.onrender.com/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ message: input }),
        }
      );

      // ❌ Handle HTTP errors
      if (!res.ok) {
        throw new Error("API request failed");
      }

      const data = await res.json();
      console.log("FULL RESPONSE:", data);

      let answer = "";

      // ✅ Clean response
      if (data.output) {
        let rawText = data.output;

        rawText = rawText
          .replace(/\\n/g, "\n")
          .replace(/\*\*/g, "")
          .replace(/```/g, "")
          .replace(/(\d+\.)/g, "\n$1");

        answer = rawText;
      } else if (data.error) {
        answer = "❌ " + JSON.stringify(data.error);
      } else {
        answer = "⚠️ Unexpected response format";
      }

      const botMessage = { role: "bot", text: answer };
      setMessages((prev) => [...prev, botMessage]);

    } catch (error) {
      console.error("ERROR:", error);

      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          text: "❌ Backend not reachable or failed request",
        },
      ]);
    }

    setLoading(false);
    setInput("");
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Interview Trainer Agent</h1>

      {/* Chat Box */}
      <div style={styles.chatBox}>
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              ...styles.message,
              alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
              backgroundColor:
                msg.role === "user" ? "#007bff" : "#f1f1f1",
              color: msg.role === "user" ? "white" : "black",
            }}
          >
            <pre style={{ margin: 0, whiteSpace: "pre-wrap" }}>
              {msg.text}
            </pre>
          </div>
        ))}

        {/* ⏳ Loading */}
        {loading && (
          <div style={styles.botLoading}>
            Typing...
          </div>
        )}

        <div ref={chatEndRef} />
      </div>

      {/* Input */}
      <div style={styles.inputArea}>
        <input
          style={styles.input}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask interview questions..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button style={styles.button} onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

// 🎨 Styles
const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    height: "100vh",
    backgroundColor: "#f7f7f8",
    fontFamily: "Arial",
  },
  header: {
    margin: "15px",
  },
  chatBox: {
    width: "60%",
    height: "70%",
    backgroundColor: "white",
    borderRadius: "10px",
    padding: "15px",
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
  },
  message: {
    maxWidth: "75%",
    padding: "12px",
    borderRadius: "12px",
    lineHeight: "1.5",
  },
  botLoading: {
    alignSelf: "flex-start",
    backgroundColor: "#f1f1f1",
    padding: "10px",
    borderRadius: "10px",
    fontStyle: "italic",
  },
  inputArea: {
    display: "flex",
    width: "60%",
    marginTop: "15px",
    gap: "10px",
  },
  input: {
    flex: 1,
    padding: "12px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    outline: "none",
  },
  button: {
    padding: "12px 20px",
    borderRadius: "8px",
    border: "none",
    backgroundColor: "#007bff",
    color: "white",
    cursor: "pointer",
  },
};

export default App;