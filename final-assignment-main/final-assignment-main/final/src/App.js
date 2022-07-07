import "./App.css";
import React, { useState, useEffect, useCallback } from "react";
import { AuthProvider } from "./contexts/authContext";
import { Route } from "react-router-dom";
import Signup from "./signup";
import Login from "./login";
import User from "./components/user";
import img3 from "./images/Frame 4@3x.png";
import Table from "react-bootstrap/Table";
import deleteimg from "./images/trash-can-outline.png";
import editimg from "./images/Vector.png";

//import { db } from "./firebase";
//import { collection, getDocs } from "firebase/firestore";
//import { getDialogUtilityClass } from "@mui/material";

function App(props) {
  const [details, setDetails] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  //const detailCollectionref = collection(db, "details");

  const fetchDetailsHandler = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(
        "https://database-60c4a-default-rtdb.firebaseio.com/details.json"
      );
      if (!response.ok) {
        throw new Error("Something went wrong!");
      }

      const data = await response.json();

      const loadedDetails = [];

      for (const key in data) {
        loadedDetails.push({
          firstName: data[key].firstName,
          lastName: data[key].lastName,
          age: data[key].age,
          location: data[key].location,
          occupation: data[key].occupation,
          url: data[key].url,
        });
      }

      setDetails(loadedDetails);
    } catch (error) {
      setError(error.message);
    }
    setIsLoading(false);
  }, []);

  useEffect(() => {
    fetchDetailsHandler();
    //const getDetails = async () => {
    //  const dataa = await getDocs(detailCollectionref);
    // console.log(dataa);
    // };
  }, [fetchDetailsHandler]);
  var checkboxes = document.querySelectorAll("input[type='checkbox']");

  const checkAll = (myCheckbox) => {
    if (myCheckbox.checked === true) {
      checkboxes.forEach(function (checkbox) {
        checkbox.checked = true;
      });
    } else {
      checkboxes.forEach(function (checkbox) {
        checkbox.checked = false;
      });
    }
  };

  async function addDetailsHandler(movie) {
    const response = await fetch(
      "https://database-60c4a-default-rtdb.firebaseio.com/details.json",
      {
        method: "POST",
        body: JSON.stringify(movie),
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    const data = await response.json();
    console.log(data);
  }

  return (
    <AuthProvider>
      <Route path="/signup">
        <Signup></Signup>
      </Route>
      <Route path="/login">
        <Login></Login>
      </Route>
      <Route path="/enterdetails">
        <User onAddDetails={addDetailsHandler}></User>
      </Route>
      <Route path="/details">
        <header className="rpheader">
          <img src={img3} alt="" />
          <h1>Real Persona</h1>
        </header>
        <div className="pm">
          <h1>Persona Management</h1>
        </div>
        <div className="nump">
          <div className="per">
            450 <br></br> Personas
          </div>
          <input
            type="text"
            placeholder="Search by Name, Location, Occupation"
          ></input>
          <div className="right">
            <button className="del">
              <img className="deleteheader" src={deleteimg}></img>
              <span>Delete</span>
            </button>
            <button className="newp">+New Persona</button>
          </div>
        </div>

        <Table className="dtab">
          <thead>
            <tr>
              <td>
                <input type="checkbox" id="option-all" onChange={checkAll} />
              </td>
              <th></th>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Location</th>
              <th>Occupation</th>
              <th>Age</th>
              <th>Uploaded by</th>
              <th>Uploaded on</th>
              <th>No. of downloads</th>
              <th>Actions</th>
              <th></th>
            </tr>
          </thead>

          {details.map((detail) => (
            <tbody>
              <td>
                <input type="checkbox" />
              </td>

              <td>
                <img className="tableimage" src={detail.url}></img>
              </td>

              <td>{detail.firstName}</td>
              <td>{detail.lastName}</td>
              <td>{detail.location}</td>
              <td>{detail.occupation}</td>
              <td>{detail.age}</td>
              <td>Gokul</td>
              <td>
                2/5/2022<br></br>
                3:30PM(IST)
              </td>
              <td>23,242</td>
              <td>
                <img className="delimg" src={deleteimg}></img>
                <img className="editimg" src={editimg}></img>
              </td>
            </tbody>
          ))}
        </Table>
      </Route>
    </AuthProvider>
  );
}

export default App;
