import React, { useEffect, useState } from "react";
import "./Slider.css";

const images = [
  {
    src: "https://www.w3schools.com/howto/img_nature_wide.jpg",
    caption: "Caption Text",
  },
  {
    src: "https://www.w3schools.com/howto/img_snow_wide.jpg",
    caption: "Caption Two",
  },
  {
    src: "https://www.w3schools.com/howto/img_mountains_wide.jpg",
    caption: "Caption Three",
  },
];

const Slider = () => {
  const [slideIndex, setSlideIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setSlideIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 2000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div>
      <div className="slideshow-container">
        {images.map((image, index) => (
          <div
            key={index}
            className="mySlides fade"
            style={{ display: index === slideIndex ? "block" : "none" }}
          >
            <div className="numbertext">{index + 1} / {images.length}</div>
            <img src={image.src} style={{ width: "100%" }} alt={`Slide ${index + 1}`} />
          </div>
        ))}
      </div>
      
    </div>
  );
};

export default Slider;