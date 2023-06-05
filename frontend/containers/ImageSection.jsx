import React, { useState, useEffect, useRef } from "react";
import { Fade } from "react-reveal";
import { Col, Container, Row, Button } from "reactstrap";
import DisplayLottie from "./DisplayLottie";
import { imageSection } from "../text";

const Upload = ({setUploadCompleted}) => {
  const [progress, setProgress] = useState(0);
  const [binType, setBinType] = useState(null);
  const simulateUpload = useRef(null);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];

    if (simulateUpload.current) {
      clearInterval(simulateUpload.current);
    }

    if (file) {
      setProgress(0);
      setUploadCompleted(false); // Reset uploadCompleted state when a new file is selected
    }
  
    simulateUpload.current = setInterval(() => {
      setProgress((oldProgress) => {
        if (oldProgress >= 100) {
          clearInterval(simulateUpload.current);
          setUploadCompleted(true);
          fetch("BACK_END_API", {
            method: "POST",
          })
            .then((response) => response.text()) 
            .then((data) => {
              console.log(data); 
              setBinType(data); 
            })
            .catch((error) => console.log(error));   

          return oldProgress;
        }
        return oldProgress + 1;
      });
    }, 10);
  };

  useEffect(() => {
    return () => {
      clearInterval(simulateUpload.current);
    };
  }, []);

  return (
    <Container className="text-center my-5 section section-lg">
      <h1 className="h1 image1">{imageSection.title}</h1>
      {imageSection.data.map((section, index) => {
        return (
          <Row className="my-5" key={index}>
            <Col lg="6" className="order-2 order-lg-1">
              <Fade left duration={2000}>
                <DisplayLottie animationPath={section.lottieAnimationFile} />
              </Fade>
            </Col>
            <Col lg="6" className="order-1 order-lg-2">
              <Fade right duration={2000}>
                <h3 className="h3 mb-2 image1">{section.title}</h3>
                <div className="image1">
                  {section.steps.map((step, i) => {
                    return <p key={i}>{step}</p>;
                  })}
                </div>
                <div style={{ marginTop: "20px" }}>
                  <label htmlFor="uploadImage" className="btn btn-primary">
                    Upload Image
                    <input
                      id="uploadImage"
                      type="file"
                      accept="image/*"
                      style={{ display: "none" }}
                      onChange={handleFileUpload}
                    />
                  </label>
                </div>
                <div className="mt-3" style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                  <progress value={progress} max="100" />
                  <span style={{ marginTop: "10px" }}>Done! Refer to the directions below!</span>
                </div>
              </Fade>
            </Col>
          </Row>
        );
      })}
    </Container>
  );
};

export default Upload;
