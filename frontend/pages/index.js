import React, { useState } from "react"; 
import dynamic from "next/dynamic";
import PropTypes from "prop-types";
import Header from "../containers/Header";
import Upload from "../containers/ImageSection";
import MapSection from "../containers/MapSection";

export default function Home() {
  const [uploadCompleted, setUploadCompleted] = useState(false);
  const [currentMarkerType, setCurrentMarkerType] = useState(0);

  const handleUploadCompleted = () => {
    setUploadCompleted(true);
    setCurrentMarkerType((currentMarkerType + 1) % 3); // Cycle through 0, 1, 2
  };

  return (
    <div>
      <Header />
      <Upload setUploadCompleted={handleUploadCompleted} />  
      <MapSection uploadCompleted={uploadCompleted} currentMarkerType={currentMarkerType} />  
    </div>
  );
}
