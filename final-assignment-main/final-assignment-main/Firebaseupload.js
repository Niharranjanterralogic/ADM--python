import React, { useState } from "react";
import { storage } from "./firebase";
import "./FB.css";
function Firebaseupload(props) {
  const [image, setImage] = useState(null);
  const [url, setUrl] = useState("");
  const [progress, setProgress] = useState(0);
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
  props.imagepath = url;
  console.log("hah", imagepath);
  console.log("image:", image);
  console.log(url);
  return (
    <div className="column2">
      <img className="detailimage" src={url}></img>
      <input className="boxx" type="file" onChange={handleChange}></input>

      <button className="uploadbutton" onClick={handleUpload}>
        Upload
      </button>
    </div>
  );
}

export default Firebaseupload;
