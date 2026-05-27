import { useState, useCallback, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/AppSidebar";
import { AppHeader } from "@/components/AppHeader";
import { InfoPanels } from "@/components/InfoPanels";
import { LoadingBar } from "@/components/LoadingBar";

const API_BASE = "http://127.0.0.1:8000/api";

function Index() {
  const [recentQuestions, setRecentQuestions] = useState<string[]>([]);
  const [documents, setDocuments] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    const saved = localStorage.getItem("recentQuestions");
    if (saved) {
      setRecentQuestions(JSON.parse(saved));
    }
  }, []);

  const fetchDocuments = useCallback(async () => {
    try {
      const res = await fetch(`${API_BASE}/documents`);

      if (!res.ok) throw new Error();

      const data = await res.json();

      const nextDocuments = Array.isArray(data?.documents)
        ? [...data.documents].reverse()
        : [];

      setDocuments(nextDocuments);
    } catch {
      setDocuments([]);
    }
  }, []);

  useEffect(() => {
    fetchDocuments();
  }, [fetchDocuments]);

  return (
    <SidebarProvider>
      <div className="min-h-screen flex w-full">
        <AppSidebar />

        <div className="flex-1 flex flex-col min-w-0">
          <LoadingBar visible={loading} />

          {/* ✅ NO upload here */}
          <AppHeader />

          <main className="flex-1 overflow-y-auto">
            <div className="max-w-[1000px] mx-auto px-6 py-8">

              {recentQuestions.length === 0 && documents.length === 0 ? (
                <div className="text-center py-20 text-muted-foreground">
                  <p className="text-lg mb-2">No data yet</p>
                  <p className="text-sm">
                    Go to{" "}
                    <span
                      onClick={() => navigate("/chatbots")}
                      className="font-semibold text-primary cursor-pointer underline"
                    >
                      ChatBots
                    </span>{" "}
                    to start asking questions and uploading documents.
                  </p>
                </div>
              ) : (
                <InfoPanels
                  onQuestionClick={() => {}}
                  recentQuestions={recentQuestions}
                  documents={documents}
                  setDocuments={setDocuments}
                />
              )}

            </div>
          </main>
        </div>
      </div>
    </SidebarProvider>
  );
}

export default Index;