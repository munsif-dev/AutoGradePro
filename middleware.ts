import { NextResponse } from "next/server";
import { getAuth } from "firebase-admin/auth"; // Import from firebase-admin
import { firebaseAdminApp } from "./lib/fireBaseadmin";
// Correct path to firebaseAdmin.ts

// List of public routes that don't require authentication
const publicRoutes = ["/", "/login", "/register"];

export async function middleware(req) {
  const { pathname } = req.nextUrl; // Get the request URL
  const auth = getAuth(firebaseAdminApp); // Firebase admin for server-side verification
  const token = req.headers.get("authorization")?.split(" ")[1]; // Get token from the request header

  // Check if the route is public
  if (publicRoutes.includes(pathname)) {
    return NextResponse.next(); // Allow public routes to be accessed without authentication
  }

  // If it's not a public route, check the Firebase token
  if (token) {
    try {
      // Verify the token using Firebase Admin SDK
      const decodedToken = await auth.verifyIdToken(token);
      if (decodedToken) {
        // Authenticated, continue to the route
        return NextResponse.next();
      }
    } catch (error) {
      console.error("Invalid token:", error);
      return NextResponse.redirect("/login");
    }
  }

  // If no token or token is invalid, redirect to login
  return NextResponse.redirect("/login");
}

export const config = {
  matcher: [
    // Skip Next.js internals and all static files
    "/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)",
    // Always run for API routes
    "/(api|trpc)(.*)",
  ],
};
