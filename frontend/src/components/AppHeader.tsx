import { Upload, Bell, Share2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { SidebarTrigger } from "@/components/ui/sidebar";
import { useRef } from "react";
import { toast } from "sonner";

interface AppHeaderProps {
  onUpload?: (file: File) => void; // ✅ optional
  uploading?: boolean;
}

export function AppHeader({ onUpload, uploading }: AppHeaderProps) {
  const fileRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file || !onUpload) return;

    const allowed = [
      "application/pdf",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
      "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ];

    if (!allowed.includes(file.type)) {
      toast.error("Only PDF, DOCX, PPTX allowed");
      return;
    }

    onUpload(file);
    e.target.value = "";
  };

  return (
    <header className="h-14 border-b flex items-center justify-between px-4 bg-card">
      <SidebarTrigger />

      <div className="flex items-center gap-2">
        <Button
          variant="ghost"
          size="icon"
          onClick={() => toast.info("Share link copied")}
        >
          <Share2 className="h-4 w-4" />
        </Button>

        <Button variant="ghost" size="icon">
          <Bell className="h-4 w-4" />
        </Button>

        {/* ✅ Upload ONLY if onUpload exists */}
        {onUpload && (
          <>
            <input
              ref={fileRef}
              type="file"
              className="hidden"
              onChange={handleFileChange}
            />

            <Button
              onClick={() => fileRef.current?.click()}
              disabled={uploading}
              className="gap-2"
            >
              <Upload className="h-4 w-4" />
              {uploading ? "Uploading..." : "Upload"}
            </Button>
          </>
        )}
      </div>
    </header>
  );
}