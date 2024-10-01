import type { Metadata } from "next";
import "./globals.css";

import { ClerkProvider } from "@clerk/nextjs";

export const metadata: Metadata = {
  title: "AutoGradePro",
  description: "An Automated Paper Grading System",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body>
          <div className="absolute top-0 left-0 z-0 ellipse"></div>

          <main className="relative overflow-hidden">{children}</main>
        </body>
      </html>
    </ClerkProvider>
  );
}
