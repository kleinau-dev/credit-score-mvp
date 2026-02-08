import { api } from "./http";

interface LoginResponse {
    access_token: string;
    token_type: string;
}

export async function login(email: string, password: string) {
    const response = await api.post<LoginResponse>("/auth/login", {
        email,
        password,
    });

    return response.data;
}