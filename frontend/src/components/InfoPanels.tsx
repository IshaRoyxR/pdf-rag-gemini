import { FileText, Clock, Trash2 } from "lucide-react";
import { toast } from "sonner";
import { useState } from "react";

const API_BASE = "http://127.0.0.1:8000/api";

interface InfoPanelsProps {
  onQuestionClick: (q: string) => void;
  recentQuestions: string[];
  documents: string[];
  setDocuments: React.Dispatch<React.SetStateAction<string[]>>;
}

export function InfoPanels({
  onQuestionClick,
  recentQuestions,
  documents,
  setDocuments,
}: InfoPanelsProps) {

  const [deleting, setDeleting] = useState<string | null>(null);

  // ✅ DELETE FUNCTION (IMPROVED)
  const handleDelete = async (filename: string) => {
    if (deleting === filename) return;

    setDeleting(filename);

    try {
      const res = await fetch(`${API_BASE}/documents/${filename}`, {
        method: "DELETE",
      });

      if (!res.ok) {
        throw new Error("Delete failed");
      }

      // ✅ update UI instantly
      setDocuments((prev) => prev.filter((doc) => doc !== filename));

      toast.success(`"${filename}" deleted`);

    } catch (err) {
      console.error(err);
      toast.error("Failed to delete document");
    } finally {
      setDeleting(null);
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

      {/* 🔹 Recent Questions */}
      <div className="border rounded-lg bg-card shadow-sm">
        <div className="px-5 py-4 border-b">
          <h2 className="text-sm font-semibold text-foreground flex items-center gap-2">
            <Clock className="h-4 w-4 text-muted-foreground" />
            Recent Questions
          </h2>
        </div>

        {recentQuestions.length === 0 ? (
          <p className="px-5 py-4 text-sm text-muted-foreground">
            No recent questions
          </p>
        ) : (
          <ul>
            {recentQuestions.map((q, index) => (
              <li key={`${q}-${index}`}>
                <button
                  onClick={() => onQuestionClick(q)}
                  className="w-full text-left px-5 py-3 text-sm text-foreground hover:bg-muted/50 transition border-b last:border-b-0"
                >
                  {q}
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>

      {/* 🔹 Documents */}
      <div className="border rounded-lg bg-card shadow-sm">
        <div className="px-5 py-4 border-b">
          <h2 className="text-sm font-semibold text-foreground flex items-center gap-2">
            <FileText className="h-4 w-4 text-muted-foreground" />
            Documents
          </h2>
        </div>

        {documents.length === 0 ? (
          <p className="px-5 py-4 text-sm text-muted-foreground">
            No documents uploaded yet
          </p>
        ) : (
          <ul>
            {documents.map((doc, index) => (
              <li
                key={`${doc}-${index}`}
                className="px-5 py-3 text-sm text-foreground border-b last:border-b-0 flex items-center justify-between hover:bg-muted/40 transition"
              >
                <div className="flex items-center gap-2 overflow-hidden">
                  <span className="inline-block h-2 w-2 rounded-full bg-accent flex-shrink-0" />
                  <span className="truncate">{doc}</span>
                </div>

                {/* 🗑 DELETE BUTTON */}
                <button
                  onClick={() => handleDelete(doc)}
                  disabled={deleting === doc}
                  className="text-red-500 hover:text-red-700 disabled:opacity-50"
                >
                  <Trash2 className="h-4 w-4" />
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}