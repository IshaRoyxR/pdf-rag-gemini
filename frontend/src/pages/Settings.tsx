import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/AppSidebar";
import { AppHeader } from "@/components/AppHeader";
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { useState } from "react";
import { toast } from "sonner";
import { User, LogOut } from "lucide-react";

function Settings() {
  const [darkMode, setDarkMode] = useState(false);

  const handleLogout = () => {
    setDarkMode(false);
    document.documentElement.classList.remove("dark");
    toast.success("Logged out successfully.");
  };

  const toggleTheme = (checked: boolean) => {
    setDarkMode(checked);
    document.documentElement.classList.toggle("dark", checked);
  };

  return (
    <SidebarProvider>
      <div className="min-h-screen flex w-full">
        <AppSidebar />

        <div className="flex-1 flex flex-col min-w-0">
          <AppHeader />

          <main className="flex-1 overflow-y-auto">
            <div className="max-w-[1000px] mx-auto px-6 py-8">
              <h1 className="text-2xl font-semibold mb-1">Settings</h1>
              <p className="text-sm text-muted-foreground mb-6">
                Manage your account preferences.
              </p>

              <div className="space-y-6">
                <div className="border rounded-lg bg-card p-5">
                  <h2 className="text-sm font-semibold flex items-center gap-2 mb-4">
                    <User className="h-4 w-4" />
                    Profile
                  </h2>

                  <div className="space-y-2 text-sm">
                    <div className="flex justify-between">
                      <span>Name</span>
                      <span className="font-medium">John Doe</span>
                    </div>

                    <div className="flex justify-between">
                      <span>Email</span>
                      <span className="font-medium">john@example.com</span>
                    </div>
                  </div>
                </div>

                <div className="border rounded-lg bg-card p-5">
                  <h2 className="text-sm font-semibold mb-4">Appearance</h2>

                  <div className="flex justify-between items-center">
                    <span>Dark Mode</span>
                    <Switch checked={darkMode} onCheckedChange={toggleTheme} />
                  </div>
                </div>

                <Button variant="destructive" onClick={handleLogout}>
                  <LogOut className="h-4 w-4 mr-2" />
                  Logout
                </Button>
              </div>
            </div>
          </main>
        </div>
      </div>
    </SidebarProvider>
  );
}

export default Settings;