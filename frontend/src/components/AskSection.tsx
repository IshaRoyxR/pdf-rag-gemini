import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Search } from "lucide-react";

interface AskSectionProps {
  onAsk: (question: string) => void;
  loading: boolean;
}

export function AskSection({ onAsk, loading }: AskSectionProps) {
  const [question, setQuestion] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!question.trim()) return;
    onAsk(question.trim());
  };

  return (
    <div className="mb-8">
      <h1 className="text-2xl font-semibold text-foreground mb-1">
        Ask Anything from your File
      </h1>
      <p className="text-muted-foreground text-sm mb-5">
        Get instant AI-powered answers from your uploaded documents.
      </p>

      <form onSubmit={handleSubmit} className="flex gap-3">
        <div className="relative flex-1">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Type your question"
            className="w-full h-12 pl-11 pr-4 rounded-full border-2 border-border bg-card text-foreground placeholder:text-muted-foreground focus:outline-none focus:border-primary transition-colors"
          />
        </div>
        <Button
          type="submit"
          disabled={loading || !question.trim()}
          className={`h-12 px-8 rounded-lg font-semibold ${loading ? "animate-pulse-ring" : ""}`}
        >
          {loading ? "Thinking…" : "ASK"}
        </Button>
      </form>
    </div>
  );
}
