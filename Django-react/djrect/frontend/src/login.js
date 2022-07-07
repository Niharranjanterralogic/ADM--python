import React, { Fragment, useRef, useState } from "react";
import img1 from "./images/LockKey@3x.png";
import img2 from "./images/EnvelopeSimple@3x.png";
import img3 from "./images/Frame 4@3x.png";
import { useAuth } from "./contexts/authContext";
import { useHistory } from "react-router-dom";
import { Alert } from "react-bootstrap";

function Login() {
  const history = useHistory();
  const emailRef = useRef();
  const passwordRef = useRef();
  const { login } = useAuth();
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();

    try {
      setError();
      setLoading(true);
      await login(emailRef.current.value, passwordRef.current.value);
      history.push("/welcome");
    } catch {
      setError("Failed to Login In!");
    }
    setLoading(false);
    console.log("log");
  }

  return (
    <Fragment>
      <form onSubmit={handleSubmit}>
        <header className="header">
          <img className="image" src={img3} alt=""></img>
          <h1 className="title">Real Persona</h1>
        </header>

        <div className="box">
          {error && (
            <Alert variant="danger" className="aalt">
              {error}
            </Alert>
          )}
          <h1 className="text-center">Admin Login</h1>

          <input
            className="user"
            type="text"
            placeholder="  Email ID"
            style={{
              background: `url(${img2})`,
              backgroundPosition: "5px",
              backgroundRepeat: "no-repeat",
              backgroundSize: "25px",
            }}
            ref={emailRef}
            required
          ></input>
          <input
            className="pass"
            type="password"
            placeholder="  Password"
            style={{
              background: `url(${img1})`,
              backgroundPosition: "5px",
              backgroundRepeat: "no-repeat",
              backgroundSize: "25px",
            }}
            ref={passwordRef}
            required
          ></input>
          <button disabled={loading} type="submit" className="btn">
            Login
          </button>
        </div>
      </form>
    </Fragment>
  );
}

export default Login;