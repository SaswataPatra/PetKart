import axios from "axios";
import { API_BASE_URL } from "./config";

export async function login(email: string, password: string) {
    const response = await axios.post(`${API_BASE_URL}/auth/login`, {
        email,
        password
    })

    return response.data
}

export interface IRegister {
    name: string
    email: string
    password: string
    billing_address: string
    shipping_address: string
    payment_methods: string
    image: string
}

export async function register(data: IRegister) {
    const response = await axios.post(`${API_BASE_URL}/auth/signup`, data)

    return response.data
}

export function fetchToken() {
    const item = localStorage.getItem("token")
    return item ?? ""
}

export async function enrollAdmin(email: string) {
    const token = fetchToken()
    const response = await axios.post(`${API_BASE_URL}/auth/admin/enroll`, {
        email
    }, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    })

    return response.data
}

export async function fetchProducts() {
    const response = await axios.get(`${API_BASE_URL}/products`)

    return response.data?.products ?? []
}

export async function convertBase64(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => resolve(reader.result as string)
        reader.onerror = error => reject(error)
    })
}