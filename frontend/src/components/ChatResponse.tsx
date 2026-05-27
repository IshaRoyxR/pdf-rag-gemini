import ReactMarkdown from "react-markdown";

interface ChatResponseProps {
  question: string;
  answer: string;
  source?: string;
  score?: number;
}

export function ChatResponse({ question, answer, source, score }: ChatResponseProps) {
  return (
    <div className="mb-8 animate-fade-in-up">
      <div className="border rounded-lg bg-card overflow-hidden">
        <div className="h-0.5 bg-muted overflow-hidden">
          <div className="h-full w-1/4 bg-primary rounded-full animate-indeterminate" style={{ animationPlayState: "paused" }} />
        </div>

        <div className="p-5">
          <p className="text-sm font-medium text-muted-foreground mb-1">You asked:</p>
          <p className="text-foreground font-medium mb-4">{question}</p>

          <div className="border-t pt-4">
            <p className="text-sm font-medium text-muted-foreground mb-2">Answer:</p>
            <div className="markdown-response text-foreground text-sm leading-relaxed">
              <ReactMarkdown>{answer}</ReactMarkdown>
            </div>

            {(source || score !== undefined) && (
              <div className="mt-4 pt-3 border-t border-border/50 flex flex-wrap gap-x-4 gap-y-1 text-xs text-muted-foreground">
                {source && <span>Source: <span className="font-medium">{source}</span></span>}
                {score !== undefined && (
                  <span>
                    Similarity Score:{" "}
                    <span className="font-medium">
                      {Math.round(score)}%{score === 0 ? " (Out of context)" : ""}
                    </span>
                  </span>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
