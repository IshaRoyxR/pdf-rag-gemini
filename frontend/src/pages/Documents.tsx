import { useState, useCallback, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/AppSidebar";
import { AppHeader } from "@/components/AppHeader";
import { LoadingBar } from "@/components/LoadingBar";
import { Button } from "@/components/ui/button";
import { FileText, Download, Trash2, HelpCircle } from "lucide-react";
import { toast } from "sonner";

const API_BASE = "http://127.0.0.1:8000/api";

function Documents() {
  const [documents, setDocuments] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  const navigate = useNavigate();

  const fetchDocuments = useCallback(async () => {
    setLoading(true);
    setError(false);

    try {
      const res = await fetch(`${API_BASE}/documents`);
      if (!res.ok) throw new Error();

      const data = await res.json();
      const nextDocuments = Array.isArray(data?.documents)
        ? [...data.documents].reverse()
        : [];

      setDocuments(nextDocuments);
    } catch {
      setError(true);
      setDocuments([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchDocuments();
  }, [fetchDocuments]);

  const handleDelete = useCallback(async (docName: string) => {
    try {
      const res = await fetch(`${API_BASE}/documents/${encodeURIComponent(docName)}`, {
        method: "DELETE",
      });

      if (!res.ok) throw new Error();

      toast.success(`"${docName}" deleted`);
      setDocuments((prev) => prev.filter((d) => d !== docName));
    } catch {
      toast.error("Delete failed");
    }
  }, []);

  const handleDownload = (doc: string) => {
    window.open(`${API_BASE}/documents/${encodeURIComponent(doc)}/download`);
  };

  return (
    <SidebarProvider>
      <div className="min-h-screen flex w-full">
        <AppSidebar />

        <div className="flex-1 flex flex-col min-w-0">
          <LoadingBar visible={loading} />

          {/* ✅ NO upload */}
          <AppHeader />

          <main className="flex-1 overflow-y-auto">
            <div className="max-w-[1000px] mx-auto px-6 py-8">

              <h1 className="text-2xl font-semibold mb-1">Documents</h1>
              <p className="text-sm text-muted-foreground mb-6">
                Manage your uploaded documents.
              </p>

              {loading ? (
                <div className="text-center py-12 text-sm text-muted-foreground">
                  Loading…
                </div>
              ) : error ? (
                <div className="text-center py-12 text-sm text-red-500">
                  Failed to load
                </div>
              ) : documents.length === 0 ? (
                <div className="text-center py-12 text-sm text-muted-foreground">
                  No documents uploaded yet
                </div>
              ) : (
                <div className="border rounded-lg bg-card">

                  {documents.map((doc, i) => (
                    <div
                      key={doc}
                      className={`flex justify-between px-5 py-3 ${
                        i !== documents.length - 1 ? "border-b" : ""
                      }`}
                    >
                      <div className="flex items-center gap-3">
                        <FileText className="h-4 w-4" />
                        <span className="text-sm">{doc}</span>
                      </div>

                      <div className="flex gap-2">

                        {/* ❓ Ask */}
                        <Button
                          variant="ghost"
                          size="icon"
                          onClick={() =>
                            navigate(`/chat?file=${encodeURIComponent(doc)}`)
                          }
                        >
                          <HelpCircle className="h-4 w-4 text-blue-500" />
                        </Button>

                        {/* Download */}
                        <Button
                          variant="ghost"
                          size="icon"
                          onClick={() => handleDownload(doc)}
                        >
                          <Download className="h-4 w-4" />
                        </Button>

                        {/* Delete */}
                        <Button
                          variant="ghost"
                          size="icon"
                          onClick={() => handleDelete(doc)}
                        >
                          <Trash2 className="h-4 w-4 text-red-500" />
                        </Button>

                      </div>
                    </div>
                  ))}

                </div>
              )}

            </div>
          </main>
        </div>
      </div>
    </SidebarProvider>
  );
}

export default Documents;