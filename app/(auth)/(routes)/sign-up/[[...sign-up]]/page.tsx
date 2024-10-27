"use client";
import { useState } from "react";
import Link from "next/link";
import {
  auth,
  provider,
  db,
} from "@/app/(auth)/(routes)/_components/firebaseConfig";
import { createUserWithEmailAndPassword, signInWithPopup } from "firebase/auth";
import { doc, setDoc } from "firebase/firestore";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("student");
  const [isLecturer, setIsLecturer] = useState(false);
  const [University, setUniversity] = useState("");

  const handleRegister = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const userCredential = await createUserWithEmailAndPassword(
        auth,
        email,
        password
      );
      const user = userCredential.user;
      console.log("User registered:", user);
      // Store user data in Firestore
      await setDoc(doc(db, "users", user.uid), {
        email: user.email,
        role: role,
        University: isLecturer ? University : null,
      });
    } catch (error) {
      console.error("Error registering:", error);
      toast.error("Error registering: " + (error as Error).message);
    }
  };

  const handleGoogleSignIn = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;

      // Check if user exists in Firestore, if not, add them
      const docRef = doc(db, "users", user.uid);
      await setDoc(docRef, {
        email: user.email,
        role: "student", // Default role as student for Google sign-in
      });
    } catch (error) {
      console.error("Error with Google Sign-In:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center">
      <div className="max-w-md w-full bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-bold mb-4 text-center">Register</h2>
        <form onSubmit={handleRegister}>
          <div className="mb-4">
            <label className="block text-sm font-medium">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full px-4 py-2 border rounded-lg"
            />
          </div>
          <div className="mb-4">
            <label className="block text-sm font-medium">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full px-4 py-2 border rounded-lg"
            />
          </div>
          <div className="mb-4">
            <label className="block text-sm font-medium">Role</label>
            <select
              value={role}
              onChange={(e) => {
                setRole(e.target.value);
                setIsLecturer(e.target.value === "lecturer");
              }}
              className="w-full px-4 py-2 border rounded-lg"
            >
              <option value="student">Student</option>
              <option value="lecturer">Lecturer</option>
            </select>
          </div>

          {isLecturer && (
            <div className="mb-4">
              <label className="block text-sm font-medium">
                Working University
              </label>
              <input
                type="text"
                value={University}
                onChange={(e) => setUniversity(e.target.value)}
                className="w-full px-4 py-2 border rounded-lg"
              />
            </div>
          )}

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded-lg"
          >
            Register
          </button>
        </form>

        <div className="mt-6 text-center">
          <button
            onClick={handleGoogleSignIn}
            className="w-full bg-red-500 text-white py-2 rounded-lg"
          >
            Register with Google
          </button>
        </div>

        <div className="mt-4 text-center">
          <p className="text-sm">
            Already have an account?{" "}
            <Link href="/sign-in" className="text-blue-500 underline">
              Sign In
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
}
