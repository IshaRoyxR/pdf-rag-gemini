export function LoadingBar({ visible }: { visible: boolean }) {
  if (!visible) return null;
  return (
    <div className="fixed top-0 left-0 right-0 h-1 bg-muted z-50 overflow-hidden">
      <div className="h-full w-1/4 bg-primary rounded-full animate-indeterminate" />
    </div>
  );
}
