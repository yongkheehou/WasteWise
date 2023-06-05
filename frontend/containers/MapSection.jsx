import React, { useState, useEffect } from "react";
import { Fade } from "react-reveal";
import { Col, Container, Row } from "reactstrap";
import styles from "../styles/MapSection.module.css";
import dynamic from 'next/dynamic';

const MapSection = () => {
  const [location, setLocation] = useState({ lat: 1.3521, lng: 103.8198 });
  const [markers, setMarkers] = useState([]);
  const [nearestBins, setNearestBins] = useState(null); // Variable to store the nearest bins data

  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setLocation({
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          });
        },
        (error) => {
          console.log("Geolocation error: ", error);
        }
      );
    } else {
      console.log("Geolocation is not supported by this browser.");
    }
  }, []);

  useEffect(() => {
    if (binType) {
      // Make the fetch request to get nearest bins based on binType
      fetch("BACK_END_API", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          number: 5,
          user_coordinates: [location.lat, location.lng],
          bin_type: binType,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          setNearestBins(data);
          // Extract the coordinates from the response and set markers
          const extractedMarkers = data?.data?.map((bin) => ({
            lat: bin.coordinates[0],
            lng: bin.coordinates[1],
          }));
          setMarkers(extractedMarkers);
        })
        .catch((error) => console.log(error));
    }
  }, [binType, location]);

  const renderMap = () => {
    if (typeof window !== "undefined") {
      const { Map, TileLayer, Marker, Popup } = require("react-leaflet");
      require("leaflet/dist/leaflet.css");

      return (
        <div className={styles.mapContainer}>
          <Fade>
            <Map center={location} zoom={13} style={{ height: "60vw", width: "80vw" }}>
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              />

              <Marker position={[location.lat, location.lng]}>
                <Popup>
                  <div className={styles.popupContent}>
                    <p className={styles.centeredText}>Your Location</p>
                  </div>
                </Popup>
              </Marker>

              {markers.map((marker, idx) => (
                <Marker key={idx} position={[marker.coordinates[0], marker.coordinates[1]]}>
                  <Popup>
                    <div className={styles.popupContent}>
                      <p className={styles.centeredText}>Distance: {marker.distance}</p>
                      <p className={styles.centeredText}>Address: {marker.address}</p>
                      <p className={styles.centeredText}>Description: {marker.description}</p>
                    </div>
                  </Popup>
                </Marker>
              ))}
            </Map>
          </Fade>
        </div>
      );
    }
    return null;
  };  

  return (
    <div className={styles.mapSection}>
      <Container className="text-center my-5 section section-lg">
        <h1 className={`h1 map1 ${styles.centeredText}`}>Find Your Nearest Bin! </h1>
        <Row className="my-5 justify-content-center align-items-center">
          <Col lg="6" className="order-2 order-lg-1 d-flex justify-content-center align-items-center">
            {renderMap()}
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default MapSection;