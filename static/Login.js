import React from 'react';
import './Login.css';
import {Link} from "react-router-dom";

function Login() {
    return (
    <div><h1>Login Page</h1>
    <Link to="/Signup">Sign Up</Link>
    </div>
    );
}

export default Login;