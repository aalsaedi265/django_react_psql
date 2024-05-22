
import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import { useState, useEffect } from "react";
// protects route meaning need access token to get to route

function ProtectedRoute({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null)
    
    useEffect(() => {
        auth().catch(()=> setIsAuthorized(false))
    },[])

    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        try {
            const res = await api.post("/api/token/refresh/", {
                refresh: refreshToken,
            })
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
            } else {
                setIsAuthorized(false)
            }
        } catch (error) {
            console.log(error)
            setIsAuthorized(false)
        }
    }
//check if expired or not , if exp refresh
    const auth = async () => {
        //localstorage allows for presistence in the browser
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (!token) {
            setIsAuthorized(false)
            return
        }
        const decode = jwtDecode(token)
        const tokenExpiration = decode.exp
        const now = Date.now / 1000 // get in sec instead of msec

        if (tokenExpiration < now) {
            await refreshToken()
        } else {
            setIsAuthorized(true)
        }

    }
//checks if you got token if not will be redirected
    if (isAuthorized === null) {
        return <div>LOADING ...</div>
    }
    return isAuthorized ? children : <Navigate to="/login" />
}
export default ProtectedRoute