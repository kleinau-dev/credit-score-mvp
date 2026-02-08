import { useState } from "react";
import { login as loginRequest } from "../api/auth";

export function useAuth() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function login(email: string, password: string) {
    try {
      setLoading(true);
      setError(null);

      const data = await loginRequest(email, password);

      localStorage.setItem("access_token", data.access_token);

      return true;
    } catch (err) {
      setError("Credenciais inválidas");
      return false;
    } finally {
      setLoading(false);
    }
  }

  function logout() {
    localStorage.removeItem("access_token");
  }

  function isAuthenticated() {
    return !!localStorage.getItem("access_token");
  }

  return {
    login,
    logout,
    isAuthenticated,
    loading,
    error,
  };
}