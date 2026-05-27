import { useState, useCallback, useEffect, useRef } from "react";
import { useSearchParams } from "react-router-dom";
import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/AppSidebar";
import { AppHeader } from "@/components/AppHeader";
import { ChatResponse } from "@/components/ChatResponse";
import { LoadingBar } from "@/components/LoadingBar";
import { toast } from "sonner";
import { Send, Paperclip, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

const API_BASE = "http://127.0.0.1:8000/api";

interface ChatEntry {
  question: string;
  answer: string;
  source?: string;
  score?: number;
}

const providers = ["gemini", "openai", "ollama"];
const modes = ["chat", "qa", "summary", "completion"];

function ChatBots() {
  const [provider, setProvider] = useState("gemini");
  const [mode, setMode] = useState("qa");
  const [chatHistory, setChatHistory] = useState<ChatEntry[]>([]);
  const [question, setQuestion] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const [searchParams] = useSearchParams();
  const bottomRef = useRef<HTMLDivElement>(null);
  const fileRef = useRef<HTMLInputElement>(null);

  // ✅ Load chat (session only)
  useEffect(() => {
    const saved = sessionStorage.getItem("chatHistory");
    if (saved) setChatHistory(JSON.parse(saved));
  }, []);

  // ✅ Save chat
  useEffect(() => {
    sessionStorage.setItem("chatHistory", JSON.stringify(chatHistory));
  }, [chatHistory]);

  // ✅ Auto scroll
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatHistory]);

  // ✅ Load file from Documents page (❓ click)
  useEffect(() => {
    const fileFromUrl = searchParams.get("file");

    if (fileFromUrl) {
      setFile({ name: decodeURIComponent(fileFromUrl) } as File);
    }
  }, [searchParams]);

  const handleAsk = useCallback(
    async (q: string) => {
      if (!q.trim()) return;

      setLoading(true);

      try {
        // ✅ Upload file if newly selected
        if (file && file instanceof File && file.size) {
          const formData = new FormData();
          formData.append("file", file);

          const uploadRes = await fetch(`${API_BASE}/upload`, {
            method: "POST",
            body: formData,
          });

          if (!uploadRes.ok) throw new Error("Upload failed");

          toast.success(`${file.name} uploaded`);
        }

        // ✅ Ask question
        const res = await fetch(`${API_BASE}/chat`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question: q,
            provider,
            mode,
            filename: file?.name || null, // 🔥 important
          }),
        });

        if (!res.ok) throw new Error();

        const data = await res.json();

        setChatHistory((prev) => [
          ...prev,
          {
            question: q,
            answer: data.answer,
            source: data.source,
            score: data.score,
          },
        ]);
      } catch {
        toast.error("Something went wrong");
      } finally {
        setLoading(false);
      }
    },
    [provider, mode, file]
  );

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    handleAsk(question);
    setQuestion("");
  };

  return (
    <SidebarProvider>
      <div className="flex h-screen w-full">
        <AppSidebar />

        <div className="flex flex-col flex-1">
          <LoadingBar visible={loading} />

          {/* ❌ No upload in header */}
          <AppHeader />

          {/* CHAT AREA */}
          <div className="flex-1 overflow-y-auto px-6 py-6 space-y-6">
            {chatHistory.length === 0 && (
              <div className="text-center mt-20 text-muted-foreground">
                Ask something from your document 👇
              </div>
            )}

            {chatHistory.map((entry, i) => (
              <ChatResponse key={i} {...entry} />
            ))}

            <div ref={bottomRef} />
          </div>

          {/* 🔥 INPUT AREA */}
          <div className="border-t p-4 bg-background">
            <div className="max-w-4xl mx-auto">

              {/* Provider + Mode */}
              <div className="flex gap-3 mb-3">
                <Select value={provider} onValueChange={setProvider}>
                  <SelectTrigger className="w-[130px]">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    {providers.map((p) => (
                      <SelectItem key={p} value={p}>
                        {p.toUpperCase()}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>

                <Select value={mode} onValueChange={setMode}>
                  <SelectTrigger className="w-[130px]">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    {modes.map((m) => (
                      <SelectItem key={m} value={m}>
                        {m.toUpperCase()}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              {/* FILE CHIP */}
              {file && (
                <div className="flex items-center gap-2 mb-2 text-sm bg-muted px-3 py-1 rounded w-fit">
                  📄 {file.name}
                  <X
                    className="h-4 w-4 cursor-pointer"
                    onClick={() => setFile(null)}
                  />
                </div>
              )}

              {/* INPUT */}
              <form onSubmit={handleSubmit} className="flex gap-2">

                <Button
                  type="button"
                  variant="ghost"
                  onClick={() => fileRef.current?.click()}
                >
                  <Paperclip />
                </Button>

                <input
                  ref={fileRef}
                  type="file"
                  className="hidden"
                  onChange={(e) => setFile(e.target.files?.[0] || null)}
                />

                <input
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  placeholder="Ask something..."
                  className="flex-1 h-12 px-4 rounded-lg border bg-card"
                />

                <Button type="submit" disabled={loading}>
                  <Send className="h-4 w-4" />
                </Button>
              </form>

            </div>
          </div>
        </div>
      </div>
    </SidebarProvider>
  );
}

export default ChatBots;