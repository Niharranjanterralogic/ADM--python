import React, { Fragment, useRef, useState } from "react";
import { useHistory } from "react-router-dom";

import { storage } from "../firebase";

import "./user.css";

function User(props) {
  const fRef = useRef();
  const lRef = useRef();
  const ageRef = useRef();
  const occRef = useRef();
  const locRef = useRef();
  const history = useHistory();
  const [image, setImage] = useState(null);
  const [url, setUrl] = useState("");
  const [progress, setProgress] = useState(0);

  /* const handleUpload = () => {
    const uploadTask = storage.ref(`images/${image.name}`).put(image);
    uploadTask.on(
      "state_changed",
      (snapshot) => {
        const progress = Math.round(
          (snapshot.bytesTransferred / snapshot.totalBytes) * 100
        );
        setProgress(progress);
      },
      (error) => {
        console.log(error);
      },
      () => {
        storage
          .ref("images")
          .child(image.name)
          .getDownloadURL()
          .then((url) => {
            console.log(url);
            setUrl(url);
          });
      }
    );
  };*/
  const handleChange = (event) => {
    if (event.target.files[0]) {
      setImage(event.target.files[0]);
    }
  };
  const handleUpload = () => {
    const uploadTask = storage.ref(`images/${image.name}`).put(image);
    uploadTask.on(
      "state_changed",
      (snapshot) => {
        const progress = Math.round(
          (snapshot.bytesTransferred / snapshot.totalBytes) * 100
        );
        setProgress(progress);
      },
      (error) => {
        console.log(error);
      },
      () => {
        storage
          .ref("images")
          .child(image.name)
          .getDownloadURL()
          .then((url) => {
            console.log(url);
            setUrl(url);
          });
      }
    );
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const detail = {
      firstName: fRef.current.value,
      lastName: lRef.current.value,
      age: ageRef.current.value,
      occupation: occRef.current.value,
      location: locRef.current.value,
      url: url,
    };
    props.onAddDetails(detail);
  };
  return (
    <Fragment>
      <div className="main">
        <form onSubmit={handleSubmit}>
          <div className="child1">
            <input
              type="text"
              className="fname"
              ref={fRef}
              placeholder="First Name"
            ></input>
            <input
              type="text"
              className="lname"
              ref={lRef}
              placeholder="Last Name"
            ></input>

            <input
              className="age"
              type="number"
              ref={ageRef}
              placeholder="Age"
            ></input>
            <select
              className="loc"
              ref={locRef}
              name="location"
              placeholder="Location"
            >
              <option></option>
              <option>Nellore</option>
              <option>Banglore</option>
              <option>Hyderabad</option>
            </select>
            <input
              type="text"
              className="occ"
              ref={occRef}
              placeholder="Occupation"
            ></input>

            <button className="deletebtn">Save</button>
          </div>
        </form>

        <div className="child2">
          <div>
            <input className="boxx" type="file" onChange={handleChange}></input>
            <button className="uploadbtn" onClick={handleUpload}></button>
          </div>
        </div>
      </div>
    </Fragment>
  );
}

export default User;
