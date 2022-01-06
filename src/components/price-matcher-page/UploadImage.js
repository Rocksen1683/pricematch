import React, { useEffect, useState } from "react";
// import { storage } from "./firebase"
import { app } from "./firebase";
import { getStorage, ref, uploadBytes } from "firebase/storage";
import "./price-match-new.css";
import ArrowUpwardIcon from "@material-ui/icons/ArrowUpward";
// import { ShopContextProvider } from "./ShopContext";
import ShopItem from "./ShopItem";
import { collection, getDocs } from "firebase/firestore";
import db from './firebase'
import { onSnapshot } from 'firebase/firestore';


function UploadImage() {
  const [documents, setDocuments] = useState([])
  useEffect(
    ()=> 
    onSnapshot(collection(db, "applications"), (snapshot)=> 
      setDocuments(snapshot.docs.map(doc => doc.data()))), [])
  const [imageAsFile, setImageAsFile] = useState();
  const [displayShops, setDisplayShops] = useState(false);
  const storage = getStorage(app);

  const handleImageAsFile = (e) => {
    const image = e.target.files[0];
    setImageAsFile(image);
    console.log(imageAsFile);
  };

  const handleFirebaseUpload = (e) => {
    e.preventDefault();
    console.log("start of upload");
    if (imageAsFile === "") {
      console.error(`not an image, the image file is a ${typeof imageAsFile}`);
    }
    setDisplayShops(true);
    const storageRef = ref(storage, "photo.jpg");
    uploadBytes(storageRef, imageAsFile).then((snapshot) => {
      console.log("Uploaded Image!");
    });
    setImageAsFile(false)
  };
  return (
    <div className="container">
      <div className="section-main">
        <div className="section-title-main">
          <h2 className="display-4">Show your product.</h2>
        </div>
        <div className="section-description-main">
          <p>
            Please give us a picture of your product and we will tell you where
            to get it.
          </p>
        </div>
      </div>
      <form onSubmit={handleFirebaseUpload}>
        <div className="wrapper">
          <div className="file-upload">
            <input type="file" onChange={handleImageAsFile} />
            <ArrowUpwardIcon color="secondary" />
          </div>
        </div>
        <button type="submit" className="btn btn-outline-info">
          Submit
        </button>
      </form>
      <div className="image">
        {imageAsFile ? <h2>Image uploaded {imageAsFile.name}</h2> : null}
      </div>
      {/* <div className="shops">
        {displayShops ? (
          <ShopContextProvider>
            <Shop university={university} />
          </ShopContextProvider>
        ) : null}
      </div> */}
      <div className="shops">
        {
          console.log(documents)
        }
        {
          // console.log(documents.length)
          (documents.length > 0)?
          (documents.map(
            (doc) => {
              console.log(doc)
              return <ShopItem storeName={doc.StoreName} price={doc.Price} name={doc.Name} />
            }
          )): "Loading..."
        }
      </div>
    </div>
  );
}

export default UploadImage;
