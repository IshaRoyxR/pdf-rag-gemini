import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/AppSidebar";
import { AppHeader } from "@/components/AppHeader";
import { Button } from "@/components/ui/button";
import { Calendar } from "lucide-react";
import { toast } from "sonner";

function Schedule() {
  return (
    <SidebarProvider>
      <div className="min-h-screen flex w-full">
        <AppSidebar />

        <div className="flex-1 flex flex-col min-w-0">
          <AppHeader />

          <main className="flex-1 overflow-y-auto">
            <div className="max-w-[1000px] mx-auto px-6 py-8">
              <h1 className="text-2xl font-semibold mb-1">Schedule</h1>
              <p className="text-sm text-muted-foreground mb-6">
                Manage your scheduled tasks.
              </p>

              <div className="text-center py-16">
                <Calendar className="h-12 w-12 mx-auto mb-4 text-muted-foreground" />
                <p className="text-sm text-muted-foreground mb-4">
                  No scheduled tasks yet
                </p>
                <Button onClick={() => toast.info("Coming soon!")}>
                  Create Schedule
                </Button>
              </div>
            </div>
          </main>
        </div>
      </div>
    </SidebarProvider>
  );
}

export default Schedule;