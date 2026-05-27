import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { Toaster } from "@/components/ui/toaster";
import { TooltipProvider } from "@/components/ui/tooltip";

import Index from "./pages/Index.tsx";
import ChatBots from "./pages/ChatBots.tsx";
import Schedule from "./pages/Schedule.tsx";
import Documents from "./pages/Documents.tsx";
import Settings from "./pages/Settings.tsx";
import NotFound from "./pages/NotFound.tsx";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <Routes>

          {/* ✅ MAIN PAGE → ChatBots */}
          <Route path="/" element={<ChatBots />} />

          {/* ✅ Insights */}
          <Route path="/insights" element={<Index />} />

          {/* ✅ ChatBots */}
          <Route path="/chatbots" element={<ChatBots />} />

          <Route path="/schedule" element={<Schedule />} />
          <Route path="/documents" element={<Documents />} />
          <Route path="/settings" element={<Settings />} />

          {/* ✅ fallback → no 404 */}
          <Route path="*" element={<Navigate to="/" />} />

        </Routes>
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;