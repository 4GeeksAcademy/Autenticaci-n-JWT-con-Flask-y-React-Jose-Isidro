import { useState } from "react"
import { Link } from "react-router-dom";


export const Signup = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        const resp = await fetch("https://ubiquitous-space-sniffle-5g9w7wrxvqqv3vvxp-3001.app.github.dev/api/signup", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });
        setEmail(""),setPassword("")
        
        if (resp.ok) {
            alert("Usuario creado");
        } else {
            alert("Error en registro");
        }
        
    };

    return (
        <div className="container-sm w-25 p-3">
            <h1>Registrarse</h1>
            <form className="row justify-content-md-center" onSubmit={handleSubmit}>
                <div className="col-12">
                    <label htmlFor="inputEmail4" className="form-label">Email</label>
                    <input type="email" className="form-control" id="inputEmail4" value={email} onChange={e => setEmail(e.target.value)}/>
                </div>
                <div className="col-12">
                    <label htmlFor="inputPassword4" className="form-label">Password</label>
                    <input type="password" className="form-control" id="inputPassword4" value={password} onChange={e => setPassword(e.target.value)} />
                </div>
                <div className="col-12 my-3">
                    <button type="submit" className="btn btn-primary px-5" >Resgistrarse</button>
                </div>
                <div className="col-12 my-3">
                    <Link to={"/Login"} className="">Iniciar Sesión</Link>
                </div>

            </form>
        </div>

    )
}
