import React, { useState } from "react";
import "./Header.css";
import {Link} from "react-router-dom";

function Header() {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
       <header>
            <img 
                src="https://i.ibb.co/wZVPystV/Party-Manifesto-and-Govt-Schemes-Implementation-Status-Check-20250327-180457-0000.png" 
                alt="logo" 
            />
            <span style={{ color: "lightgrey" }}>|</span>
            <p>GovtInsight</p>
            <span className="menu-icon" onClick={toggleMenu}>&#9776;</span>
            <ul className={menuOpen ? "nav-menu active":"nav-menu"}>
                
                <li><Link to="/">Home</Link></li>
                <li><Link to="/View">View</Link></li>
                <li><Link to="/Complaint">Complaint</Link></li>
                <li><Link to="/Login">Login</Link></li>
            </ul>
        </header>
    );
}

export default Header;
