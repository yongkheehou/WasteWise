import React, { useEffect } from "react";
import { intro } from "../text";
import dynamic from "next/dynamic";
import { Button, Container, Row, Col } from "reactstrap";
import GreetingLottie from "./DisplayLottie";

const ParticleBg = dynamic(() => import("particles-bg"), {
  ssr: false,
});

const Header = () => {
  useEffect(() => {
    document.documentElement.scrollTop = 0;
    document.scrollingElement.scrollTop = 0;
  });

  return (
    <main>
      <div className="position-relative">
        <section className="section section-lg section-shaped pb-250">
          <div className="shape shape-style-1 bg-gradient-warning">
            <span />
            <span />
            <span />
            <span />
            <span />
            <ParticleBg type="polygon" bg={true} num={1} />
          </div>
          <Container className="py-lg-md d-flex">
            <div className="col px-0">
              <Row>
                <Col lg="6">
                  <div className="d-flex align-items-start justify-content-center justify-content-lg-start">
                    <h1 className="display-3 text-white mr-4 align-self-center">
                      {intro.title + " "}
                    </h1>
                    <img
                      src="wastewise.png"
                      alt="Circular Icon"
                      style={{
                        width: "100px",
                        height: "100px",
                        borderRadius: "50%",
                      }}
                    />
                  </div>
                  <p className="lead text-white mt-4">{intro.description}</p>
                  <div className="btn-wrapper my-4">
                    <Button color="primary" href="https://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/waste-minimisation-and-recycling">
                      Learn More!
                    </Button>
                  </div>
                </Col>
                <Col lg="6">
                  <GreetingLottie animationPath="/lottie/coding.json" />
                </Col>
              </Row>
            </div>
          </Container>
          {/* SVG separator */}
          <div className="separator separator-bottom separator-skew">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              preserveAspectRatio="none"
              version="1.1"
              viewBox="0 0 2560 100"
              x="0"
              y="0"
            >
              <polygon className="fill-white" points="2560 0 2560 100 0 100" />
            </svg>
          </div>
        </section>
      </div>
    </main>
  );
};

export default Header;
