import { createContext, useContext, useState } from "react";
import { login as loginService } from "./auth.service";

type AuthContextType = {
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
};

const AuthContext = createContext<AuthContextType>(null!);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("access_token")
  );

  async function login(email: string, password: string) {
    const data = await loginService(email, password);
    localStorage.setItem("access_token", data.access_token);
    setToken(data.access_token);
  }

  function logout() {
    localStorage.removeItem("access_token");
    setToken(null);
  }

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
